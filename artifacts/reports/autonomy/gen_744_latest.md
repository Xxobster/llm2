# Autonomy public-indicator hunt gen 744

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T102201Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1460_below_at_h` | one_head_filter_pi_star | 252 | 20.5861 | 1.8069 | 0.6587 | 3.9883 | 0.0186 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1460_below_at_h` | one_head_filter_pi_star | 267 | 21.8115 | 1.7385 | 0.6554 | 3.9472 | 0.0181 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1460_above_at_h` | one_head_filter_pi_star | 69 | 5.7348 | 1.8301 | 0.6957 | 2.2904 | 0.0126 | 0.3043 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1460_below_at_h` | one_head_filter_pi_star | 308 | 25.1854 | 1.8051 | 0.6396 | 4.2381 | 0.0120 | 0.3214 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1460_below_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 1.7480 | 0.6340 | 4.0271 | 0.0112 | 0.3268 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1460_above_at_h` | one_head_filter_pi_star | 70 | 5.8189 | 1.5258 | 0.6714 | 1.4957 | 0.0086 | 0.3429 | ok | RAN |
| ETHUSDT | 8 | `sma1460_above_at_h` | one_head_filter_pi_star | 77 | 6.5521 | 1.0731 | 0.5455 | 0.2755 | 0.0030 | 0.2078 | ok | RAN |
| ETHUSDT | 4 | `sma1460_above_at_h` | one_head_filter_pi_star | 88 | 7.4882 | 1.0475 | 0.5568 | 0.1898 | 0.0020 | 0.2159 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1460_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4672 | 0.2941 | -1.1661 | -0.0564 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1460_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3442 | 0.2941 | -1.4812 | -0.0702 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
