# Subject Line Scoring Rubric

Score every candidate variant in two passes: hard fails first, then the 10-point scorecard. Pass threshold: at least 8/10 with zero hard fails, for every shipped variant. Regenerate and re-score anything below that until the whole set clears.

## Hard fails - score 0, regenerate, no exceptions

- Fake "Re:" or "Fwd:" prefix, or any framing implying a prior conversation that never happened. This is the deceptive-subject-line case CAN-SPAM prohibits.
- Subject promises anything the email body does not actually deliver.
- Spam-trigger vocabulary in the subject: "free", "guarantee", "act now", "limited time", "click here". Flag the words here; route the full inbox-placement review to the deliverability skill.
- B2B cold only: the prospect's first name in the subject - a mail-merge signal correlated with fewer replies (attributed to a sales-engagement platform's data).
- Exceeds the regime's truncation budget: ~35 characters for B2B cold, ~50 for a B2C subject.
- Duplicate angle: the variant differs from another shipped variant only in wording, not in angle.

## 10-point scorecard, per variant

| Criterion                 | Points | Full marks means                                                                                                                  |
| ------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Length and truncation fit | 0-2    | B2B cold: 1-4 words, within ~35 chars. B2C: within ~50 chars, preheader 90-140 chars that extends (never repeats) the subject     |
| Angle execution           | 0-2    | Concretely expresses the chosen personalization angle - pain, trigger event, competitor, initiative - not a generic gesture at it |
| Reader's-world framing    | 0-2    | Anchored to the recipient's job or life, not the sender's product; no salesy verbs, no urgency words, no pitch                    |
| Body-promise match        | 0-2    | The body's opening fully honors what the subject implies                                                                          |
| Set distinctness          | 0-1    | Angle genuinely distinct from every other variant in the shipped set                                                              |
| Human sound               | 0-1    | Survives being read aloud as something a person would type; no templated AI phrasing                                              |

## Worked scored example - B2B cold

Context: recipient is a VP Operations; chosen angle is a trigger event (they posted five SDR job openings); body offers a benchmark on SDR ramp time.

| Check                     | "sdr ramp time"                                         | "Quick question?"                     |
| ------------------------- | ------------------------------------------------------- | ------------------------------------- |
| Hard fails                | none                                                    | none                                  |
| Length and truncation fit | 2 - 3 words, 13 chars                                   | 2 - 2 words, 15 chars                 |
| Angle execution           | 2 - names the exact consequence of their hiring trigger | 0 - no angle at all                   |
| Reader's-world framing    | 2 - their metric, no product                            | 1 - neutral but empty                 |
| Body-promise match        | 2 - body delivers the ramp benchmark                    | 1 - body content is a surprise        |
| Set distinctness          | 1                                                       | 0 - interchangeable with any campaign |
| Human sound               | 1                                                       | 1                                     |
| **Total**                 | **10/10 - ship**                                        | **5/10 - regenerate**                 |

## Worked scored example - B2C lifecycle

Context: cart-abandonment email; body contains the saved cart and a free-shipping offer.

| Check                     | "Your cart is saved - shipping's on us"                 | "You won't BELIEVE this deal!!!"                                                                                |
| ------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Hard fails                | none                                                    | fails: excessive punctuation reads as spam bait and the body has one specific offer, not an unbelievable "deal" |
| Length and truncation fit | 2 - 38 chars; preheader extends with the offer deadline | -                                                                                                               |
| Angle execution           | 2 - direct pattern, names the concrete benefit          | -                                                                                                               |
| Reader's-world framing    | 2 - their cart, their saving                            | -                                                                                                               |
| Body-promise match        | 2 - body shows the cart and the offer                   | -                                                                                                               |
| Set distinctness          | 1                                                       | -                                                                                                               |
| Human sound               | 1                                                       | -                                                                                                               |
| **Total**                 | **10/10 - ship**                                        | **0 - hard fail, regenerate**                                                                                   |

## Delivery table template

Present the shipped set to the user in this shape (add a Preheader column for B2C):

| #   | Variant | Angle                  | Words / chars | Score | Notes                                   |
| --- | ------- | ---------------------- | ------------- | ----- | --------------------------------------- |
| A   | ...     | trigger event          | 3 / 14        | 9/10  | control                                 |
| B   | ...     | internal-style noun    | 2 / 11        | 8/10  | challenger                              |
| C   | ...     | specific pain question | 4 / 19        | 8/10  | park if volume only supports 2 variants |
