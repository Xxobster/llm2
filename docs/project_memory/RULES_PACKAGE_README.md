# Trading Bot Cursor Rules v2.1

This package replaces the duplicated 17,000-word rule collection with a layered system that Cursor can apply consistently.

## Files

- `TRADING_BOT_RESEARCH_STANDARD_V2.md` â€” the complete canonical methodology, audit, risk, validation and live-readiness standard.
- `FROZEN_DEFAULT_GATES_V2_1.md` â€” reviewed and frozen historical, stress, risk, shadow and micro-live gate policy.
- `trading-bot-core.mdc` â€” short always-on Cursor rule that routes relevant work to the detailed standard and project profile.
- `TRADING_PROJECT_PROFILE.template.md` â€” per-repository venue, product, wallet, risk, path, VPS and preference values.
- `TRADESIM_BACKTEST_ENGINE_GUIDE.md` — how the shared backtest engine (tradesim) works: exact fields a strategy must emit, frozen fill/fee/slippage/funding defaults, lower-timeframe TP vs SL resolution, and candle refresh rules. Strategy repos use this file as the interface contract.
- `LEAKAGE_TEST_GUIDE.md` — how every coding agent must run the shared `leakage` package before train/test: prefix-invariance, future-mutation, `LEAKAGE_POTENTIAL` registry, CLI and API.
- `CURSOR_BOOTSTRAP_PROMPT.md` â€” copy/paste prompt for installing/adapting the package in a repository.
- `REORGANIZATION_ANALYSIS.md` â€” what was wrong with the original collection and how conflicts were resolved.

## Recommended installation

Place the files as follows:

```text
.cursor/rules/trading-bot-core.mdc
docs/project_memory/TRADING_BOT_RESEARCH_STANDARD_V2.md
docs/project_memory/FROZEN_DEFAULT_GATES_V2_1.md
docs/project_memory/TRADING_PROJECT_PROFILE.md
```

Create `TRADING_PROJECT_PROFILE.md` from the template and verify every value for that repository. The V2.1 gates are installed by default and cannot be relaxed after the affected OOS is viewed.

Do not put the entire detailed standard in an always-on `.mdc` rule. The short core rule remains active and tells Cursor when it must read the full standard. This reduces prompt noise while keeping the detailed requirements enforceable.

## First use

Attach the ZIP to Cursor (or extract/copy the package into the trading-bot repository), open `CURSOR_BOOTSTRAP_PROMPT.md`, and paste its contents into Cursor. Cursor will install the layered rules, complete the verified project profile, hash the evidence and audit the existing implementation without touching live systems.

The bootstrap task installs and audits the rules. It deliberately does not authorize deployment, live restarts, order placement or risk changes.

## leakage engine (Xxobster / botsgeneral) — mandatory before train/test

Every coding agent that trains or tests models on project-built indicators MUST run the
**latest** `leakage` package from `C:\\projects\\botsgeneral\\packages\\leakage` first:

- Call `prefer_botsgeneral_leakage()` before other leakage imports; refuse if
  `leakage.__file__` lacks `botsgeneral`.
- Decisive check: prefix-invariance via the production `build_features` path.
- On hard-fail: stop; mark columns `LEAKAGE_POTENTIAL`; fix builder; rebuild; re-audit.
- Operator guide in this package: `LEAKAGE_TEST_GUIDE.md`.

## tradesim engine (Xxobster / botsgeneral) — mandatory

Every strategy program that backtests, plots, or compares live vs BT MUST use the **latest**
	radesim from C:\\projects\\botsgeneral\\packages\\tradesim:

- Call prefer_botsgeneral_tradesim() before other tradesim imports; refuse if 	radesim.__file__ lacks otsgeneral.
- Prefer 
un_backtest(..., strategy_meta={name, batch, model_path, tp_pct, sl_pct, ...}).
- Artifacts: D:\\projectsdata\\backtests\\tradesim_runs.sqlite + D:\\projectsdata\\backtests\\reports\\{run_id}\\.
- Reopen without resim: 	radesim-research open --run-id ...
- Operator guide in this package: TRADESIM_BACKTEST_ENGINE_GUIDE.md.

## Backtest-engine conformance (v2.2)

The v2.1 package stated the correct execution principles as prose. That proved insufficient: a repository can have a fully green test suite, satisfy every reviewer's reading of the checklist, and still exempt the entry bar from its own stop â€” which on one daily strategy hid that 47.6% of trades were stopped out on their entry day and turned an out-of-sample Profit Factor of 1.50 into 0.90.

v2.2 adds the enforcement mechanism:

- **Section 9.6** makes first-bar exit resolution explicit and non-negotiable, including same-bar fees, funding and hold counting.
- **Section 4.4** bans re-implementing a trade simulator when a shared conformant engine exists, and requires a fixture-pack pass plus an explained parity diff if one is unavoidable.
- **Section 24.0** defines conformance identifiers (`EXEC-001` â€¦ `EXEC-017` and the other areas), requires each to be bound to a discoverable test, requires a checker in which a **missing** test fails the build like a failing one, requires a shared content-hashed golden fixture pack as the single arbiter across repositories, and requires every result artifact to carry a conformance stamp. A number without a green stamp is not quotable evidence.
- **Section 28** adds the entry-bar free-pass, the separate entry-bar code path, the fee/funding-free same-bar round trip, "green suite presented as parity", and "quoting an unstamped number" as forbidden patterns.

The negative control matters as much as the positive test: `EXEC-014` requires proving that a quiet entry bar does **not** close the position, so an engine cannot pass by closing everything immediately.

## Important policy changes from the old rules

- Leverage is selected after edge and quantity, under capital/liquidation constraints; it is not maximized to improve returns.
- Win rate is reported with uncertainty but is not a universal deployment gate.
- Limit/maker execution still models non-fill, queue, latency, partial fills and adverse selection.
- Exact target venue/product history outranks â€œlongest possibleâ€ proxy history.
- Vectorization applies to bulk calculations; stateful execution uses chronological event loops.
- Research uses bounded preregistered generations rather than adding indicators until something passes.
- Readiness, failure reasons and human authorization are stored separately.
- Close-based live loops schedule on the bar boundary (idle, pre-close wake-up, post-close confirmation window, exactly one decision per bar) instead of a fixed wall-clock poll; per-timeframe defaults are in section 22.1.
- The wake cadence is the *source* timeframe (including candles a collector writes to a shared database) while the evaluation cadence is the *decision* timeframe, and an open position keeps a 30â€“60 s reconciliation heartbeat regardless of bar length; see section 22.1.

## Versioning

Hash the installed detailed standard and completed profile and store the hashes with every research run. Any material change creates a new evidence version and invalidates inherited readiness for affected results.

## Frozen V2.1 headline gates

- daily MTM annualized Sharpe >= 1.00 and HAC-adjusted Sharpe >= 0.75;
- pooled outer-OOS PF >= 1.20;
- >= 80% eligible positive/PF>1 outer folds;
- DSR >= 0.95;
- >= 50 pooled OOS trades and >= 10 per gating fold;
- moderate-stress PnL > 0 and PF >= 1.05;
- baseline/stress MDD <= 20%/25%, margin utilization <= 60%;
- PBO <= 0.20 only when a complete valid matrix exists;
- no universal win-rate gate.
