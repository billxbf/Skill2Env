import { describe, expect, it } from 'vitest';
import type { SiteContext, SitePageInfo } from '../../types.js';
import { createTestContext } from '../test-context.js';
import { canonicalFormDriftRule } from './canonical-form-drift.js';
import { sitemapDateDriftRule } from './sitemap-date-drift.js';

function site(canonicals: Record<string, string>): SiteContext {
  const pages = new Map<string, SitePageInfo>();
  for (const [url, canonical] of Object.entries(canonicals)) {
    pages.set(url, {
      statusCode: 200,
      canonical,
      noindex: false,
      nofollow: false,
      disallowed: false,
      hreflangOut: {},
    });
  }
  return {
    entryUrl: 'https://example.com/',
    pageCount: pages.size,
    depthByUrl: new Map(),
    inboundLinksByUrl: new Map(),
    outboundLinksByUrl: new Map(),
    pages,
    normalize: (url) => url,
  };
}

describe('crawl-canonical-form-drift', () => {
  it('is not measured without a crawl', async () => {
    const result = await canonicalFormDriftRule.run(createTestContext('<html></html>'));
    expect(result.status).toBe('not-measured');
  });

  it('passes when every canonical uses the same form', async () => {
    const result = await canonicalFormDriftRule.run(
      createTestContext('<html></html>', {
        site: site({
          'https://example.com/': 'https://example.com/',
          'https://example.com/about': 'https://example.com/about',
        }),
      })
    );
    expect(result.status).toBe('pass');
  });

  it('warns when canonicals mix www and the apex', async () => {
    const result = await canonicalFormDriftRule.run(
      createTestContext('<html></html>', {
        site: site({
          'https://example.com/': 'https://example.com/',
          'https://example.com/about': 'https://www.example.com/about',
        }),
      })
    );
    expect(result.status).toBe('warn');
  });
});

describe('crawl-sitemap-date-drift', () => {
  it('is not measured without sitemap entries', async () => {
    const result = await sitemapDateDriftRule.run(createTestContext('<html></html>'));
    expect(result.status).toBe('not-measured');
  });

  it('warns when lastmod and dateModified name different days', async () => {
    const html = `<html><body>
      <script type="application/ld+json">{"@type":"Article","dateModified":"2024-01-02"}</script>
    </body></html>`;
    const result = await sitemapDateDriftRule.run(
      createTestContext(html, {
        sitemapEntries: [{ loc: 'https://example.com/', lastmod: '2020-05-01' }],
      })
    );
    expect(result.status).toBe('warn');
  });

  it('passes when the days match', async () => {
    const html = `<html><body>
      <script type="application/ld+json">{"@type":"Article","dateModified":"2024-01-02T10:00:00Z"}</script>
    </body></html>`;
    const result = await sitemapDateDriftRule.run(
      createTestContext(html, {
        sitemapEntries: [{ loc: 'https://example.com/', lastmod: '2024-01-02' }],
      })
    );
    expect(result.status).toBe('pass');
  });
});
