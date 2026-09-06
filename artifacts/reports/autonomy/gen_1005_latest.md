# Autonomy public-indicator hunt gen 1005

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T110251Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret394_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 2.4557 | 0.7325 | 4.7846 | 0.0304 | 0.4140 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret394_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.2022 | 0.7052 | 4.5430 | 0.0269 | 0.3988 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret394_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.8132 | 0.6704 | 3.3838 | 0.0123 | 0.3296 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret394_pos_at_h` | one_head_filter_pi_star | 113 | 9.2671 | 1.7684 | 0.6637 | 2.4712 | 0.0116 | 0.3009 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret394_neg_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.6938 | 0.6615 | 3.1458 | 0.0110 | 0.3231 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret394_pos_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.5183 | 0.6119 | 1.9684 | 0.0084 | 0.2836 | ok | RAN |
| ETHUSDT | 8 | `ret394_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.1249 | 0.5825 | 0.6926 | 0.0046 | 0.2320 | ok | RAN |
| ETHUSDT | 4 | `ret394_pos_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.0977 | 0.5882 | 0.5138 | 0.0036 | 0.2471 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret394_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5883 | 0.3500 | -0.8891 | -0.0407 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret394_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0565 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret394_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret394_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret394_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret394_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret394_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret394_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret394_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret394_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret394_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret394_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret394_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret394_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret394_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret394_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
