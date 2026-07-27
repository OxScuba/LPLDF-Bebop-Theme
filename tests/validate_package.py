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
        self.elements_by_id = {}
        self.fragment_links = []
        self.lightboxes = []
        self.images_without_alt = []
        self.links_without_href = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        classes = set(values.get("class", "").split())
        if "id" in values:
            self.ids.append(values["id"])
            self.elements_by_id[values["id"]] = {
                "tag": tag,
                "classes": classes,
                "position": self.getpos(),
            }
        if tag == "img" and "alt" not in values:
            self.images_without_alt.append(self.getpos())
        if tag == "a" and not values.get("href"):
            self.links_without_href.append(self.getpos())
        if tag == "a" and values.get("href", "").startswith("#"):
            self.fragment_links.append({
                "target": values["href"][1:],
                "classes": classes,
                "position": self.getpos(),
            })
        if "lpldf-lightbox" in classes:
            self.lightboxes.append({
                "id": values.get("id"),
                "position": self.getpos(),
            })


def fail(message, failures):
    failures.append(message)


def validate_internal_windows(path, parser, failures):
    """Contrôle générique des fenêtres CSS reposant sur :target."""
    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        fail(f"{path}: identifiants dupliqués {duplicates}", failures)

    for link in parser.fragment_links:
        if not link["target"]:
            continue
        target = parser.elements_by_id.get(link["target"])
        if target is None:
            fail(f"{path}: lien interne sans cible #{link['target']}", failures)
            continue
        closing_link = {
            "lpldf-lightbox__close",
            "lpldf-lightbox__backdrop",
        } & link["classes"]
        if not closing_link:
            continue
        if target["tag"] != "section" or "lpldf-return-anchor" not in target["classes"]:
            fail(
                f"{path}: la fermeture vers #{link['target']} doit viser "
                "une section .lpldf-return-anchor",
                failures,
            )
        if target["position"] >= link["position"]:
            fail(f"{path}: l’ancre #{link['target']} doit précéder la fenêtre", failures)

    close_links = sum(
        "lpldf-lightbox__close" in link["classes"]
        for link in parser.fragment_links
    )
    backdrop_links = sum(
        "lpldf-lightbox__backdrop" in link["classes"]
        for link in parser.fragment_links
    )
    if parser.lightboxes and close_links != len(parser.lightboxes):
        fail(
            f"{path}: {len(parser.lightboxes)} fenêtre(s) mais "
            f"{close_links} bouton(s) de fermeture",
            failures,
        )
    if parser.lightboxes and backdrop_links != len(parser.lightboxes):
        fail(
            f"{path}: {len(parser.lightboxes)} fenêtre(s) mais "
            f"{backdrop_links} arrière-plan(s) fermant(s)",
            failures,
        )
    opener_targets = {
        link["target"]
        for link in parser.fragment_links
        if not (
            {"lpldf-lightbox__close", "lpldf-lightbox__backdrop"}
            & link["classes"]
        )
    }
    for lightbox in parser.lightboxes:
        if not lightbox["id"]:
            fail(f"{path}: fenêtre CSS sans identifiant", failures)
        elif lightbox["id"] not in opener_targets:
            fail(
                f"{path}: fenêtre #{lightbox['id']} sans lien d’ouverture",
                failures,
            )


