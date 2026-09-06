# Autonomy public-indicator hunt gen 729

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T091639Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema1380_below_at_h` | one_head_filter_pi_star | 290 | 23.6903 | 1.7445 | 0.6552 | 4.0162 | 0.0181 | 0.3207 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1380_below_at_h` | one_head_filter_pi_star | 294 | 24.0171 | 1.7078 | 0.6531 | 3.9449 | 0.0176 | 0.3265 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema1380_above_at_h` | one_head_filter_pi_star | 73 | 6.2118 | 1.3367 | 0.6164 | 1.0791 | 0.0137 | 0.2603 | ok | RAN |
| ETHUSDT | 4 | `ema1380_above_at_h` | one_head_filter_pi_star | 80 | 6.8074 | 1.3262 | 0.6000 | 1.0450 | 0.0126 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `ema1380_below_at_h` | one_head_filter_pi_star | 277 | 22.6505 | 1.7006 | 0.6354 | 3.7402 | 0.0114 | 0.3213 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1380_below_at_h` | one_head_filter_pi_star | 289 | 23.5107 | 1.7082 | 0.6298 | 3.7980 | 0.0112 | 0.3218 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1380_above_at_h` | one_head_filter_pi_star | 106 | 8.6433 | 1.5836 | 0.6415 | 1.9644 | 0.0087 | 0.2642 | ok | RAN |
| SOLUSDT | 4 | `ema1380_above_at_h` | one_head_filter_pi_star | 109 | 8.8879 | 1.5347 | 0.6422 | 1.8274 | 0.0080 | 0.2936 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1380_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0587 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1380_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0599 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
