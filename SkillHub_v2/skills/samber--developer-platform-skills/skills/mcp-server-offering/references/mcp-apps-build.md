# Building an MCP App

Implementation walkthrough for the MCP Apps decision in `SKILL.md` step 2. Source: the official MCP Apps build guide (modelcontextprotocol.io, "Build an MCP App") and the `modelcontextprotocol/ext-apps` repository. The toolkit is under active development: re-check package and function names against the API docs before shipping.

## Pick the path

- **Agent-assisted (fastest).** Install the official `create-mcp-app` skill, then ask the coding agent for the app ("Create an MCP App that displays a color picker"). It scaffolds server, UI and configuration.
  - Claude Code: `/plugin marketplace add modelcontextprotocol/ext-apps`, then `/plugin install mcp-apps@modelcontextprotocol-ext-apps`.
  - Any skills-compatible agent: `npx skills add modelcontextprotocol/ext-apps`.
- **Manual.** Follow the steps below. Use it when the team wants to own every file, or when the server is not in TypeScript (port the pattern; the protocol is plain JSON-RPC over `postMessage`).

## Manual setup

Prerequisite: Node.js 18 or higher, and working knowledge of MCP tools and resources, since an app combines both.

1. **Lay out the project.** Keep server and UI apart:
   - `server.ts`: the MCP server, registering the tool and the UI resource.
   - `mcp-app.html`: the UI entry point.
   - `src/mcp-app.ts`: the UI logic.
   - `package.json`, `tsconfig.json`, `vite.config.ts`.
2. **Install dependencies.**
   - Runtime: `@modelcontextprotocol/ext-apps` (server helpers plus the UI `App` class) and `@modelcontextprotocol/sdk`.
   - Build: `typescript`, `vite`, `vite-plugin-singlefile`, and an HTTP layer (the guide uses `express` + `cors`, run with `tsx`).
3. **Bundle the UI into one HTML file.** The host renders the resource in an iframe with a deny-by-default CSP. Either inline every script and stylesheet with `vite-plugin-singlefile` (the guide's `build` script: `INPUT=mcp-app.html vite build`), or keep external assets and declare their origins in `_meta.ui.csp`. Inlining is the default: fewer origins, smaller attack surface.
4. **Register the tool with its UI.** On the server, call `registerAppTool(server, name, config, handler)` from `@modelcontextprotocol/ext-apps/server`. The config carries `_meta: { ui: { resourceUri } }`, where `resourceUri` uses the `ui://` scheme (for example `ui://get-time/mcp-app.html`; the path is free-form). The handler still returns a normal MCP result (`content`, structured data): that result is what non-app hosts and the model see.
5. **Serve the UI resource.** Call `registerAppResource(server, resourceUri, resourceUri, { mimeType: RESOURCE_MIME_TYPE }, handler)`. The handler reads the bundled HTML and returns it as the resource `text` with the same `RESOURCE_MIME_TYPE`.
6. **Expose the server.** Serve MCP over Streamable HTTP (the guide mounts `StreamableHTTPServerTransport` on `POST /mcp`). Remote hosting and OAuth follow `SKILL.md` step 4 like any other tool.
7. **Write the UI.** In `src/mcp-app.ts`:
   - Create `new App({ name, version })` and call `app.connect()` once at start-up.
   - Handle the result the host pushes when the tool runs in `app.ontoolresult`.
   - Call server tools from user actions with `app.callServerTool({ name, arguments })`. Each call is a round-trip to the server: show a loading state and handle errors.
   - The `App` class also covers logging, opening URLs, and updating the model's context with structured data from the app.
   - Any framework works; the official examples ship React, Vue, Svelte, Preact, Solid and vanilla templates.

## Test

1. Build and start: `npm run build && npm run serve` (the guide's server listens on `http://localhost:3001/mcp`).
2. **Local test host.** Clone `modelcontextprotocol/ext-apps`, run `npm install` in `examples/basic-host`, then `SERVERS='["http://localhost:3001/mcp"]' npm start` and open `http://localhost:8080`. Pick the tool, call it, and check the app renders and its tool calls work.
3. **Real host.** Tunnel the local server (`npx cloudflared tunnel --url http://localhost:3001`) and add the URL as a custom connector in Claude (Settings, Connectors, Add custom connector; paid plans). Repeat in a second host from the client matrix.
4. **Fallback.** Call the same tool from a client without the extension and confirm the plain result alone completes the job.

## Before shipping

- Run the tool through its step 3 risk tier with the UI as the caller: every write the app can trigger passes the same gate.
- Review `_meta.ui.csp` and `_meta.ui.permissions`: nothing listed that the app doesn't load or use.
- Escape model- and user-supplied data in the UI like any untrusted input.
- Version the `ui://` resource together with the tool's result shape (step 5).
