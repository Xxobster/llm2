# Autonomy public-indicator hunt gen 066

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T135236Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `pvc_cross_down_0` | one_head_filter_pi_star | 22 | 1.9398 | 1.8739 | 0.6818 | 1.4777 | 0.0222 | 0.2273 | TPM<MIN | RAN |
| ETHUSDT | 8 | `pvc_neg_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.8067 | 0.6696 | 3.9406 | 0.0210 | 0.3616 | EBR>35% | RAN |
| ETHUSDT | 4 | `pvc_neg_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8098 | 0.6652 | 3.7433 | 0.0204 | 0.3529 | EBR>35% | RAN |
| SOLUSDT | 4 | `pvc_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.0118 | 0.6763 | 3.7990 | 0.0164 | 0.3873 | EBR>35% | RAN |
| SOLUSDT | 8 | `pvc_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.9517 | 0.6707 | 3.5935 | 0.0157 | 0.4012 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `pvc_cross_up_0` | one_head_filter_pi_star | 13 | 1.5180 | 1.2878 | 0.6154 | 0.4818 | 0.0091 | 0.1538 | TPM<MIN | RAN |
| SOLUSDT | 8 | `pvc_pos_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.4729 | 0.6146 | 2.3862 | 0.0067 | 0.2683 | ok | RAN |
| SOLUSDT | 4 | `pvc_pos_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.4188 | 0.6058 | 2.1630 | 0.0061 | 0.2692 | ok | RAN |
| ETHUSDT | 4 | `pvc_pos_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.1832 | 0.6111 | 0.8615 | 0.0060 | 0.2222 | ok | RAN |
| ETHUSDT | 8 | `pvc_pos_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.1917 | 0.6065 | 0.8890 | 0.0060 | 0.2129 | ok | RAN |
| SOLUSDT | 8 | `pvc_cross_up_0` | one_head_filter_pi_star | 22 | 2.0365 | 1.1190 | 0.6818 | 0.2338 | 0.0028 | 0.1364 | TPM<MIN | RAN |
| SOLUSDT | 4 | `pvc_cross_up_0` | one_head_filter_pi_star | 17 | 1.5737 | 1.0574 | 0.6471 | 0.1026 | 0.0014 | 0.1765 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `pvc_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `pvc_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `pvc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `pvc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `pvc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `pvc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `pvc_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `pvc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `pvc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `pvc_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `pvc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `pvc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
