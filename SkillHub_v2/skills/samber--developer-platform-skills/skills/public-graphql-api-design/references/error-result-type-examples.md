# Error result-type examples

Worked material for step 4 of the workflow. Source: Apollo's official GraphQL schema guidance on error patterns, corroborated independently by Shopify's `graphql-design-tutorial`.

## The two mechanisms

**Built-in top-level errors** - what every GraphQL server emits without design work:

```json
{
  "data": { "user": null },
  "errors": [
    {
      "message": "Internal server error",
      "path": ["user"],
      "extensions": { "code": "INTERNAL_SERVER_ERROR" }
    }
  ]
}
```

**Right for:**

- Unexpected server faults.
- Authentication/authorization failures.
- Malformed-query validation.

Anything the caller can't plan around.

**Wrong for:**

- Expected business outcomes (item out of stock).
- Operations with several distinct failure modes.
- Errors needing rich typed data.

Those are data, and belong in the schema.

## The union result pattern (default for mutations)

```graphql
type Mutation {
  createOrder(input: CreateOrderInput!): CreateOrderResult!
}

union CreateOrderResult =
  | CreateOrderSuccess
  | ValidationError
  | InsufficientInventory
  | PaymentFailed

type CreateOrderSuccess {
  order: Order!
}
type ValidationError {
  message: String!
  field: String
}
type InsufficientInventory {
  message: String!
  unavailableItems: [OrderItem!]!
}
type PaymentFailed {
  message: String!
  reason: PaymentFailureReason!
  retryable: Boolean!
}
```

Clients handle each branch with `... on TypeName` fragments. The payoff: the possible-outcomes list lives in the schema, not in prose docs a client can ignore - a client cannot accidentally skip a failure mode the way it can with an untyped error body.

## The interface variant

For sharing common error fields across otherwise-distinct error types:

```graphql
interface Error {
  message: String!
}

type NotFoundError implements Error {
  message: String!
}
type PermissionError implements Error {
  message: String!
  requiredRole: Role!
}

union UserResult = User | NotFoundError | PermissionError
```

Useful when several unrelated operations share a small set of failure shapes and clients want one fragment (`... on Error { message }`) matching any of them.

## The error-code enum

Layer a shared enum under either pattern so clients switch on stable codes while `message` text stays free to change:

```graphql
enum ErrorCode {
  VALIDATION_FAILED
  UNAUTHENTICATED
  NOT_FOUND
  INSUFFICIENT_FUNDS
  RATE_LIMITED
}
```

The enum is the schema-level expression of an error-code taxonomy; the deeper taxonomy discipline (catalog ownership, stability contract, documentation anchors) is `samber/developer-platform-skills@api-error-design`'s ground.

## Batch and partial-success shapes

- Batch mutations: return `{ successful: [Item!]!, failed: [BatchError!]! }` instead of failing the whole batch on one bad item - `BatchError` carries an `index` or `itemId` plus a typed `error` union.
- Non-batch partial data (a field backed by a flaky upstream): give each independently fetched field its own result union - `profileImage: ImageResult!` with `union ImageResult = Image | FetchError` - preferred over a nullable field with a sibling error string, because it's typed.

## Disclosure traps this pattern interacts with

- **Null-vs-error as an existence oracle**: if an unauthorized field returns `null` when the resource exists but errors when it doesn't (or vice versa), the response shape distinguishes "exists" from "doesn't" for an attacker. Pick one behavior and apply it uniformly regardless of existence.
- **Raw internal errors**: never surface `Database error: SQLSTATE[23000]...` - translate to a public message plus an `extensions.code` (built-in path) or a typed error object (result-type path). Keep stack traces out of production responses entirely.
