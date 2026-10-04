# Angle examples

Filled examples in the output format from SKILL.md. Prospect names and companies are illustrative; in real use, every fact must come from a supplied or verified signal - never from these examples.

## Good - B2B, hiring signal

Context: the user sells onboarding software for sales teams.

```
### Angle 1 - Hiring and job postings
- Signal: Acme has 4 open SDR roles on its careers page (careers page, seen 2026-08-20)
- Inference: they are scaling outbound fast, so ramp time and inconsistent messaging across new reps are likely live problems this quarter.
- Hook: "Four open SDR roles on your careers page - that usually means ramp time just became the number your quarter depends on."
- Ask it justifies: a short call comparing how similar-stage teams cut ramp time.
- Label: verified / 5 days old
```

Why it works: dated, specific to this account, and the inference lands directly on what the user sells. It fails the swap test - the hook makes no sense sent to a company that is not hiring SDRs.

## Good - B2B, leadership change

Context: the user sells revenue analytics.

```
### Angle 2 - Leadership and role changes
- Signal: Priya Rao started as VP Revenue Operations at Northwind last month (professional-network announcement, 2026-07-28)
- Inference: a new RevOps leader typically audits reporting in the first 90 days and needs an early, visible win.
- Hook: "Congrats on the new seat - most RevOps leaders tell us the first thing they inherit is a forecast nobody trusts."
- Ask it justifies: an offer to share a first-90-days reporting audit checklist, no meeting required.
- Label: verified / 4 weeks old
```

Why it works: the congratulations is attached to a consequence and a problem, and the ask is sized to the relationship (a give, not a demo demand).

## Good - B2C, lifecycle signal

Context: an online coffee retailer messaging its own customers.

```
### Angle 1 - Purchase behaviour
- Signal: customer ordered a 250g bag of the same roast on the 3rd of each of the last 3 months (order history, first-party)
- Inference: they are on a ~30-day replenishment cycle and are about 5 days from running out.
- Hook: trigger a replenishment message ~25 days after each order - "About time for a restock?" - with their usual roast pre-filled.
- Ask it justifies: one-tap reorder; optionally introduce a subscription with a small incentive.
- Label: verified first-party / current
```

Why it works: the "angle" is a segment trigger plus timing, not a hand-written line - the correct B2C shape. It uses only data the customer gave the business directly.

## Bad - funding congratulations with no connection

Context: the user sells design software; the prospect's company raised a Series B.

```
### Angle - Funding and financial events (REJECTED)
- Signal: Contoso raised a $30M Series B (press coverage, 2026-08-01)
- Inference: none stated.
- Hook: "Congrats on the Series B - exciting times ahead!"
- Ask it justifies: "would love to connect."
- Label: verified / 3 weeks old
```

Why it fails: the signal is real, but there is no inference - it flunks the so-what test. From the prospect's seat: "so what?" Nothing links the round to a design problem, and the hook passes the swap test (any funded company could receive it verbatim).

Discard, or repair it by finding the consequence: if the round funds a product-team hiring wave and the user sells design collaboration, _that_ chain passes.

## Bad - personal trivia as an angle

```
### Angle - Relationship signals (REJECTED)
- Signal: prospect attended the same university as the sender (public profile)
- Inference: none possible about a business problem.
- Hook: "Saw you went to Oakfield too - small world!"
- Ask it justifies: nothing; the ask that follows will be unrelated to the observation.
- Label: verified / not applicable
```

Why it fails: this is the canonical practitioner example of a fake angle - flattery or trivia followed by an unrelated pitch. It proves research happened without giving the prospect a reason to care. A genuine mutual-connection angle needs a person who can actually vouch, tied to a relevant ask.

## Bad - B2C creepy over-familiarity

```
### Angle - Browsing and engagement (REJECTED)
- Signal: customer viewed the same jacket 11 times this week (on-site analytics, first-party)
- Hook: "We noticed you've looked at this jacket 11 times!"
```

Why it fails: the underlying signal is legitimate first-party data and the interest is real - but the hook surfaces the surveillance instead of the interest. Repair, not discard: "Still thinking about the [jacket]? It's back in your size." Same signal, same trigger, no count, no watching-you framing.
