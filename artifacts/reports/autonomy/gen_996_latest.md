# Autonomy public-indicator hunt gen 996

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T093343Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema1005_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.8059 | 0.6681 | 3.7544 | 0.0189 | 0.3406 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1005_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 1.7080 | 0.6581 | 3.5885 | 0.0177 | 0.3504 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema1005_below_at_h` | one_head_filter_pi_star | 245 | 20.0339 | 1.6970 | 0.6408 | 3.5034 | 0.0111 | 0.3020 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1005_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 1.6693 | 0.6395 | 3.5168 | 0.0108 | 0.3062 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema1005_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 1.2445 | 0.5970 | 1.1076 | 0.0096 | 0.2313 | ok | RAN |
| SOLUSDT | 4 | `ema1005_above_at_h` | one_head_filter_pi_star | 130 | 10.6003 | 1.5516 | 0.6308 | 2.1133 | 0.0086 | 0.3000 | ok | RAN |
| SOLUSDT | 8 | `ema1005_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.5106 | 0.6261 | 1.8736 | 0.0079 | 0.3043 | ok | RAN |
| ETHUSDT | 4 | `ema1005_above_at_h` | one_head_filter_pi_star | 127 | 10.4811 | 1.1397 | 0.5748 | 0.6192 | 0.0057 | 0.2205 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1005_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6020 | 0.2941 | -0.7739 | -0.0334 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1005_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1005_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1005_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1005_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1005_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1005_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1005_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1005_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1005_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1005_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1005_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1005_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1005_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1005_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1005_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
