# Worked examples

Two versions of the same quickstart for an imaginary hosted API (`Pigeon`, a transactional messaging API). The product is invented so the pair can carry every defect at once; every defect in it is real and documented, but do not cite Pigeon as evidence of anything.

For a real published page to read alongside this, the Good Docs Project points at Jekyll's docs as a quickstart done well - notably, its setup information sits in a separate document linked from the first step rather than inside the quickstart.

Read the negative example first - the mistakes in it are the ones that survive review most often because each one looks helpful in isolation.

## Table of Contents

- [Negative example](#negative-example)
- [Installation](#installation)
- [Configuration](#configuration)
- [Sending](#sending)
- [Positive example](#positive-example)
- [Before you start](#before-you-start)
- [1. Install the client](#1-install-the-client)
- [2. Send a message](#2-send-a-message)
- [3. Confirm delivery](#3-confirm-delivery)
- [What just happened](#what-just-happened)
- [Next steps](#next-steps)
- [Applying this to other product classes](#applying-this-to-other-product-classes)

## Negative example

```markdown
# Getting started with Pigeon

Welcome to Pigeon! Pigeon is a modern messaging platform built on an
event-driven architecture. Before we begin, it helps to understand how
delivery guarantees work. Pigeon uses at-least-once delivery with
idempotency keys, which means…

[four more paragraphs]

## Installation

Run `npm install` to install dependencies.

## Configuration

Create a client with your API key. You can find your API key in the
account settings section of the dashboard.

    const pigeon = new Pigeon("sk_live_4eC39H");

## Sending

Now send a message. Note that you need a verified sender identity first;
see the sender verification guide.

    await pigeon.messages.send({ to: "+15551234567", body: "Hi" });

That's it! Explore the API reference to learn about scheduling, templates,
webhooks, batching, analytics, and our Terraform provider.
```

### Why each part fails

| Line                                    | Defect                                    | Cost                                                              |
| --------------------------------------- | ----------------------------------------- | ----------------------------------------------------------------- |
| Delivery-guarantee preamble             | Explanation before action                 | Reader spends the budget reading, not running                     |
| `npm install` with no package name      | Assumed environment                       | Command fails verbatim; reader must guess                         |
| "find your API key in account settings" | Credential path not linked                | Reader leaves the page and often does not return                  |
| `sk_live_4eC39H`                        | Plausible fake value, and a live-mode key | Pasted verbatim; fails with an auth error the page never mentions |
| Sender verification named at step 3     | Prerequisite discovered mid-run           | Run stops; the real blocker is a separate multi-hour process      |
| No expected output anywhere             | Nothing observable                        | Reader cannot tell success from silent failure                    |
| Seven next steps                        | Choice overload                           | Reader browses instead of continuing                              |

## Positive example

```markdown
# Send your first Pigeon message in 5 minutes

You will send a test message from your terminal and see its delivery
status change to `delivered`.

## Before you start

- Node.js 18 or later: check with `node --version` (https://nodejs.org)
- A Pigeon test API key: [create one](https://example.com/keys) (no card required)

Test keys start with `sk_test_` and send to the sandbox only, so nothing
reaches a real phone.

## 1. Install the client

    npm install @pigeon/client@3

## 2. Send a message

Create `send.js`:

    import { Pigeon } from "@pigeon/client";

    const pigeon = new Pigeon("<YOUR_TEST_API_KEY>");

    const message = await pigeon.messages.send({
      to: "+15005550006",          // sandbox number, always accepts
      body: "Hello from Pigeon",
    });

    console.log(message.id, message.status);

Run it:

    node send.js

You should see:

    msg_01HQ4B9K queued

`401 Unauthorized`? The key was not copied whole; it ends with a
checksum segment. Copy it again from the keys page.

## 3. Confirm delivery

    npx pigeon messages get msg_01HQ4B9K

You should see:

    status: delivered
    delivered_at: 2026-08-26T09:14:22Z

Still `queued` after 30 seconds? The sandbox delivers within 5 seconds;
a longer wait means the message was sent to a non-sandbox number.

## What just happened

You created a message and Pigeon delivered it asynchronously: the send
call returns immediately with a `queued` status, and delivery status
arrives later.

## Next steps

- [Receive delivery webhooks](…)
- [API reference](…)
- [Community Discord](…)
```

### What the rewrite changed

1. Title promises an outcome and a time; the cold run enforces both.
2. Every prerequisite appears before step 1 with a check command and a one-click credential link.
3. The sandbox number removes the sender-verification prerequisite entirely - the strongest fix available is deleting a requirement, not documenting it.
4. Placeholder is unmistakable; the key shown is test-scoped, so a copy-paste mistake cannot cost money.
5. Every step shows real output and one fail branch tied to the most common error.
6. The asynchronous-delivery concept is explained only after the reader has seen it happen, in two sentences.
7. Three next steps, one per intent: build further, look things up, ask a human.

## Applying this to other product classes

- **CLI**: the success moment is the artefact on disk; show `ls`/`cat` output, not just the command's exit.
- **Self-hosted**: the success moment is a health endpoint answering; give one container command with pinned tags, and state resource requirements as prerequisites.
- **Data platform**: insert the rows in the quickstart itself, then query them - a demo dataset the reader did not create weakens the proof.
