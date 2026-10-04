import { describe, expect, it } from 'vitest';
import { createTestContext } from '../test-context.js';
import { entityIdRule } from './entity-id.js';
import { ratingScopeRule } from './rating-scope.js';

function page(body: string, url = 'https://example.com/product') {
  return createTestContext(`<html><body>${body}</body></html>`, { url });
}

describe('schema-entity-id', () => {
  it('passes when there is no identity schema', async () => {
    const result = await entityIdRule.run(
      page('<script type="application/ld+json">{"@type":"Product","name":"Hat"}</script>')
    );
    expect(result.status).toBe('pass');
  });

  it('passes an absolute @id', async () => {
    const result = await entityIdRule.run(
      page(
        '<script type="application/ld+json">{"@type":"Organization","name":"Acme","@id":"https://example.com/#organization"}</script>'
      )
    );
    expect(result.status).toBe('pass');
  });

  it('warns when Organization has no @id', async () => {
    const result = await entityIdRule.run(
      page('<script type="application/ld+json">{"@type":"Organization","name":"Acme"}</script>')
    );
    expect(result.status).toBe('warn');
    expect(result.message).toContain('missing @id');
  });

  it('warns on a fragment @id', async () => {
    const result = await entityIdRule.run(
      page(
        '<script type="application/ld+json">{"@type":"Organization","name":"Acme","@id":"#organization"}</script>'
      )
    );
    expect(result.status).toBe('warn');
    expect(result.message).toContain('relative @id');
  });
});

describe('schema-rating-scope', () => {
  it('passes when there is no rating', async () => {
    const result = await ratingScopeRule.run(page('<p>No rating</p>'));
    expect(result.status).toBe('pass');
  });

  it('passes when the rating value is visible', async () => {
    const html = `<p>Rated 4.8 out of 5</p>
      <script type="application/ld+json">{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"10"}</script>`;
    const result = await ratingScopeRule.run(page(html));
    expect(result.status).toBe('pass');
  });

  it('warns when the rating sits on a privacy URL', async () => {
    const html = `<p>Rated 4.8</p>
      <script type="application/ld+json">{"@type":"AggregateRating","ratingValue":"4.8"}</script>`;
    const result = await ratingScopeRule.run(page(html, 'https://example.com/privacy'));
    expect(result.status).toBe('warn');
  });

  it('warns when ratingValue is not in the text', async () => {
    const html = `<p>Customers like it</p>
      <script type="application/ld+json">{"@type":"AggregateRating","ratingValue":"4.8"}</script>`;
    const result = await ratingScopeRule.run(page(html));
    expect(result.status).toBe('warn');
  });
});
