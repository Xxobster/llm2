# Autonomy public-indicator hunt gen 1653

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T232754Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret279_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.2034 | 0.6048 | 1.1231 | 0.0062 | 0.1796 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret279_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.1273 | 0.5926 | 0.7568 | 0.0039 | 0.2037 | ok | RAN |
| SOLUSDT | 8 | `ret279_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.0731 | 0.5765 | 0.4100 | 0.0015 | 0.1471 | ok | RAN |
| SOLUSDT | 4 | `ret279_neg_at_h` | one_head_filter_pi_star | 142 | 11.6115 | 1.0415 | 0.5845 | 0.2066 | 0.0009 | 0.1479 | ok | RAN |
| SOLUSDT | 8 | `ret279_pos_at_h` | one_head_filter_pi_star | 182 | 14.9249 | 1.0159 | 0.5330 | 0.0879 | 0.0003 | 0.1154 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret279_pos_at_h` | one_head_filter_pi_star | 181 | 14.8429 | 0.9617 | 0.5249 | -0.2138 | -0.0007 | 0.1050 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret279_pos_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 0.7901 | 0.5395 | -1.2342 | -0.0088 | 0.0921 | ok | RAN |
| ETHUSDT | 4 | `ret279_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 0.7551 | 0.5230 | -1.5358 | -0.0103 | 0.0920 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret279_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4385 | 0.3158 | -1.3087 | -0.0646 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret279_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret279_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret279_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret279_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret279_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret279_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret279_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret279_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret279_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret279_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret279_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret279_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret279_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret279_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret279_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
