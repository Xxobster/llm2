# tradesim backtest engine — strategy guide

**Audience:** every strategy repository that will call the shared backtest engine.  
**Engine package:** `packages/tradesim` (install from the `botsgeneral` repo).  
**Frozen:** 2026-07-26  
**Companion:** this file is part of Trading Bot Cursor Rules v2; keep it next to the research standard.

**Full engine + metrics reference (formulas, win-rate FAQ):**  
`docs/project_memory/TRADESIM_ENGINE_AND_METRICS.md`

---

## 1. What the engine is (and is not)

The engine does **not** invent entries, take-profits or stop-losses.  
Your strategy produces a list of trades. The engine walks candle data and answers:

> Given these entry / take-profit (TP) / stop-loss (SL) points, what would have happened with live-like fills, fees and funding?

It then reports win rate, Sharpe ratio, Sortino ratio, max drawdown, number of trades, longs/shorts, fees, funding, and related metrics.

**Your job:** causal signals and points (no looking ahead).  
**Engine’s job:** honest execution of those points.

Walk-forward, train/test splits and feature building stay in the strategy / research harness. Pass the engine only the trade list for the fold you are evaluating.

---

## 2. Exact data the strategy must give

### 2.1 Per trade (required)

| Field | Type | Meaning |
|---|---|---|
| `symbol` | string | e.g. `BTCUSDT` |
| `decision_ts_ms` | int | Open time (UTC milliseconds) of the **closed** decision candle. The signal is known only **after** this candle closes. |
| `side` | `+1` or `-1` | Long or short |
| `stop_price` **or** `stop_offset` | float | Absolute SL, **or** fraction of the **actual entry fill** (engine applies the fraction after the fill) |
| `target_price` **or** `target_offset` | float | Absolute TP, **or** fraction of the actual entry fill |
| `qty` | float | Optional. Omit in research → smallest exchange-legal size. Set only to override. |

### 2.2 Per trade (optional)

| Field | Meaning |
|---|---|
| `max_hold_bars` | Force a **market** exit after N decision bars (this exit **does** use market-exit slippage) |
| `tp_legs` | Multi-leg TP; quantity fractions must sum to `1.0` |
| `break_even` | Move SL to break-even after a trigger (only if live does the same) |
| `trail` | Trailing stop (only if live does the same) |

### 2.3 Hard rules for the strategy

1. Features and the decision use **only** data available at `decision_ts_ms`. No future candles, no centered windows, no full-history normalization fitted on the test period.
2. Do **not** compute SL/TP from a fill price you invent. Either give absolute levels you will also use live, or give **offsets** and let the engine attach them to the **simulated** fill.
3. One decision per closed decision candle (same rule as live).

---

## 3. How the engine executes (frozen defaults)

| Step | Behaviour |
|---|---|
| Market data | Binance USDⓈ-M perpetual Open-High-Low-Close-Volume (OHLCV) for research. Label results `RESEARCH_PROXY`. Live trading is on Bybit USDT perpetual. **Last** for signals/fills/TP–SL path; **Mark** for liquidation (and for TP/SL only if live triggers on Mark). Both for go/no-go. |
| Entry | Fill at the **next candle’s open** after `decision_ts_ms`, with **entry slippage**, **taker** fee. |
| Take-profit | **Limit** order. When price **touches** the TP level → fill **exactly at the TP price**. **No exit slippage.** |
| Stop-loss | **Limit** order. When price **touches** the SL level → fill **exactly at the SL price**. **No exit slippage.** |
| Fees | **Taker** rate on every fill by default (Bybit non-VIP **0.055%** = `0.00055`) — this is the **stress / feasibility** baseline. **Live product default is maker-first:** Post-Only entry, resting limit take-profit, resting limit stop; charge maker **0.02%** = `0.0002` on legs that rest. Taker only when there is no choice (Post-Only cancelled, gap-through flatten, max-hold, liquidation). A crossing limit is taker, not maker. |
| Sizing | **Smallest exchange-legal quantity** (`SizingMode.MIN_EXCHANGE`) unless `Signal.qty` is set |
| Starting funds | **100 USDT**; if equity hits ≤ 0 → **WALLET BLOWN**, trading stops, timestamp recorded |
| Funding | Actual historical funding rates at each settlement while the position is open (not a flat average). |
| Same candle hits both TP and SL | Resolve on a **lower timeframe**. If both still hit on one lower bar → **SL wins**. |
| Entry bar | SL and TP are active from the **fill instant** on that same bar. **No free bar of immunity.** |
| **Limit / Post-Only entry (`EXEC-021`)** | Decision timeframe **places** the rest. Walk **1-minute** from the start of the fillable bar. **Fill = first 1-minute that touches the limit, at the limit price** (not the 4-hour/1-hour open). Take-profit and stop arm **only after that 1-minute fill**. If 1-minute prints take-profit 103 before buy limit 98: **not a fill, not a win**. After 98, 103 must print again. |

