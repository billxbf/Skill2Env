import type { CheerioAPI } from 'cheerio';
import type { AnyNode } from 'domhandler';
import type { AuditContext } from '../../types.js';
import { defineRule, pass, warn } from '../define-rule.js';

/** Explicit role → roles that must appear on an ancestor. */
const REQUIRED_PARENT: Record<string, string[]> = {
  listitem: ['list'],
  tab: ['tablist'],
  menuitem: ['menu', 'menubar'],
  menuitemcheckbox: ['menu', 'menubar'],
  option: ['listbox'],
  treeitem: ['tree'],
};

/** Explicit role → a descendant role the widget is empty without. */
const REQUIRED_CHILD: Record<string, string> = {
  tablist: 'tab',
  menu: 'menuitem',
  menubar: 'menuitem',
  listbox: 'option',
  list: 'listitem',
  tree: 'treeitem',
};

function roleOf($: CheerioAPI, el: AnyNode): string {
  return ($(el).attr('role') || '').trim().toLowerCase();
}

function ancestorHasRole($: CheerioAPI, el: AnyNode, roles: string[]): boolean {
  let parent = $(el).parent();
  while (parent.length > 0) {
    const role = (parent.attr('role') || '').trim().toLowerCase();
    if (roles.includes(role)) return true;
    parent = parent.parent();
  }
  return false;
}

/**
 * Rule: Required ARIA parent and child roles
 *
 * Only elements that set role= are checked, so a normal ul/li is left to
 * the list-structure rule. A tab outside a tablist, or a tablist with no
 * tab, is reported.
 */
export const ariaRequiredRule = defineRule({
  id: 'a11y-aria-required',
  name: 'Required ARIA Structure',
  description: 'Checks that explicit ARIA widget roles have their required parent and child roles',
  category: 'a11y',
  weight: 4,
  run: (context: AuditContext) => {
    const { $ } = context;
    const issues: string[] = [];

    $('[role]').each((_, el) => {
      const role = roleOf($, el);
      const parents = REQUIRED_PARENT[role];
      if (parents && !ancestorHasRole($, el, parents)) {
        issues.push(`${role} is outside ${parents.join(' or ')}`);
      }
      const child = REQUIRED_CHILD[role];
      if (child) {
        const found = $(el)
          .find('[role]')
          .toArray()
          .some((node) => roleOf($, node) === child);
        if (!found) issues.push(`${role} contains no ${child}`);
      }
    });

    if (issues.length === 0) {
      return pass('a11y-aria-required', 'Explicit ARIA widgets have their required roles', {
        issues: [],
      });
    }

    return warn('a11y-aria-required', issues.slice(0, 5).join('; '), {
      issues: issues.slice(0, 10),
      total: issues.length,
      recommendation:
        'Put tab inside tablist, menuitem inside menu, option inside listbox, and give each of those widgets at least one child of the required role.',
    });
  },
});
