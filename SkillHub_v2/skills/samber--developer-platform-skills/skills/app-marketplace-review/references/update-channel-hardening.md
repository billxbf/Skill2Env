# Update-channel incidents and hardening controls

The 2024-2026 incident record behind this skill's central claim: the update/publish channel, not initial review, is where documented marketplace damage actually happened. Read the working rule at the bottom before citing any of it.

## The one fully attributable incident-to-change chain: npm, 2025

Two chained attacks:

1. The **Josh Junon ("Qix") maintainer phish** (September 8, 2025): phishing impersonating npm support led to a 2FA reset and malicious releases of ~18 high-profile packages including chalk, debug, ansi-styles, strip-ansi, supports-color. Blast radius: a billion-plus weekly downloads; payloads targeted browser crypto wallets.
2. The **Shai-Hulud worm** (notified September 14, 2025): the first self-replicating npm worm, compromising maintainer accounts via malicious post-install scripts, stealing secrets, and auto-republishing trojanized packages. GitHub removed 500+ malicious package versions across ~195 packages, confirmed by a CISA alert September 23, 2025.

Follow-on waves: Sha1-Hulud/"2.0" (November-December 2025) and a forced token reset ("Mini Shai-Hulud", May 19, 2026).

GitHub's response is **fully attributable and concrete**, per its own blog ("Our plan for a more secure npm supply chain", September 2025):

- Mandatory 2FA for local publishing.
- Granular tokens with a **7-day default and 90-day maximum expiration** (classic-token creation disabled, migration deadline November 19, 2025).
- Expanded **Trusted Publishing** (OIDC-based, no long-lived tokens, provenance attestations).
- Deprecation of classic tokens and TOTP in favor of FIDO-based 2FA.

GitHub reported completing this overhaul in December 2025. Notably, the worm itself used secret scanning offensively before the defensive hardening landed.

## Highest incident volume: VS Code / Visual Studio Marketplace

ReversingLabs reported malicious detections on VS Code "almost quadrupled from 27 in 2024 to 105" in the first 10 months of 2025 - still the most current confirmed full-year comparison as of this check; no superseding 2026 full-year count has been published yet, though ReversingLabs' 2026 Software Supply Chain Security Report frames the marketplace as now spanning seven distinct campaign types. Named cases:

- **`prettier-vscode-plus`** (November 21, 2025): publisher "publishingsofficial" impersonated Prettier, delivering the Anivia loader → OctoRAT, discovered by Checkmarx Zero/Hunt.io. Removed within ~4 hours after ~6 downloads - the one benchmarked case that is a fresh malicious upload rather than an update-channel compromise, and its blast radius stayed in single digits.
- **GlassWorm** (2025): a self-propagating worm documented by Koi Security, spreading through Open VSX and Microsoft's marketplace by hiding payloads in invisible Unicode characters and harvesting npm/GitHub/Git/Open VSX credentials.
- **Wiz's research** (February 2025 onward): 100+ cases of secret leakage in `.vsix` packages, including tokens that could push malicious updates to a ~150,000 cumulative install base.
- **Fake-PNG trojan campaign** (active since February 2025, discovered December 2, 2025, by ReversingLabs): 19 extensions shipped a pre-packaged `node_modules` folder with a modified `path-is-absolute` or `@actions/io` dependency that auto-executes on VS Code startup and decodes an obfuscated dropper disguised as a PNG file. Reported to Microsoft and removed.
- **Name-reuse loophole** (discovered August 2025 by ReversingLabs): an unpublished extension's name stays reserved, but a _removed_ one frees its name for reuse - attackers republished malicious code under a deleted extension's former name (the "shiba" ransomware campaign). A distinct mechanism from typosquatting or update-channel compromise: it targets the marketplace's own name-lifecycle rules.

Microsoft's response is **attributable**, per its own blog ("Security and Trust in Visual Studio Marketplace", June 11, 2025), which documents the layered pipeline:

- Multi-engine AV static scan on submit.
- A rescan shortly after publish.
- Periodic marketplace-wide bulk rescans.
- Sandbox dynamic detection.
- Community "Report a concern".
- Mandatory signature verification enforced at install.
- Impersonation prevention.
- Secret detection, shipped later in blocking mode.

Caveat that belongs next to any citation of these controls: independent researchers (Wiz; Mazin Ahmed) **demonstrated bypasses of them in 2025** - the documented controls have real-world gaps, not just theoretical ones.

## The over-attribution cautionary cases: Chrome Web Store and Shopify

**Cyberhaven** (December 24-26, 2024): a phishing email tricked an employee into granting OAuth consent to a malicious app. "The same code had been injected into at least 35 extensions collectively used by roughly 2,600,000 people" (BleepingComputer). This was a **consent-phishing / publisher-compromise attack, not a review failure**, and there is **no confirmed public evidence Google changed the Chrome Web Store's review process specifically in response to it**.

Manifest V3's ban on remotely hosted code was a separate, pre-existing multi-year rollout completed ~2024-2025 that does not address stolen-publisher-credential update pushes. Attributing a CWS review change to Cyberhaven would be speculation.

The one documented, dated CWS process change, integrating appeals into the developer dashboard, is not tied to any specific malware incident either.

**Shopify's three reported incidents:**

1. The "888" third-party data leak (2024, disclosed July 2024, ~179,873 rows, app unnamed).
2. Consentik/Omegatheme's consent-banner plugin (2025-2026, carried a "Made for Shopify" badge, quietly closed after Cybernews notification).
3. Disputifier (disclosed January 2026, 200,000+ merchant records reportedly exposed).

All **third-party-app breaches, not Shopify-review failures**. Shopify has issued no official statement attributing any 2025-2026 review-process change (expanded automated checks, AI self-review, protected-customer-data access flow) to any single one of them.

## Working rule for using this record

State incidents and process changes as **two separate claims with two separate confidence levels**:

- **"Confirmed as reported"**: the breach happened, sourced to the vendor or the primary security researcher.
- **"Causal review-process change"**: claim it only when the operator's own blog or docs state the causal link, as GitHub/npm and Microsoft/VS Marketplace do. Never infer it from timing alone, as the Cyberhaven and Shopify cases show.

## The control set, in detail

1. **Phishing-resistant (FIDO) publisher 2FA** - the Qix phish defeated TOTP-style 2FA via a reset flow. FIDO is the control the npm hardening converged on.
2. **Short-lived, scoped publish tokens** - 7-day default / 90-day maximum lifetime (the shipped npm model). A stolen token expires before most attackers use it.
3. **Publish-to-propagation hold** - 24-48 hours between a cleared update and auto-propagation to installed clients, with an operator kill switch inside the window and an expedite path for genuine security fixes. Chrome and npm's lack of exactly this hold is the gap third-party supply-chain analyses (Aikido/Nx) flag. Some third-party tools impose their own default 48-hour hold as a mitigation the stores don't provide.
4. **OIDC trusted publishing from CI/CD** - no long-lived credential exists to steal. Provenance attestations tie the artifact to the build that produced it.
5. **Signed artifacts, signature enforced at install** - survives a fully compromised publish pipeline. This is the VS Marketplace model. Highest effort: requires client-side enforcement, key management, and a revocation story.
