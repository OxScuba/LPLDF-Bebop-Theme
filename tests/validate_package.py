#!/usr/bin/env python3
"""Contrôles statiques simples du paquet LPLDF be-BOP."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


class FragmentParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.images_without_alt = []
        self.links_without_href = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            self.ids.append(values["id"])
        if tag == "img" and "alt" not in values:
            self.images_without_alt.append(self.getpos())
        if tag == "a" and not values.get("href"):
            self.links_without_href.append(self.getpos())


def fail(message, failures):
    failures.append(message)


def main():
    failures = []
    cms_files = sorted((ROOT / "cms").glob("*.html"))
    if len(cms_files) != 14:
        fail(f"14 CMS attendus, {len(cms_files)} trouvés", failures)

    for path in cms_files:
        content = path.read_text(encoding="utf-8")
        parser = FragmentParser()
        try:
            parser.feed(content)
            parser.close()
        except Exception as exc:
            fail(f"{path.name}: HTML illisible ({exc})", failures)
            continue
        duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
        if duplicates:
            fail(f"{path.name}: identifiants dupliqués {duplicates}", failures)
        if parser.images_without_alt:
            fail(f"{path.name}: image sans attribut alt", failures)
        if parser.links_without_href:
            fail(f"{path.name}: lien sans href", failures)
        if "REMPLACER_IMG_" in content:
            fail(f"{path.name}: placeholder d’image non remplacé", failures)
        if "/format/2048" in content:
            fail(f"{path.name}: format d’image 2048 non disponible dans be-BOP", failures)
        if not content.lstrip().startswith("<style>"):
            fail(f"{path.name}: import CSS absent au début", failures)
        if "custom.css" not in content:
            fail(f"{path.name}: import du thème CSS absent", failures)
        if '<div class="lpldf-page' not in content:
            fail(f"{path.name}: conteneur .lpldf-page absent", failures)

    css = (ROOT / "custom.css").read_text(encoding="utf-8")
    if css.count("{") != css.count("}"):
        fail("custom.css: accolades non équilibrées", failures)
    if "CSS LPLDF connecté" in css:
        fail("custom.css: badge de test encore présent", failures)
    if ".lpldf-page" not in css or "header.header" not in css:
        fail("custom.css: règles principales absentes", failures)
    if ".lpldf-adventurers-simple" not in css:
        fail("custom.css: sélecteur des aventuriers absent", failures)

    product_cms_files = sorted((ROOT / "produits" / "cms-apres-produit").glob("*.html"))
    if len(product_cms_files) != 11:
        fail(f"11 blocs CMS produit attendus, {len(product_cms_files)} trouvés", failures)
    for path in product_cms_files:
        content = path.read_text(encoding="utf-8")
        parser = FragmentParser()
        parser.feed(content)
        parser.close()
        if "custom.css" not in content:
            fail(f"{path.name}: import du thème CSS absent", failures)
        if "lpldf-product-extra" not in content:
            fail(f"{path.name}: bloc éditorial produit absent", failures)
        if parser.images_without_alt or parser.links_without_href:
            fail(f"{path.name}: attribut HTML obligatoire manquant", failures)

    product_files = sorted((ROOT / "produits" / "papier").glob("*.txt"))
    if len(product_files) != 11:
        fail(f"11 fiches papier attendues, {len(product_files)} trouvées", failures)
    isbn_pattern = re.compile(r"979\d{10}")
    isbns = []
    for path in product_files:
        content = path.read_text(encoding="utf-8")
        found = isbn_pattern.findall(content)
        if len(found) != 1:
            fail(f"{path.name}: un ISBN attendu, {len(found)} trouvé(s)", failures)
        isbns.extend(found)
    if len(isbns) != len(set(isbns)):
        fail("ISBN dupliqué dans les fiches papier", failures)

    forbidden = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".txt", ".html", ".css", ".csv"}:
            if path.is_relative_to(ROOT / "juridique"):
                continue
            text = path.read_text(encoding="utf-8")
            if "REMPLACER_IMG_" in text:
                forbidden.append(str(path.relative_to(ROOT)))
    if forbidden:
        fail("Placeholders restants : " + ", ".join(forbidden), failures)

    if failures:
        print("ÉCHEC")
        for item in failures:
            print(f"- {item}")
        return 1

    print("OK")
    print(f"- {len(cms_files)} pages CMS")
    print(f"- {len(product_files)} fiches papier et {len(set(isbns))} ISBN uniques")
    print(f"- {len(product_cms_files)} blocs CMS après produit")
    print("- CSS équilibré, badge de test absent")
    print("- Aucun placeholder d’image restant hors juridique")
    return 0


if __name__ == "__main__":
    sys.exit(main())
