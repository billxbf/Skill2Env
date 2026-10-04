# Certification program design

Read before recommending anything at the certification rung. These are the obligations that separate a certification from a quiz with a PDF.

Vendor pricing, validity windows and renewal rules move constantly. Re-check the vendor's own certification page before quoting one to a buyer, and always quote it with its date.

## Scheme requirements

ISO/IEC 17024 is the international standard for bodies certifying persons. Most vendor devtool certifications are **not** accredited to it and do not need to be - it is still the checklist the credential gets measured against once an enterprise buyer, a partner contract or a job posting relies on it.

A documented certification scheme contains:

- Scope of certification, job and task description, required competence, abilities and prerequisites.
- Assessment methods.
- Criteria for initial certification **and recertification**.
- Criteria for suspending and withdrawing a certification.

Two structural rules bite for a vendor program:

- **Impartiality**: the decision to award certification cannot be outsourced to another body. Delivery can be subcontracted; the pass/fail decision cannot.
- **Separation of training and certification**: a body that also sells training must show that the training does not compromise the certification's impartiality. Selling the course that guarantees the exam is exactly the conflict the standard polices.

## Job task analysis is the input, not the syllabus

Derive competencies from what practitioners actually do in the role - sourced from interviews, support data and telemetry. It is also the only defensible source for published domain weights.

- Feature-derived syllabus: certifies familiarity with a menu.
- Job-task-derived syllabus: certifies ability to do the job.

Worked example of published weights (CKA):

- Troubleshooting: 30%
- Cluster Architecture/Installation/Configuration: 25%
- Services & Networking: 20%
- Workloads & Scheduling: 15%
- Storage: 10%

Weights are a claim about the job, and a candidate can hold you to them.

## Cut scores need a standard-setting study

Picking 70% because it looks like a pass mark is indefensible. Fund a study or do not publish pass/fail.

- Panel of **5-15 subject-matter experts** representing key stakeholder groups.
- **Modified Angoff**: each expert estimates, item by item, the proportion of _minimally competent_ candidates who would answer correctly; several rounds, experts revise against peer estimates and real performance data; results averaged or taken at the median.
- **Bookmark**: order items by difficulty, experts mark where a threshold candidate stops succeeding.
- **Contrasting groups**: classify real candidates by known competence, find where the score distributions cross.

Consequence for a small program: a real cut score costs a day of 5-15 experts' time per exam version. A program that cannot fund that should publish a completion badge instead.

## Exam format

Performance-based exams - solving real tasks in a live environment - are the format that survives contact with a developer audience, and the one with the highest per-item build and hosting cost, because every task needs a disposable, deterministic environment. Recall-item exams are cheap to build and the first to be devalued by leaked content.

Reference point: CKA is an "online, proctored, performance-based test that requires solving multiple tasks from a command line running Kubernetes", 2 hours, $445 exam-only, valid two years, and the price includes two exam attempts plus two 36-hour simulator sessions. HashiCorp runs Associate and Professional/Advanced tiers per product, online with a live proctor verifying identity and monitoring the session; each product's own certification page, not the top-level certifications index, publishes exam price and duration. Its Associate-tier exams (Terraform, Vault) are recall-item, multiple-choice, one hour, $70.50 per attempt; its Professional-tier exam (Terraform Authoring and Operations Advanced) is lab-based plus multiple choice, four hours including a 15-minute break, $295 per attempt. Both tiers are valid two years.

## Validity and renewal - four shipped models

| Program              | Validity                                   | Renewal path                                                                                                                                                                                                             | Cost to holder                                                 |
| -------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| CKA                  | 2 years                                    | Retake                                                                                                                                                                                                                   | Full price                                                     |
| HashiCorp            | 2 years                                    | Pass same-level or higher exam; window opens 6 months before expiry                                                                                                                                                      | Full price                                                     |
| AWS                  | 3 years (retake) or 1 year (activity path) | Retake the latest version, pass a higher-level exam, or complete maintenance activities on the vendor's learning platform                                                                                                | 50% discount voucher; game-based recert free at the entry tier |
| Microsoft role-based | 1 year                                     | Short **unproctored, open-book** online assessment inside a six-month eligibility window, taken "as many times as you need as long as you pass before your certification expires"; Fundamentals credentials never expire | Free                                                           |

The spread is a strategy choice, not an industry standard:

- Free renewal: maximizes the installed base of certified people.
- Paid retake: maximizes per-credential revenue and shrinks that base.

Decide which one the business actually needs before copying a competitor's window.

AWS's stated rationale for expiry: recertification "helps strengthen the overall value of your AWS Certification and shows individuals and employers that your credential covers the latest AWS knowledge, skills, and best practices." Use that framing only if you can fund the re-alignment it implies.

## The re-alignment liability

CKA states it will be aligned with the most recent Kubernetes minor version within approximately **4 to 8 weeks** of that release. That is the real cost line: every product release re-dates the item bank, the lab images and the courseware behind them.

Planning rule: a certification's refresh cadence is set by the **product's** release cadence, never by the education team's calendar. A program shipping faster than it can re-align its exam certifies a version nobody runs.

## Exam fraud is a permanent operating cost

"Brain dumps" - reconstructed and resold live exam content - are the standing threat to any high-value IT credential. Once an item bank leaks, the credential measures memorization of the dump.

Documented countermeasures, all recurring costs:

- Performance-based tasks over recall items.
- Large rotating item banks.
- Live proctoring and identity verification.
- Item exposure analysis.
- Legal action against dump sites.

Credential value and operating cost rise together; budget them together.

## Portability

Issue on Open Badges (maintained by 1EdTech, formerly IMS Global) - a free open specification for "information-rich visual tokens of verifiable achievements". Version 3.0 is current: each badge is digitally signed by its issuer and compatible with the Verifiable Credentials Data Model 2.0, and holders can post it to a site, share it socially, or import it into a wallet via the Badge Connect API. A credential locked inside your own dashboard cannot do the job the holder wants it for.

Adoption figures once cited for Open Badges (27 certified platforms, 74M+ badges issued as of 2022) are **not** on 1EdTech's current standard page - treat them as unverified and do not put them in a business case.

## Negative example - the borrowed benchmark

Wrong, and the most common way this reference gets misused:

> "Industry standard is a two-year validity window with a paid retake, and courseware re-aligned within 4-8 weeks of each release, so that is what we will do."

Nothing in that sentence is a standard. Two years with a paid retake is what CKA and HashiCorp chose; Microsoft chose one year renewed free and open-book; AWS chose three years with a discount voucher. The 4-8 week window is CKA's own published commitment for tracking Kubernetes minors, not a norm - and it is a cost promise, not a badge of quality.

Right:

> "We propose two years with a paid retake, matching CKA and HashiCorp, and reject Microsoft's free annual model because we want per-credential revenue more than a large certified installed base. Our re-alignment window is six weeks, set by our own minor-release cadence; CKA's 4-8 weeks is the closest published comparator, not a target we inherit."

The difference is not tone. The second version names who chose what, when it was read, and which trade-off the recommendation is buying.

## Refusal checklist

Refuse to recommend certification when any of these is unfunded:

- The job task analysis.
- The standard-setting study.
- Item security.
- The appeals path.
- The recertification cycle.

Downgrade to a skill badge and name the missing item as the escalation trigger.
