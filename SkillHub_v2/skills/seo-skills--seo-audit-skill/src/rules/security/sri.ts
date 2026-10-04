import type { AuditContext } from '../../types.js';
import { defineRule, pass, warn } from '../define-rule.js';

const SAMPLE_LIMIT = 8;

interface ExternalAsset {
  url: string;
  kind: 'script' | 'stylesheet';
}

function pageOrigin(pageUrl: string): string | null {
  try {
    return new URL(pageUrl).origin;
  } catch {
    return null;
  }
}

function absolute(raw: string, pageUrl: string): URL | null {
  try {
    return new URL(raw, pageUrl);
  } catch {
    return null;
  }
}

/**
 * Rule: Subresource Integrity
 *
 * A cross-origin script or stylesheet with no integrity hash can be replaced
 * by whoever controls that host. Same-origin assets are skipped.
 */
export const sriRule = defineRule({
  id: 'security-sri',
  name: 'Subresource Integrity',
  description: 'Checks that cross-origin scripts and stylesheets set an integrity hash',
  category: 'security',
  weight: 3,
  run: (context: AuditContext) => {
    const origin = pageOrigin(context.url);
    if (!origin) {
      return pass('security-sri', 'Page URL has no origin to compare assets against', {
        assets: [],
      });
    }

    const missing: ExternalAsset[] = [];
    const { $ } = context;

    const consider = (raw: string | undefined, kind: ExternalAsset['kind'], integrity: string | undefined) => {
      if (!raw || integrity?.trim()) return;
      if (/^(?:data|javascript|blob):/i.test(raw.trim())) return;
      const url = absolute(raw, context.url);
      if (!url || (url.protocol !== 'http:' && url.protocol !== 'https:')) return;
      if (url.origin === origin) return;
      if (missing.length >= SAMPLE_LIMIT) return;
      missing.push({ url: url.href, kind });
    };

    $('script[src]').each((_, el) => {
      const node = $(el);
      consider(node.attr('src'), 'script', node.attr('integrity'));
    });
    $('link[rel="stylesheet"][href]').each((_, el) => {
      const node = $(el);
      consider(node.attr('href'), 'stylesheet', node.attr('integrity'));
    });

    if (missing.length === 0) {
      return pass('security-sri', 'No cross-origin script or stylesheet is missing an integrity hash', {
        assets: [],
      });
    }

    return warn(
      'security-sri',
      `${missing.length} cross-origin asset(s) have no integrity hash`,
      {
        assets: missing,
        recommendation:
          'Add an integrity attribute with a sha384 or sha256 hash, and crossorigin="anonymous", to cross-origin scripts and stylesheets.',
      }
    );
  },
});
