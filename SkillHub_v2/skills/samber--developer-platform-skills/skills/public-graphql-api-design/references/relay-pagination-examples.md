# Relay pagination examples

Worked material for step 3 of the workflow. Source: Apollo's official GraphQL schema guidance on the Relay Connection specification.

## The connection shape

```graphql
type Query {
  posts(first: Int, after: String, last: Int, before: String): PostConnection!
}

type PostConnection {
  edges: [PostEdge!]!
  pageInfo: PageInfo!
  totalCount: Int
}

type PostEdge {
  node: Post!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}
```

Usage rules:

- `first`+`after` paginate forward, `last`+`before` paginate backward - never mix directions in one request.
- Apply the same connection shape to paginated relationship fields on any type (`User.posts(first: Int, after: String): PostConnection!`), not just top-level `Query` fields.

## Cursor design rules

A cursor must be opaque (clients never parse it), stable (the same cursor always points at the same position), and serializable (typically base64). Three encodings:

| Encoding                        | When                         | Caveat                                              |
| ------------------------------- | ---------------------------- | --------------------------------------------------- |
| ID alone                        | unsorted or ID-ordered lists | doesn't preserve position under a custom sort       |
| `timestamp:id` (or sort-key:id) | sorted lists                 | required whenever sort order isn't ID order         |
| encoded offset                  | almost never                 | least stable - inherits offset's drift under writes |

## Offset vs cursor, the mechanics

- Offset allows arbitrary page jumps but breaks under concurrent writes: items shift between reads, so pages duplicate or skip rows. Deep offsets degrade - `OFFSET 10000` scans past 10,000 rows.
- Cursor pagination stays consistent under live writes and stays fast at any depth: an indexed `WHERE created_at < $cursor ORDER BY created_at DESC LIMIT 20` costs the same on page 1 and page 500. The price: no arbitrary page jumping, more implementation code.
- Index whatever the cursor filters and sorts on (`created_at`, or a composite like `(author_id, created_at)`) - an unindexed cursor query silently degrades to the full-scan cost offset had.

## The `totalCount` trap

A naive `COUNT(*)` over a large filtered table is expensive; never let it block every paginated response. Options in order of preference for a public API:

1. Make `totalCount` nullable and skip computing it when expensive.
2. Return an estimate and document it as one.
3. Serve exact counts from a separate, explicitly costed query.

Never ship a non-null `totalCount` on a public schema without confirming the count is cheap at real data scale - non-null is a promise you can't walk back without a breaking change.

## Server-side page-size cap

The schema cannot express an upper bound on an `Int` argument, so enforce it in the resolver (`Math.min(first, 100)`-style clamping) and document the cap next to the field. The cap doubles as the list-cost multiplier when a cost model prices connections (see the rate-limit sibling skill for scoring mechanics).

## Typed sort and filter arguments

```graphql
type Query {
  posts(
    first: Int
    after: String
    orderBy: PostOrder
    filter: PostFilter
  ): PostConnection!
}

input PostOrder {
  field: PostOrderField!
  direction: OrderDirection!
}

enum PostOrderField {
  CREATED_AT
  TITLE
  COMMENT_COUNT
}
enum OrderDirection {
  ASC
  DESC
}

input PostFilter {
  authorId: ID
  publishedAfter: DateTime
}
```

Never `orderBy: String` or `filter: JSON` - a typed input documents the legal values in the schema itself and keeps cursor encoding coherent (the cursor must embed the active sort key).
