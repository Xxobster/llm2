# Autonomy public-indicator hunt gen 424

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T074944Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma660_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.1662 | 0.6959 | 4.6684 | 0.0261 | 0.3866 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma660_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.9762 | 0.6782 | 4.0315 | 0.0227 | 0.3851 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma660_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.7718 | 0.6599 | 3.3621 | 0.0120 | 0.3299 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma660_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.7366 | 0.6553 | 3.3520 | 0.0117 | 0.3252 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma660_above_at_h` | one_head_filter_pi_star | 144 | 11.8087 | 1.5503 | 0.6111 | 2.2381 | 0.0090 | 0.3194 | ok | RAN |
| SOLUSDT | 4 | `sma660_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.4557 | 0.5954 | 1.8252 | 0.0075 | 0.3282 | ok | RAN |
| ETHUSDT | 4 | `sma660_above_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 1.1521 | 0.5973 | 0.7265 | 0.0056 | 0.2081 | ok | RAN |
| ETHUSDT | 8 | `sma660_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.1394 | 0.5975 | 0.6985 | 0.0052 | 0.2327 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma660_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma660_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
