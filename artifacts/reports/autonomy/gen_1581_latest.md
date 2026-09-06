# Autonomy public-indicator hunt gen 1581

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T155821Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret269_neg_at_h` | one_head_filter_pi_star | 154 | 12.5804 | 1.1573 | 0.6039 | 0.8861 | 0.0049 | 0.2013 | ok | RAN |
| ETHUSDT | 8 | `ret269_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.1420 | 0.5867 | 0.8850 | 0.0046 | 0.1837 | ok | RAN |
| SOLUSDT | 8 | `ret269_pos_at_h` | one_head_filter_pi_star | 168 | 13.7768 | 1.1926 | 0.5714 | 0.9490 | 0.0034 | 0.1071 | ok | RAN |
| SOLUSDT | 8 | `ret269_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 1.0420 | 0.5644 | 0.2253 | 0.0009 | 0.1534 | ok | RAN |
| SOLUSDT | 4 | `ret269_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0224 | 0.5780 | 0.1256 | 0.0005 | 0.1503 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret269_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 0.9940 | 0.5401 | -0.0344 | -0.0001 | 0.1176 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret269_pos_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 0.8223 | 0.5361 | -1.0483 | -0.0069 | 0.0904 | ok | RAN |
| ETHUSDT | 4 | `ret269_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.7849 | 0.5301 | -1.3367 | -0.0088 | 0.0929 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret269_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret269_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret269_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret269_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret269_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret269_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret269_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret269_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret269_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret269_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret269_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret269_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret269_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret269_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret269_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret269_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
