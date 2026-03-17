#!/usr/bin/env node
/**
 * Build search index: extracts plain text from all book HTML files
 * and saves as search-index.json for fast client-side search.
 *
 * Usage: node build-search-index.js
 */

const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const booksData = JSON.parse(fs.readFileSync(path.join(__dirname, 'books_index.json'), 'utf8'));
const hongYinBooks = [15, 26, 39, 45, 46, 51];

function htmlToText(html) {
  const dom = new JSDOM(html);
  const text = dom.window.document.body.textContent || '';
  return text.replace(/\s+/g, '');
}

function extractTextFromFile(filePath) {
  const fullPath = path.join(__dirname, filePath);
  if (!fs.existsSync(fullPath)) return '';
  const html = fs.readFileSync(fullPath, 'utf8');

  const dom = new JSDOM(html);
  const doc = dom.window.document;
  const body = doc.body;
  if (!body) return '';

  // Remove scripts
  body.querySelectorAll('script').forEach(el => el.remove());

  // Remove nav images
  body.querySelectorAll('img').forEach(img => {
    const src = (img.getAttribute('src') || '').toLowerCase();
    if (src.includes('up.gif') || src.includes('left.gif') ||
        src.includes('right.gif') || src.includes('1pix.gif')) {
      const parent = img.parentElement;
      if (parent && parent.tagName === 'A') parent.remove();
      else img.remove();
    }
  });

  // Remove hr
  body.querySelectorAll('hr').forEach(el => el.remove());

  // For minghui format, extract only jingwenTitle + jingwenBody
  const jwTitle = doc.querySelector('.jingwenTitle');
  const jwBody = doc.querySelector('.jingwenBody');
  if (jwTitle && jwBody) {
    jwBody.querySelectorAll('hr').forEach(el => {
      let next = el.nextSibling;
      while (next) { let tmp = next.nextSibling; next.remove(); next = tmp; }
      el.remove();
    });
    const titleText = (jwTitle.textContent || '').replace(/\s+/g, '');
    const bodyText = (jwBody.textContent || '').replace(/\s+/g, '');
    return titleText + bodyText;
  }

  const text = (body.textContent || '').replace(/\s+/g, '');
  return text;
}

function buildIndex() {
  const index = {};
  let fileCount = 0;

  for (const book of booksData) {
    if (hongYinBooks.includes(book.id)) continue;

    const files = [];
    if (book.type === 'single') {
      files.push(book.file);
    } else if (book.chapters) {
      for (const ch of book.chapters) {
        files.push(ch.file);
      }
    }

    for (const filePath of files) {
      const text = extractTextFromFile(filePath);
      if (text) {
        index[filePath] = text;
        fileCount++;
      }
    }
  }

  const outPath = path.join(__dirname, 'search-index.json');
  fs.writeFileSync(outPath, JSON.stringify(index));
  const sizeMB = (fs.statSync(outPath).size / 1024 / 1024).toFixed(2);
  console.log(`Done! Indexed ${fileCount} files. Output: search-index.json (${sizeMB} MB)`);
}

buildIndex();
