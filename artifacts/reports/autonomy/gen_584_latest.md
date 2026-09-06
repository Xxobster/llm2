# Autonomy public-indicator hunt gen 584

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T232902Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1060_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 2.0725 | 0.6832 | 4.2421 | 0.0224 | 0.3614 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1060_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8791 | 0.6749 | 3.9331 | 0.0201 | 0.3498 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1060_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.8494 | 0.6475 | 3.8211 | 0.0128 | 0.3238 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1060_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.7288 | 0.6393 | 3.5919 | 0.0114 | 0.3156 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1060_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.7576 | 0.6512 | 2.5771 | 0.0109 | 0.3178 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1060_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.8158 | 0.6396 | 2.5362 | 0.0108 | 0.2973 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma1060_above_at_h` | one_head_filter_pi_star | 133 | 10.9324 | 1.1463 | 0.5714 | 0.6627 | 0.0058 | 0.2256 | ok | RAN |
| ETHUSDT | 8 | `sma1060_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.1127 | 0.5686 | 0.5216 | 0.0044 | 0.1830 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1060_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0560 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1060_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0589 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1060_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1060_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
