# Process supervision and candle freshness (mandatory)

Two process classes. Agents must not confuse them.

| Class | Examples | Duty |
|---|---|---|
| **A. Long batch (finite)** | Fleet backtests, walk-forward, model hunts, large downloads, leakage+score pipelines, Finplot batches | Must finish. Run under a **watchdog** that restarts on crash/stall. Bounded restarts. |
| **B. Continuous service (infinite)** | Trading / shadow bots, candle collectors, poker bots, indicator refreshers that feed live, message bridges tied to live | Must **always** be running when authorized. Supervised (`systemd` / equivalent). Auto-restart. Health-checked. Fail closed on bad data. |

Default research posture remains `LIVE_STOP / RESEARCH_ONLY`. Continuous-service rules apply whenever a service is **authorized to run** (live, shadow, or always-on infrastructure such as the candle collector). Authorization to research is not authorization to leave live bots unmanaged.

---

## A. Long batch jobs (local machine)

Any local command expected to take **more than ~10 minutes**:

1. Do **not** leave a bare `python …` with no monitor.
2. Launch under a project watchdog (example: `scripts/watchdog_run.ps1`) with `python -u` so logs grow.
3. Poll process id + child-log growth. Restart on crash or stall (bounded `MaxRestarts`, default 3).
4. Clean exit code 0 is **not** restarted.
5. Never trust a frozen terminal header (`status: running` with stuck `running_for_ms`) — verify the process id is alive.
6. If the watchdog itself dies, restart the **watchdog**, not only the child.
7. Prefer checkpoint/resume for multi-hour hunts so a restart does not recompute finished work.

Watchdog does **not** authorize live deploy, VPS restarts, or order placement.

---

## B. Continuous services (must always run)

Authorized continuous services include (non-exhaustive):

- candle / market-data collectors;
- trading bots and shadow bots;
- poker bots and other always-on game agents on the same ops stack;
- any writer that live decision code depends on (indicators tip refreshers, funding ingest, etc.).

### B.1 Supervision

- Install under a process supervisor (`systemd` preferred on VPS; Docker restart policy; or an equivalent with crash restart).
- Policy: **restart on failure**, bounded crash loops with alerting, singleton lock (one instance per unit).
- A process being “present” is **not** health. Health requires: process active + fresh heartbeat + fresh data tip + (for trading) exchange reconciliation + protective orders when in position.
- After any code deploy, config change, reboot, or incident: **verify** every concerned unit is `active` and healthy. If it cannot stay up, find the root cause and fix it — do not leave it down.
- Do not stop, mask, disable, or delete an authorized continuous unit unless the user explicitly authorized that exact action (or an incident policy already freezes trading and the user ordered a stop).
- Research agents still need explicit authorization before restarting/stopping **live trading** units; infrastructure collectors that are already authorized must be restored if found down.

### B.2 Collector failure → bots must not trade

If the candle collector (or equivalent ingest) reports an error, cannot fetch the tip, or the warehouse tip is behind exchange time:

1. Mark the affected `symbol` / `timeframe` (and dependents) **DATA_UNSAFE**.
2. Every concerned bot must **fail closed**:
   - no new entries;
   - cancel resting **entry** intents / working LIMIT entries that have not filled;
   - keep existing positions **protected** (stop / take-profit / reduce-only exits stay);
   - emit a distinct event (e.g. `CANDLE_STALE` / `COLLECTOR_ERROR`) with symbol, timeframe, local tip, expected tip, server time.
3. Resume entries only after tip freshness **passes** again for that bot’s decision (and touch) timeframes.

This applies even when only a **15-minute** series is missing or late. Wrong tip ⇒ wrong features ⇒ wrong signal.

### B.3 Per-bot tip freshness check (mandatory before every decision)

Before computing a signal or opening risk on a closed bar, each bot MUST verify the local last **closed** candle is the one the exchange clock implies.

Canonical check (vectorize / cheap path):

```text
tf_ms              = timeframe length in milliseconds
server_now_ms      = exchange server time (REST time endpoint or equivalent; not only local wall clock)
expected_closed_open_ms = floor(server_now_ms / tf_ms) * tf_ms - tf_ms
local_closed_open_ms    = open time of latest CLOSED candle in the bot’s data source for symbol/tf

IF local_closed_open_ms is missing:
    FAIL → CANDLE_MISSING
ELIF local_closed_open_ms < expected_closed_open_ms:
    FAIL → CANDLE_STALE (tip behind server)
ELIF local_closed_open_ms > expected_closed_open_ms:
    FAIL → CANDLE_AHEAD (clock / incomplete bar treated as closed — refuse)
ELIF abs(local_wall_ms - server_now_ms) > clock_skew_max_ms:
    FAIL → CLOCK_SKEW
ELSE:
    PASS (optionally also require collector last_ok for this series)
```

Defaults (project may freeze stricter values in the project profile):

| Timeframe | `confirm_timeout_sec` (bar late) | `clock_skew_max_ms` | Tip lag allow after close |
|-----------|----------------------------------|---------------------|---------------------------|
| 1m–5m     | see standard §22.1               | 3000                | `confirm_timeout_sec`     |
| 15m       | 90                               | 5000                | 90s                       |
| 1h+       | §22.1                            | 5000                | §22.1                     |

Rules:

- Compare against **exchange server time**, not only the machine clock.
- Decision timeframe **and** any touch / lower timeframe used for fills must both pass.
- Higher-timeframe features use only completed, lagged HTF bars; if HTF tip is stale, fail closed the same way.
- Never invent OHLC, never `fillna` the tip, never trade on a forming candle.
- Heartbeats between closes must re-check tip freshness; a tip that goes stale mid-hold blocks **new** risk and logs; it does not remove protective exits.

### B.4 Poker / non-market continuous agents

Same supervision class as trading bots: always-on supervisor, health heartbeat, auto-restart, singleton, alert on crash loop. Domain-specific “data tip” checks replace candles (table state, connection, session). Fail closed: do not act on stale or disconnected state.

---

## Agent checklist

**Long batch:** watchdog → verify pid → report exit / artifact path.  
**Continuous:** list units → if down or unhealthy, restore (when authorized) → verify tip freshness gate exists in bot code → never leave collector/bots silently dead.

## Evidence / conformance

Treat tip freshness as a live safety gate. Suggested identifier: `LIVE-DATA-001` (last closed candle matches exchange-server expected tip; collector error fails closed). Bind a discoverable test or ops probe; a missing binding is a live-readiness blocker.