### 3.0 Limit-entry 1-minute movie (mandatory)

This is the same rule as `TRADING_BOT_RESEARCH_STANDARD_V2.md` §9.6.1. Repeat here because this file is the engine contract.

1. Any decision timeframe (15-minute, 1-hour, 4-hour, …) may emit the limit.
2. A decision-bar high/low that *eventually* includes the limit only means “a fill can exist in this bar.” It does **not** put you in at that bar’s **open**.
3. Walk 1-minute bars from minute 0 of that bar to **find the fill**, then continue the same 1-minute walk for take-profit/stop **after** the fill.
4. Worked example: buy limit 98, take-profit 103, stop 95, 4-hour open 100. Path 100 → 103 → 98. At 103 you are **not** in. Fill is 98. Then need take-profit/stop after 98.

An engine that books the 103 in that example is **illegal**. Do not quote its profit factor.

### Entry slippage only

- `entry_slippage`: project-frozen (typical starting range about 0.02%–0.15%).  
- `market_exit_slippage`: used only for **timeout / max-hold / end-of-data** market exits — **not** for TP or SL.

### Gaps and limit TP/SL

If a bar opens beyond the TP or SL level, the engine still assumes the resting limit **fills at the limit price** (your policy: small size, orders fill). That is optimistic versus a stop-market. Live maker-first must flatten at market on the next heartbeat if mark is through the stop and the limit did not fill.

---

## 4. Lower timeframe for TP vs SL order

When the decision candle’s high/low contains **both** TP and SL, the engine walks a finer series:

| Decision timeframe | Preferred touch timeframe |
|---|---|
| 4h / 1d | **1m** (required for `EXEC-021` limit chronology) |
| 1h | **1m** |
| 15m | **1m** |
| 5m | **1m** |
| 1m | none → SL first if both touched |

If touch data does not fully cover that decision bar → fall back to **SL first**.

### When to refresh candles (research machine)

Warehouse: `D:\projectsdata\candles\market_ohlcv.sqlite`

Refresh **before a walk-forward campaign** (or when the test calendar window moves):

1. Decision timeframe OHLCV for every symbol in the campaign  
2. Touch timeframe(s) from the table above  
3. Historical funding for those symbols  

You do **not** need to refresh after every single trial — only when the window or symbol/timeframe set changes.

Example:

```text
python -m botsgeneral research-candles --only binance --symbols BTCUSDT,ETHUSDT --timeframes 1m,5m,1h,4h
```

---

## 5. How to call the engine (research runner)

We do **not** use a third-party `backtest.py` library. The shared engine is **`tradesim`**.

Preferred API for every strategy:

