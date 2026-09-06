# Autonomy public-indicator hunt gen 1621

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T200605Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret275_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.1737 | 0.6059 | 0.9959 | 0.0052 | 0.1765 | ok | RAN |
| ETHUSDT | 8 | `ret275_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.1020 | 0.5893 | 0.6011 | 0.0033 | 0.1964 | ok | RAN |
| SOLUSDT | 8 | `ret275_pos_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.1095 | 0.5422 | 0.5642 | 0.0019 | 0.1084 | ok | RAN |
| SOLUSDT | 4 | `ret275_pos_at_h` | one_head_filter_pi_star | 171 | 14.0228 | 1.0700 | 0.5556 | 0.3666 | 0.0013 | 0.1053 | ok | RAN |
| SOLUSDT | 4 | `ret275_neg_at_h` | one_head_filter_pi_star | 182 | 14.8061 | 1.0060 | 0.5604 | 0.0345 | 0.0001 | 0.1429 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret275_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 0.9824 | 0.5587 | -0.1047 | -0.0004 | 0.1397 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret275_pos_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 0.8433 | 0.5417 | -0.9288 | -0.0060 | 0.0833 | ok | RAN |
| ETHUSDT | 4 | `ret275_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8044 | 0.5215 | -1.2422 | -0.0081 | 0.0860 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret275_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4385 | 0.3158 | -1.3087 | -0.0634 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret275_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0722 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret275_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret275_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret275_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret275_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret275_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret275_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret275_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret275_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret275_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret275_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret275_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret275_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret275_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret275_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
