import type { AuditContext } from '../../types.js';
import { defineRule, pass, warn } from '../define-rule.js';

function readHeader(headers: Record<string, string>, name: string): string {
  const target = name.toLowerCase();
  for (const [key, value] of Object.entries(headers)) {
    if (key.toLowerCase() === target && value.trim()) return value.trim();
  }
  return '';
}

function hasPaymentTerms(headers: Record<string, string>): boolean {
  if (readHeader(headers, 'pay')) return true;
  if (readHeader(headers, 'crawler-price')) return true;
  if (readHeader(headers, 'x-crawler-price')) return true;
  return /payment/i.test(readHeader(headers, 'link'));
}

/**
 * Rule: Pay-per-crawl response
 *
 * A 402 with no price or payment link blocks a crawler and tells it nothing
 * about how to proceed. A 200, and a 402 that names terms, pass.
 */
export const payPerCrawlRule = defineRule({
  id: 'geo-pay-per-crawl',
  name: 'Pay-Per-Crawl Response',
  description: 'Checks that an HTTP 402 response includes payment terms',
  category: 'geo',
  weight: 3,
  run: (context: AuditContext) => {
    const terms = hasPaymentTerms(context.headers);
    if (context.statusCode !== 402) {
      return pass('geo-pay-per-crawl', 'The response is not a pay-per-crawl challenge', {
        statusCode: context.statusCode,
        terms,
      });
    }
    if (terms) {
      return pass('geo-pay-per-crawl', 'HTTP 402 includes payment terms', {
        statusCode: 402,
        terms: true,
      });
    }
    return warn('geo-pay-per-crawl', 'HTTP 402 does not say how a crawler can pay', {
      statusCode: 402,
      terms: false,
      recommendation:
        'Add a Pay or Crawler-Price header, or a Link with rel=payment, to the 402 response.',
    });
  },
});
