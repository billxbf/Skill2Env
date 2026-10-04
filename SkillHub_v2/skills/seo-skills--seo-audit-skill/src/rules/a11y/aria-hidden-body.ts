import type { AuditContext } from '../../types.js';
import { defineRule, fail, pass } from '../define-rule.js';

/**
 * Rule: aria-hidden on the document
 *
 * aria-hidden="true" on html or body asks assistive technology to ignore
 * the entire page.
 */
export const ariaHiddenBodyRule = defineRule({
  id: 'a11y-aria-hidden-body',
  name: 'aria-hidden on Document',
  description: 'Checks that html and body are not aria-hidden',
  category: 'a11y',
  weight: 8,
  run: (context: AuditContext) => {
    const hidden: string[] = [];
    context.$('html, body').each((_, el) => {
      if (context.$(el).attr('aria-hidden') === 'true') {
        hidden.push(context.$(el).prop('tagName')?.toString().toLowerCase() || 'element');
      }
    });

    if (hidden.length === 0) {
      return pass('a11y-aria-hidden-body', 'html and body are not aria-hidden', { hidden: [] });
    }

    return fail(
      'a11y-aria-hidden-body',
      `aria-hidden="true" on ${hidden.join(' and ')} hides the page from assistive technology`,
      {
        hidden,
        recommendation: 'Remove aria-hidden from html and body. Hide a widget, not the document.',
      }
    );
  },
});
