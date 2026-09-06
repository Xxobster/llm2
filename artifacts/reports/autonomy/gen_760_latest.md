# Autonomy public-indicator hunt gen 760

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T113219Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1500_below_at_h` | one_head_filter_pi_star | 277 | 22.6284 | 1.7489 | 0.6570 | 4.0144 | 0.0183 | 0.3285 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1500_below_at_h` | one_head_filter_pi_star | 251 | 20.5044 | 1.7128 | 0.6494 | 3.6878 | 0.0173 | 0.3307 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1500_below_at_h` | one_head_filter_pi_star | 295 | 23.9988 | 1.8663 | 0.6475 | 4.3446 | 0.0125 | 0.3288 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1500_above_at_h` | one_head_filter_pi_star | 69 | 5.7358 | 1.7554 | 0.6812 | 1.9191 | 0.0108 | 0.3188 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1500_below_at_h` | one_head_filter_pi_star | 308 | 25.0564 | 1.6747 | 0.6266 | 3.7258 | 0.0104 | 0.3247 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1500_above_at_h` | one_head_filter_pi_star | 71 | 5.9010 | 1.5581 | 0.6620 | 1.5582 | 0.0088 | 0.3380 | ok | RAN |
| ETHUSDT | 8 | `sma1500_above_at_h` | one_head_filter_pi_star | 72 | 6.1637 | 1.2079 | 0.5972 | 0.7134 | 0.0084 | 0.2361 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1500_above_at_h` | one_head_filter_pi_star | 85 | 7.0149 | 0.9537 | 0.5412 | -0.1863 | -0.0020 | 0.1882 | ok | RAN |
| BTCUSDT | 4 | `sma1500_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0506 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1500_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0592 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
