# Grant programs, gates and reporting

Confirm a program's open status, its figures and its residency rules on its own page before writing anything. Calls open and close on their own schedules.

## Gates, by program

Each entry reads: who it can pay / the gate that rejects most applicants / published size.

- **NLnet Foundation, Open Internet Stack funds (formerly branded NGI Zero, whose Entrust/Core/Commons calls are now permanently closed).** "individuals, research organisations, non-profits, public institutions, companies of any size and type", no entity needed / a "European dimension" is a knock-out criterion, and code, hardware and documentation ship under recognised open licences / €5,000-€50,000 for a first grant, €500,000 lifetime cap per recipient, spread across three thematically named programmes (Restack, CodeSupply, ELFA), each with its own rolling deadline on the 3rd of every odd month.
- **Sovereign Tech Fund (Germany).** Maintainers, companies and communities anywhere / existing, widely deployed base technology only: "We do not finance the development of prototypes" / €50,000 minimum project cost, no published maximum, though independent reporting notes individual awards reaching roughly €1M in practice.
- **Prototype Fund (Germany).** An individual or a team of up to four that must form a GbR: "Payments to companies, associations, universities... are not possible" / German tax residency for the lead, plus a fixed annual window / up to €95,000 per team for the six-month regular phase (€47,500 solo), with an optional four-month second stage adding up to €63,333 team / €31,667 solo.
- **Open Technology Fund.** "Individuals or organizations (for-profit or nonprofit) of all ages", contracted directly / OFAC-sanctioned countries excluded, and the project must serve internet freedom / $10,000-$900,000 over up to 24 months on the Internet Freedom Fund.
- **Chan Zuckerberg Initiative EOSS.** Organisations only: "Grants are not permitted to individuals, only to organizations" / demonstrated impact on biomedical research / $50,000-$200,000 a year for two years, indirect costs capped at 15%.
- **Alfred P. Sloan Foundation, Open Source in Science.** Not individuals, not generally for-profits / funds "tooling, institutions, economic models, and incentives" around research software rather than individual projects / unpublished, and no unsolicited full proposal is reviewed.
- **GitHub Secure Open Source Fund.** A maintainer in a region GitHub Sponsors supports / fixed sessions, prioritising maintainers deep in the dependency tree / $10,000, staged across the sprint and two check-ins.
- **FLOSS/fund.** Individuals and organisations globally / a published `funding.json` manifest is a submission prerequisite, and barely used projects are not considered / $10,000 minimum, $100,000 a year maximum.

## Getting paid with no legal entity

The entity question settles eligibility before proposal quality does.

- **No entity needed.** NLnet pays each person on a grant directly and accepts a pseudonymous application until award. The Open Technology Fund contracts with the applicant.
- **Organisation-only programs.** Route through a fiscal host, or name a fiscal sponsor the program already accepts. CZI's EOSS names NumFOCUS and Code for Science & Society, requires one secured by the full-proposal deadline, and warns that fiscally sponsored applications may be eligible for only a subset of its co-funders.
- **Incorporating** is the slowest route, and only the Prototype Fund forces it, requiring a selected team to found a German GbR.

## What the application asks for

Recurring fields across the open forms. Draft each once, reuse across programs:

- Summary of the project and the expected result.
- Budget as a task and effort breakdown, the rate applied, and expenses. Expect the rate to be questioned.
- Comparison to existing and historical efforts, what differs here, and whether contributing to one instead was considered.
- Expected technical challenges, and the applicant background and prior contributions that de-risk them.
- Ecosystem: dependencies, main users, how you will engage them.
- Other funding, past and present. Some programs refuse work another public body already funds.
- Milestones for the funding period, and who benefits, how many.
- Generative-AI disclosure where asked. NLnet wants the prompts and logs, and warns non-disclosure is likely to get the proposal rejected.

Two-stage programs ask far less up front. Sloan takes a two-page letter of inquiry by email and can take eight weeks to reply. CZI's EOSS letter of intent carried a summary, the value to the field, a landscape analysis and the repository list; budget, personnel, milestones, evaluation indicators, institutional sign-off and a diversity statement were asked of invited applicants only.

## Criteria worth writing to

- NLnet: technical excellence and feasibility 30%, relevance, impact and strategic potential 40%, cost effectiveness 30%, then a second stage of clarifying questions on rate justification and sustainability.
- Sovereign Tech Fund: prevalence, relevance to societal sectors, vulnerability (whether the maintenance is structurally underfunded), public interest, feasibility, and demonstrated expertise or maintainer endorsement.
- Prototype Fund: fit, degree of innovation, feasibility within six months, social benefit, chances against existing products, and absence of double funding.

## After the award

- **NLnet.** Nothing upfront: milestones fixed in a memorandum of understanding, payment requested on reaching one. Every deliverable ships under an open licence, and a grant over €50,000 may have payment conditioned on an independent security audit and the resolution of its findings.
- **Sovereign Tech Fund.** Invoices, approved then paid within about 30 days. Progress reports are tied to invoicing, in a format agreed with the program manager and as light as an email linking pull requests, plus a final write-up of impact, challenges and next steps.
- **Prototype Fund.** Instalments for work performed, released at the start of each quarter, retroactively. Owes attendance at a Berlin kickoff and Demo Day, a short plain-language report the funder publishes, and a sustainability follow-up about a year later.
- **CZI EOSS.** Paid to the institution or fiscal sponsor, never to an individual. Owes annual reports that may be made public, alongside uptake indicators the funder pulls from repositories, issue trackers, package registries and community forums.
- **Sloan.** Paid to an institution. Owes interim reports of two to four pages and a final of at most ten, under set headings, plus financial reports of amount received, expended and unexpended, with any balance over $500 returned.
- **GitHub Secure Open Source Fund.** Owes a three-week security sprint at five to ten hours a week, milestones agreed with a program manager, and 6- and 12-month check-ins that release the remaining money.
- **FLOSS/fund.** Owes public acknowledgement linking the fund.

## Cross these off before spending an afternoon on them

- Mozilla Open Source Support: "on indefinite hiatus and is not currently accepting applications", with the Mozilla Technology Fund named as the alternative.
- Google Season of Docs: concluded after six years.
- Sloan's Better Software for Science: completed, succeeded by the narrower Open Source in Science.
