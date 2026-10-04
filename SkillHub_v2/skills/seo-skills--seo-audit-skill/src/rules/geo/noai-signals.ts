import type { AuditContext } from '../../types.js';
import { defineRule, pass } from '../define-rule.js';

const OPT_OUT = new Set(['noai', 'noimageai']);

function directivesFrom(value: string | undefined): string[] {
  if (!value) return [];
  return value
    .split(/[,\s]+/)
    .map((token) => token.trim().toLowerCase())
    .filter((token) => OPT_OUT.has(token));
}

/**
 * Rule: noai and noimageai
 *
 * Reports the AI opt-out directives a page declares. Declaring them is a
 * policy choice, so the rule always passes. Weight stays at 1 so the report
 * can show the finding without moving the category score much.
 */
export const noaiSignalsRule = defineRule({
  id: 'geo-noai-signals',
  name: 'AI Opt-Out Directives',
  description: 'Reports noai and noimageai in robots meta tags and the X-Robots-Tag header',
  category: 'geo',
  weight: 1,
  run: (context: AuditContext) => {
    const found = new Set<string>();

    context.$('meta[name="robots" i], meta[name="googlebot" i]').each((_, el) => {
      for (const token of directivesFrom(context.$(el).attr('content'))) found.add(token);
    });

    const header = context.headers['x-robots-tag'] || context.headers['X-Robots-Tag'];
    for (const token of directivesFrom(header)) found.add(token);

    const directives = [...found];
    if (directives.length === 0) {
      return pass('geo-noai-signals', 'No noai or noimageai directive', { directives });
    }

    return pass(
      'geo-noai-signals',
      `AI opt-out declared: ${directives.join(', ')}`,
      { directives }
    );
  },
});
