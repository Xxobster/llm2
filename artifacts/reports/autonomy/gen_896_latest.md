# Autonomy public-indicator hunt gen 896

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T010104Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1840_below_at_h` | one_head_filter_pi_star | 328 | 26.6834 | 1.6368 | 0.6494 | 3.8136 | 0.0169 | 0.3171 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma1840_below_at_h` | one_head_filter_pi_star | 300 | 24.5073 | 1.5827 | 0.6433 | 3.4209 | 0.0147 | 0.3200 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1840_below_at_h` | one_head_filter_pi_star | 302 | 24.5683 | 1.8183 | 0.6424 | 4.2744 | 0.0119 | 0.3146 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1840_below_at_h` | one_head_filter_pi_star | 310 | 25.2191 | 1.7839 | 0.6387 | 4.1481 | 0.0116 | 0.3161 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1840_above_at_h` | one_head_filter_pi_star | 75 | 6.2345 | 1.5925 | 0.6400 | 1.6448 | 0.0092 | 0.2800 | ok | RAN |
| SOLUSDT | 4 | `sma1840_above_at_h` | one_head_filter_pi_star | 22 | 1.9773 | 1.5052 | 0.5909 | 0.9450 | 0.0082 | 0.1818 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma1840_above_at_h` | one_head_filter_pi_star | 52 | 4.5729 | 1.0990 | 0.5385 | 0.3032 | 0.0042 | 0.2308 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1840_above_at_h` | one_head_filter_pi_star | 35 | 3.2192 | 0.8881 | 0.5143 | -0.3094 | -0.0057 | 0.2571 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1840_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3190 | 0.2000 | -1.5401 | -0.0793 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1840_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
