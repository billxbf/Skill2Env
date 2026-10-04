# Prep brief template

The deliverable of the skill: fill every section. An empty section means the corresponding step is unfinished, not that it does not apply.

The filled example below uses a fictional maintainer of an open-source job-queue library going on an audio-only, edited backend-engineering show.

## Table of Contents

- [Template](#template)
- [Spine (ABT)](#spine-abt)
- [Messages](#messages)
- [Opening answer](#opening-answer)
- [Story bank](#story-bank)
- [Sound bites](#sound-bites)
- [Hard questions](#hard-questions)
- [Depth rules](#depth-rules)
- [Closing call to action](#closing-call-to-action)
- [Recording-day card](#recording-day-card)
- [Promotion](#promotion)
- [Filled example (excerpt)](#filled-example-excerpt)
- [Spine (ABT)](#spine-abt)
- [Messages](#messages)
- [Opening answer](#opening-answer)
- [Story bank](#story-bank)
- [Sound bites](#sound-bites)
- [Hard questions](#hard-questions)
- [What a bad brief looks like](#what-a-bad-brief-looks-like)

## Template

```markdown
# {Show name} - prep brief

Recording: {date, time, timezone} · {audio|video|live} · {length} · {solo host|co-hosts|panel}
Host(s): {names, what they build, one thing they care about}
Audience: {level, ecosystem} - inferred from {which episodes}
Booked topic (host's words): "{...}"
Chosen angle: {the take only this guest can deliver, and why the back catalogue doesn't already have it}
Recurring threads on this show: {the 2-3 questions the hosts keep returning to}
Off-limits: {embargoes, customers, security, legal}
Disclosure line: "{one sentence, said in the first five minutes}"

## Spine (ABT)

"{We had X, and it worked, but Y, therefore Z.}"

## Messages

1. Claim: {...} | Evidence: {...} | So-what: {...}
2. ...
3. ...

## Opening answer

"{≤30s for video, punchline first, understandable with no intro before it}"

## Story bank

| #   | Story | Numbers | Five-second moment | What I got wrong | Answers which question |
| --- | ----- | ------- | ------------------ | ---------------- | ---------------------- |

Open loop to plant early, close late: {...}

## Sound bites

- {15-25 words, works cold}
- Liftable one: {project named next to its category, one number spoken}
- ...

## Hard questions

| Question | Concession (say first) | Bridge to message |
| -------- | ---------------------- | ----------------- |

## Depth rules

Assume: {what the audience already knows}
Explain: {the 2-3 concepts that need a definition}
Never say: {jargon to drop}

## Closing call to action

"{one destination, spelled if unusual}"

## Recording-day card

{5-8 bullets, glanceable}

## Promotion

Send host before publication: {bio, headshot, links, timestamps}
Publication day: {surface → sound bite used}
Week 1: {comments, README/talks page}
Evergreen: {post from transcript}
Attribution: {vanity URL or code, signup field option}
```

## Filled example (excerpt)

```markdown
# Backend Weekly - prep brief

Recording: 12 Sept, 15:00 CET · audio-only, edited · 50 min · solo host
Host: Dana R., runs payments infra at a mid-size marketplace; cares about operational
blast radius, allergic to vendor pitches (cut one short in ep. 118).
Audience: hands-on backend engineers, mostly Go and Python - inferred from eps. 118-121,
where the host asks about retry semantics and on-call load, never about pricing.
Booked topic (host's words): "why job queues are harder than people think"
Chosen angle: retry budgets, not brokers - the show has covered broker comparisons twice
(eps. 114, 119) and never once covered retry amplification.
Recurring threads: "what broke at 3am", "would you run this yourself or buy it", "what
does this cost you operationally".
Off-limits: the managed-hosting beta (unannounced), the fintech customer's name.
Disclosure line: "I maintain Fable-Q, and I also sell hosting for it - so take my
enthusiasm with that in mind."

## Spine (ABT)

"Teams pick a queue carefully, and the broker almost never fails, but their own retry
policy multiplies load until nothing drains, therefore budget retries before you tune
brokers."

## Messages

1. Claim: Most queue outages are retry storms, not broker failures.
   Evidence: 6 of the last 8 incident write-ups in our issue tracker were retry storms;
   the broker was healthy in all six.
   So-what: Budget your retries before you tune your broker.
2. Claim: Exactly-once delivery is a property of the consumer, not the queue.
   Evidence: our idempotency-key adoption cut duplicate side effects to near zero without
   changing brokers.
   So-what: Put the dedupe key in the payload on day one; it is unaffordable to add later.
3. Claim: A queue you cannot drain is an outage that has not happened yet.
   Evidence: 40k-message backlog took 9 hours to clear on a single-consumer deployment.
   So-what: Measure drain rate, not queue depth.

## Opening answer

"The outage that taught me this had nothing to do with the queue. Our own dashboard went
down because four services each retried three times - eighty-one times the load, on a
broker that was completely healthy the whole night."

## Story bank

| #   | Story                                       | Numbers                           | Five-second moment                                            | What I got wrong                                    | Answers                       |
| --- | ------------------------------------------- | --------------------------------- | ------------------------------------------------------------- | --------------------------------------------------- | ----------------------------- |
| 1   | Retry storm took down our own dashboard     | 3 retries × 4 services = 81x load | Realising the broker graphs were flat while everything burned | I set retries per service, not per request path     | "worst outage", "why retries" |
| 2   | Duplicate refunds during a broker migration | 340 duplicates, all recoverable   | Reading the second refund confirmation email                  | Assumed the broker's dedupe covered handler crashes | "exactly once", "migrations"  |

Open loop: mention early that one of these cost real money, come back to it at the end.

## Sound bites

- A queue you cannot drain is an outage that has not happened yet.
- Exactly-once is something your consumer earns, not something a broker sells you.
- Retries multiply: three retries across four services is eighty-one times the load.
- Liftable: "Fable-Q is a job queue for Go services, and it's the retry budget - not the
  broker - that decides whether your backlog of forty thousand ever drains."

## Hard questions

| Question                                             | Concession (say first)                                                             | Bridge                                                                              |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Why not just use the cloud provider's managed queue? | For most teams that is the right call - it is cheaper and there is nothing to run. | Message 2: the delivery guarantee you need still lives in your consumer either way. |
| You sell hosting; isn't this a long ad?              | Fair - I make money if you use this.                                               | Message 1: the retry-budget advice costs you nothing and works on any broker.       |
```

## What a bad brief looks like

- An "angle" that is really a topic ("we'll cover job queues") - nothing in it is specific to this guest, so any of the show's previous forty guests could have said it.
- A spine in AAA form: "we built a queue, and it's fast, and it's open source." No tension, so no reason to keep listening. The ABT rewrite has to hurt somewhere.
- An opening answer that starts with credentials ("I've been doing distributed systems for twelve years") and only reaches the point at second forty.
- Messages that are product features ("we support priority queues") instead of claims about the listener's world.
- Evidence the user cannot source live ("studies show most teams…").
- A story with no number and no mistake - it will be cut from the episode.
- Sound bites containing the product name, which never survive a clip. The one exception is the deliberate liftable bite, where naming the project next to its category is the whole point. If every bite does it, none of them get used.
- Hard questions with answers that bridge immediately, with nothing conceded first.
