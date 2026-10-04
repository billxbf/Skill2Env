export type PageKind = 'article' | 'product' | 'other';

const ARTICLE = new Set(['Article', 'NewsArticle', 'BlogPosting', 'TechArticle', 'ScholarlyArticle']);
const PRODUCT = new Set(['Product']);

/**
 * Coarse kind for comparing a page with others like it.
 * Schema type wins. The path is only a fallback.
 */
export function pageKindFrom(types: string[], url: string): PageKind {
  if (types.some((type) => ARTICLE.has(type))) return 'article';
  if (types.some((type) => PRODUCT.has(type))) return 'product';
  try {
    const path = new URL(url).pathname.toLowerCase();
    if (/\/(blog|news|articles|posts)(\/|$)/.test(path)) return 'article';
    if (/\/(product|products|shop)(\/|$)/.test(path)) return 'product';
  } catch {
    // A URL that does not parse stays "other".
  }
  return 'other';
}
