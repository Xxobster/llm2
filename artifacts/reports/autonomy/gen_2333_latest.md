# Autonomy public-indicator hunt gen 2333

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T044211Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret377_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.1452 | 0.5747 | 0.8191 | 0.0042 | 0.1782 | ok | RAN |
| ETHUSDT | 8 | `ret377_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.1406 | 0.5765 | 0.7784 | 0.0041 | 0.1765 | ok | RAN |
| SOLUSDT | 8 | `ret377_pos_at_h` | one_head_filter_pi_star | 147 | 11.9864 | 1.1718 | 0.5646 | 0.8151 | 0.0033 | 0.1020 | ok | RAN |
| SOLUSDT | 4 | `ret377_pos_at_h` | one_head_filter_pi_star | 161 | 13.1280 | 1.0353 | 0.5466 | 0.1879 | 0.0007 | 0.1056 | ok | RAN |
| SOLUSDT | 4 | `ret377_neg_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.0138 | 0.5816 | 0.0836 | 0.0003 | 0.1480 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret377_neg_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 0.9362 | 0.5485 | -0.4230 | -0.0014 | 0.1408 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret377_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.8467 | 0.5449 | -0.9326 | -0.0065 | 0.1011 | ok | RAN |
| ETHUSDT | 8 | `ret377_pos_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 0.8083 | 0.5354 | -1.2223 | -0.0083 | 0.1061 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret377_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5901 | 0.2353 | -0.8024 | -0.0333 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret377_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0754 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret377_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret377_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret377_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret377_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret377_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret377_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret377_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret377_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret377_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret377_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret377_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret377_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret377_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret377_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
