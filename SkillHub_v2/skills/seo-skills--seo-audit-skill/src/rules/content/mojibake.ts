import type { AuditContext } from '../../types.js';
import { defineRule, fail, pass } from '../define-rule.js';
import { collectVisibleText } from './utils/visible-text.js';

/**
 * Sequences produced when UTF-8 bytes are decoded as Latin-1 or Windows-1252.
 * A curly apostrophe (UTF-8 E2 80 99) comes back as U+00E2 U+20AC U+2122.
 * é (UTF-8 C3 A9) comes back as U+00C3 U+00A9.
 */
const MOJIBAKE =
  /\u00E2\u20AC[\u0098-\u009D\u0152\u0153\u0178\u02DC\u2018\u2019\u201C\u201D\u2122]|\u00C3[\u00A0-\u00FF]|\u00C2[\u00A0-\u00BF]|\u00EF\u00BF\u00BD|\uFFFD/;

const SAMPLE_LIMIT = 3;

/**
 * Rule: Mojibake in visible text
 *
 * A page that shows â€™ or Ã© was saved in a different encoding than the one
 * it declares. The check reads visible text only, so a script or a code
 * sample discussing the sequences does not fail the page.
 */
export const mojibakeRule = defineRule({
  id: 'content-mojibake',
  name: 'Mojibake In Visible Text',
  description:
    'Checks visible text for UTF-8 bytes that were decoded as Latin-1 or Windows-1252',
  category: 'content',
  weight: 8,
  run: (context: AuditContext) => {
    const samples: string[] = [];

    for (const chunk of collectVisibleText(context.$)) {
      if (!MOJIBAKE.test(chunk)) continue;
      MOJIBAKE.lastIndex = 0;
      samples.push(chunk.replace(/\s+/g, ' ').trim().slice(0, 120));
      if (samples.length >= SAMPLE_LIMIT) break;
    }

    if (samples.length === 0) {
      return pass('content-mojibake', 'No mojibake in visible text', {
        samples: [],
      });
    }

    return fail(
      'content-mojibake',
      `Visible text contains encoding corruption (${samples.length} sample${samples.length === 1 ? '' : 's'})`,
      {
        samples,
        recommendation:
          'Serve the HTML as UTF-8 and re-save the source as UTF-8. Typical corruption is a curly quote or accented letter decoded as Latin-1.',
      }
    );
  },
});
