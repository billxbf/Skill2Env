import type { AuditContext } from '../../types.js';
import { defineRule, pass, warn } from '../define-rule.js';
import { extractJsonLdScripts, extractTypedItems } from '../schema/utils.js';

interface DatedSource {
  name: string;
  year: number;
}

function yearOf(value: unknown): number | null {
  if (typeof value !== 'string') return null;
  const match = value.match(/\b(19|20)\d{2}\b/);
  return match ? Number(match[0]) : null;
}

function yearInPath(url: string): number | null {
  try {
    const match = new URL(url).pathname.match(/\/(20\d{2})(?:\/|$)/);
    return match ? Number(match[1]) : null;
  } catch {
    return null;
  }
}

/**
 * Rule: Published dates disagree
 *
 * A page can state its year in schema datePublished, in a time element, and
 * in the URL. dateModified is a different fact and is not compared.
 * One source is not a disagreement.
 */
export const dateAgreementRule = defineRule({
  id: 'content-date-agreement',
  name: 'Date Agreement',
  description:
    'Checks that schema datePublished, visible time elements, and a year in the URL agree',
  category: 'content',
  weight: 5,
  run: (context: AuditContext) => {
    let published: number | null = null;
    for (const script of extractJsonLdScripts(context.$)) {
      for (const item of extractTypedItems(script)) {
        const year = yearOf(item.data.datePublished);
        if (year !== null) {
          published = year;
          break;
        }
      }
      if (published !== null) break;
    }

    const visible = new Set<number>();
    context.$('time[datetime]').each((_, el) => {
      const year = yearOf(context.$(el).attr('datetime'));
      if (year !== null) visible.add(year);
    });

    const sources: DatedSource[] = [];
    if (published !== null) sources.push({ name: 'schema datePublished', year: published });
    for (const year of visible) sources.push({ name: 'time datetime', year });
    const urlYear = yearInPath(context.url);
    if (urlYear !== null) sources.push({ name: 'URL path', year: urlYear });

    const distinct = new Set(sources.map((source) => source.year));
    const conflicts: string[] = [];

    if (published !== null && visible.size > 0 && !visible.has(published)) {
      conflicts.push(
        `schema datePublished ${published} is not among visible time years ${[...visible].join(', ')}`
      );
    }
    if (published !== null && urlYear !== null && published !== urlYear) {
      conflicts.push(`schema datePublished ${published} disagrees with URL year ${urlYear}`);
    }
    if (urlYear !== null && visible.size > 0 && !visible.has(urlYear)) {
      conflicts.push(`URL year ${urlYear} is not among visible time years ${[...visible].join(', ')}`);
    }

    if (conflicts.length === 0) {
      return pass(
        'content-date-agreement',
        distinct.size === 0
          ? 'No published-date sources to compare'
          : 'Published date sources agree',
        { sources }
      );
    }

    return warn('content-date-agreement', conflicts.join('; '), {
      sources,
      recommendation:
        'Make datePublished, the visible time element, and the year in the URL the same published year. Keep dateModified separate.',
    });
  },
});
