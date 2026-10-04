import type { AuditContext } from '../../types.js';
import { defineRule, pass, warn } from '../define-rule.js';

const GOOGLE_TAG = /googletagmanager\.com|google-analytics\.com|gtag\s*\(|\bG-[A-Z0-9]{4,}\b|\bUA-\d+-\d+\b/;
const CONSENT = /gtag\s*\(\s*['"]consent['"]|ad_user_data|ad_personalization|ad_storage/;

/**
 * Rule: Google consent mode
 *
 * Advertising tags in the EEA expect a consent update. Pages with no Google
 * tag pass. Pages that call gtag('consent') or name the consent parameters pass.
 */
export const consentModeRule = defineRule({
  id: 'technical-consent-mode',
  name: 'Google Consent Mode',
  description: 'Checks that a page loading Google tags also includes a consent update',
  category: 'technical',
  weight: 3,
  run: (context: AuditContext) => {
    const source = context.html;
    if (!GOOGLE_TAG.test(source)) {
      return pass('technical-consent-mode', 'No Google tag found', { googleTag: false });
    }
    if (CONSENT.test(source)) {
      return pass('technical-consent-mode', 'Google tag is paired with a consent update', {
        googleTag: true,
        consent: true,
      });
    }
    return warn('technical-consent-mode', 'Google tag is present and no consent update was found', {
      googleTag: true,
      consent: false,
      recommendation:
        "Call gtag('consent', 'default', ...) with ad_storage, ad_user_data, and ad_personalization before the tag loads.",
    });
  },
});
