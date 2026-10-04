# Schema convention tables

Convention reference for step 2 of the workflow. Sources: Apollo's official GraphQL schema guidance and Shopify's public `graphql-design-tutorial` (numbered rules cited inline); Marc-André Giroux's published MOIST principle.

## Casing by construct

| Construct                              | Convention                            | Example                                  |
| -------------------------------------- | ------------------------------------- | ---------------------------------------- |
| Object / interface / union / enum type | PascalCase, singular noun             | `User`, not `Users` or `user`            |
| Field, argument                        | camelCase                             | `firstName`, `emailAddress`              |
| Enum value                             | SCREAMING_SNAKE_CASE                  | `PENDING_PAYMENT`                        |
| Boolean field                          | `is`/`has`/`can`/`should` prefix      | `isActive`, `hasSubscription`, `canEdit` |
| Collection field                       | plural noun                           | `posts`, `followers`                     |
| Input type                             | mutation name + `Input`               | `CreateUserInput`                        |
| Payload/result type                    | mutation name + `Payload` or `Result` | `CreateOrderResult`                      |

- Name fields for what they return, not how they're computed: `fullName`, never `getFullName`.
- Relationship fields name the relationship: `author: User!`, not `createdBy`.
- Choose names for what makes sense to the client, not what the field is called in a legacy API or the data store (Shopify Rule #9).

## The mutation-naming fork

Both conventions are documented production practice; pick one in the interview and enforce it schema-wide:

- **Verb-first** (Apollo's default): `createUser`, `likePost` - "a mutation represents an action."
- **Noun-first** (Shopify's deliberate inversion): `userCreate`, `postLike` - groups a type's mutations together when tooling alphabetizes fields, and fits a mostly CRUD-shaped domain.

Either way, model mutations around business actions, not generic CRUD: `publishPost`, `archivePost`, `cancelOrder`, each with a tightly scoped input and payload - never one monolithic `updateOrder` for every conceivable field change.

## Mutation argument structure (Shopify Rule #22)

Keep the selection argument (which object to change) separate from the change-data argument:

```graphql
# Good  - selection and change data are distinct
type Mutation {
  collectionUpdate(
    collectionId: ID!
    collection: CollectionInput!
  ): CollectionUpdatePayload!
}

# Bad  - one merged input with a nullable id: is `id` a filter or the target?
type Mutation {
  collectionUpdate(input: CollectionUpdateInput!): CollectionUpdatePayload!
}
```

Make the selection argument non-nullable unless treating it as an optional filter has real value.

## Nullability table

| Declaration  | Meaning                       |
| ------------ | ----------------------------- |
| `String`     | nullable                      |
| `String!`    | non-null                      |
| `[String]`   | nullable list, nullable items |
| `[String!]`  | nullable list, non-null items |
| `[String]!`  | non-null list, nullable items |
| `[String!]!` | non-null list, non-null items |

Rules layered on the table:

- Use `[Type!]!` for every list field - an empty list over a null list, never a null item inside.
- A field that can legitimately fail to resolve is nullable at the object/scalar level (or gets its own result union - see the error-pattern reference), never forced into a null list.
- Mutation payload fields lean nullable "unless there is really a value to return in every possible error case" (Shopify Rule #24) - an all-non-null payload cannot represent partial failure.
- Every nullability decision is intentional; a schema where everything is nullable hides every guarantee from the client, and reflexive non-null spreads breakage (a failed non-null field nulls its whole parent chain).

## Input/output separation

Define a dedicated `input` type for what a mutation receives; never reuse an output `type` as an argument. The two differ structurally:

- Input fields are often optional on update.
- Output fields carry whatever the domain guarantees.
- An input never holds server-computed fields like `createdAt`.

## Interface vs union, by intent

- Interface (`interface Node { id: ID! }`, `interface Timestamped`) - multiple types share a capability clients query polymorphically.
- Union (`union SearchResult = User | Post | Comment`) - mutually exclusive alternatives with no shared field set.
- Don't reach for a union to avoid picking one output type: every consumer then needs `... on Type` fragments - a client-facing complexity cost, not a free abstraction.

## ID strategy

- `ID` scalar for every identifier - never `String` or `Int`.
- Implement `Node` (`interface Node { id: ID! }`) on every entity type: any object is refetchable via `node(id: ...)` regardless of which query first produced it.
- IDs are opaque and global; base64-encode compound identities (mirrors cursor opacity in the pagination reference).
- Object references over foreign keys (Shopify Rule #8): `author: User!`, not `authorId: ID!`. Reserve a bare ID field for the object's own identity only.
- Custom scalars (`DateTime`, `Email`, `URL`) for domain-validated values instead of a bare `String` every resolver re-validates ad hoc.

## MOIST: the counter-argument to consolidating types

Giroux's MOIST principle ("Moist Once Is Sometimes Tolerable") argues against reflexive DRY in schema design: `Viewer`, `UserProfile`, and `TeamMember` overlap on `name`/`email` yet serve genuinely different use cases and evolve independently. Cramming every field that sounds user-shaped into one `User` type couples unrelated use cases to one type's evolution. Cite it whenever a review is tempted to merge types purely to avoid field duplication.

## Anti-pattern list

Flag each of these in review:

- Hungarian notation (`TUser`, `strName`) or redundant type-name prefixes inside a type (`userId`/`userName` inside `type User` - just `id`/`name`).
- Implementation details in the schema: `mysql_id`, `redis_cache_key`.
- Vague catch-all shapes: `getData: JSON`, `filter: JSON`, `options: Options` - use typed, named arguments.
- Mixed casing or mixed mutation-naming order within one schema.
- Docstrings written for the engineering team ("Synced with Salesforce via nightly cron") - they publish architecture to every schema reader; write them for the public audience.
