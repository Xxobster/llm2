# Autonomy public-indicator hunt gen 1080

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T202857Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `sma2300_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0869 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma2300_above_at_h` | one_head_filter_pi_star | 57 | 5.0126 | 1.5229 | 0.6140 | 1.3624 | 0.0185 | 0.2281 | ok | RAN |
| ETHUSDT | 8 | `sma2300_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.5860 | 0.6407 | 3.5631 | 0.0156 | 0.3144 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma2300_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.5561 | 0.6380 | 3.4232 | 0.0150 | 0.3056 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2300_below_at_h` | one_head_filter_pi_star | 283 | 23.0226 | 1.8371 | 0.6466 | 4.1662 | 0.0125 | 0.3216 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2300_above_at_h` | one_head_filter_pi_star | 69 | 5.7358 | 1.8732 | 0.6812 | 2.3025 | 0.0113 | 0.2464 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2300_above_at_h` | one_head_filter_pi_star | 42 | 3.7993 | 1.2560 | 0.5714 | 0.6389 | 0.0101 | 0.2143 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma2300_below_at_h` | one_head_filter_pi_star | 322 | 26.1953 | 1.6465 | 0.6273 | 3.6362 | 0.0099 | 0.3199 | ok | RAN |
| SOLUSDT | 8 | `sma2300_above_at_h` | one_head_filter_pi_star | 67 | 5.5695 | 1.7130 | 0.6567 | 1.8566 | 0.0097 | 0.2985 | GATE_CAND | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma2300_above_at_h` | one_head_filter_pi_star | 11 | 2.0201 | 0.3638 | 0.2727 | -1.8830 | -0.0747 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2300_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
