/*
 * quora-extract.js — open every fold on a Quora page, then read it out flat.
 *
 * Runs in the page, in your own logged-in browser. Two jobs, in order:
 *
 *   1. EXPAND to a fixpoint. Quora folds the same conversation in at least three
 *      independent mechanisms (answer truncation, comment collapse, nested-reply
 *      collapse), and opening one reveals more of the others. So: click every
 *      expander, wait, look again, repeat until a round finds nothing new.
 *
 *   2. EXTRACT. Best effort, and deliberately a distant second. Quora's class
 *      names are obfuscated and rot; the expansion loop matches on visible label
 *      text, which is stable because it is the product. If the structured parse
 *      degrades, `text` is still the fully expanded page and that is the 90%.
 *
 * Entry points, all attached to window:
 *   __quoraExpand()   -> Promise<{rounds, clicked}>   expand only
 *   __quoraExtract()  -> {url, question, answers, comments, text}
 *   __quoraHarvest()  -> Promise<record>              expand then extract
 *   __quoraMarkdown() -> Promise<string>              record as Markdown
 *   __quoraCopy()     -> Promise<void>                Markdown to clipboard
 *
 * Paste into the devtools console, or load via scripts/quora_harvest.py.
 */

(function () {
  'use strict';

  const CONFIG = {
    maxRounds: 40,
    settleMs: 450,
    clickGapMs: 60,
    maxLabelLength: 48,
  };

  /* Labels on things that hide content. Matched against trimmed textContent of
   * short, clickable elements. Add to this list when Quora invents a new fold —
   * it is the only part of the file that should need touching. */
  const EXPANDERS = [
    /^\(?\s*more\s*\)?$/i,
    /^continue reading$/i,
    /^read more$/i,
    /^view\s+\d+[\d,.KM\s]*(more\s+)?(comments?|replies|answers?)$/i,
    /^view\s+more\s+(comments?|replies|answers?)$/i,
    /^\d+[\d,.KM]*\s+(comments?|replies)$/i,
    /^see\s+(more|all)(\s+\w+)?$/i,
    /^show\s+more(\s+\w+)?$/i,
    /^load\s+more(\s+\w+)?$/i,
    /^\d+\s+more\s+\w+$/i,
  ];

  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  function isVisible(el) {
    if (!el || !el.isConnected) return false;
    const rect = el.getBoundingClientRect();
    if (rect.width === 0 && rect.height === 0) return false;
    const style = getComputedStyle(el);
    return style.visibility !== 'hidden' && style.display !== 'none';
  }

  /* Clickable enough: Quora uses div soup, so accept the affordances it actually
   * emits (pointer cursor, click wrapper, button role) as well as real buttons. */
  function looksClickable(el) {
    const tag = el.tagName;
    if (tag === 'BUTTON' || tag === 'A') return true;
    if (el.getAttribute('role') === 'button') return true;
    if (el.hasAttribute('tabindex')) return true;
    const cls = typeof el.className === 'string' ? el.className : '';
    if (/q-click-wrapper|cursor--pointer|qu-cursor--pointer/.test(cls)) return true;
    return getComputedStyle(el).cursor === 'pointer';
  }

  function ownLabel(el) {
    const text = (el.textContent || '').replace(/\s+/g, ' ').trim();
    if (!text || text.length > CONFIG.maxLabelLength) return null;
    return text;
  }

  function findExpanders() {
    const found = [];
    const seen = new Set();
    for (const el of document.querySelectorAll('div, span, button, a')) {
      const label = ownLabel(el);
      if (!label) continue;
      if (!EXPANDERS.some((re) => re.test(label))) continue;
      if (!isVisible(el) || !looksClickable(el)) continue;
      /* Prefer the innermost match: skip an ancestor of something already found. */
      if (found.some((prev) => el.contains(prev.el))) continue;
      const key = label + '@' + Math.round(el.getBoundingClientRect().top) +
        ',' + Math.round(el.getBoundingClientRect().left);
      if (seen.has(key)) continue;
      seen.add(key);
      found.push({ el, label });
    }
    return found;
  }

  async function expand() {
    const clicked = [];
    let rounds = 0;
    for (; rounds < CONFIG.maxRounds; rounds++) {
      const targets = findExpanders();
      if (targets.length === 0) break;
      let clickedThisRound = 0;
      for (const { el, label } of targets) {
        if (!el.isConnected) continue;
        try {
          el.scrollIntoView({ block: 'center', behavior: 'instant' });
          el.click();
          clicked.push(label);
          clickedThisRound++;
          await sleep(CONFIG.clickGapMs);
        } catch (err) {
          /* A stale node or a wrapper that swallows clicks. Keep going — a
           * partially expanded page still beats the folded one. */
        }
      }
      if (clickedThisRound === 0) break;
      await sleep(CONFIG.settleMs);
    }
    return { rounds, clicked };
  }

  /* ---- extraction (best effort; see header) ---- */

  function cleanText(el) {
    if (!el) return '';
    return (el.innerText || el.textContent || '')
      .replace(/\u00a0/g, ' ')
      .split('\n')
      .map((line) => line.replace(/[ \t]+$/g, ''))
      .join('\n')
      .replace(/\n{3,}/g, '\n\n')
      .trim();
  }

  function profileName(link) {
    const name = (link.textContent || '').replace(/\s+/g, ' ').trim();
    if (name) return name;
    const m = (link.getAttribute('href') || '').match(/\/profile\/([^/?#]+)/);
    return m ? decodeURIComponent(m[1]).replace(/-/g, ' ') : '';
  }

  /* A comment is the smallest box holding both a profile link and a permalink
   * to itself (/comment/... or ?comment_id=...). That pairing is structural
   * rather than cosmetic, so it survives class renames. */
  function extractComments() {
    const permalinks = Array.from(
      document.querySelectorAll('a[href*="/comment/"], a[href*="comment_id="]')
    );
    const records = [];
    const claimed = new Set();
    for (const link of permalinks) {
      let box = link.parentElement;
      let host = null;
      for (let depth = 0; box && depth < 12; depth++, box = box.parentElement) {
        if (box.querySelector('a[href*="/profile/"]')) { host = box; break; }
      }
      if (!host || claimed.has(host)) continue;
      claimed.add(host);
      const author = host.querySelector('a[href*="/profile/"]');
      records.push({
        author: author ? profileName(author) : '',
        author_url: author ? author.href : '',
        permalink: link.href,
        when: (link.textContent || '').trim(),
        text: cleanText(host),
      });
    }
    return records;
  }

  function extractAnswers() {
    const blocks = Array.from(
      document.querySelectorAll('[class*="spacing_log_answer_content"], [class*="AnswerBase"]')
    ).filter(isVisible);
    const bodies = blocks.length ? blocks : Array.from(document.querySelectorAll('article'));
    return bodies.map((el) => ({ text: cleanText(el) })).filter((a) => a.text.length > 80);
  }

  function extract() {
    const heading = document.querySelector('h1, [class*="puppeteer_test_question_title"]');
    return {
      url: location.href,
      captured_at: new Date().toISOString(),
      question: heading ? cleanText(heading) : '',
      title: document.title,
      answers: extractAnswers(),
      comments: extractComments(),
      text: cleanText(document.body),
    };
  }

  function toMarkdown(rec) {
    const out = [];
    out.push('# ' + (rec.question || rec.title));
    out.push('');
    out.push('**Source:** <' + rec.url + '>  ');
    out.push('**Captured:** ' + rec.captured_at);
    out.push('');
    rec.answers.forEach((a, i) => {
      out.push('## Answer ' + (i + 1));
      out.push('');
      out.push(a.text);
      out.push('');
    });
    if (rec.comments.length) {
      out.push('## Comments (' + rec.comments.length + ')');
      out.push('');
      for (const c of rec.comments) {
        const who = c.author || 'unknown';
        const when = c.when ? ' · ' + c.when : '';
        out.push('### ' + who + when + (c.permalink ? ' · [permalink](' + c.permalink + ')' : ''));
        out.push('');
        out.push(c.text);
        out.push('');
      }
    }
    out.push('## Full expanded page text');
    out.push('');
    out.push('```');
    out.push(rec.text);
    out.push('```');
    return out.join('\n');
  }

  async function harvest() {
    const expansion = await expand();
    const rec = extract();
    rec.expansion = expansion;
    return rec;
  }

  window.__quoraExpand = expand;
  window.__quoraExtract = extract;
  window.__quoraHarvest = harvest;
  window.__quoraMarkdown = async () => toMarkdown(await harvest());
  window.__quoraToMarkdown = toMarkdown;
  window.__quoraCopy = async () => {
    const md = await window.__quoraMarkdown();
    await navigator.clipboard.writeText(md);
    console.log('quora-harvest: ' + md.length + ' chars on the clipboard');
  };

  console.log('quora-harvest loaded. __quoraCopy() expands everything and copies Markdown.');
})();
