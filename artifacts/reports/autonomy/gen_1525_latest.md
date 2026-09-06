# Autonomy public-indicator hunt gen 1525

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T050604Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret261_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 2.0903 | 0.7006 | 4.1781 | 0.0254 | 0.4204 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret261_neg_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9679 | 0.6850 | 4.3643 | 0.0238 | 0.3700 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret261_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.9330 | 0.6685 | 3.8127 | 0.0137 | 0.3591 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret261_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.7891 | 0.6505 | 3.3399 | 0.0127 | 0.3495 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret261_pos_at_h` | one_head_filter_pi_star | 166 | 13.6128 | 1.6363 | 0.6265 | 2.6539 | 0.0095 | 0.3072 | ok | RAN |
| SOLUSDT | 8 | `ret261_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.5561 | 0.6229 | 2.4501 | 0.0086 | 0.2800 | ok | RAN |
| ETHUSDT | 8 | `ret261_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.1440 | 0.5922 | 0.7641 | 0.0052 | 0.2179 | ok | RAN |
| ETHUSDT | 4 | `ret261_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.1114 | 0.5914 | 0.5924 | 0.0039 | 0.1989 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret261_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0385 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret261_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret261_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret261_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret261_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret261_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret261_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret261_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret261_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret261_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret261_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret261_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret261_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret261_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret261_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret261_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
