# Autonomy public-indicator hunt gen 2174

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T084404Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma517_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.0893 | 0.5892 | 0.5400 | 0.0028 | 0.1838 | ok | RAN |
| ETHUSDT | 4 | `wma517_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.0584 | 0.5787 | 0.3546 | 0.0019 | 0.2022 | ok | RAN |
| SOLUSDT | 8 | `wma517_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.0391 | 0.5698 | 0.2269 | 0.0008 | 0.1676 | ok | RAN |
| SOLUSDT | 8 | `wma517_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.0368 | 0.5526 | 0.2134 | 0.0007 | 0.1000 | ok | RAN |
| SOLUSDT | 4 | `wma517_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.0204 | 0.5421 | 0.1179 | 0.0004 | 0.1000 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma517_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 0.9815 | 0.5549 | -0.1124 | -0.0004 | 0.1593 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma517_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8526 | 0.5344 | -0.9185 | -0.0059 | 0.0899 | ok | RAN |
| ETHUSDT | 4 | `wma517_above_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 0.8088 | 0.5275 | -1.2119 | -0.0080 | 0.0934 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma517_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma517_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma517_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma517_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma517_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma517_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma517_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma517_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma517_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma517_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma517_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma517_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma517_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma517_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma517_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma517_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
