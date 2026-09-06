# Autonomy public-indicator hunt gen 1774

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T115950Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma454_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1706 | 0.5955 | 0.9880 | 0.0053 | 0.2079 | ok | RAN |
| ETHUSDT | 8 | `wma454_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1548 | 0.5934 | 0.9016 | 0.0047 | 0.1923 | ok | RAN |
| SOLUSDT | 8 | `wma454_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.0850 | 0.5642 | 0.4773 | 0.0017 | 0.1620 | ok | RAN |
| SOLUSDT | 4 | `wma454_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.0837 | 0.5771 | 0.4639 | 0.0017 | 0.1543 | ok | RAN |
| SOLUSDT | 8 | `wma454_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.0085 | 0.5333 | 0.0490 | 0.0002 | 0.1056 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma454_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 0.9679 | 0.5312 | -0.1919 | -0.0006 | 0.1094 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma454_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8494 | 0.5474 | -0.9473 | -0.0061 | 0.0947 | ok | RAN |
| ETHUSDT | 4 | `wma454_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8309 | 0.5319 | -1.0656 | -0.0070 | 0.0957 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma454_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma454_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4116 | 0.2778 | -1.4041 | -0.0707 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma454_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma454_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