```python
from tradesim import run_backtest, Signal, BarSeries

bundle = run_backtest(
    strategy_id="my-strategy",          # required — associates the run with the strategy
    strategy_version="2026-07-26",
    bars=decision_bars,                 # set bars.symbol or pass symbol=
    symbol="BTCUSDT",                   # loads Bybit min qty/step/notional from cache
    signals=signals,                    # leave Signal.qty unset → min exchange size
    touch_bars=touch_bars,              # optional lower TF
    funding_ts_ms=..., funding_rate=...,
    strategy_meta={                     # shown in report + metrics window
        "name": "my-strategy",
        "batch": "wf-2026-07",
        "model_name": "trial.joblib",
        "model_path": r"C:\projects\xgb\models\trial.joblib",
        "tp_pct": 1.0,
        "sl_pct": 2.0,
    },
    # store_path / reports_dir default to D:/projectsdata/backtests/...
    # plot defaults to True on interactive terminals (TRADESIM_NO_PLOT=1 to disable)
)
# bundle.metrics  → Sharpe, Sortino, WR, trades/month, …
# bundle.wallet_blown → True if the 100 USDT wallet hit zero
# bundle.report_dir → D:/projectsdata/backtests/reports/<run_id>/
print(bundle.headline)
```

Every run writes a **report folder** (no need to re-simulate later):

| File | Contents |
|---|---|
| `REPORT.md` | Strategy table + headline metrics + reopen command |
| `strategy.json` | Name, batch, model path, TP/SL, features, … |
| `metrics.json` / `metrics.txt` | Full metrics |
| `trades.csv` / `equity.csv` | Trade blotter + equity curve |
| `meta.json` | Fingerprints + `tradesim-research open` command |

Reopen chart + metrics (full period, from embedded bars):

```text
tradesim-research open --run-id <run_id>
```

Refresh Bybit instrument limits (uses **Xxobster_local** keys by default):

```text
python -m tradesim.venue --account Xxobster_local refresh --from-registry
python -m tradesim.venue list
```

Cache path: `D:/projectsdata/candles/bybit_instruments.sqlite`.

### Refresh research candles before every backtest / live comparison

**Mandatory** for backtest-versus-live-log work (also in `RULES.md`):

```text
python -m tradesim.research.candles --symbols BTCUSDT --timeframes 1h,1m --price-type both
```

```python
from tradesim.research import ensure_candles
ensure_candles(["BTCUSDT"], ["1h", "1m"], price_types=("last", "mark"))
```

### Finplot review (`plot=True` / interactive default)

TradingView-inspired dark chart over the **whole** bar period (`max_bars=0`):

1. **Top — equity** (wallet USDT): equity line, high-water mark, Peak / Final / Max DD.
2. **Bottom — price**: black background; green translucent zone = TP side, red = SL side
   (~10% opacity); white entry line; dashed SL/TP; markers snapped onto candle opens
   (not floating between bars); labels `TP +x%`, `SL -y%`, realized `%` at exit.
3. **Metrics window**: strategy details (name, batch, model path, TP/SL, …) + full headline
   + `as_backtesting_stats()`; click the price chart to reopen it.

```python
bundle = run_backtest(..., plot=True, strategy_meta={...})
# or reopen without re-simulating:
# tradesim-research open --run-id bundle.run_id
from tradesim.research.plot import plot_backtest
plot_backtest(bars, bundle.result, relative_equity=False, max_bars=0)
```

### Metrics (backtesting.py parity + extras)

`bundle.metrics` is the authoritative report. For names familiar from GitHub
`backtesting.py`, call `bundle.metrics.as_backtesting_stats()` — includes # trades,
longs/shorts, win rate, Sortino, durations (avg/min/max), SQN, Kelly, buy & hold,
volatility, avg/max drawdown, fees, funding, etc.

Frozen research defaults inside `run_backtest`:

| Setting | Value |
|---|---|
| Starting funds | **100 USDT** |
| Position size | **Smallest exchange-legal** (`min_qty` / `min_notional`) |
| Leverage | 1× |
| TP / SL | Limit, no exit slip |
| Entry | Next open + entry slip, taker fee |
| Wallet blown | Trading stops; flag + timestamp recorded and printed |

