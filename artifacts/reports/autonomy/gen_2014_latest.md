# Autonomy public-indicator hunt gen 2014

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T105358Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma492_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1576 | 0.5934 | 0.9173 | 0.0048 | 0.1813 | ok | RAN |
| ETHUSDT | 4 | `wma492_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1141 | 0.5806 | 0.6943 | 0.0035 | 0.1989 | ok | RAN |
| SOLUSDT | 8 | `wma492_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.1238 | 0.5602 | 0.6853 | 0.0022 | 0.0995 | ok | RAN |
| SOLUSDT | 4 | `wma492_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.0893 | 0.5765 | 0.4871 | 0.0018 | 0.1588 | ok | RAN |
| SOLUSDT | 4 | `wma492_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.0573 | 0.5489 | 0.3234 | 0.0011 | 0.1033 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma492_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 0.9981 | 0.5489 | -0.0116 | -0.0000 | 0.1576 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma492_above_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 0.8279 | 0.5337 | -1.0640 | -0.0070 | 0.0899 | ok | RAN |
| ETHUSDT | 4 | `wma492_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8000 | 0.5304 | -1.2781 | -0.0083 | 0.0994 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma492_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma492_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma492_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma492_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma492_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma492_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma492_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma492_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma492_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma492_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma492_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma492_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma492_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma492_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma492_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma492_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
