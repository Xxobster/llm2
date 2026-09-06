# Autonomy public-indicator hunt gen 779

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T133731Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma490_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1373 | 0.7049 | 4.6647 | 0.0255 | 0.3880 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma490_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.1434 | 0.7000 | 4.6284 | 0.0249 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma490_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.9226 | 0.6667 | 3.8167 | 0.0135 | 0.3385 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma490_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.8275 | 0.6633 | 3.6219 | 0.0123 | 0.3214 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma490_above_at_h` | one_head_filter_pi_star | 150 | 12.3782 | 1.3335 | 0.6200 | 1.5225 | 0.0118 | 0.2200 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma490_above_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.5518 | 0.6139 | 2.3614 | 0.0087 | 0.2975 | ok | RAN |
| SOLUSDT | 4 | `sma490_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.5315 | 0.6096 | 2.4662 | 0.0084 | 0.2888 | ok | RAN |
| ETHUSDT | 4 | `sma490_above_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.1470 | 0.5819 | 0.7551 | 0.0056 | 0.2260 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma490_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma490_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma490_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma490_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
