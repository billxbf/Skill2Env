import type { AuditContext } from '../../types.js';
import { defineRule, pass, warn } from '../define-rule.js';
import { collectVisibleText } from './utils/visible-text.js';

/** Markdown that reached the reader as characters instead of formatting. */
const MARKDOWN = [
  /\*\*[^*\n]{1,120}\*\*/,
  /__[^_\n]{1,120}__/,
  /\[[^\]\n]{1,120}\]\((?:https?:\/\/|\/)[^)\s]+\)/,
  /!\[[^\]]*\]\([^)\s]+\)/,
];

const SAMPLE_LIMIT = 3;

/**
 * Rule: Unrendered Markdown in visible text
 *
 * A CMS that prints a Markdown field as text leaves **bold** and
 * [label](url) on the page. Text inside code and pre is ignored.
 */
export const unrenderedMarkupRule = defineRule({
  id: 'content-unrendered-markup',
  name: 'Unrendered Markup',
  description: 'Checks visible text for Markdown that was printed instead of rendered',
  category: 'content',
  weight: 6,
  run: (context: AuditContext) => {
    const samples: string[] = [];

    for (const chunk of collectVisibleText(context.$)) {
      const match = MARKDOWN.map((pattern) => chunk.match(pattern)?.[0]).find(Boolean);
      if (!match) continue;
      samples.push(match);
      if (samples.length >= SAMPLE_LIMIT) break;
    }

    if (samples.length === 0) {
      return pass('content-unrendered-markup', 'No unrendered Markdown in visible text', {
        samples: [],
      });
    }

    return warn(
      'content-unrendered-markup',
      `Visible text contains unrendered Markdown: ${samples.join('; ')}`,
      {
        samples,
        recommendation:
          'Render the field as HTML before publishing, or stop storing Markdown in a plain-text slot.',
      }
    );
  },
});
