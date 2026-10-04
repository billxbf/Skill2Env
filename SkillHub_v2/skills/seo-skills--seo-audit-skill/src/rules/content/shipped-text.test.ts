import { describe, expect, it } from 'vitest';
import { createTestContext } from '../test-context.js';
import { dateAgreementRule } from './date-agreement.js';
import { hiddenTextRule } from './hidden-text.js';
import { mojibakeRule } from './mojibake.js';
import { placeholderTextRule } from './placeholder-text.js';
import { staleCopyrightRule } from './stale-copyright.js';
import { unrenderedMarkupRule } from './unrendered-markup.js';

const year = new Date().getFullYear();

describe('content-mojibake', () => {
  it('passes clean text', async () => {
    const result = await mojibakeRule.run(
      createTestContext('<html><body><p>It’s a café.</p></body></html>')
    );
    expect(result.status).toBe('pass');
  });

  it('fails when a curly quote was decoded as Windows-1252', async () => {
    const broken = `<html><body><p>It\u00E2\u20AC\u2122s broken.</p></body></html>`;
    const result = await mojibakeRule.run(createTestContext(broken));
    expect(result.status).toBe('fail');
  });

  it('ignores the same sequence inside a script', async () => {
    const result = await mojibakeRule.run(
      createTestContext('<html><body><script>var s = "Itâ€™s";</script><p>Fine.</p></body></html>')
    );
    expect(result.status).toBe('pass');
  });
});

describe('content-unrendered-markup', () => {
  it('passes ordinary prose', async () => {
    const result = await unrenderedMarkupRule.run(
      createTestContext('<html><body><p>A plain sentence.</p></body></html>')
    );
    expect(result.status).toBe('pass');
  });

  it('warns on literal markdown bold', async () => {
    const result = await unrenderedMarkupRule.run(
      createTestContext('<html><body><p>See **this offer** today.</p></body></html>')
    );
    expect(result.status).toBe('warn');
  });

  it('ignores markdown inside code', async () => {
    const result = await unrenderedMarkupRule.run(
      createTestContext('<html><body><pre><code>**bold**</code></pre></body></html>')
    );
    expect(result.status).toBe('pass');
  });
});

describe('content-placeholder-text', () => {
  it('passes finished copy', async () => {
    const result = await placeholderTextRule.run(
      createTestContext('<html><body><p>Welcome to the shop.</p></body></html>')
    );
    expect(result.status).toBe('pass');
  });

  it('fails on an unrendered mustache tag', async () => {
    const result = await placeholderTextRule.run(
      createTestContext('<html><body><p>Hello {{ name }}</p></body></html>')
    );
    expect(result.status).toBe('fail');
  });

  it('warns on a visible TODO note', async () => {
    const result = await placeholderTextRule.run(
      createTestContext('<html><body><p>TODO: write the intro.</p></body></html>')
    );
    expect(result.status).toBe('warn');
  });
});

describe('content-stale-copyright', () => {
  it('passes when the footer has no copyright', async () => {
    const result = await staleCopyrightRule.run(
      createTestContext('<html><body><p>No footer year.</p></body></html>')
    );
    expect(result.status).toBe('pass');
  });

  it('passes the current year', async () => {
    const result = await staleCopyrightRule.run(
      createTestContext(`<html><body><footer>Copyright ${year}</footer></body></html>`)
    );
    expect(result.status).toBe('pass');
  });

  it('warns when the footer year is behind', async () => {
    const result = await staleCopyrightRule.run(
      createTestContext('<html><body><footer>© 2019</footer></body></html>')
    );
    expect(result.status).toBe('warn');
  });

  it('uses the end of a range', async () => {
    const result = await staleCopyrightRule.run(
      createTestContext(`<html><body><footer>© 2019-${year}</footer></body></html>`)
    );
    expect(result.status).toBe('pass');
  });
});

describe('content-date-agreement', () => {
  it('passes when there is nothing to compare', async () => {
    const result = await dateAgreementRule.run(
      createTestContext('<html><body><p>Undated.</p></body></html>')
    );
    expect(result.status).toBe('pass');
  });

  it('passes when schema and the time element share a year', async () => {
    const html = `<html><body>
      <time datetime="2024-05-01">May 2024</time>
      <script type="application/ld+json">{"@type":"Article","datePublished":"2024-05-01"}</script>
    </body></html>`;
    const result = await dateAgreementRule.run(createTestContext(html));
    expect(result.status).toBe('pass');
  });

  it('warns when the URL year and datePublished differ', async () => {
    const html = `<html><body>
      <script type="application/ld+json">{"@type":"Article","datePublished":"2024-05-01"}</script>
    </body></html>`;
    const result = await dateAgreementRule.run(
      createTestContext(html, { url: 'https://example.com/blog/2020/post' })
    );
    expect(result.status).toBe('warn');
  });
});

describe('content-hidden-text', () => {
  const long = 'This block of hidden copy is long enough to be worth a crawler reading it in full.';

  it('passes visible text', async () => {
    const result = await hiddenTextRule.run(
      createTestContext(`<html><body><p>${long}</p></body></html>`)
    );
    expect(result.status).toBe('pass');
  });

  it('warns on a long inline display:none block', async () => {
    const result = await hiddenTextRule.run(
      createTestContext(`<html><body><div style="display:none">${long}</div></body></html>`)
    );
    expect(result.status).toBe('warn');
  });

  it('ignores screen-reader text and navigation', async () => {
    const html = `<html><body>
      <span class="sr-only" style="display:none">${long}</span>
      <nav><span style="display:none">${long}</span></nav>
    </body></html>`;
    const result = await hiddenTextRule.run(createTestContext(html));
    expect(result.status).toBe('pass');
  });
});
