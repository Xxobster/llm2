# Autonomy public-indicator hunt gen 1144

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T040820Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma2460_below_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.5954 | 0.6394 | 3.5599 | 0.0158 | 0.3091 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2460_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.5891 | 0.6412 | 3.5777 | 0.0157 | 0.3059 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma2460_below_at_h` | one_head_filter_pi_star | 283 | 23.1412 | 1.8276 | 0.6572 | 4.2533 | 0.0126 | 0.3251 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2460_below_at_h` | one_head_filter_pi_star | 313 | 25.4632 | 1.7137 | 0.6358 | 4.0033 | 0.0110 | 0.3195 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2460_above_at_h` | one_head_filter_pi_star | 47 | 4.6144 | 1.2626 | 0.5745 | 0.7237 | 0.0103 | 0.2553 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma2460_above_at_h` | one_head_filter_pi_star | 77 | 6.2797 | 1.6268 | 0.6494 | 1.7234 | 0.0088 | 0.2597 | ok | RAN |
| SOLUSDT | 4 | `sma2460_above_at_h` | one_head_filter_pi_star | 58 | 4.7679 | 1.6280 | 0.6379 | 1.5403 | 0.0084 | 0.1897 | ok | RAN |
| ETHUSDT | 4 | `sma2460_above_at_h` | one_head_filter_pi_star | 43 | 3.9550 | 1.0871 | 0.5581 | 0.2366 | 0.0032 | 0.2093 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2460_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2460_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
