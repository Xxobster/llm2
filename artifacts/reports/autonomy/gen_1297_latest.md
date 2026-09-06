# Autonomy public-indicator hunt gen 1297

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T195754Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema2800_below_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.5980 | 0.6424 | 3.5063 | 0.0157 | 0.3061 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema2800_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 1.5548 | 0.6395 | 3.5028 | 0.0152 | 0.3052 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2800_below_at_h` | one_head_filter_pi_star | 274 | 22.2904 | 1.8635 | 0.6496 | 4.2673 | 0.0129 | 0.3321 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2800_below_at_h` | one_head_filter_pi_star | 272 | 22.1277 | 1.8725 | 0.6507 | 4.2815 | 0.0129 | 0.3309 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2800_above_at_h` | one_head_filter_pi_star | 120 | 9.8630 | 1.6865 | 0.6500 | 2.3876 | 0.0102 | 0.2583 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2800_above_at_h` | one_head_filter_pi_star | 111 | 9.1025 | 1.5203 | 0.6396 | 1.8038 | 0.0080 | 0.2703 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2800_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.7248 | 0.3684 | -0.5505 | -0.0273 | 0.1053 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2800_above_at_h` | one_head_filter_pi_star | 12 | 3.7398 | 0.4897 | 0.2500 | -2.0354 | -0.0379 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2800_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2800_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
