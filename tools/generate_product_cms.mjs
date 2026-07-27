import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const sourceDir = path.join(root, 'produits', 'papier');
const outputDir = path.join(root, 'produits', 'cms-apres-produit');
fs.mkdirSync(outputDir, { recursive: true });

const esc = (value = '') =>
  value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');

const between = (text, start, end) => {
  const from = text.indexOf(start);
  if (from < 0) return '';
  const after = from + start.length;
  const to = end ? text.indexOf(end, after) : text.length;
  return text.slice(after, to < 0 ? text.length : to).trim();
};

const paragraphs = (text) =>
  text
    .split(/\n\s*\n/)
    .map((part) => part.replace(/\s+/g, ' ').trim())
    .filter(Boolean);

const bullets = (text) =>
  text
    .split('\n')
    .map((line) => line.trim())
    .filter((line) => line.startsWith('•'))
    .map((line) => line.replace(/^•\s*/, '').replace(/;$/, ''));

const files = fs.readdirSync(sourceDir).filter((name) => /^T\d\d_.*\.txt$/.test(name)).sort();

for (const file of files) {
  const raw = fs.readFileSync(path.join(sourceDir, file), 'utf8');
  const title = between(raw, 'NOM DU PRODUIT\n', '\n\nSLUG');
  const slug = between(raw, 'SLUG\n', '\n\nPRIX');
  const description = between(raw, '--- DÉBUT ---', '--- FIN ---');
  const intro = between(description, '', '\n\nAu cœur de cette aventure');
  const introParts = paragraphs(intro);
  const quoteIndex = introParts.findIndex((part) => /^«.*»$/.test(part));
  const quote = quoteIndex >= 0 ? introParts[quoteIndex] : '';
  const hookParts = introParts.filter((_, index) => index !== quoteIndex);
  const heart = paragraphs(
    between(description, 'Au cœur de cette aventure', '\n\nCe que l’enfant apprend à faire')
  );
  const learn = bullets(
    between(description, 'Ce que l’enfant apprend à faire', '\n\nLa leçon ne prend jamais')
  );
  const parent = paragraphs(
    between(description, 'Une seconde lecture pour les parents', '\n\nLe guide et l’inspiration du tome')
  ).filter((part) => !part.startsWith('Après la lecture'));
  const guide = paragraphs(
    between(description, 'Le guide et l’inspiration du tome', '\n\nTrois questions pour prolonger la lecture')
  );
  const questions = bullets(
    between(description, 'Trois questions pour prolonger la lecture', '\n\nCe que contient l’album')
  );
  const contents = bullets(
    between(description, 'Ce que contient l’album', '\n\nInformations bibliographiques')
  );
  const info = bullets(
    between(description, 'Informations bibliographiques', '\n\nÀ qui offrir ce livre ?')
  );
  const isbn = info.find((item) => item.startsWith('ISBN :'))?.replace('ISBN :', '').trim() ?? '';
  const tome = info.find((item) => item.startsWith('Tome :'))?.replace('Tome :', '').trim() ?? '';

  const html = `<style>
@import url("https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css");
</style>

<section class="lpldf-product-extra" aria-label="En savoir plus sur ${esc(title)}">
  <div class="lpldf-product-extra__intro">
    <div class="lpldf-shell lpldf-product-extra__grid">
      <div>
        <p class="lpldf-eyebrow">Dans cette aventure</p>
        <h2>${esc(hookParts[0] || title)}</h2>
        <p>${esc(heart[0] || hookParts[1] || '')}</p>
        ${quote ? `<blockquote class="lpldf-product-extra__quote">${esc(quote)}</blockquote>` : ''}
      </div>
      <div class="lpldf-product-extra__facts">
        <div class="lpldf-product-extra__fact"><span>Âge conseillé</span><strong>Dès 7 ans</strong></div>
        <div class="lpldf-product-extra__fact"><span>Format</span><strong>Album carré · 38 pages</strong></div>
        <div class="lpldf-product-extra__fact"><span>Lecture</span><strong>Autonome ou accompagnée</strong></div>
        <div class="lpldf-product-extra__fact"><span>ISBN</span><strong>${esc(isbn)}</strong></div>
      </div>
    </div>
  </div>

  <div class="lpldf-product-extra__body">
    <div class="lpldf-shell">
      <div class="lpldf-product-extra__cards">
        <article class="lpldf-product-extra__card">
          <span aria-hidden="true">01</span>
          <h3>Ce que l’enfant apprend</h3>
          <ul>${learn.map((item) => `<li>${esc(item)}</li>`).join('')}</ul>
        </article>
        <article class="lpldf-product-extra__card">
          <span aria-hidden="true">02</span>
          <h3>Une seconde lecture</h3>
          <p>${esc(parent[0] || '')}</p>
        </article>
        <article class="lpldf-product-extra__card">
          <span aria-hidden="true">03</span>
          <h3>Dans l’album</h3>
          <ul>${contents.slice(0, 4).map((item) => `<li>${esc(item)}</li>`).join('')}</ul>
        </article>
      </div>

      <div class="lpldf-product-extra__questions">
        <p class="lpldf-eyebrow">Après la dernière page</p>
        <h3>Trois questions pour prolonger la lecture</h3>
        <ol>${questions.map((item) => `<li>${esc(item)}</li>`).join('')}</ol>
      </div>

      <div class="lpldf-product-extra__meta">
        <span>Tome ${esc(tome)}</span>
        <span>${esc(guide[0] || 'Les Petites Leçons de Frédéric')}</span>
        <span>ISBN ${esc(isbn)}</span>
      </div>

      <div class="lpldf-center">
        <a class="lpldf-button lpldf-button--secondary" href="/la-collection">Voir toute la collection <span aria-hidden="true">→</span></a>
        <a class="lpldf-button" href="/quel-tome-choisir">Comparer les tomes <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>
</section>
`;

  fs.writeFileSync(path.join(outputDir, `${slug}.html`), html);
}

console.log(`${files.length} blocs CMS produit générés dans ${outputDir}`);
