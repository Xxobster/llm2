# Autonomy public-indicator hunt gen 1878

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T212649Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma471_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1582 | 0.5892 | 0.9122 | 0.0048 | 0.1946 | ok | RAN |
| ETHUSDT | 4 | `wma471_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1107 | 0.5838 | 0.6719 | 0.0035 | 0.2054 | ok | RAN |
| SOLUSDT | 4 | `wma471_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 1.0373 | 0.5680 | 0.2086 | 0.0008 | 0.1538 | ok | RAN |
| SOLUSDT | 4 | `wma471_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.0381 | 0.5417 | 0.2220 | 0.0007 | 0.1042 | ok | RAN |
| SOLUSDT | 8 | `wma471_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.0308 | 0.5368 | 0.1799 | 0.0006 | 0.1000 | ok | RAN |
| SOLUSDT | 8 | `wma471_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.0101 | 0.5519 | 0.0604 | 0.0002 | 0.1639 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma471_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 0.8035 | 0.5260 | -1.2698 | -0.0081 | 0.0990 | ok | RAN |
| ETHUSDT | 8 | `wma471_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8041 | 0.5455 | -1.2459 | -0.0081 | 0.0909 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma471_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma471_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma471_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma471_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma471_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma471_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma471_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma471_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma471_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma471_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma471_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma471_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma471_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma471_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma471_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma471_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
