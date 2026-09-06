# Autonomy public-indicator hunt gen 1000

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T100526Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `sma2100_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1160 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma2100_above_at_h` | one_head_filter_pi_star | 52 | 4.7154 | 1.4928 | 0.6346 | 1.2289 | 0.0181 | 0.2500 | ok | RAN |
| ETHUSDT | 4 | `sma2100_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.5799 | 0.6429 | 3.5439 | 0.0157 | 0.3065 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma2100_below_at_h` | one_head_filter_pi_star | 321 | 26.1140 | 1.5581 | 0.6417 | 3.2968 | 0.0150 | 0.3146 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2100_above_at_h` | one_head_filter_pi_star | 71 | 5.9020 | 2.0188 | 0.6901 | 2.4710 | 0.0136 | 0.2958 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2100_above_at_h` | one_head_filter_pi_star | 44 | 3.6576 | 1.8799 | 0.6818 | 1.8283 | 0.0120 | 0.2955 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2100_above_at_h` | one_head_filter_pi_star | 62 | 5.2168 | 1.3036 | 0.5968 | 0.9118 | 0.0117 | 0.2258 | ok | RAN |
| SOLUSDT | 8 | `sma2100_below_at_h` | one_head_filter_pi_star | 302 | 24.5683 | 1.7533 | 0.6358 | 3.9858 | 0.0114 | 0.3245 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2100_below_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 1.7614 | 0.6369 | 4.1851 | 0.0114 | 0.3200 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma2100_above_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3356 | 0.2308 | -1.4359 | -0.0914 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2100_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
