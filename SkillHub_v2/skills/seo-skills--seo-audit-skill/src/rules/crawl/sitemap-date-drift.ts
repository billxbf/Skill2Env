import type { AuditContext } from '../../types.js';
import { defineRule, notMeasured, pass, warn } from '../define-rule.js';
import { extractJsonLdScripts, extractTypedItems } from '../schema/utils.js';

function day(value: unknown): string | null {
  if (typeof value !== 'string') return null;
  const match = value.match(/\d{4}-\d{2}-\d{2}/);
  return match ? match[0] : null;
}

function sameResource(left: string, right: string): boolean {
  try {
    const a = new URL(left);
    const b = new URL(right);
    const path = (value: string) => (value.length > 1 && value.endsWith('/') ? value.slice(0, -1) : value);
    return a.origin === b.origin && path(a.pathname) === path(b.pathname);
  } catch {
    return left === right;
  }
}

/**
 * Rule: Sitemap lastmod versus schema dateModified
 *
 * When both dates exist and name different days, one of them is wrong.
 * A page with only one of the two dates passes. A missing sitemap is unmeasured.
 */
export const sitemapDateDriftRule = defineRule({
  id: 'crawl-sitemap-date-drift',
  name: 'Sitemap Date Drift',
  description: 'Checks that sitemap lastmod and schema dateModified fall on the same day',
  category: 'crawl',
  weight: 4,
  run: (context: AuditContext) => {
    if (!context.sitemapEntries) {
      return notMeasured(
        'crawl-sitemap-date-drift',
        'Sitemap entries were not fetched, so lastmod cannot be compared with dateModified'
      );
    }

    let modified: string | null = null;
    for (const script of extractJsonLdScripts(context.$)) {
      for (const item of extractTypedItems(script)) {
        modified = day(item.data.dateModified);
        if (modified) break;
      }
      if (modified) break;
    }

    const entry = context.sitemapEntries.find((item) => sameResource(item.loc, context.url));
    const lastmod = day(entry?.lastmod);

    if (!modified || !lastmod) {
      return pass('crawl-sitemap-date-drift', 'No lastmod and dateModified pair to compare', {
        modified,
        lastmod,
      });
    }

    if (modified === lastmod) {
      return pass('crawl-sitemap-date-drift', `lastmod and dateModified are both ${modified}`, {
        modified,
        lastmod,
      });
    }

    return warn(
      'crawl-sitemap-date-drift',
      `Sitemap lastmod ${lastmod} disagrees with schema dateModified ${modified}`,
      {
        modified,
        lastmod,
        recommendation: 'Make lastmod and dateModified the same day, or stop publishing the one that is stale.',
      }
    );
  },
});
