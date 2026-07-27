import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const out = path.join(root, 'tests', 'preview');
fs.mkdirSync(out, { recursive: true });

const css = fs.readFileSync(path.join(root, 'custom.css'), 'utf8');
const cms = fs
  .readFileSync(path.join(root, 'cms', 'Home.html'), 'utf8')
  .replace(/<style>[\s\S]*?<\/style>\s*/m, '')
  .replaceAll('src="/picture/', 'src="https://xn--lespetitesleonsdefrdric-89b1db.fr/picture/')
  .replace(
    /<p>\[Product=pack-decouverte-t00-t04\?display=img-1\]<\/p>/g,
    `<article class="tagWidget tagWidget-main">
      <img src="https://xn--lespetitesleonsdefrdric-89b1db.fr/picture/raw/pack-decouverte-bastiat-t00-a-t04-0-Ex6zm4/format/1024?v=1" alt="Pack Découverte">
      <div style="padding:18px"><h3>Pack Découverte Bastiat — T00 à T04</h3><strong>40 €</strong></div>
    </article>`
  )
  .replace(
    /<p>\[TagProducts=livre-papier\]<\/p>/g,
    Array.from({ length: 8 }, (_, index) => {
      const tome = String(index).padStart(2, '0');
      return `<article class="tagWidget tagWidget-main"><div style="min-height:230px;background:linear-gradient(145deg,#fff8e8,#fff);display:grid;place-items:center;color:#183247;font:700 2rem Georgia">T${tome}</div><div style="padding:18px"><h3>Tome ${tome}</h3><strong>10 €</strong></div></article>`;
    }).join('')
  )
  .replace(
    /<p>\[Slider=avis-lecteurs\?autoplay=7000\]<\/p>/g,
    '<blockquote style="margin:0;padding:34px;font:italic 1.25rem Georgia;color:#183247">« Une collection qui donne envie aux enfants de poser des questions. »</blockquote>'
  );

const shell = `<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Aperçu LPLDF V5</title>
  <style>${css}</style>
  <style>
    body{margin:0}
    .preview-header{height:84px;padding:0 4vw;display:flex;align-items:center;justify-content:space-between;background:#183247;color:#fff;font-family:Outfit,Arial}
    .preview-header strong{font-size:1.25rem}.preview-header nav{display:flex;gap:24px}
    .preview-nav{height:58px;padding:0 4vw;display:flex;align-items:center;gap:28px;background:#fff8e8;color:#183247;font-family:Outfit,Arial}
    .preview-footer{min-height:180px;padding:50px 5vw;background:#183247;color:#fff;font-family:Outfit,Arial}
  </style>
</head>
<body>
  <header class="preview-header"><strong>Les Petites Leçons de Frédéric</strong><nav><span>Ebooks</span><span>Bitcoin</span><span>Contact</span></nav></header>
  <div class="preview-nav"><span>Les Livres</span><span>Quel tome choisir ?</span><span>L’Univers</span><span>Parents & éducateurs</span></div>
  ${cms}
  <footer class="preview-footer"><strong>Les Petites Leçons de Frédéric</strong><p>Des histoires pour apprendre à penser librement.</p></footer>
</body>
</html>`;

fs.writeFileSync(path.join(out, 'home-v5.html'), shell);
console.log(path.join(out, 'home-v5.html'));
