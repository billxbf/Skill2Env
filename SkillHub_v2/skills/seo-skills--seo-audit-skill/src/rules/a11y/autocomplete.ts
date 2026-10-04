import type { AuditContext } from '../../types.js';
import { defineRule, pass, warn } from '../define-rule.js';

const EXPECTED: Record<string, string> = {
  email: 'email',
  tel: 'tel',
};

/**
 * Rule: Autocomplete tokens on email and telephone fields
 *
 * A missing or wrong autocomplete token makes the browser offer the wrong
 * saved value. Other input types are left to form-label checks.
 */
export const autocompleteRule = defineRule({
  id: 'a11y-autocomplete',
  name: 'Autocomplete Tokens',
  description: 'Checks that email and tel inputs set the matching autocomplete token',
  category: 'a11y',
  weight: 3,
  run: (context: AuditContext) => {
    const missing: Array<{ type: string; name?: string }> = [];

    context.$('input[type="email"], input[type="tel"]').each((_, el) => {
      const node = context.$(el);
      const type = (node.attr('type') || '').toLowerCase();
      const expected = EXPECTED[type];
      if (!expected) return;
      const tokens = (node.attr('autocomplete') || '').toLowerCase().split(/\s+/).filter(Boolean);
      if (tokens.includes(expected)) return;
      missing.push({ type, ...(node.attr('name') ? { name: node.attr('name') } : {}) });
    });

    if (missing.length === 0) {
      return pass('a11y-autocomplete', 'Email and telephone inputs set autocomplete, or the page has none', {
        missing: [],
      });
    }

    return warn(
      'a11y-autocomplete',
      `${missing.length} email or telephone input(s) are missing the matching autocomplete token`,
      {
        missing,
        recommendation: 'Set autocomplete="email" on email fields and autocomplete="tel" on telephone fields.',
      }
    );
  },
});
