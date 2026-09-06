# Autonomy public-indicator hunt gen 1205

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T104601Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret215_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.2103 | 0.7101 | 4.7144 | 0.0271 | 0.3964 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret215_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.1058 | 0.7052 | 4.4003 | 0.0249 | 0.3988 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret215_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.0629 | 0.6757 | 4.0975 | 0.0160 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret215_neg_at_h` | one_head_filter_pi_star | 188 | 15.4035 | 1.9318 | 0.6649 | 3.8391 | 0.0140 | 0.3723 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret215_pos_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.5338 | 0.6190 | 2.3667 | 0.0080 | 0.2917 | ok | RAN |
| ETHUSDT | 4 | `ret215_pos_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.2049 | 0.5859 | 1.0564 | 0.0072 | 0.2323 | ok | RAN |
| SOLUSDT | 4 | `ret215_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.4397 | 0.6183 | 2.1159 | 0.0071 | 0.2634 | ok | RAN |
| ETHUSDT | 8 | `ret215_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1910 | 0.5851 | 1.0037 | 0.0066 | 0.2234 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret215_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5735 | 0.2632 | -0.9106 | -0.0446 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret215_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0456 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret215_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret215_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret215_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret215_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret215_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret215_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret215_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret215_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret215_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret215_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret215_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret215_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret215_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret215_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
