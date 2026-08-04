# Best research double vs live bots (2026-08-04 snapshot)

**Maximum readiness remains `RESEARCH_ONLY`.** Numbers below are different evidence classes; do not treat live micro as a full-period backtest, or k9 double as live authorization.

## A) Best double (research)

| Field | Value |
|-------|--------|
| Arm | **`k9_double3h`** (best PF of size-double grid) |
| Rule | K=9 concurrent / side (max 18 total); qty = **2×** min-exchange if signal ≤3h after last same-side entry, else 1× |
| Signal filter | `mean_strength` · hold 12 · Take Profit 1% · Stop Loss 2% |
| Window | Fold V2 stitched outer OOS (pre–lockbox 2026-05-01) |
| Trades | **13 069** |
| Profit Factor | **4.427** |
| Net PnL | **+3 132.83 USDT** (min-exchange / 2× size stack) |
| Bootstrap positive expectancy | 100% |
| Folds PF>1 / PnL>0 | 6/6 |
| Liquidations | 0 |

Per fold:

| Fold | Trades | PF | PnL | Win rate |
|------|--------|-----|-----|----------|
| 0 | 2335 | 3.75 | 505 | 86.7% |
| 1 | 2210 | 3.05 | 256 | 77.4% |
| 2 | 2213 | 4.18 | 430 | 80.8% |
| 3 | 2316 | 4.96 | 734 | 87.3% |
| 4 | 2314 | 5.19 | 713 | 88.3% |
| 5 | 1681 | 5.29 | 495 | 87.8% |

Report: `structure_v1_eth_cluster_size_double_k3_9_001_latest.json`

**Not live:** this arm is **not** deployed. Live ETH single-book is still none|hold6|tp1%|K=1; multitrade is K=7 fib book3+.

---

## B) Live bots now (snapshot ~2026-08-04 11:00 UTC)

### Accounts (Bybit via VPS)

| Account | Role | Equity (USDT) | Wallet | Unrealized PnL |
|---------|------|---------------|--------|----------------|
| **Xxobster7** | BTC + ETH + SOL single-book micro | **19.29** | 19.24 | **+0.054** |
| **Xxobster8** | ETH multitrade v1.1 | **62.96** | 62.90 | **+0.054** |

### Open positions (live)

**Xxobster7**

| Symbol | Side | Size | Avg entry | UPnL | Leverage |
|--------|------|------|-----------|------|----------|
| BTCUSDT | Sell | 0.001 | 63779 | +0.071 | 18× |
| ETHUSDT | Buy | 0.01 | 1867.93 | −0.019 | 18× |
| SOLUSDT | Sell | 0.1 | 73.58 | +0.002 | 18× |

**Xxobster8** (hedge ETH)

| Side | Size | Avg entry | UPnL |
|------|------|-----------|------|
| Sell | 0.03 | 1860.23 | −0.169 |
| Buy | 0.03 | 1858.42 | +0.223 |

### Closed PnL (Bybit closed-PnL API, last ≤100 rows — sample is tiny)

**Xxobster7** (structure fleet activity): **3** closed records  

| Symbol | n | Net PnL | PF | WR |
|--------|---|---------|-----|-----|
| ALL | 3 | **−0.703** | 0.31 | 67% |
| BTC | 1 | −1.012 | — | 0% |
| ETH | 2 | +0.309 | ∞ | 100% |

**Xxobster8:** **2** closed records (may include pre/other activity on account)

| Symbol | n | Net PnL |
|--------|---|---------|
| ALL | 2 | **+1.025** |
| BTC | 1 | +0.888 |
| ETH | 1 | +0.138 |

### Live runner state (local ledger — no closed-trade journal)

| Bot | Service state | Decisions logged | Entries vs skips | Last bar processed |
|-----|---------------|------------------|------------------|--------------------|
| BTC single | active | 21 (~Aug 3 16:00 → Aug 4 11:00 UTC) | 1 open-path / **19** already-open | 2026-08-04T11:00Z |
| ETH single | active | 19 | **19** already-open (Buy stuck) | same |
| SOL single | active | 19 | 1 open-path / **18** already-open | same |
| ETH multi v1.1 | active | 6 | 6 order-ok attempts | same |

Live geometry vs research double:

| | Live single (7) | Live multi (8) | Best double research |
|--|-----------------|----------------|----------------------|
| K | **1** | **7** | **9** |
| Hold | **6** | 6 / addon 12 | **12** |
| Clarity | none (flat gate) | mean_strength | mean_strength |
| Size 2× ≤3h | **no** | **no** | **yes** |
| TP | 1% | 1% / book3+ fib 2.618% | 1% flat |

### Official settle proxy for **current** live ETH direction (single-book, not double)

| Metric | Value |
|--------|--------|
| ETH 1h direction settle PF | ≈ **1.77** (6473 trades, fold V2) |
| Evidence class | nested hunt settle, not double/K9 |

---

## C) How to read the comparison

1. **Best double PF 4.43 on 13k trades** is multi-year fold-stitched research with concurrency + size double — max readiness still research-only.  
2. **Live** is ~1 day micro: equity ~19 USDT (fleet 7) / ~63 USDT (multi 8), **almost no closed sample**, positions still open → **no reliable live PF**.  
3. Closed PnL PF on 3 trades (fleet 7) is **not** comparable to 13k-trade stitch.  
4. Live bots do **not** run k9_double3h.

Sources: VPS `account_summary` + Bybit `get_closed_pnl` + `micro_live_state.sqlite` decisions; research `structure_v1_eth_cluster_size_double_k3_9_001_latest.json`.
