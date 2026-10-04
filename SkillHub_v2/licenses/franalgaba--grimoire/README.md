# Grimoire

<p align="center"><em>"Verba Volant, Scripta Manent."</em></p>

[![CI](https://github.com/franalgaba/grimoire/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/grimoire/actions/workflows/ci.yml)

Grimoire is a language for agents to express financial intent with readable syntax and deterministic execution. Spells compile to an intermediate representation (IR) and run through protocol adapters, so you can swap venues by changing aliases and configuration instead of rewriting strategy logic.

[Examples](./spells) | [Skills](./skills)

---

## Start here

Grimoire has one runtime semantics: preview first, then commit for irreversible actions. The same behavior applies across CLI and library entry points.

For a single onboarding flow for both users and agents, start with:

- `docs/tutorials/quickstart-users-and-agents.md`

### CLI entry point (`grimoire`)

Use this for reproducible simulation and onchain execution with adapters and state persistence.

```bash
npm i -g @grimoirelabs/cli

grimoire setup

grimoire simulate spells/compute-only.spell --chain 1

grimoire cast spells/uniswap-swap-execute.spell \
  --dry-run \
  --key-env PRIVATE_KEY \
  --rpc-url <rpc>
```

`grimoire setup` notes:

- setup is always execute-mode onboarding
- guided mode prompts for required values (chain, RPC, wallet source, doctor checks)
- blank RPC input falls back to public chain RPC
- setup runs a smoke preview and `venue doctor` by default
- when password is entered interactively, setup writes `.grimoire/setup.env` (can disable with `--no-save-password-env`)
- CLI auto-loads nearest `.grimoire/setup.env` on startup and does not override already-set env vars
- set `GRIMOIRE_SETUP_ENV_FILE` to point to an explicit env file when running outside the project tree
- `.grimoire/setup.env` contains plaintext secrets; keep it local-only and rotate/delete when not needed

`simulate` also supports `--rpc-url <rpc>` with resolution order:
`--rpc-url` -> `RPC_URL_<chainId>` -> `RPC_URL`.

When you are ready to execute live:

```bash
grimoire cast spells/uniswap-swap-execute.spell --key-env PRIVATE_KEY --rpc-url <rpc>
```

Want live snapshot params for strategy inputs?

```bash
grimoire venue morpho-blue vaults --chain 8453 --asset USDC --min-tvl 5000000 --format spell
grimoire venue pendle chains
```

Before running venue actions in a new environment, validate adapter/env/RPC readiness:

```bash
grimoire venue doctor --chain 1 --adapter uniswap --rpc-url <rpc> --json
```

If this command errors with `Unknown venue adapter "doctor"`, your installed CLI is outdated.
Use one of:

- `npm i -g @grimoirelabs/cli@latest`
- `npx -y @grimoirelabs/cli@latest venue doctor --chain 1 --adapter uniswap --rpc-url <rpc> --json`
- `bun run packages/cli/src/index.ts venue doctor --chain 1 --adapter uniswap --rpc-url <rpc> --json`

Advisory steps (`advise`) call Pi when a model is configured (spell model, CLI model/provider, or Pi defaults). If no model is available, the runtime uses the spell’s fallback. Record advisory outputs with `simulate` (or `cast --dry-run`), then replay deterministically with `--advisory-replay` for live execution.

Advisory docs:

- `docs/how-to/use-advisory-decisions.md`
- `docs/explanation/advisory-decision-flow.md`
- `docs/reference/spell-syntax.md#advisory-syntax`

Protocol comparison docs:

- `docs/how-to/compare-protocol-metrics.md`
- `docs/reference/venues.md#metric-surfaces`

See `grimoire --help` for all CLI commands.

### Library entry point (`@grimoirelabs/core`)

Use this when embedding Grimoire into an app/agent process. The library shares the same compiler/interpreter semantics and preview/commit model as the CLI.

See `docs/reference/compiler-runtime.md` for `compile`, `preview`, `commit`, `execute`, and session APIs.

### Agent-assisted entry point (skills)

Use skills in `skills/` so agents can work immediately with Grimoire:

- install: `npx skills add https://github.com/franalgaba/grimoire`
- `skills/grimoire/` for install, CLI usage, syntax starter, and runbook
- venue skills for snapshot params (`skills/grimoire-aave/`, `skills/grimoire-uniswap/`, `skills/grimoire-morpho-blue/`, `skills/grimoire-across/`, `skills/grimoire-hyperliquid/`, `skills/grimoire-pendle/`, `skills/grimoire-polymarket/`)

For Claude Code, run the same install command in the Claude Code terminal and start a new session to load the skills.

---

## Example spell

```spell
spell YieldOptimizer {

  assets: [USDC, DAI]

  advisors: {
    risk: {
      model: "anthropic:haiku"
    }
  }

  venues: {
    aave_v3: @aave_v3
    morpho_blue: @morpho_blue
  }

  params: {
    amount: 100000
  }

  on hourly: {
    decision = advise risk: "Do gas costs justify rebalancing now?" {
      output: {
        type: boolean
      }
      timeout: 10
      fallback: true
    }

    if decision {
      amount_to_move = to_number(balance(USDC)) * 50%
      aave_v3.withdraw(USDC, amount_to_move)
      morpho_blue.lend(USDC, amount_to_move)
    }
  }
}
```

## Features

- **Human-readable DSL** with brace-delimited syntax
- **Explicit constraints** and limits via `with` and `limits`
- **Adapter-based venues** (SDKs live in `@grimoirelabs/venues`)
- **Official adapters** include Aave V3, Uniswap V3/V4, Morpho Blue, Across, Hyperliquid, Pendle, and Polymarket
- **Onchain + offchain** actions (EVM + Hyperliquid)
- **Judgment boundary** with explicit `advise` blocks
- **Structured control flow** (loops, conditionals, try/catch, atomic)
- **State persistence** and run history for deterministic execution
- **Unified runtime semantics** across CLI and programmatic embedding

ENS profile hydration is available on CLI runs via `--ens-name` and `--ens-rpc-url`.

## Documentation

Documentation follows [Diataxis](https://diataxis.fr/) in `docs/`:

- `docs/tutorials/`
- `docs/how-to/`
- `docs/reference/`
- `docs/explanation/`

Start at `docs/README.md` for navigation.

## Updating

- Update the CLI: `npm i -g @grimoirelabs/cli@latest`
- Use `npx` for latest without install: `npx -y @grimoirelabs/cli@latest <command>`
- Update packages in your project: `npm i @grimoirelabs/core@latest @grimoirelabs/venues@latest`

## Development

```bash
bun install
bun run validate
```

For onchain tests and advanced workflows, see `docs/`.

## License

MIT
