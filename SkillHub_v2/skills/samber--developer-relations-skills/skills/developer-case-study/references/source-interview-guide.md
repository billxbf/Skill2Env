# Source interview guide

How to prepare, run and mine the interview a technical case study is built from. The call is the whole raw material: a study cannot be rescued in editing if the interview produced adjectives instead of mechanisms and numbers.

## Table of Contents

- [Before the call](#before-the-call)
- [Recording](#recording)
- [Borrow the Mom Test discipline](#borrow-the-mom-test-discipline)
- [Question ladder](#question-ladder)
- [Manager or platform-owner add-ons](#manager-or-platform-owner-add-ons)
- [During the call](#during-the-call)
- [After the call](#after-the-call)
- [Disqualifying signals](#disqualifying-signals)

## Before the call

Reconstruct the story from what you already hold, then use the call to confirm and correct:

- Support threads and issues the adopter filed - the before-state pain, in their words, already timestamped.
- Migration pull requests, public repos, their changelog.
- Usage telemetry on your side: when volume moved, when error rates dropped.
- Account or community notes: who championed it, what nearly blocked it.
- Their own engineering blog, conference talks, job posts - often describes the surrounding stack.

Send an agenda and one warning: "bring the dashboard numbers from before and after". An engineer who has not looked at the old dashboard cannot produce a baseline from memory.

Book the implementing engineer for an hour, and their manager or platform owner separately for twenty minutes. In a joint call the hands-on voice defers, and the hands-on voice is the one readers trust.

## Recording

Ask for consent to record at the start of the call, not in advance email only, and confirm it on the recording. Keep the transcript until publication plus the approval file. Verbatim quotes are the artefact's backbone, and paraphrase drifts toward vendor register - precisely what a technical reader detects.

## Borrow the Mom Test discipline

Rob Fitzpatrick's _The Mom Test_ was written for discovery interviews with prospects, but its central rule transfers exactly: ask about specifics that already happened, never about opinions or hypotheticals.

```
Weak: "Was it much faster?" - invites a compliment.
Strong: "What did the dashboard read the week before cutover, and what does
         it read now?" - produces a number you can publish.
```

Every rung below is phrased that way on purpose.

The scope does not transfer - you are not learning whether the product is wanted, you are documenting a deployment that already happened. Take the questioning discipline and leave the framework's discovery goals behind.

## Question ladder

Run in order; each rung needs the previous one concrete.

**1. System context**

- What does this service do, and where does it sit in your architecture?
- What scale does it run at - requests, jobs, data volume, team size?
- What else is in the stack around it?

**2. Before-state**

- What was in place before, and who built it?
- How did it fail, and how often?
- Who got paged, and what did they do at 3am?
- Show me the shape of the old design - draw it if easier.

**3. Cost of the before-state**

- How much engineering time went into keeping it alive?
- What did it block on the roadmap?
- Did it ever cost revenue, customers, or an SLA?

**4. Trigger**

- What made this worth fixing _now_ rather than last year?
- Was there a specific incident, deadline or growth threshold?

**5. Alternatives**

- What else did you evaluate, including building it yourselves?
- Why was each rejected - and what did each one do better?
- What almost made you choose differently?

**6. Implementation**

- Walk me through what you built, component by component.
- What order did you do it in, and how long did each phase take?
- Who worked on it, and what were they doing instead?
- What surprised you - good or bad?
- What did you have to change in the surrounding system?

**7. Numbers**

- What did the key metric read before, and what does it read now?
- Which dashboard, log or bill does that come from?
- Over what window, and is it steady or still moving?
- Who on your team can confirm these numbers if someone asks?

**8. What it cost**

- How long was the migration, in engineer-weeks?
- Did you run both systems in parallel, and for how long?
- What broke during rollout?
- What did the team have to learn, and how long did that take?

**9. What is still unsolved**

- What parts did you deliberately not move, and why?
- What still does not work the way you want?
- What would you do differently starting today?
- Who should _not_ copy this setup?

**10. Advice to a peer**

- If an engineer at a similar company asked you about this over coffee, what would you tell them?
- What do you wish someone had told you before you started?

Rung 10 is where the publishable quote usually appears, because the engineer stops reporting and starts explaining.

## Manager or platform-owner add-ons

- What did this change about how your team operates?
- How did you justify the spend or the time?
- What would have happened if you had done nothing?
- How many teams use it now, and how did that spread?

## During the call

- Ask for the mechanism, never the adjective. "Faster" gets one follow-up: "faster from what to what, measured where?" If the second answer is still vague, note it as a qualitative claim and move on rather than inventing precision.
- Let silence run. The most useful admissions land three seconds after the answer you thought was finished.
- Read back numbers as you capture them, including the instrument, and confirm on the recording.
- Confirm name spelling and exact job title on the call. Titles change and reviewers correct them late.
- Flag the two or three sentences worth publishing as they happen: "that line about being paged twice a week - can we quote that?"
- Note anything the engineer marks as sensitive; it saves a round with their security reviewer.

## After the call

- Write the evidence ledger the same day: claim, evidence class, instrument, who can re-derive it.
- Send a short thank-you that restates the numbers you captured and asks for a correction if any are wrong. Errors surface here far more cheaply than in legal review.
- Ask for the architecture diagram they already have internally. Redrawing from memory is where most technical inaccuracies enter.

## Disqualifying signals

Stop and re-scope the artefact when you hear:

- "We're still evaluating it" - not production, no story yet.
- "We never really measured the old system" - no baseline, so no delta claim.
- "You'd have to ask marketing whether we can say that" and nobody has engaged them - handle approval before writing.
- "That was on our fork" or "we're on the unreleased build" - no reader can reproduce it.
- Every number comes from your dashboards and the customer cannot confirm any of them.
- The engineer will not be quoted and nobody else will either - it becomes an anonymised pattern write-up.
