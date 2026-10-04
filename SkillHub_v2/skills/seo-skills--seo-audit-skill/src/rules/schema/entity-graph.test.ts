import { describe, expect, it } from 'vitest';
import type { SchemaNodeSummary, SiteContext, SitePageInfo } from '../../types.js';
import { createTestContext } from '../test-context.js';
import { entityConflictRule } from './entity-conflict.js';
import { entityDanglingRule } from './entity-dangling.js';
import { entityTypeDriftRule } from './entity-type-drift.js';

function page(nodes?: SchemaNodeSummary[]): SitePageInfo {
  return {
    statusCode: 200,
    noindex: false,
    nofollow: false,
    disallowed: false,
    hreflangOut: {},
    ...(nodes ? { schemaNodes: nodes } : {}),
  };
}

function site(pages: Record<string, SchemaNodeSummary[] | undefined>): SiteContext {
  const map = new Map<string, SitePageInfo>();
  for (const [url, nodes] of Object.entries(pages)) map.set(url, page(nodes));
  return {
    entryUrl: 'https://example.com/',
    pageCount: map.size,
    depthByUrl: new Map(),
    inboundLinksByUrl: new Map(),
    outboundLinksByUrl: new Map(),
    pages: map,
    normalize: (url) => url,
  };
}

const ID = 'https://example.com/#organization';

describe('schema entity graph', () => {
  it('is not measured on a single-page audit', async () => {
    const result = await entityConflictRule.run(createTestContext('<html></html>'));
    expect(result.status).toBe('not-measured');
    expect(result.weight).toBe(0);
  });

  it('warns when one @id has two logos', async () => {
    const context = createTestContext('<html></html>', {
      site: site({
        'https://example.com/': [{ id: ID, types: ['Organization'], logo: 'https://example.com/a.png', refs: [] }],
        'https://example.com/about': [{ id: ID, types: ['Organization'], logo: 'https://example.com/b.png', refs: [] }],
      }),
    });
    expect((await entityConflictRule.run(context)).status).toBe('warn');
  });

  it('warns when a publisher @id is never declared', async () => {
    const context = createTestContext('<html></html>', {
      site: site({
        'https://example.com/a': [{ types: ['Article'], refs: ['https://example.com/#missing'] }],
        'https://example.com/b': [{ types: ['WebPage'], refs: [] }],
      }),
    });
    expect((await entityDanglingRule.run(context)).status).toBe('warn');
  });

  it('passes when the referenced @id is declared', async () => {
    const context = createTestContext('<html></html>', {
      site: site({
        'https://example.com/a': [{ types: ['Article'], refs: [ID] }],
        'https://example.com/b': [{ id: ID, types: ['Organization'], refs: [] }],
      }),
    });
    expect((await entityDanglingRule.run(context)).status).toBe('pass');
  });

  it('warns when one @id changes type', async () => {
    const context = createTestContext('<html></html>', {
      site: site({
        'https://example.com/a': [{ id: ID, types: ['Organization'], refs: [] }],
        'https://example.com/b': [{ id: ID, types: ['LocalBusiness'], refs: [] }],
      }),
    });
    expect((await entityTypeDriftRule.run(context)).status).toBe('warn');
  });
});
