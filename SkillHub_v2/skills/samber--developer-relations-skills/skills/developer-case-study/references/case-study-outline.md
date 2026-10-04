# Case study outline and worked examples

Section-by-section guidance for the spine in SKILL.md, plus positive/negative pairs.

Word budgets assume a 1,200-1,800 word study. They are self-set proportions, not measured norms - the three published vendor studies measured for this skill run about 1,650, 2,100 and 2,400 words. Scale them to the material and keep sections 4, 5 and 7 dominant.

## Contents

- Section guidance
- Worked examples
- One-page summary shape
- Quote handling

## Section guidance

**1. Headline outcome (~60 words).** The change and its shape, in the first screen. Lead with the delta, not with the customer's company description. A reader who bounces here read one sentence - make it the number.

**2. The adopter and the system (~120 words).** Enough to size the situation: what the company does, what the relevant service does, its scale, the surrounding stack. Skip the boilerplate "founded in 2014, headquartered in…" - it signals a marketing artefact within one line.

**3. Before-state and its cost (~250 words).** The old design and how it failed, in mechanism terms, plus what the failure cost in engineer time, incidents or blocked roadmap. This section is what makes a reader recognise their own system; vagueness here loses them for the rest of the piece.

**4. Why this technology (~200 words).** What else was evaluated - including building it in-house - and the property that decided it. Name at least one thing an alternative did better. A section where every alternative is uniformly worse reads as fiction and costs more trust than it buys.

**5. What they built (~400 words).** Architecture with named components, the SDK or language, the sequencing, and the domain constraints that shaped it (regulatory windows, retry caps, peak-hour limits). A before/after diagram pair carries more here than any paragraph. Include code only if the adopter's engineers wrote it and cleared it; do not manufacture snippets.

**6. Results (~200 words).** Two to four numbers, each with instrument and window. Put the measurement method next to the number, not in a footnote - a reader who does not trust the setup does not read the figure.

**7. What it cost and what is unsolved (~200 words).** Covers:

- Migration effort.
- Dual-running period.
- What broke.
- What was deliberately left behind.
- What still does not work.
- Who should not copy this.

Vendor-published studies routinely skip it, which is the cheapest differentiation available to you.

**8. What is next (~70 words).** Their roadmap for the system, in their words. Doubles as an honest signal that the story is not finished.

## Worked examples

**Headline outcome**

```
Bad:  Acme is a leading provider of cloud-native retail solutions. After
      partnering with us, Acme unlocked transformative efficiency gains and
      dramatically improved reliability across their platform.
Good: Acme's checkout jobs used to fail on roughly 1 in 20 runs and needed a
      manual replay every morning. Eight weeks after moving the pipeline onto
      durable workflows, the failure rate sits at 0.1% and the morning replay
      ritual is gone.
```

The bad version has no mechanism, no number, no instrument. The good one gives a before value, an after value, a window, and a human consequence a reader recognises.

**Before-state**

```
Bad:  Their legacy system struggled to scale and created significant
      operational overhead for the engineering team.
Good: Four cron jobs  -  notify, verify-notify, collect, verify-collect  -  each
      retried against the same Postgres table with no shared state. When a
      retry storm hit during a promotion, the jobs re-notified customers
      already charged, and an engineer spent the next morning reconciling by
      hand. That happened three times in Q1.
```

**Results with provenance**

```
Bad:  Performance improved by over 300% and the team saved countless hours.
Good: Median end-to-end run time went from 42 minutes to 11 minutes, measured
      on their Grafana pipeline dashboard over the four weeks before and after
      cutover. The team estimates the removed manual replay saved about six
      engineer-hours a week; that figure is their estimate, not instrumented.
```

Note the second number is explicitly downgraded rather than dressed up as measured.

**Limitations**

```
Bad:  (section omitted)
Good: The migration took two engineers about seven weeks, five of them spent
      on backfilling in-flight jobs rather than on the new pipeline. They ran
      both systems in parallel for three weeks and paid double compute during
      that window. Their batch reconciliation job stayed on cron: it runs once
      a day, and the team saw no reason to move it. Teams whose jobs are
      short, idempotent and already reliable would not get the same return.
```

**Limitations that are really a roadmap**

```
Bad:  We plan to consolidate the orchestration layer into Python, and chat
      approvals are on the roadmap for next quarter.
Good: The orchestration layer is Go; the team that maintains it writes Python
      everywhere else, so every change to it goes through the two people who
      know both. Approvals still happen outside the system  -  the integration
      only posts notifications  -  so an on-call engineer still opens a second
      tool to unblock a run.
```

Both describe the same two facts. The first tells the reader what the vendor hopes happens next; the second tells them what they would inherit on day one. Only the second is a limitation.

**Quote**

```
Bad:  "This best-in-class solution has been a game-changer for our team,
       enabling us to deliver value faster than ever."  -  VP of Engineering
Good: "It used to wake us up twice a week. I haven't touched the runbook since
       March."  -  Priya N., Staff Engineer, Payments
```

The bad quote is unattributable to a human and unfalsifiable. The good one is specific, dated, and comes from the person who was paged.

## One-page summary shape

Derived from the approved study, never written independently:

- The headline outcome, verbatim from section 1.
- Adopter, industry, relevant scale - three lines.
- Three numbers with their instruments.
- One quote with name and title.
- One line naming the main trade-off. Keeping it in the short version is what stops the one-pager from reading like an ad.
- A single link to the full study.

## Quote handling

- Transcribe verbatim; trim only filler words, never rebuild a sentence.
- Mark cuts inside a quote with an ellipsis and never splice two answers into one quote.
- Attribute with the exact name and title confirmed on the call.
- Two quotes from different altitudes - implementer and owner - cover "it works" and "it changed how we operate".
- If the reviewer rewrites a quote into vendor register, push back once with the original, then accept their version: it is their voice to give.
- Never publish a placeholder quote. No approved quote means the study ships without one.
