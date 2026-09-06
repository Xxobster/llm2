# Autonomy public-indicator hunt gen 800

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T154027Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1600_below_at_h` | one_head_filter_pi_star | 265 | 21.6481 | 1.7589 | 0.6604 | 3.9849 | 0.0186 | 0.3283 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1600_below_at_h` | one_head_filter_pi_star | 281 | 22.9551 | 1.6825 | 0.6441 | 3.7629 | 0.0170 | 0.3167 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1600_above_at_h` | one_head_filter_pi_star | 70 | 5.8189 | 1.9497 | 0.6857 | 2.3652 | 0.0142 | 0.3286 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1600_below_at_h` | one_head_filter_pi_star | 293 | 23.8361 | 1.8193 | 0.6348 | 4.1861 | 0.0120 | 0.3174 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1600_below_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.7187 | 0.6329 | 3.9331 | 0.0108 | 0.3165 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1600_above_at_h` | one_head_filter_pi_star | 64 | 5.3201 | 1.6147 | 0.6875 | 1.8142 | 0.0103 | 0.3281 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma1600_above_at_h` | one_head_filter_pi_star | 100 | 8.2528 | 1.2391 | 0.5900 | 0.9191 | 0.0100 | 0.2100 | ok | RAN |
| ETHUSDT | 8 | `sma1600_above_at_h` | one_head_filter_pi_star | 80 | 6.6023 | 1.2293 | 0.5875 | 0.7943 | 0.0096 | 0.2625 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1600_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1600_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0599 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
