# Autonomy public-indicator hunt gen 630

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T022621Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma300_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9866 | 0.6979 | 4.4770 | 0.0234 | 0.3698 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma300_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9564 | 0.6989 | 4.3284 | 0.0225 | 0.3817 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma300_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.1926 | 0.6905 | 4.1762 | 0.0169 | 0.3810 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma300_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1043 | 0.6886 | 3.9195 | 0.0160 | 0.3713 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma300_above_at_h` | one_head_filter_pi_star | 200 | 16.4397 | 1.2476 | 0.5950 | 1.3121 | 0.0085 | 0.2300 | ok | RAN |
| ETHUSDT | 4 | `wma300_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2442 | 0.5969 | 1.2290 | 0.0083 | 0.2245 | ok | RAN |
| SOLUSDT | 8 | `wma300_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3830 | 0.6053 | 1.9352 | 0.0060 | 0.2632 | ok | RAN |
| SOLUSDT | 4 | `wma300_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3719 | 0.5991 | 1.9591 | 0.0058 | 0.2594 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma300_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma300_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
