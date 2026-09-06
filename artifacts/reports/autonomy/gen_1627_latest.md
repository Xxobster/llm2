# Autonomy public-indicator hunt gen 1627

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T203926Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma691_below_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.2033 | 0.5882 | 1.1240 | 0.0059 | 0.2000 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma691_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.1201 | 0.5689 | 0.6731 | 0.0036 | 0.1796 | ok | RAN |
| SOLUSDT | 8 | `sma691_above_at_h` | one_head_filter_pi_star | 118 | 9.6766 | 1.0637 | 0.5508 | 0.2945 | 0.0012 | 0.1271 | ok | RAN |
| SOLUSDT | 4 | `sma691_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.0226 | 0.5328 | 0.1132 | 0.0004 | 0.1168 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma691_below_at_h` | one_head_filter_pi_star | 202 | 16.4331 | 0.9395 | 0.5495 | -0.3746 | -0.0013 | 0.1386 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma691_below_at_h` | one_head_filter_pi_star | 203 | 16.5144 | 0.9174 | 0.5468 | -0.5192 | -0.0017 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma691_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.9024 | 0.5667 | -0.5097 | -0.0040 | 0.1067 | ok | RAN |
| ETHUSDT | 8 | `sma691_above_at_h` | one_head_filter_pi_star | 139 | 11.4256 | 0.8750 | 0.5540 | -0.6756 | -0.0052 | 0.1007 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma691_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma691_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0701 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma691_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma691_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma691_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma691_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma691_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma691_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma691_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma691_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma691_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma691_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma691_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma691_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma691_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma691_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
