/**
 * GEO (Generative Engine Optimization) Rules
 *
 * This module exports all AI/GEO readiness audit rules and registers them.
 * These rules evaluate how well a page is prepared for consumption by
 * AI systems, generative search engines, and large language models.
 *
 * Includes:
 * - Semantic HTML structure for AI comprehension
 * - Content structure for reliable extraction
 * - AI bot access (robots.txt analysis)
 * - llms.txt reference (emerging standard)
 * - Schema-to-content drift detection
 */

import { registerRule } from '../registry.js';

import { semanticHtmlRule } from './semantic-html.js';
import { contentStructureRule } from './content-structure.js';
import { aiBotAccessRule } from './ai-bot-access.js';
import { llmsTxtRule } from './llms-txt.js';
import { schemaDriftRule } from './schema-drift.js';
import { contentSignalsRule } from './content-signals.js';
import { noaiSignalsRule } from './noai-signals.js';
import { agentsMdRule } from './agents-md.js';
import { wellKnownAgentRule } from './well-known.js';
import { rslLicenseRule } from './rsl-license.js';
import { markdownResponseRule } from './markdown-response.js';
import { markdownPageRule } from './markdown-page.js';
import { payPerCrawlRule } from './pay-per-crawl.js';

// Export all rules
export {
  semanticHtmlRule,
  contentStructureRule,
  aiBotAccessRule,
  llmsTxtRule,
  schemaDriftRule,
  contentSignalsRule,
  noaiSignalsRule,
  agentsMdRule,
  wellKnownAgentRule,
  rslLicenseRule,
  markdownResponseRule,
  markdownPageRule,
  payPerCrawlRule,
};

// Register all rules
registerRule(semanticHtmlRule);
registerRule(contentStructureRule);
registerRule(aiBotAccessRule);
registerRule(llmsTxtRule);
registerRule(schemaDriftRule);
registerRule(contentSignalsRule);
registerRule(noaiSignalsRule);
registerRule(agentsMdRule);
registerRule(wellKnownAgentRule);
registerRule(rslLicenseRule);
registerRule(markdownResponseRule);
registerRule(markdownPageRule);
registerRule(payPerCrawlRule);
