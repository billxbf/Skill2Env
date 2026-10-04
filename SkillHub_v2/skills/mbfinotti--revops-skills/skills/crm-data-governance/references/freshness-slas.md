# Refresh Cadence and Freshness SLAs

## Cadence defaults by field category

Practitioner-published defaults (single-source; calibrate against the user's own decay evidence - bounce rates, conflict rates). The table is an assignment, not a menu of competing options - a field belongs to one category and inherits its cadence, so ranking the rows against each other would be false precision. The ranked choice sits one level down, in the replication pattern chosen to deliver the cadence - that ranking is made in the system-of-record rules, not here.

| Field category                        | Refresh cadence        |
| ------------------------------------- | ---------------------- |
| Email validity                        | Before send / 0-7 days |
| Title and seniority                   | Every 30-60 days       |
| Phone numbers                         | Quarterly              |
| Location / time zone                  | Quarterly              |
| Company size, growth rate             | Quarterly              |
| Industry / subindustry                | Semiannually           |
| Account hierarchy (parent/subsidiary) | Quarterly              |
| Funding and financial events          | Monthly                |
| Buying signals (intent, job postings) | Weekly or continuous   |
| Technographics                        | Every 60-90 days       |

For open-deal fields (close date, amount, next step), derive refresh SLAs from the user's own sales cycle length and state the derivation in the spec. A practical trigger: flag opportunities after 30+ days without stage progression as stale, regardless of when the fields themselves last changed.

## Last verified is not last modified

- **Last modified** only proves something changed - a correction, an unrelated edit, a sync write. **Last verified** records when the value was confirmed accurate. Track it at the field level, not the record level.
- Two companion attributes: **verification status** (how it was confirmed - human review, automated check, third-party confirmation) and **source confidence** (reliability of the confirming source).
- Pair schedule-based refresh with **trigger-based re-verification**: hard bounce, job-change signal, ownership change, ICP redefinition. One practitioner default: auto-enroll a record into re-verification 90 days after its last-verified date - a default to calibrate, not a standard.
- Cadence must be field-specific and risk-weighted; a uniform refresh cadence becomes "a vanity metric rather than a trust metric."

## B2C notes

- Behavioral and event fields are continuously written by systems: govern their schema, identity keys, and retention, not a refresh cadence.
- Consent and preference fields refresh on interaction events and legal-basis changes, and carry retention-schedule enforcement as part of their SLA.
