# Autonomy public-indicator hunt gen 649

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T034034Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema1180_below_at_h` | one_head_filter_pi_star | 258 | 21.0762 | 1.7612 | 0.6550 | 3.8642 | 0.0182 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1180_below_at_h` | one_head_filter_pi_star | 257 | 20.9945 | 1.7049 | 0.6498 | 3.6763 | 0.0170 | 0.3307 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1180_below_at_h` | one_head_filter_pi_star | 268 | 21.9146 | 1.6631 | 0.6306 | 3.5347 | 0.0110 | 0.3060 | ok | RAN |
| SOLUSDT | 4 | `ema1180_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.6573 | 0.6350 | 3.4393 | 0.0108 | 0.3156 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1180_above_at_h` | one_head_filter_pi_star | 108 | 8.8064 | 1.5310 | 0.6389 | 1.8864 | 0.0080 | 0.2963 | ok | RAN |
| SOLUSDT | 8 | `ema1180_above_at_h` | one_head_filter_pi_star | 106 | 8.6433 | 1.5002 | 0.6321 | 1.7436 | 0.0072 | 0.2830 | ok | RAN |
| ETHUSDT | 8 | `ema1180_above_at_h` | one_head_filter_pi_star | 94 | 7.7577 | 1.1212 | 0.5638 | 0.4726 | 0.0049 | 0.2128 | ok | RAN |
| ETHUSDT | 4 | `ema1180_above_at_h` | one_head_filter_pi_star | 106 | 8.7480 | 1.0768 | 0.5660 | 0.3151 | 0.0032 | 0.2170 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1180_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1180_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
