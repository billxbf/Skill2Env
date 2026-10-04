import type { AuditContext } from '../../types.js';
import { defineRule, fail, pass, warn } from '../define-rule.js';
import { collectVisibleText } from './utils/visible-text.js';

/** Template syntax that only makes sense before render. */
const TEMPLATE = [/\{\{[^{}]{1,80}\}\}/, /\{%[^%]{1,80}%\}/, /<%[\s\S]{1,80}%>/, /\[object Object\]/];

/** Notes left for the author, not for the reader. */
const NOTE = /\b(?:TODO|FIXME)\s*:/;

const SAMPLE_LIMIT = 3;

/**
 * Rule: Placeholder and template leftovers
 *
 * Lorem ipsum is `htmlval-lorem-ipsum`. This rule catches the other things
 * that ship when a template did not render: mustache, Liquid, ERB, a
 * stringified object, and TODO/FIXME notes in visible text.
 */
export const placeholderTextRule = defineRule({
  id: 'content-placeholder-text',
  name: 'Placeholder Text',
  description:
    'Checks visible text for unrendered template syntax and TODO or FIXME notes',
  category: 'content',
  weight: 8,
  run: (context: AuditContext) => {
    const templates: string[] = [];
    const notes: string[] = [];

    for (const chunk of collectVisibleText(context.$)) {
      const template = TEMPLATE.map((pattern) => chunk.match(pattern)?.[0]).find(Boolean);
      if (template && templates.length < SAMPLE_LIMIT) templates.push(template);
      const note = chunk.match(NOTE)?.[0];
      if (note && notes.length < SAMPLE_LIMIT) notes.push(chunk.replace(/\s+/g, ' ').trim().slice(0, 80));
    }

    if (templates.length > 0) {
      return fail(
        'content-placeholder-text',
        `Visible text contains unrendered template syntax: ${templates.join('; ')}`,
        {
          templates,
          notes,
          recommendation:
            'Render the template before the page is served. A visitor should not see {{ }}, {% %}, or [object Object].',
        }
      );
    }

    if (notes.length > 0) {
      return warn(
        'content-placeholder-text',
        `Visible text contains author notes: ${notes.join('; ')}`,
        {
          templates,
          notes,
          recommendation: 'Remove TODO and FIXME notes from published copy.',
        }
      );
    }

    return pass('content-placeholder-text', 'No template leftovers or author notes in visible text', {
      templates: [],
      notes: [],
    });
  },
});
