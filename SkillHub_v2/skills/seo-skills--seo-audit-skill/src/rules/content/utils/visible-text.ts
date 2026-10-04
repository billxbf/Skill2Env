import type { CheerioAPI } from 'cheerio';

/** Elements whose text is not page copy a visitor reads. */
const SKIP = 'script, style, noscript, textarea, svg, template, pre, code';

/**
 * Visible text nodes under body, skipping code, scripts, and stylesheets.
 *
 * @param $ - Parsed page
 * @returns One string per text node that survived the skip list
 */
export function collectVisibleText($: CheerioAPI): string[] {
  const chunks: string[] = [];

  const visit = (root: ReturnType<CheerioAPI>) => {
    root.contents().each((_, node) => {
      if (node.type !== 'text') return;
      const parent = node.parent;
      if (!parent || parent.type !== 'tag') return;
      if ($(parent).closest(SKIP).length > 0) return;
      const text = node.data ?? '';
      if (text.trim().length > 0) chunks.push(text);
    });
  };

  visit($('body'));
  $('body *').each((_, el) => {
    visit($(el));
  });

  return chunks;
}
