# Autonomy public-indicator hunt gen 2171

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T080956Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma763_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1724 | 0.5876 | 0.9744 | 0.0049 | 0.1921 | ok | RAN |
| ETHUSDT | 8 | `sma763_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.0896 | 0.5683 | 0.5496 | 0.0028 | 0.1803 | ok | RAN |
| SOLUSDT | 8 | `sma763_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.0556 | 0.5373 | 0.2703 | 0.0011 | 0.1269 | ok | RAN |
| SOLUSDT | 4 | `sma763_above_at_h` | one_head_filter_pi_star | 132 | 10.8247 | 1.0453 | 0.5455 | 0.2156 | 0.0008 | 0.1136 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma763_below_at_h` | one_head_filter_pi_star | 212 | 17.2466 | 0.9835 | 0.5613 | -0.1024 | -0.0003 | 0.1368 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma763_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9057 | 0.5468 | -0.5978 | -0.0020 | 0.1281 | ok | RAN |
| ETHUSDT | 4 | `sma763_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 0.8984 | 0.5689 | -0.5476 | -0.0042 | 0.0958 | ok | RAN |
| ETHUSDT | 8 | `sma763_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 0.8557 | 0.5563 | -0.7761 | -0.0060 | 0.1192 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma763_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma763_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0583 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma763_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma763_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma763_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma763_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma763_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma763_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma763_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma763_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma763_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma763_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma763_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma763_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma763_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma763_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
