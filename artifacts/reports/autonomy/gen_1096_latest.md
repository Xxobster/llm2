# Autonomy public-indicator hunt gen 1096

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T223457Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma2340_above_at_h` | one_head_filter_pi_star | 50 | 4.9089 | 1.5543 | 0.6200 | 1.4486 | 0.0203 | 0.2600 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2340_above_at_h` | one_head_filter_pi_star | 54 | 4.8848 | 1.4428 | 0.6111 | 1.1998 | 0.0160 | 0.2407 | ok | RAN |
| ETHUSDT | 4 | `sma2340_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.5764 | 0.6409 | 3.5452 | 0.0153 | 0.3027 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma2340_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.5427 | 0.6336 | 3.3883 | 0.0150 | 0.3093 | ok | RAN |
| SOLUSDT | 4 | `sma2340_above_at_h` | one_head_filter_pi_star | 71 | 5.9020 | 1.9612 | 0.6761 | 2.3552 | 0.0126 | 0.2817 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2340_below_at_h` | one_head_filter_pi_star | 307 | 24.9751 | 1.7901 | 0.6417 | 4.1706 | 0.0116 | 0.3257 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2340_below_at_h` | one_head_filter_pi_star | 313 | 25.4632 | 1.7650 | 0.6390 | 4.1137 | 0.0115 | 0.3259 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2340_above_at_h` | one_head_filter_pi_star | 72 | 5.9188 | 1.7958 | 0.6528 | 2.0456 | 0.0107 | 0.2778 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2340_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2340_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
