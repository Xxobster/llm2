# Autonomy public-indicator hunt gen 1590

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T165852Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma426_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.2077 | 0.6022 | 1.1783 | 0.0062 | 0.1823 | GATE_CAND | RAN |
| ETHUSDT | 4 | `wma426_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1489 | 0.5979 | 0.8897 | 0.0046 | 0.1799 | ok | RAN |
| SOLUSDT | 8 | `wma426_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.0946 | 0.5706 | 0.5287 | 0.0019 | 0.1638 | ok | RAN |
| SOLUSDT | 4 | `wma426_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.0899 | 0.5749 | 0.4791 | 0.0018 | 0.1617 | ok | RAN |
| SOLUSDT | 8 | `wma426_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.0387 | 0.5531 | 0.2204 | 0.0007 | 0.1006 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma426_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 0.9652 | 0.5337 | -0.2116 | -0.0007 | 0.1088 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma426_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8503 | 0.5455 | -0.9399 | -0.0060 | 0.0963 | ok | RAN |
| ETHUSDT | 4 | `wma426_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8224 | 0.5266 | -1.1148 | -0.0073 | 0.1011 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma426_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma426_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma426_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma426_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma426_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma426_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma426_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma426_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma426_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma426_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma426_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma426_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma426_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma426_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma426_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma426_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
