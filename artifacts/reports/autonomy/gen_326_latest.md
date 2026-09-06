# Autonomy public-indicator hunt gen 326

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T111028Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma110_cross_up` | one_head_filter_pi_star | 12 | 1.0195 | 7.6900 | 0.8333 | 2.4649 | 0.0442 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma110_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9225 | 0.6954 | 4.2663 | 0.0227 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma110_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.7449 | 0.6765 | 3.6946 | 0.0198 | 0.3627 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma110_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2436 | 0.6928 | 4.1952 | 0.0184 | 0.4157 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma110_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2125 | 0.6933 | 4.1226 | 0.0182 | 0.4110 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma110_cross_down` | one_head_filter_pi_star | 27 | 2.5115 | 2.1538 | 0.6667 | 1.6203 | 0.0136 | 0.0741 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma110_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.3395 | 0.6124 | 1.5765 | 0.0103 | 0.2303 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma110_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2922 | 0.6077 | 1.3702 | 0.0092 | 0.2320 | ok | RAN |
| SOLUSDT | 8 | `wma110_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3580 | 0.5991 | 1.8750 | 0.0053 | 0.2547 | ok | RAN |
| SOLUSDT | 4 | `wma110_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.2949 | 0.5896 | 1.5921 | 0.0045 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma110_cross_down` | one_head_filter_pi_star | 29 | 2.4031 | 1.0236 | 0.4828 | 0.0568 | 0.0011 | 0.2759 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma110_cross_up` | one_head_filter_pi_star | 22 | 1.9091 | 0.8227 | 0.4091 | -0.4004 | -0.0086 | 0.3182 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma110_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma110_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma110_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma110_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
