# Autonomy public-indicator hunt gen 2205

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T130939Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret358_neg_at_h` | one_head_filter_pi_star | 154 | 12.5804 | 1.2869 | 0.6169 | 1.4181 | 0.0083 | 0.2078 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret358_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.2333 | 0.6057 | 1.2888 | 0.0072 | 0.1943 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret358_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.3118 | 0.5852 | 1.5240 | 0.0055 | 0.1136 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret358_pos_at_h` | one_head_filter_pi_star | 155 | 12.6388 | 1.2109 | 0.5806 | 1.0334 | 0.0039 | 0.1226 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret358_neg_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 0.9509 | 0.5476 | -0.3185 | -0.0010 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret358_neg_at_h` | one_head_filter_pi_star | 198 | 16.2978 | 0.9196 | 0.5455 | -0.5182 | -0.0018 | 0.1465 | ok | RAN |
| ETHUSDT | 8 | `ret358_pos_at_h` | one_head_filter_pi_star | 199 | 16.3039 | 0.7665 | 0.5276 | -1.4639 | -0.0098 | 0.0955 | ok | RAN |
| ETHUSDT | 4 | `ret358_pos_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 0.7335 | 0.5227 | -1.6385 | -0.0118 | 0.0966 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret358_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4748 | 0.3158 | -1.1705 | -0.0569 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret358_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4039 | 0.2105 | -1.4311 | -0.0749 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret358_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret358_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret358_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret358_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret358_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret358_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret358_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret358_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret358_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret358_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret358_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret358_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret358_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret358_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
