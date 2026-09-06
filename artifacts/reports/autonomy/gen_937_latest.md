# Autonomy public-indicator hunt gen 937

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T053319Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1900_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1900_below_at_h` | one_head_filter_pi_star | 311 | 25.4059 | 1.6374 | 0.6431 | 3.6932 | 0.0163 | 0.3183 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1900_below_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 1.6040 | 0.6411 | 3.5689 | 0.0161 | 0.3160 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema1900_below_at_h` | one_head_filter_pi_star | 272 | 22.2417 | 1.9522 | 0.6581 | 4.5597 | 0.0147 | 0.3272 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1900_below_at_h` | one_head_filter_pi_star | 275 | 22.4870 | 1.7474 | 0.6400 | 3.9145 | 0.0120 | 0.3236 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1900_above_at_h` | one_head_filter_pi_star | 108 | 8.8064 | 1.5525 | 0.6296 | 1.9069 | 0.0078 | 0.2407 | ok | RAN |
| SOLUSDT | 4 | `ema1900_above_at_h` | one_head_filter_pi_star | 106 | 8.6438 | 1.3693 | 0.6226 | 1.3203 | 0.0054 | 0.2358 | ok | RAN |
| ETHUSDT | 4 | `ema1900_above_at_h` | one_head_filter_pi_star | 72 | 5.9420 | 1.0933 | 0.5694 | 0.3175 | 0.0041 | 0.2083 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1900_above_at_h` | one_head_filter_pi_star | 23 | 2.7027 | 0.8843 | 0.4348 | -0.3028 | -0.0068 | 0.3478 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1900_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0454 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1900_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0612 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
