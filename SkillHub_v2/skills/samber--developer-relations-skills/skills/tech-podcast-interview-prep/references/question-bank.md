# Hard-question bank

Source material for step 8. Build the user's eight predicted questions from the show's own back catalogue first. Use these classes to fill the gaps and to find the two questions the user is hoping nobody asks.

For each class: what the host is really asking, the concession that has to come first, and the way guests usually fail it.

## Two answer shapes

Most questions are not attacks, and treating every one as a bridging opportunity is what makes a guest sound coached. Sort them first.

**Ordinary question → ADD** (Matt Abrahams). Answer, then Detailed example, then Describe relevance:

> _"How do you decide what to retry?"_
> **A:** "By the cost of doing it twice, not by the error code." **D:** "We retried payment webhooks for a year on a 500, and every duplicate charge came from that rule." **D:** "So if you only change one thing this week, split your retry policy by side-effect cost - it takes an afternoon."

The common failure is a missing first beat: the guest opens with the example and never states the answer, so the listener spends thirty seconds waiting to find out what the point is.

**Hostile or off-limits question → ABC**, with the honest answer wedged in before the bridge. Acknowledge what was actually asked, answer it including the part that does not flatter you, then bridge to one prepared message. Bridging straight from the question is the move a technical audience recognises instantly.

## 1. Competitor comparison

_"How is this different from {the obvious alternative}?"_

- Really asking: is there a reason to switch, or is this a rebuild of something that works?
- Concede first: where the alternative is genuinely the better choice, by name.
- Fails when: the guest refuses to name competitors, or lists features instead of naming the one workload where the trade-off flips.

## 2. "Why not just use X?"

_"Couldn't I do this with a cron job and a database table?"_

- Really asking: is the complexity you are adding justified?
- Concede first: for a small enough workload, yes, and say where the line is.
- Fails when: the guest treats the simple solution as naive. The audience has shipped that simple solution and it worked.

## 3. Licensing, pricing or model changes

_"You changed your licence / raised prices / closed the source of X."_

- Really asking: can I depend on you?
- Concede first: what the change cost users, and what was communicated badly.
- Fails when: the guest calls it a misunderstanding. Explain the constraint that forced the decision and what stays guaranteed.

## 4. Outage, CVE, or data-loss incident

_"What happened during the {incident}?"_

- Really asking: do you understand your own failure, and did anything change?
- Concede first: the impact in real units - users affected, duration, data lost.
- Fails when: the guest hides behind "we take reliability seriously". Give the mechanism, the fix, and the detection change.

## 5. AI-hype scepticism

_"Isn't the AI part just marketing?"_

- Really asking: are you shipping substance or a press release?
- Concede first: the AI feature that did not work and was removed.
- Fails when: the guest defends everything. Naming the failure earns the one example that stuck.

## 6. Open-source monetization

_"How do you make money, and what stops you from pulling the rug?"_

- Really asking: what is the incentive structure I am betting on?
- Concede first: the tension is real - the guest is paid by something.
- Fails when: the guest is vague about revenue. State the model plainly and the guarantee that is written down (licence, foundation, governance doc).

## 7. "Who is this not for?"

Often not asked directly - offer it anyway. Naming the workloads where the tool is wrong is the highest-trust answer available and it pre-empts half the other questions.

- Fails when: the guest says "any team can benefit", which the audience translates as "he does not know his own product".

## 8. Career, credibility, or authority challenges

_"You've only worked on this for a year - why should we listen to you?"_ or _"You're in DevRel, do you actually write code?"_

- Concede first: the limit of the user's experience, precisely.
- Bridge to: the specific evidence the user does own - the incidents they debugged, the code they wrote, the users they watched fail.
- Fails when: the guest inflates the credential. One overstated claim, and a listener who checks it discredits the whole episode.

## 9. Roadmap and futures

_"What's coming next?"_

- The trap is enthusiasm, not hostility: this is where guests leak embargoed work.
- Answer with what is already public plus the problem the team is thinking about, never a date.

## 10. The lightning round

Many shows close with rapid-fire questions (favourite tool, hottest take, worst advice). Prepare three: a genuine hot take the user can defend, a tool recommendation that is not their own product, and a piece of common advice they disagree with. Refusing to play makes the guest look guarded on the way out.

## Rehearsal method

1. Ask the user each predicted question out loud, in the host's phrasing, without warning.
2. Time the answer. Over 90 seconds - the skill's own self-set conversational ceiling, not a measured one - means it needs a shorter first sentence, not a shorter story. On a live show, run the same drill against 15-20 seconds instead - the point has to arrive in the first sentence because there is no edit behind it.
3. Check the concession came before the bridge. If it did not, ask the question again immediately - the second attempt is usually right.
4. Stop after the eight questions. Rehearsing further produces answers that sound rehearsed, which costs more than the coverage gains.