Inspect stored runs:

```text
tradesim-research list --db D:/projectsdata/backtests/tradesim_runs.sqlite
tradesim-research list --db ... --strategy my-strategy
tradesim-research show --db ... --run-id my-strategy-abc123
tradesim-research trades --db ... --run-id my-strategy-abc123
```

Every run stores: full metrics JSON, every trade, equity curve, conformance stamp, and
`wallet_blown` / `ruined_at_ts_ms`.

### Metrics captured (headline)

Period (days + date range), trades total, longs/shorts, trades/month, win rate (+ Wilson
interval), profit factor, expectancy, payoff, Sharpe (raw + annualised + HAC), Sortino,
max drawdown (MTM), Calmar, exposure, turnover, fees / slip / funding, entry-bar exit
rate, ambiguous bars, liquidations, skips, wallet blown.

Absolute USDT PnL is recorded but secondary — with min size it is small by design.

---

## 6. Mental model (one trade)

**Market next-open (stress / default when the live order is market):**

```text
1h candle closes at T → strategy emits:
   long, qty=0.01, stop=95, target=110

Engine:
  fill entry at open of next 1h bar ± entry slip, taker fee
  from that fill onward (including the rest of that bar):
      walk 1m to see whether 95 or 110 was touched first
      if both on same 1m bar → stop at 95 (limit, no slip)
      if only target → exit at 110 (limit, no slip)
  while open: apply each historical funding settlement
  on exit: fee on the exit fill (no TP/SL slip for resting limits)
```

**Resting limit / Post-Only (`EXEC-021`) — this is the live product default:**

```text
4h (or 1h / 15m) candle closes → strategy rests a buy limit at 98
   take-profit 103, stop 95

Engine:
  walk 1m from the open of the next 4h bar
  first 1m whose low <= 98 → FILL AT 98 (not at the 4h open)
  ignore any 1m that printed 103 or 95 BEFORE that fill (you were not in)
  AFTER the fill, walk remaining 1m for 103 then 95
  same 4h candle after a real fill is allowed
```

---

## 7. What you must not do

- Fill the entry at the signal candle’s close  
- Start SL/TP checks only on the bar **after** entry  
- **Treat a resting-limit fill as the decision-bar open, or fire take-profit/stop on 1-minute bars before the 1-minute path has touched the limit (`EXEC-021`)**  
- Assume TP always wins when both levels sit in one candle  
- Ignore funding on perpetuals when a history series exists  
- Quote full-history optimised results as if they were walk-forward out-of-sample  
- Change fee/slip/TP-SL assumptions after looking at out-of-sample results  

---

## 8. Checklist before a research run

- [ ] Signals use only closed-candle data at `decision_ts_ms`  
- [ ] Each trade has side, stop, target, fixed `qty`  
- [ ] Decision + touch candles refreshed for the backtest window  
- [ ] Funding series present (or funding explicitly marked unavailable)  
- [ ] Entry slip frozen; TP/SL have **zero** exit slip  
- [ ] Walk-forward folds defined **before** looking at test metrics  
- [ ] Result carries a green tradesim conformance stamp before you publish numbers  

---

## 9. Where the engine lives

| Item | Location |
|---|---|
| Library | `C:\projects\botsgeneral\packages\tradesim` |
| This contract (botsgeneral copy) | `docs/project_memory/STRATEGY_TO_TRADESIM_CONTRACT.md` |
| This guide (rules pack) | `TRADESIM_BACKTEST_ENGINE_GUIDE.md` (this file) |
| Full methodology | `TRADING_BOT_RESEARCH_STANDARD_V2.md` |
| Frozen gates | `FROZEN_DEFAULT_GATES_V2_1.md` |

Phase 3 migrations wire each strategy repo onto `tradesim` one repository at a time. Until then, treat this file as the interface contract every new backtest path must implement.
