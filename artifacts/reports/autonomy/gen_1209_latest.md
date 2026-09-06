# Autonomy public-indicator hunt gen 1209

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T111427Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema2580_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 1.6121 | 0.6435 | 3.6745 | 0.0163 | 0.3072 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2580_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 1.5956 | 0.6453 | 3.6466 | 0.0161 | 0.3110 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2580_below_at_h` | one_head_filter_pi_star | 274 | 22.2904 | 1.8448 | 0.6460 | 4.2024 | 0.0130 | 0.3212 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2580_below_at_h` | one_head_filter_pi_star | 287 | 23.3480 | 1.8128 | 0.6446 | 4.1308 | 0.0123 | 0.3240 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2580_above_at_h` | one_head_filter_pi_star | 103 | 8.4658 | 1.8465 | 0.6602 | 2.7268 | 0.0115 | 0.2718 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2580_above_at_h` | one_head_filter_pi_star | 99 | 8.2282 | 1.7279 | 0.6566 | 2.2700 | 0.0104 | 0.2727 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2580_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.7376 | 0.3684 | -0.5246 | -0.0265 | 0.1053 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2580_above_at_h` | one_head_filter_pi_star | 16 | 4.8283 | 0.4368 | 0.2500 | -2.6971 | -0.0366 | 0.2500 | ok | RAN |
| BTCUSDT | 8 | `ema2580_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0444 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2580_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
