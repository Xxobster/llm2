# Autonomy public-indicator hunt gen 438

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T112153Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma180_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0306 | 0.6974 | 4.6133 | 0.0242 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma180_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0357 | 0.6990 | 4.6672 | 0.0241 | 0.3724 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma180_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.3582 | 0.7035 | 4.5455 | 0.0187 | 0.3837 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma180_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2227 | 0.6964 | 4.2237 | 0.0179 | 0.3869 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma180_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2376 | 0.6054 | 1.1814 | 0.0080 | 0.2270 | ok | RAN |
| ETHUSDT | 4 | `wma180_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1844 | 0.5947 | 0.9699 | 0.0063 | 0.2211 | ok | RAN |
| SOLUSDT | 4 | `wma180_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.3231 | 0.5990 | 1.6685 | 0.0050 | 0.2690 | ok | RAN |
| SOLUSDT | 8 | `wma180_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3083 | 0.5902 | 1.6475 | 0.0049 | 0.2634 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma180_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma180_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
