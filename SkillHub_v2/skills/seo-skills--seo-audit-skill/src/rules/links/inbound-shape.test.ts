import { describe, expect, it } from 'vitest';
import type { InboundEdge, SiteContext } from '../../types.js';
import { createTestContext } from '../test-context.js';
import { chromeInboundRule } from './chrome-inbound.js';
import { weakInboundRule } from './weak-inbound.js';

const PAGE = 'https://example.com/pricing';
const ENTRY = 'https://example.com/';

function site(edges: InboundEdge[]): SiteContext {
  return {
    entryUrl: ENTRY,
    pageCount: 2,
    depthByUrl: new Map(),
    inboundLinksByUrl: new Map(),
    outboundLinksByUrl: new Map(),
    inboundEdgesByUrl: new Map([[PAGE, edges]]),
    normalize: (url) => url,
  };
}

describe('links-weak-inbound', () => {
  it('is not measured without the site graph', async () => {
    expect((await weakInboundRule.run(createTestContext('<html></html>'))).status).toBe('not-measured');
  });

  it('warns when a non-entry page has one dofollow inbound link', async () => {
    const result = await weakInboundRule.run(
      createTestContext('<html></html>', {
        url: PAGE,
        site: site([{ from: ENTRY, nofollow: false, anchor: 'Pricing', chrome: false }]),
      })
    );
    expect(result.status).toBe('warn');
  });

  it('passes the crawl entry URL', async () => {
    const result = await weakInboundRule.run(
      createTestContext('<html></html>', {
        url: ENTRY,
        site: site([{ from: PAGE, nofollow: false, anchor: 'Home', chrome: true }]),
      })
    );
    expect(result.status).toBe('pass');
  });
});

describe('links-chrome-inbound', () => {
  it('warns when every inbound link is in site chrome', async () => {
    const result = await chromeInboundRule.run(
      createTestContext('<html></html>', {
        url: PAGE,
        site: site([{ from: ENTRY, nofollow: false, anchor: 'Pricing', chrome: true }]),
      })
    );
    expect(result.status).toBe('warn');
  });

  it('passes when one inbound link is in the body', async () => {
    const result = await chromeInboundRule.run(
      createTestContext('<html></html>', {
        url: PAGE,
        site: site([
          { from: ENTRY, nofollow: false, anchor: 'Pricing', chrome: true },
          { from: 'https://example.com/blog', nofollow: false, anchor: 'See pricing', chrome: false },
        ]),
      })
    );
    expect(result.status).toBe('pass');
  });
});
