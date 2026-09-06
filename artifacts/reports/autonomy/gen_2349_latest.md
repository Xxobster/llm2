# Autonomy public-indicator hunt gen 2349

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T065928Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret379_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.2415 | 0.6024 | 1.2670 | 0.0068 | 0.1807 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret379_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.0791 | 0.5783 | 0.4375 | 0.0024 | 0.1687 | ok | RAN |
| SOLUSDT | 4 | `ret379_pos_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.0792 | 0.5570 | 0.4005 | 0.0015 | 0.1076 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret379_neg_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 0.9984 | 0.5625 | -0.0101 | -0.0000 | 0.1490 | ok | RAN |
| SOLUSDT | 8 | `ret379_pos_at_h` | one_head_filter_pi_star | 147 | 12.0547 | 0.9905 | 0.5238 | -0.0489 | -0.0002 | 0.1088 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret379_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 0.8929 | 0.5297 | -0.6838 | -0.0023 | 0.1459 | ok | RAN |
| ETHUSDT | 4 | `ret379_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 0.8511 | 0.5440 | -0.8971 | -0.0063 | 0.0989 | ok | RAN |
| ETHUSDT | 8 | `ret379_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8102 | 0.5316 | -1.2033 | -0.0084 | 0.1053 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret379_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0613 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret379_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4039 | 0.2105 | -1.4311 | -0.0694 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret379_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret379_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret379_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret379_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret379_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret379_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret379_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret379_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret379_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret379_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret379_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret379_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret379_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret379_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
