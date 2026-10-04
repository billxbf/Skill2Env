# Backoff, jitter, retry budgets, and deadlines - the math

Canonical source for the jitter comparison: Marc Brooker, AWS Architecture Blog, "Exponential Backoff and Jitter" (2015, updated 2023 - the update states the guidance "continues to serve as a pillar for how Amazon builds remote client libraries"). His core finding: capped exponential backoff _alone_ "helps only a small amount" under contention - jitter, not backoff, is what reduces total client work in a retry storm.

## The four strategies

| Strategy                          | Formula                                          | Trade-off                                                                                          |
| --------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| Full jitter (recommended default) | `sleep = random(0, min(cap, base * 2^attempt))`  | Lowest total client work and lowest server load; slightly more total time to completion            |
| Decorrelated jitter               | `sleep = min(cap, random(base, sleep_prev * 3))` | More total work than full jitter, completes slightly faster                                        |
| Equal jitter                      | half the backoff fixed, other half randomized    | Brooker's "clear loser" among the jittered approaches - more work than full jitter and much slower |
| No jitter (plain exponential)     | `sleep = base * 2^attempt`                       | Categorically the worst - so slow in total that Brooker's own comparison graph leaves it off       |

Why no-jitter fails at fleet scale: 1,000 clients that failed together all retry at exactly t+100ms, t+200ms, t+400ms - re-creating the overload spike that caused the failures. Full jitter spreads the same population across the whole window.

Brooker's 2019 follow-up ("Timeouts, retries and backoff with jitter", AWS Builders' Library) extends jitter to any periodic job, with one caution: apply jitter _consistently per host_, so an overload pattern stays diagnosable instead of looking like random noise.

## A concrete documented schedule

Resend's documented client loop - a citable worked example for integrator docs:

```js
const delay =
  Math.min(1000 * Math.pow(2, attempt), 30000) + // 1s → 2s → 4s → 8s ... cap 30s
  Math.random() * 1000; // jitter
```

Prefer the retry library over hand-rolled math wherever one exists - the formula is one line there, pre-debugged:

- Python (tenacity): `wait_exponential_jitter(initial=1, max=10)`, bounded with `stop_after_attempt(5) | stop_after_delay(60)`
- JVM (Resilience4j): `IntervalFunction.ofExponentialBackoff(...)` with `exponentialBackoffMultiplier: 2`

Bound **both** attempts and total duration (the tenacity combinator above): each attempt can look reasonable while the loop blows past the caller's own budget. Log every retry - attempt number, error, next wait; both libraries treat retry logging as a default, not an opt-in.

## Retry budget: the fleet-wide cap

Per-caller attempt caps cannot prevent amplification: a fleet of 100 instances each retrying 3 times amplifies load on a struggling downstream by 300x while every instance's cap looks reasonable in isolation.

- Mechanism: track the ratio of retried to original requests over a sliding window (e.g. 1 minute); once it exceeds the budget (e.g. 20%), stop retrying and fail fast.
- Named implementation - AWS SDK standard mode's token bucket: each retry deducts tokens, each success replenishes; when the bucket empties, the SDK returns the error without retrying. 2026 rebalance: a transient-error retry now costs **14 tokens** (up from 5); a throttling retry still costs **5** - the higher transient cost makes the quota engage sooner during a sustained outage, so the downstream recovers faster.

## Deadline propagation

- Set **one overall deadline at the top** of the call; budget per-attempt timeouts inside it. Never create a fresh overall timeout inside each retry attempt - that silently extends the caller's real wait past what they committed to, and the "successful" retry may answer a caller who already gave up.
- Down a call chain, pass the remaining budget with the request so each hop subtracts its own time before calling deeper - a mid-chain service must never start work whose timeout exceeds what the top-level caller has left. gRPC is the citable mechanics: deadlines are absolute in the API but sent as _relative_ timeouts on the wire, converted at each hop, precisely to dodge clock skew between machines.
- Setting a single timeout value: measure p99 latency under normal load and set the timeout at 2-3x that p99 - not a round number, and never the OS default (120-300s, which pins a thread to a hung connection for minutes).

## Pattern stacking

When retry is combined with other resilience patterns, the execution order matters (Resilience4j's documented order):

```
Retry → CircuitBreaker → RateLimiter → Bulkhead → call
```

- Retry wraps the outermost layer, so one logical call can still retry across circuit-breaker rejections during the half-open probe.
- The circuit breaker is retry's complement, not its substitute: once a downstream is confirmed down, the OPEN state short-circuits further retries instead of making every caller pay the full backoff schedule.
- Half-open recovery must gate to one or two trial requests, not the whole backlog, or it re-creates the thundering herd.
