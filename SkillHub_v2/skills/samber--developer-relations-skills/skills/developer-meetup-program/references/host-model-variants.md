# Host model variants

Contents: the three host models compared · what changes per model · B2D versus developer-plus audiences · listing-platform considerations · a negative example.

## The three models

Vendor-affiliated user groups are the older tradition, not a later corruption of an independent one: SHARE (1955) and DECUS (1961) were corporate-user groups decades before the volunteer hobbyist chapter became common. Read the three models as different contracts with the room, not as a maturity ladder.

|                              | Independent, vendor-neutral       | Vendor-backed volunteer chapter                        | Company-staffed series                                    |
| ---------------------------- | --------------------------------- | ------------------------------------------------------ | --------------------------------------------------------- |
| Who runs the evening         | Local volunteers                  | Local volunteers                                       | Company staff                                             |
| Who owns the brand           | The group                         | The vendor                                             | The company                                               |
| Program control              | Organizers, no vendor veto        | Organizers, within vendor guidelines                   | Company                                                   |
| Typical money                | In-kind venue and food            | In-kind, plus vendor swag and speaker access           | Company budget line                                       |
| Named example                | CNCF Community Groups, DevOpsDays | HashiCorp User Groups (50,000 members, 184 groups)     | CMX Circuit Tour                                          |
| Main risk                    | Organizer burnout, no safety net  | Chapter reads as marketing if the vendor over-programs | No local ownership; the series stops when the budget does |
| Non-host speaker per edition | Structural requirement            | Strongly advised                                       | The only defense against a customer-only room             |

## What changes per model

**Independent.** Neutrality is the product. CNCF caps organizer teams at 50% from any one company and escalates neutrality complaints: written warning, then a community meeting, then disabling the chapter.

Sponsors buy logistics, never airtime. A competitor on stage is a feature.

**Vendor-backed.** The vendor supplies branding, a listing platform, sometimes travel for speakers. The organizer's job is to keep the program interesting to people who have not yet bought anything: mix ecosystem and adjacent-technology talks in, and keep the vendor's own staff to a minority of slots across a quarter, not per evening.

**Company-staffed.** Consistency is the upside; the downside is that nobody in the room has a reason to protect it. Compensate deliberately: a local co-host with real program input, an advisory group of regulars, and a stated policy on what the company will not do from the stage. Budget ownership inside the company (DevRel, marketing, or field) is not a settled norm - ask, and write the answer into the charter, because it decides who can cancel the series.

## B2D versus developer-plus audiences

Two company shapes run developer programs for different reasons, and the meetup's topic strategy follows.

- **Developer-first (B2D)** - the product is sold to developers; the attendee evaluating the API is frequently the person who requisitions it. Product-adjacent topics carry little tension, and adoption is a defensible primary outcome.
- **Developer-plus** - a B2B or B2C business that also exposes products to developers. The attendee is one segment of a much larger buying org and rarely the decision-maker, so the program justifies itself as brand and ecosystem investment. Topics skew to the platform ecosystem rather than the core product.

The operational mechanics on either side (topic-selection process, recruiting channels, employer buy-in tactics) are not documented in any source found for this skill - derive them with the user rather than asserting a standard.

## Listing-platform considerations

Stay tool-independent in the plan; choose the platform on these properties rather than on a brand.

- **Recurring-event support** - can a monthly slot be cloned with its settings, or is every edition set up from scratch?
- **Group-level versus event-level audience** - some platforms hold members at the calendar/group level, which means the audience survives a cancelled edition; others only hold per-event RSVPs.
- **Waitlist with auto-promotion** - required to make overbooking work.
- **Export of the member list** - if the organizers cannot export, the group cannot leave.
- **Fees** - some platforms charge organizer dues; treat any quoted price as unverified until confirmed inside a live organizer account.
- **Discovery** - whether people who are not already following the group can find the event at all.

Two live examples for orientation only, both with unverified pricing:

- Meetup.com runs a paid organizer subscription and gates the details behind an account.
- Luma is calendar-centric, supports event cloning, tags and calendar-level memberships, and documents workarounds rather than native recurrence.

## Negative example: the model nobody named

Constructed for illustration - a composite of the failure pattern, not a transcript of one named group.

> A vendor's DevRel team launches "the <Product> User Group" in four cities. Each evening is two talks by company engineers plus a roadmap update. Local "organizers" are volunteers recruited to book rooms, with no say in the program. Attendance is strong for three editions, then halves; the volunteers stop replying.

Three failures, all from leaving the model implicit:

- The room was told "user group" (independent) and given a company-staffed series.
- The volunteers were given the workload of organizers and the authority of helpers.
- No edition had a speaker without a stake in the product, so once the roadmap was known there was no reason to return.

The repair is to pick one model and say it out loud: either give the volunteers program control and one guaranteed non-company slot per edition, or drop the "user group" framing and run it as the company event series it actually is.
