# Autonomy public-indicator hunt gen 040

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T120849Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `dpo_cross_up_0` | one_head_filter_pi_star | 17 | 1.3989 | 1.7790 | 0.6471 | 1.0291 | 0.0270 | 0.1176 | TPM<MIN | RAN |
| SOLUSDT | 8 | `dpo_cross_down_0` | one_head_filter_pi_star | 21 | 1.7781 | 3.7325 | 0.8095 | 2.2325 | 0.0222 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 8 | `dpo_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 4 | `dpo_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 8 | `dpo_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1832 | 0.6890 | 4.0479 | 0.0180 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 4 | `dpo_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1841 | 0.6909 | 4.0513 | 0.0179 | 0.4182 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `dpo_cross_down_0` | one_head_filter_pi_star | 21 | 2.1132 | 1.2353 | 0.5238 | 0.4193 | 0.0071 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 4 | `dpo_pos_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| ETHUSDT | 8 | `dpo_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2101 | 0.5901 | 0.9692 | 0.0068 | 0.1988 | ok | RAN |
| SOLUSDT | 8 | `dpo_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3928 | 0.5953 | 2.1177 | 0.0058 | 0.2512 | ok | RAN |
| SOLUSDT | 4 | `dpo_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3628 | 0.5953 | 1.9682 | 0.0053 | 0.2419 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `dpo_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `dpo_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `dpo_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `dpo_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `dpo_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `dpo_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `dpo_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `dpo_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `dpo_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `dpo_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `dpo_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `dpo_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `dpo_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
