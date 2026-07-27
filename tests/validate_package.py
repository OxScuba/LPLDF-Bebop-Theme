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

    collection = (ROOT / "cms" / "La_Collection.html").read_text(encoding="utf-8")
    product_shortcodes = re.findall(
        r"\[Product=([^?\]]+)\?display=([^\]]+)\]",
        collection,
    )
    if len(product_shortcodes) != 13:
        fail(
            f"La_Collection.html: 13 widgets natifs attendus, "
            f"{len(product_shortcodes)} trouvé(s)",
            failures,
        )
    if len({slug for slug, _ in product_shortcodes}) != len(product_shortcodes):
        fail("La_Collection.html: widget produit dupliqué", failures)
    if any(display != "img-4" for _, display in product_shortcodes):
        fail("La_Collection.html: tous les widgets doivent utiliser img-4", failures)
    expected_packs = {
        "pack-decouverte-t00-t04",
        "pack-saison-2-t05-t09",
    }
    if not expected_packs.issubset({slug for slug, _ in product_shortcodes}):
        fail("La_Collection.html: un des deux packs est absent", failures)
    if "lpldf-native-collection-marker" not in collection:
        fail("La_Collection.html: marqueur du catalogue natif absent", failures)

    css = (ROOT / "custom.css").read_text(encoding="utf-8")
    if css.count("{") != css.count("}"):
        fail("custom.css: accolades non équilibrées", failures)
    if "CSS LPLDF connecté" in css:
        fail("custom.css: badge de test encore présent", failures)
    if ".lpldf-page" not in css or "header.header" not in css:
        fail("custom.css: règles principales absentes", failures)
    if ".lpldf-adventurers-simple" not in css:
        fail("custom.css: sélecteur des aventuriers absent", failures)
    if ".lpldf-image-lightbox" not in css:
        fail("custom.css: visionneuse des images produit absente", failures)
    if ".lpldf-native-collection-marker" not in css or ".tagWidget.tagWidget-main" not in css:
        fail("custom.css: présentation du catalogue natif absente", failures)
    if ":has(> .my-5 > .lpldf-native-collection-marker)" not in css:
        fail("custom.css: sélecteur de la structure réelle be-BOP absent", failures)

    gallery_script = ROOT / "product-gallery.js"
    if not gallery_script.exists():
        fail("product-gallery.js: script de visionneuse absent", failures)
    else:
        gallery_js = gallery_script.read_text(encoding="utf-8")
        if ".aspect-video img" not in gallery_js or "displayedImage.addEventListener" not in gallery_js:
            fail("product-gallery.js: branchement sur la grande image absent", failures)
        if "a[href" in gallery_js or "ring-2" in gallery_js:
            fail("product-gallery.js: les miniatures ne doivent pas ouvrir la visionneuse", failures)

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
        if content.count("product-gallery.js") != 1:
            fail(f"{path.name}: chargement de la visionneuse produit absent", failures)
        if "21 × 21 cm · 38 pages" not in content:
            fail(f"{path.name}: format physique 21 × 21 cm absent", failures)
        if parser.images_without_alt or parser.links_without_href:
            fail(f"{path.name}: attribut HTML obligatoire manquant", failures)

    pack_cms_files = sorted((ROOT / "produits" / "cms-apres-pack").glob("*.html"))
    if len(pack_cms_files) != 2:
        fail(f"2 blocs CMS pack attendus, {len(pack_cms_files)} trouvés", failures)
    for path in pack_cms_files:
        content = path.read_text(encoding="utf-8")
        parser = FragmentParser()
        parser.feed(content)
        parser.close()
        if "custom.css" not in content:
            fail(f"{path.name}: import du thème CSS absent", failures)
        if "lpldf-product-extra" not in content or "lpldf-pack-volumes" not in content:
            fail(f"{path.name}: contenu éditorial du pack incomplet", failures)
        if content.count("lpldf-pack-volume") < 5:
            fail(f"{path.name}: les cinq tomes du pack ne sont pas présentés", failures)
        if "21 × 21 cm" not in content:
            fail(f"{path.name}: format physique 21 × 21 cm absent", failures)
        if parser.images_without_alt or parser.links_without_href:
            fail(f"{path.name}: attribut HTML obligatoire manquant", failures)

    product_files = sorted((ROOT / "produits" / "papier").glob("*.txt"))
    if len(product_files) != 11:
        fail(f"11 fiches papier attendues, {len(product_files)} trouvées", failures)
    isbn_pattern = re.compile(r"979\d{10}")
    isbns = []
    for path in product_files:
        content = path.read_text(encoding="utf-8")
        if "DESCRIPTION COURTE" not in content:
            fail(f"{path.name}: description courte absente", failures)
        if "Format : 21 × 21 cm" not in content:
            fail(f"{path.name}: format physique 21 × 21 cm absent", failures)
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
            if "15 × 15" in text or "15x15" in text:
                fail(f"{path.relative_to(ROOT)}: ancien format 15 × 15 cm", failures)
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
    print(f"- {len(pack_cms_files)} blocs CMS après pack")
    print("- CSS équilibré, badge de test absent")
    print("- Aucun placeholder d’image restant hors juridique")
    return 0


if __name__ == "__main__":
    sys.exit(main())
