# Autonomy public-indicator hunt gen 1152

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T051229Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma2480_above_at_h` | one_head_filter_pi_star | 44 | 3.9802 | 1.4936 | 0.6136 | 1.1513 | 0.0181 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2480_below_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.5954 | 0.6389 | 3.5008 | 0.0157 | 0.3117 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2480_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 1.5788 | 0.6414 | 3.6153 | 0.0156 | 0.3061 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma2480_above_at_h` | one_head_filter_pi_star | 68 | 5.5457 | 2.0772 | 0.6471 | 2.4148 | 0.0135 | 0.2647 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2480_below_at_h` | one_head_filter_pi_star | 299 | 24.4495 | 1.8061 | 0.6522 | 4.1994 | 0.0125 | 0.3278 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2480_above_at_h` | one_head_filter_pi_star | 48 | 4.7126 | 1.3166 | 0.5833 | 0.8784 | 0.0118 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `sma2480_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.7464 | 0.6472 | 4.0770 | 0.0115 | 0.3269 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2480_above_at_h` | one_head_filter_pi_star | 76 | 6.2476 | 1.8824 | 0.6711 | 2.1628 | 0.0109 | 0.2368 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2480_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2480_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
