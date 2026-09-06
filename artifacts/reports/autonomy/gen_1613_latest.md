# Autonomy public-indicator hunt gen 1613

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T192158Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret274_neg_at_h` | one_head_filter_pi_star | 154 | 12.5804 | 1.2091 | 0.6104 | 1.1510 | 0.0061 | 0.1883 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret274_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.0700 | 0.5771 | 0.4244 | 0.0023 | 0.1943 | ok | RAN |
| SOLUSDT | 8 | `ret274_pos_at_h` | one_head_filter_pi_star | 177 | 14.5149 | 1.0834 | 0.5480 | 0.4494 | 0.0015 | 0.1130 | ok | RAN |
| SOLUSDT | 4 | `ret274_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0505 | 0.5385 | 0.2711 | 0.0009 | 0.1154 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret274_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 0.9953 | 0.5593 | -0.0276 | -0.0001 | 0.1525 | ok | RAN |
| SOLUSDT | 8 | `ret274_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 0.9581 | 0.5591 | -0.2504 | -0.0009 | 0.1505 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret274_pos_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 0.9065 | 0.5460 | -0.5380 | -0.0034 | 0.0859 | ok | RAN |
| ETHUSDT | 4 | `ret274_pos_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 0.8498 | 0.5506 | -0.8461 | -0.0062 | 0.0886 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret274_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4385 | 0.3158 | -1.3087 | -0.0659 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret274_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4385 | 0.3158 | -1.3087 | -0.0672 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret274_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret274_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret274_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret274_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret274_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret274_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret274_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret274_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret274_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret274_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret274_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret274_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret274_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret274_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
