import type { AuditContext } from '../../types.js';
import { defineRule, pass, warn } from '../define-rule.js';

/** Inline styles that remove text from view. Stylesheets are not fetched. */
const HIDDEN_STYLE =
  /display\s*:\s*none|visibility\s*:\s*hidden|font-size\s*:\s*0(?![.\d])|text-indent\s*:\s*-\d{3,}px|opacity\s*:\s*0(?:\.0+)?(?![.\d])/i;

/** Screen-reader utilities and UI that is hidden on purpose. */
const EXEMPT =
  /(?:^|\s)(?:sr-only|visually-hidden|screen-reader-text|screen-reader-only|visuallyhidden)(?:\s|$)|cookie|consent|gdpr|banner|modal|dialog|popup|drawer|offcanvas|submenu/i;

/** Ignore short labels. Cloaking that matters is a block of text. */
const MIN_CHARS = 80;

const SAMPLE_LIMIT = 3;

/**
 * Rule: Text hidden with an inline style
 *
 * Text a crawler reads and a visitor cannot see is the pattern Google's
 * hidden-text spam policy describes. Only inline styles are visible here.
 * Navigation, dialogs, and screen-reader classes are exempt.
 */
export const hiddenTextRule = defineRule({
  id: 'content-hidden-text',
  name: 'Hidden Text',
  description:
    'Checks for long text hidden with an inline style, excluding navigation, dialogs, and screen-reader text',
  category: 'content',
  weight: 6,
  run: (context: AuditContext) => {
    const { $ } = context;
    const samples: string[] = [];

    $('[style]').each((_, el) => {
      if (samples.length >= SAMPLE_LIMIT) return;
      const node = $(el);
      const style = node.attr('style') || '';
      if (!HIDDEN_STYLE.test(style)) return;
      if (node.closest('script, style, noscript, svg, template, nav, [role="navigation"], [role="dialog"], [role="menu"]').length) {
        return;
      }
      if (node.parents('[style]').toArray().some((parent) => HIDDEN_STYLE.test($(parent).attr('style') || ''))) {
        return;
      }
      const classAndId = `${node.attr('class') || ''} ${node.attr('id') || ''}`;
      if (EXEMPT.test(classAndId)) return;

      const text = node.text().replace(/\s+/g, ' ').trim();
      if (text.length < MIN_CHARS) return;
      samples.push(text.slice(0, 120));
    });

    if (samples.length === 0) {
      return pass('content-hidden-text', 'No long text hidden with an inline style', {
        samples: [],
      });
    }

    return warn(
      'content-hidden-text',
      `${samples.length} block(s) of text are hidden with an inline style`,
      {
        samples,
        recommendation:
          'Remove text that is hidden from visitors. Screen-reader text should use a dedicated class such as sr-only, which this rule ignores.',
      }
    );
  },
});
