# Extension surface ladder

Six rungs of openness, listed here in inheritance order - which is not the order they are recommended in. `SKILL.md` step 3 ranks them by value per unit of effort and that is the ordering to recommend from; this file carries the per-rung detail behind it. Walk all six and mark each _justified by the evidence_, _premature_, or _unstaffable_ before recommending one.

The ladder itself is this skill's own construction, and the time windows in "Signals you are on the wrong rung" are defaults, not measured norms.

## Contents

- Rung 1 - Documented public API and webhooks
- Rung 2 - Vendor-built integrations
- Rung 3 - Partner-built integrations, listed by you
- Rung 4 - In-product extension points
- Rung 5 - Installable third-party apps
- Rung 6 - Runtime platform
- Signals you are on the wrong rung

## Rung 1 - Documented public API and webhooks

- **Who builds**: your customers' own engineers, and integrators writing point-to-point glue.
- **You operate**: reference docs, versioning and deprecation policy, rate limits, keys, request logs.
- **Reversibility**: high. Interfaces can still be versioned out with notice.
- **Use it when**: demand is real but scattered, and no single complement is requested repeatedly.

## Rung 2 - Vendor-built integrations

- **Who builds**: you.
- **You operate**: the connectors themselves, forever, against other vendors' API changes.
- **Reversibility**: high - it is a roadmap line item.
- **Use it when**: demand is concentrated in a handful of named systems, or when you need evidence before opening anything. This is the cheapest instrument for discovering which complements customers actually adopt, and skipping it is the most common way teams over-commit.

## Rung 3 - Partner-built integrations, listed by you

- **Who builds**: agencies, integrators, and vendors of adjacent products.
- **You operate**: listing standards, a review pass, a partner support escalation path, and co-marketing expectations you will be held to.
- **Reversibility**: this is where it ends. Another company's revenue now depends on your surface.
- **Use it when**: the demand list is longer than your roadmap and outside parties already have a reason of their own to build.

## Rung 4 - In-product extension points

- **Who builds**: customers' internal teams first, then partners.
- **You operate**: a stable contract per extension point, a safety boundary, and the discipline to keep shipping without breaking them.
- **Reversibility**: low. Each point freezes an internal seam permanently.
- **Use it when**: customers need behaviour changed inside your product, not data moved between products - custom fields, hooks, event handlers, embedded UI slots, rules, templates.

## Rung 5 - Installable third-party apps

- **Who builds**: independent software vendors with their own product roadmaps.
- **You operate**: consent and scopes, security review, revocation, tenant isolation, incident handling for someone else's bug, and a developer support function.
- **Reversibility**: none in practice. Removing an app model breaks customers who depend on apps you did not write.
- **Use it when**: the complements customers want are products in their own right, big enough to fund a vendor's roadmap.

## Rung 6 - Runtime platform

- **Who builds**: vendors and customers deploying code you execute.
- **You operate**: multi-tenant isolation, resource governance, metering, a developer toolchain, and an SLA - effectively a second product.
- **Reversibility**: none. Shutting it down is a migration event for every complementor.
- **Use it when**: complements cannot work outside your execution context, and you can fund a dedicated platform team indefinitely.

One property does not appear in the ranking and belongs here: who the customer blames when a complement fails. At rungs 1 and 2 they blame themselves or the partner; from rung 3 up they blame you, whoever wrote the code.

## Signals you are on the wrong rung

- **Too high**:
  - Extension points with no complements after two quarters.
  - A review queue with nothing in it.
  - Complementors who built once and never updated.
- **Too low**:
  - The same integration requested by many customers while your roadmap keeps deferring it.
  - Customers shipping unsupported wrappers and scrapers.
  - Partners asking for permission to list something they already built.
- **Wrong builder**: you designed for independent software vendors and only internal teams show up, or the reverse. Fix the offer, not the surface.
