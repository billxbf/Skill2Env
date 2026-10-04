# Currency, Tax, and Payment

The checks that turn a correct commission calculation into a correct amount of money in the right hands.

## FX strike date

- A cross-currency commission can be converted at the conversion date, the approval date, or the payout date - three different amounts.
- The strike date is under-documented on most platforms; treat it as a per-platform verification item, never an assumption. Ask the platform, or infer it by recomputing one known line at each candidate date.
- Record the verified strike-date policy in the run scope; a run mixing lines converted at different strike dates fails the comparability gate.
- Diff the rate the platform actually applied against an independent reference rate for the strike date; a systematic spread is a finding (it may be a disclosed platform margin - verify, then document).

## Rounding

- Round to 2 decimals, at the end of the calculation, not at each step - per-step rounding compounds across hundreds of small lines.
- Per-line cent-level drift is expected and documented in the industry (a 7.50% rate can legitimately show as 7.49% or 7.51% on a single line because payouts can't split cents). Judge drift at run level against materiality, not per line.
- Verify one rounding policy applies to every line; mixed policies (some lines truncated, some rounded) indicate two calculation paths and deserve a root-cause finding.

## Minimum thresholds and carry-forward

- Sub-threshold balances roll forward to the next run - they must never be dropped. Verify last run's sub-threshold payees reappear with their balance intact.
- Real network minimums are small (examples on record: $20 network minimum, $5 platform minimum); program-side thresholds of $50-100 are common. Use whatever the program's terms state.
- A payee sitting under threshold for many consecutive runs is a dormancy signal worth surfacing, not an error.

## Payment-method fees

- Establish who bears each fee - platform, program, or partner - per payment rail (PayPal, wire, ACH/SEPA, payout providers). Fee-bearing varies by platform and rail; one documented example charges partners a per-withdrawal fee and vendors a 3.5% credit-card fee while ACH is free.
- The audit verifies the _gross_ commission; fees deducted downstream must be disclosed in the program terms, not silently netted into the commission line.
- Payment rails are deliberately not ranked here. The auditor verifies who bears each fee and does not pick the rail, and a program's rail is set by payee geography and payout size - any ordering would be false precision.

## Tax-form prerequisites

- Collect before paying, not after: **W-9** for US payees, **W-8BEN** for foreign individuals, **W-8BEN-E** for foreign entities. Platforms commonly block payout release until forms are on file - the audit blocks the same way.
- Backup withholding applies to US payees who fail to provide a valid W-9; a run paying such a payee gross is a finding.
- Expired or mismatched forms count as missing.

## US reporting thresholds (dated - re-verify before relying on them)

Current as of the 2025 US law change (OBBBA, signed July 2025); thresholds shift with legislation and inflation indexing, so re-verify each tax year:

- **1099-NEC / 1099-MISC**: $2,000 for payments made after December 31, 2025 (up from $600), inflation-indexed from 2027; royalties remain at $10.
- **1099-K** (third-party settlement organizations): reverted to $20,000 AND more than 200 transactions; the planned $600/$2,500 phase-down was repealed.
- Threshold changes alter which payees need forms and filings - re-verify W-9/W-8 coverage whenever the thresholds move.

## EU VAT and self-billing

- Affiliate commission is a marketing service. Cross-border B2B within the EU uses the **reverse charge**: the supplier invoices at 0% and the buyer self-accounts; the invoice must cite the reverse-charge basis (e.g. Article 196, Directive 2006/112/EC) and a VIES-verified VAT number.
- Major networks operate **self-billing**: the network generates the publisher's invoice on the publisher's behalf. The audit verifies the self-billed invoice matches the audited commission total for the period - it is the partner-facing artifact of the run.
- **Merchant-of-record vs agent-of-record** decides who carries the tax burden: an MoR network handles collection/self-billing; under an agent model the advertiser self-assesses VAT/GST under reverse charge and invoices the publisher supply directly. Confirm which model the program runs before judging whose ledger must show the tax.
