# Autonomy public-indicator hunt gen 2302

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T005509Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma537_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.0839 | 0.5820 | 0.5081 | 0.0027 | 0.1799 | ok | RAN |
| ETHUSDT | 4 | `wma537_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.0695 | 0.5761 | 0.4246 | 0.0022 | 0.1957 | ok | RAN |
| SOLUSDT | 8 | `wma537_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0648 | 0.5455 | 0.3687 | 0.0012 | 0.0963 | ok | RAN |
| SOLUSDT | 8 | `wma537_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.0133 | 0.5628 | 0.0790 | 0.0003 | 0.1585 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma537_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 0.9900 | 0.5365 | -0.0601 | -0.0002 | 0.0990 | ok | RAN |
| SOLUSDT | 4 | `wma537_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 0.9673 | 0.5515 | -0.1982 | -0.0007 | 0.1598 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma537_above_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 0.8255 | 0.5326 | -1.1206 | -0.0070 | 0.0924 | ok | RAN |
| ETHUSDT | 4 | `wma537_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 0.8230 | 0.5285 | -1.1383 | -0.0073 | 0.0984 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma537_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma537_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma537_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma537_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma537_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma537_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma537_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma537_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma537_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma537_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma537_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma537_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma537_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma537_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma537_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma537_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
