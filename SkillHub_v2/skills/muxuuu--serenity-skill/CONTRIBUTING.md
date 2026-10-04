# Contributing

Serenity.skill accepts contributions that improve research discipline, source quality, cross-market adaptation, examples, and local tooling.

## Good contributions

- Better source checklists for a market or sector.
- Clearer evidence standards for technology and supply-chain claims.
- Stronger examples that show normal research-partner communication.
- Deterministic scripts that use local inputs.
- Source-map updates with primary filings, exchange documents, or official company materials.

## Contribution rules

- Keep the project methodology-focused.
- Keep user-facing language plain and practical.
- Mark social/KOL material as lead generation.
- Prefer primary sources for company-specific claims.
- Avoid private information, doxxing, holdings claims, and unverified personal details.
- Avoid buy/sell commands, guaranteed-return language, and coordinated trading language.
- Avoid scripts that read secrets, access wallets, place trades, or make hidden network calls.

## Suggested PR checklist

- [ ] `python3 scripts/validate_skill.py .` passes (package structure only).
- [ ] New files are referenced from README or SKILL.md when useful.
- [ ] Company-specific examples give a research date, link material claims to sources, and explain what would change the view.
- [ ] No API keys, secrets, wallet addresses, or private data.
