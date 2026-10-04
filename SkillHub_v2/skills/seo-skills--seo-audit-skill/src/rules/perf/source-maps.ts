import type { AuditContext } from '../../types.js';
import { defineRule, pass, warn } from '../define-rule.js';

const MAPPING = /sourceMappingURL\s*=\s*(\S+)/;

/**
 * Rule: Exposed source maps
 *
 * A sourceMappingURL comment or a SourceMap header points at a map anyone
 * can fetch. The map is not downloaded; the reference is enough.
 */
export const sourceMapsRule = defineRule({
  id: 'perf-source-maps',
  name: 'Exposed Source Maps',
  description: 'Checks for sourceMappingURL comments and a SourceMap response header',
  category: 'perf',
  weight: 2,
  run: (context: AuditContext) => {
    const found: string[] = [];
    const header = context.headers['sourcemap'] || context.headers['x-sourcemap'];
    if (header) found.push(`header ${header}`);

    context.$('script').each((_, el) => {
      const text = context.$(el).html() || '';
      const match = text.match(MAPPING);
      if (match && found.length < 5) found.push(match[1]);
    });

    if (found.length === 0) {
      return pass('perf-source-maps', 'No source map reference in the page or response headers', {
        found: [],
      });
    }

    return warn('perf-source-maps', `Source map reference exposed: ${found.slice(0, 3).join(', ')}`, {
      found,
      recommendation:
        'Stop publishing sourceMappingURL and the SourceMap header on production responses, or restrict the map files.',
    });
  },
});
