# Autonomy public-indicator hunt gen 2190

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T111216Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma519_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1066 | 0.5860 | 0.6368 | 0.0033 | 0.1882 | ok | RAN |
| ETHUSDT | 4 | `wma519_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.0934 | 0.5778 | 0.5607 | 0.0030 | 0.1944 | ok | RAN |
| SOLUSDT | 4 | `wma519_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.0749 | 0.5769 | 0.4270 | 0.0015 | 0.1538 | ok | RAN |
| SOLUSDT | 8 | `wma519_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0508 | 0.5410 | 0.2854 | 0.0009 | 0.1038 | ok | RAN |
| SOLUSDT | 8 | `wma519_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.0438 | 0.5659 | 0.2562 | 0.0009 | 0.1593 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma519_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 0.9919 | 0.5389 | -0.0482 | -0.0002 | 0.0984 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma519_above_at_h` | one_head_filter_pi_star | 172 | 14.1937 | 0.8033 | 0.5291 | -1.2141 | -0.0082 | 0.0930 | ok | RAN |
| ETHUSDT | 4 | `wma519_above_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 0.7720 | 0.5249 | -1.4714 | -0.0098 | 0.0939 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma519_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma519_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma519_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma519_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma519_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma519_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma519_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma519_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma519_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma519_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma519_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma519_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma519_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma519_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma519_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma519_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
