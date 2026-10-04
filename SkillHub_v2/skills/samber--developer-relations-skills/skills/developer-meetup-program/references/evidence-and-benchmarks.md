# Evidence and benchmarks

Contents: sourced figures · baselines set by this skill · what to verify before quoting · how to replace a baseline.

Every number used anywhere in this skill appears here once, with where it came from. Quote a sourced figure externally (to a sponsor, a manager, a venue host). Never quote a baseline externally as an industry standard - say "our target" instead.

## Sourced figures

| Figure                                         | Value                                                                                               | Source                                                     |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| No-show planning ratio                         | ~30% of RSVPs                                                                                       | CNCF Community Groups best practices                       |
| Inactivity threshold                           | >90 days between events marks a chapter inactive                                                    | CNCF Community Groups                                      |
| Minimum annual meetings                        | ≥6 per calendar year (technical community groups)                                                   | CNCF Community Groups                                      |
| Active-chapter attendance bar                  | Quarterly event with >10 _attendees_, not registrations                                             | CNCF Community Groups                                      |
| Content block length                           | 1-2 hours of content plus networking                                                                | CNCF Community Groups                                      |
| Default slot                                   | Tuesday-Thursday evening, after work, adjusted locally                                              | CNCF Community Groups                                      |
| Sponsor stage-time cap                         | ≤15 minutes                                                                                         | CNCF Community Groups                                      |
| Sponsor pitch length at a community conference | "a short elevator pitch … generally in the order of a minute or two"                                | DevOpsDays organizing pages                                |
| Bought speaking slots                          | "no speaker spots can be bought by sponsors: not ever - period"                                     | DevOpsDays                                                 |
| Attendee data                                  | "devopsdays does not ever distribute attendee contact information"                                  | DevOpsDays                                                 |
| Organizer team minimum                         | ≥2 organizers with divided responsibilities; ≤50% from one company; max 5 (virtual) / 7 (in-person) | CNCF Community Groups                                      |
| Organizer team minimum, conference scale       | ≥3 people from different organizations; "not about lead generation"                                 | DevOpsDays                                                 |
| Organizer add/remove process                   | Public issue, approved at ≥50% of current organizers in favor; departures also public               | CNCF Community Groups                                      |
| Half-day step-up shape                         | ~4 hours, multiple speakers, catering breaks, at most quarterly                                     | CNCF meetups-vs-community-day guidance                     |
| Community levels                               | Explorers → Participants → Contributors → Advocates; gravity = love × reach                         | Orbit Model (published 2019, no longer actively developed) |
| Participation inequality                       | 90% lurk, 9% contribute occasionally, 1% produce most activity                                      | Jakob Nielsen, 2006                                        |
| Single-outcome rule for a company program      | "If you're starting out, just focus on one objective from the SPACES Model"                         | CMX SPACES model                                           |
| Oldest surviving vendor user group             | SHARE, founded 1955, IBM mainframe corporate users                                                  | Wikipedia, _User group_                                    |
| Vendor-backed chapter network at scale         | HashiCorp User Groups: 50,000 members, 184 groups, 64 countries                                     | hashicorp.com/community (vendor's own figures)             |
| Centrally-staffed company series               | CMX Circuit Tour - company staff run each city stop                                                 | cmxhub.com                                                 |

## Baselines set by this skill

Each of these is a designed gate, chosen to be checkable and to fail loudly, rather than a figure measured across a population of real meetups.

| Baseline                               | Value                              | Why this value                                                                                                        |
| -------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Show-up rate                           | ≥70%                               | The direct complement of CNCF's ~30% no-show figure; it is arithmetic on a sourced number, not an independent finding |
| Repeat attendance                      | ≥40% of the door                   | Below it, the room is a churn funnel; the exact cut is a judgment call                                                |
| New faces                              | >0 every edition                   | A group with zero newcomers is closing in on itself, whatever its total                                               |
| Speakers sourced from the room         | ≥1 in 3                            | Deliberately ambitious: Nielsen's 1% contributor rate says this only happens with active recruiting                   |
| Editions with confirmed speakers       | ≥2 ahead                           | One edition of buffer absorbs a single cancellation; zero means every month starts from nothing                       |
| Pipeline board states                  | Confirmed / provisional / prospect | Vocabulary, not a benchmark                                                                                           |
| First edition size                     | 10-15 attendees is a real start    | Anchored to CNCF's >10-attendee bar, then rounded into a planning range                                               |
| Venue booking horizon                  | One season (≈3 editions) at a time | Trades continuity against dependence on one host                                                                      |
| Cost per edition in the worked example | ~€250, food only                   | Illustrative of a European city, not a survey result                                                                  |

Calibrate every baseline against the group's own trailing three editions as soon as three exist. A measured local rate always beats an imported one.

## Verify before quoting

Treat each of the following as unknown until the user or the program's own organizer material settles it.

- **Listing-platform pricing and tiers** (Meetup.com dues, Luma Plus). Public list prices found via search: Meetup Standard from $29.99/month ($99.99/6 months), Meetup Pro from $55/month ($47/6 months); Luma Plus $59/month billed annually (0% platform fee, versus 5% on Luma's free tier). Confirm inside an active organizer account before quoting a final number - both note that price can vary by region, currency and signup channel (web vs. iOS/Android).
- **Google Developer Groups mechanics, now readable via search despite client-side rendering blocking direct fetch**: new-chapter applicants must check the GDG Chapter Directory for an existing chapter in their area first, then review organizer acknowledgements, a code of conduct and official naming guidelines before applying; strict brand rules govern logo spacing/distortion, color palette and typography (Google Sans). Internal budget ownership is not addressed in the public organizer material. AWS User Groups mechanics remain unread - read that program's own organizer pages instead of assuming it matches the HashiCorp or GDG models.
- **Budget ownership for a company-hosted program** (DevRel versus marketing versus field). Ask the user rather than asserting a norm.
- **Any no-show figure above 30%.** Plan against CNCF's ~30%; the 40-50% repeated for free evening events is hearsay, with no organization standing behind it.

## How to replace a baseline

1. Log door count, RSVP count, repeat attendance and new faces for three consecutive editions.
2. Take the median, not the mean - one great edition skews a mean and hides a trend.
3. Set the target one step above the median, and re-read it after another three editions.
4. Record in the charter that the number is now measured locally, with the editions it came from. A target with no stated origin gets argued about every time it is missed.
