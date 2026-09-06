# Autonomy public-indicator hunt gen 1573

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T150510Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret268_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.2083 | 0.5988 | 1.1279 | 0.0063 | 0.1914 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret268_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1742 | 0.6023 | 1.0044 | 0.0054 | 0.1871 | ok | RAN |
| SOLUSDT | 8 | `ret268_pos_at_h` | one_head_filter_pi_star | 170 | 13.8619 | 1.1877 | 0.5706 | 0.9395 | 0.0032 | 0.1118 | ok | RAN |
| SOLUSDT | 8 | `ret268_neg_at_h` | one_head_filter_pi_star | 151 | 12.4291 | 1.1224 | 0.5828 | 0.6212 | 0.0025 | 0.1589 | ok | RAN |
| SOLUSDT | 4 | `ret268_pos_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.0531 | 0.5455 | 0.3069 | 0.0010 | 0.1111 | ok | RAN |
| SOLUSDT | 4 | `ret268_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 1.0381 | 0.5783 | 0.2056 | 0.0008 | 0.1386 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret268_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.7984 | 0.5257 | -1.2260 | -0.0085 | 0.1029 | ok | RAN |
| ETHUSDT | 8 | `ret268_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.7669 | 0.5215 | -1.4844 | -0.0094 | 0.0914 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret268_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0640 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret268_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0714 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret268_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret268_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret268_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret268_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret268_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret268_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret268_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret268_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret268_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret268_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret268_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret268_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret268_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret268_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
