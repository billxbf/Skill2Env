# Interview loop design

Contents: the API-design-vs-system-design split, PM-vs-engineer loop differences, take-home practices, GitLab's real posted loop.

## API design is a named, separate interview format from general system design

Multiple companies (Meta specifically named) now split what used to be one "system design" round into two distinct interview types:

- **System design** - large-scale distributed-systems architecture.
- **API design** (reported internally at Meta as "Pirate X" in candidate-prep literature) - design decisions and their downstream consequences for the developer consuming the API. Scope is deliberately smaller than full system design: no full architecture to sketch, the bar is that the API must be clear, predictable, and hard to misuse, with error messages specific enough that a developer can act on them.

A commonly cited worked example: design a payments API scoped to card-payment processing, where the "users" are developers integrating it into their own product.

**For a PM candidate**, the bar differs by design from an engineering candidate's: assessed on how well they scope, structure, and communicate the design thinking, not on proving deep technical implementation expertise - echoed at Google, where system-design-flavored PM rounds emphasize estimation and scoping over the technical solution. Some PM loops (Uber) still include a genuine technical conversation with an engineer, where the PM candidate must explain APIs and how a system fits together without hand-waving, though without writing code.

## Take-home and written components

Sourced practice across companies, not developer-platform-specific: Google closes its PM loop with a written product exercise; Meta opens with short-answer questions due back in about 24 hours; Roblox asks candidates to explain their assessment reasoning in a short essay; LinkedIn's product-sense round has historically included a writing sample. No developer-platform-specific take-home (for example, "design this SDK" as a formal artifact) was found as a named, sourced practice - treat it as a plausible format by analogy to the API-design interview type above, not as directly confirmed practice.

## A real, posted engineering-side loop: GitLab's Partner Integration Engineer

Directly sourced from GitLab's public handbook: recruiter call -> hiring-manager interview -> 2 to 5 team interviews -> a possible executive round for senior hires. No API-design-specific round or take-home is named in the posted family description. GitLab's screening substance, per the job family's stated skills, centers on language proficiency, SDLC practice, and a real open-source contribution history that can be reviewed as existing evidence rather than tested live - a lower-cost validity signal a hiring loop can lean on if the candidate already has one.

## Building a loop for this collection's roles

- **API Product Manager** - a scoping/design-thinking round (not a coding round), a stakeholder-management or roadmap-prioritization scenario, and a written exercise if the hiring team's general PM process already uses one.
- **Platform Engineer / Platform Architect** - an API-design round distinct from general system design, a hands-on or architecture-review round matched to seniority, and a technical-leadership conversation at staff level and above.
- **Partner / Integration Engineer** - GitLab's structured sequence above, weighted toward relationship-management scenarios for a Partner Engineer and toward architecture/reliability scenarios for an Integration Engineer.

## What is confirmed vs. what is inferred

Confirmed and directly sourced: the system-design/API-design split as two distinct interview types at major companies; the PM-vs-engineer difference in what's assessed within that split; the general PM-loop take-home pattern (not platform-specific); GitLab's real posted loop structure.

Not confirmed, flagged rather than invented: a named "versioning/backward-compatibility scenario question" as a distinct, formally recognized interview round; any specific SDK-design take-home account from a named company or candidate.