def main():
    failures = []
    css_window_count = 0
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
        validate_internal_windows(path.name, parser, failures)
        css_window_count += len(parser.lightboxes)
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

    chooser = (ROOT / "cms" / "Quel_tome_choisir.html").read_text(encoding="utf-8")
    expected_choice_ids = {
        f"lpldf-choice-t{number:02d}" for number in range(1, 11)
    }
    choice_ids = set(re.findall(
        r'id="(lpldf-choice-t(?:0[1-9]|10))"',
        chooser,
    ))
    if choice_ids != expected_choice_ids:
        fail(
            "Quel_tome_choisir.html: les dix fiches T01 à T10 sont requises",
            failures,
        )
    if 'id="lpldf-choice-return"' not in chooser:
        fail(
            "Quel_tome_choisir.html: ancre de retour du comparateur absente",
            failures,
        )
    choice_grid = chooser.partition('<div class="lpldf-choice-grid">')[2].partition("</div>")[0]
    if any(
        f'href="/product/t{number:02d}-' in choice_grid
        for number in range(1, 11)
    ):
        fail(
            "Quel_tome_choisir.html: les carrés doivent ouvrir les fiches, "
            "pas les produits",
            failures,
        )
    expected_choice_products = {
        "/product/t01-les-marchands-de-chandelles",
        "/product/t02-la-vitre-magique",
        "/product/t03-la-grande-fabrique-des-regles",
        "/product/t04-le-mysterieux-argent-de-papier",
        "/product/t05-la-boussole-invisible",
        "/product/t06-le-ruban-de-solidarite",
        "/product/t07-une-histoire-de-jardin",
        "/product/t08-le-pont-du-consentement",
        "/product/t09-quand-le-gardien-oublie-sa-mission",
        "/product/t10-la-foire-aux-mille-prix",
    }
    for product_href in expected_choice_products:
        if chooser.count(f'href="{product_href}"') != 1:
            fail(
                "Quel_tome_choisir.html: bouton produit manquant ou dupliqué "
                f"pour {product_href}",
                failures,
            )
    expected_choice_images = {
        "t01-les-marchands-de-chandelles-0-lNLeCL",
        "t02-la-vitre-magique-0-VEHUVy",
        "t03-la-grande-fabrique-des-regles-0-g3lM2t",
        "t04-le-mysterieux-argent-de-papier-0-RG5sJY",
        "t05-la-boussole-invisible-0-KCAt4p",
        "t06-le-ruban-de-solidarite-0-rGyO9J",
        "t07-une-histoire-de-jardin-0-080Rmw",
        "t08-le-pont-du-consentement-0-56DBHs",
        "t09-quand-le-gardien-oublie-sa-mission-0-Dsdqyt",
        "t10-la-foire-aux-mille-prix-0-xxkk0e",
    }
    chooser_images = set(re.findall(r"/picture/raw/([^/]+)/format/", chooser))
    if not expected_choice_images.issubset(chooser_images):
        fail(
            "Quel_tome_choisir.html: une ou plusieurs couvertures manquent",
            failures,
        )
    if chooser.count('class="lpldf-tome-lightbox__nav"') != 10:
        fail(
            "Quel_tome_choisir.html: chaque fiche doit permettre de comparer "
            "le tome précédent et le suivant",
            failures,
        )

    universe = (ROOT / "cms" / "Univers.html").read_text(encoding="utf-8")
    guide_links = re.findall(r'href="#(lpldf-guide-[^"]+)"', universe)
    guide_ids = re.findall(r'id="(lpldf-guide-[^"]+)"', universe)
    if len(guide_links) != 16:
        fail(
            f"Univers.html: 16 bulles de guides attendues, {len(guide_links)} trouvée(s)",
            failures,
        )
    if len(guide_ids) != 16:
        fail(
            f"Univers.html: 16 fiches de guides attendues, {len(guide_ids)} trouvée(s)",
            failures,
        )
    if set(guide_links) != set(guide_ids):
        fail("Univers.html: une bulle de guide ne cible pas sa fiche", failures)
    if universe.count("Dans la saga") != 16:
        fail("Univers.html: chaque guide doit comporter une section « Dans la saga »", failures)
    required_guide_images = {
        "lpldf-fred-transparent-png-0-4pnzMK",
        "lpldf-friedman-transparent-png-0-v3zMSm",
        "lpldf-hayek-transparent-png-0-DhFWzM",
        "lpldf-mises-transparent-png-0-pajeKd",
        "lpldf-menger-transparent-png-0-oQtUNK",
        "lpldf-salamanque-transparent-png-0-u3VrUK",
        "lpldf-daquin-transparent-png-0-YsKfUh",
        "lpldf-satoshi-transparent-png-0-jmM4Gu",
        "lpldf-hoppe-transparent-png-0-jRk1oA",
        "lpldf-rothbard-transparent-png-0-3fVjNT",
        "lpldf-tocqueville-transparent-png-0-HvDQMA",
        "lpldf-constant-transparent-png-0-zmu1CM",
        "lpldf-say-transparent-png-0-nXGlhq",
        "lpldf-turgot-transparent-png-0-8tKafe",
        "lpldf-locke-transparent-png-0-JBdSoL",
        "lpldf-scuba-transparent-png-0-5Luhei",
    }
    missing_guide_images = sorted(required_guide_images - set(re.findall(
        r"/picture/raw/([^/]+)/format/",
        universe,
    )))
    if missing_guide_images:
        fail(
            "Univers.html: image(s) de guide absente(s) " + ", ".join(missing_guide_images),
            failures,
        )
    image_registry = (ROOT / "donnees" / "REGISTRE_IMAGES_BEBOP.csv").read_text(
        encoding="utf-8"
    )
    if sum(line.startswith("guide,") for line in image_registry.splitlines()) != 15:
        fail("REGISTRE_IMAGES_BEBOP.csv: 15 portraits de guides attendus", failures)

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
    if ".lpldf-guide-lightbox" not in css or ".lpldf-guide-list a" not in css:
        fail("custom.css: présentation interactive des guides absente", failures)
    if ".lpldf-tome-lightbox" not in css or ".lpldf-choice-grid" not in css:
        fail("custom.css: présentation du comparateur de tomes absente", failures)
    if ".lpldf-return-anchor" not in css:
        fail("custom.css: positionnement des retours de visionneuse absent", failures)

    gallery_script = ROOT / "product-gallery.js"
    if not gallery_script.exists():
        fail("product-gallery.js: script de visionneuse absent", failures)
    else:
        gallery_js = gallery_script.read_text(encoding="utf-8")
        if ".aspect-video img" not in gallery_js or "displayedImage.addEventListener" not in gallery_js:
            fail("product-gallery.js: branchement sur la grande image absent", failures)
        if "a[href" in gallery_js or "ring-2" in gallery_js:
            fail("product-gallery.js: les miniatures ne doivent pas ouvrir la visionneuse", failures)
        if (
            "location.hash" in gallery_js
            or "window.location" in gallery_js
            or "scrollIntoView" in gallery_js
        ):
            fail("product-gallery.js: la fermeture ne doit pas déplacer la page", failures)

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
        validate_internal_windows(str(path.relative_to(ROOT)), parser, failures)

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
        validate_internal_windows(str(path.relative_to(ROOT)), parser, failures)

    preview_files = sorted((ROOT / "tests" / "preview").glob("*.html"))
    for path in preview_files:
        content = path.read_text(encoding="utf-8")
        parser = FragmentParser()
        parser.feed(content)
        parser.close()
        validate_internal_windows(str(path.relative_to(ROOT)), parser, failures)

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
    print(f"- {len(guide_ids)} fiches de guides reliées à leurs bulles")
    print(f"- {len(choice_ids)} fiches de tomes reliées au comparateur")
    print(f"- {css_window_count} fenêtres CSS contrôlées avec leur retour de section")
    print("- CSS équilibré, badge de test absent")
    print("- Aucun placeholder d’image restant hors juridique")
    return 0


if __name__ == "__main__":
    sys.exit(main())
