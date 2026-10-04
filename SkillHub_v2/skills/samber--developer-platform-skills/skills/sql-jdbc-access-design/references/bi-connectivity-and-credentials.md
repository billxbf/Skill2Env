# BI Connectivity and Credential Issuance

The detail behind steps 5 and 7: what each BI tool's certification actually requires, why the wire-protocol shortcut works, what a connection-setup page must contain, and the credential ladder with its degradation path.

## The certification tax, per tool

Supporting the major BI tools means four ongoing engineering costs:

- (a) A spec-compliant driver with correct SQLSTATEs and type coercion.
- (b) Building and signing per-tool connector packages.
- (c) Renewing signing certificates on a schedule.
- (d) Absorbing first-line connectivity support - both major vendors push that back to the data-source owner by policy.

- **Tableau** requires a Type-4 JDBC 4.0+ driver (pure Java, no native code) implementing `getDriverVersion`/`getDriverName` and returning _accurate_ SQLSTATEs - Tableau warns that returning a generic error instead of SQLSTATE 28000 for invalid credentials can break connector behavior.
  - Connectors ship as signed `.taco` files; an expired signing certificate makes Tableau reject the connector outright.
  - Connection behavior is tuned via TDC customization XML whose vendor/driver name fields must exactly match what the driver reports.
  - Tableau limits its own support to "reasonable levels" of troubleshooting and explicitly won't create or customize a connector for a specific driver - connectivity support stays with you.
- **Power BI** certified connectors are built on the Power Query SDK. Certification requires:
  - A public, code-complete product working at anticipated usage levels.
  - _Documented customer demand_ (a public ideas-forum thread).
  - Submission via pull request to Microsoft's connector repository.

  Once certified, Microsoft distributes the connector but routes customer issues with it back to the partner developer - certification transfers distribution, not support. Microsoft also encourages self-signed custom connectors as a lighter-weight path than full certification.

- A schema change can break a customer's dashboard even when the data contract is honored, if it also breaks the connector package's customization file or a certified connector's expected column typing - the certification artifacts are a second stability surface coexisting with step 4's contract.

## The wire-protocol shortcut

Speaking an existing wire protocol sidesteps most of the above: every BI tool, `psql`, and every ORM already ships a Postgres driver, so a Postgres wire-protocol endpoint gets instant client compatibility with no `.taco` signing and no certification cycle. PostHog fronts its per-organization engines with exactly this. Mature wire-protocol server libraries exist in several ecosystems for emulating a Postgres endpoint over your own engine.

The cost is dialect commitment: you support the Postgres dialect and its type system, and nothing exotic. The inverse case is the anti-pattern - a custom query dialect (PostHog's own HogQL, by their own account "not a language that's already widely supported") restarts every BI integration from zero.

## The connection-setup page

Publish one per supported client; an undocumented connection string is a support ticket per customer. Each engine has its own URL template and driver class (`jdbc:postgresql://<host>:<port>/<db>` / `org.postgresql.Driver`, and equivalents per dialect), so document the exact template for the dialect you expose. Contents:

- URL template with every placeholder named, and the driver class or a bundled-driver download link. Default to bundling/shipping the driver; treat customer-supplied driver JARs as an escape hatch only (version pins), since driver mismatch is a recurring support burden.
- TLS stated as an explicit named requirement, never left to client-library defaults.
- The auth method for that client and where the credential comes from (see the ladder below).
- A distinct read-only endpoint name where the architecture has one - reader endpoints are a separate connection target from any writer, and the docs must make the distinction visible.

## The credential ladder

Preference order: **short-lived token > managed secret > static password**; inline credentials in a connection string never appear in any documented path. The industry is retiring static database passwords outright - Snowflake's dated milestone schedule (2025-2026) moves service users through three stages:

1. Moves human password users onto MFA.
2. Blocks new legacy service users.
3. Forces all service users onto key-pair, OAuth, PAT, or workload identity.

Design issuance on that trajectory:

- **Service accounts / automation**: key-pair auth where an RSA keypair signs a JWT that expires in about a minute - no password crosses the network, and a stolen token has a tiny replay window. Mark machine identities as service-type so the engine refuses password auth for them entirely.
- **BI tools**: external OAuth so the tool never stores a database password; desktop BI integrations use the authorization-code grant with PKCE (RFC 7636).
- **CLI / REST access where a redirect flow doesn't fit**: personal access tokens with a policy-bound maximum expiry.
- **Degradation path**: token-refresh support varies by client - a BI tool that can't store and refresh tokens falls back to a key-pair or PAT service account rather than to a static password. Verify each supported client's refresh capability before promising OAuth-only.

Scope every credential to one tenant's entitlement (the mapping table from the isolation design), give customers self-service issuance and revocation in the product, and rotate on the same dual-credential overlap discipline used for API keys - the credential sibling skill owns those mechanics in detail.
