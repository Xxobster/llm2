# Autonomy public-indicator hunt gen 1766

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T111452Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma453_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1896 | 0.6000 | 1.0969 | 0.0058 | 0.2000 | ok | RAN |
| ETHUSDT | 8 | `wma453_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1642 | 0.5892 | 0.9378 | 0.0050 | 0.1838 | ok | RAN |
| SOLUSDT | 4 | `wma453_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.0685 | 0.5749 | 0.3765 | 0.0014 | 0.1617 | ok | RAN |
| SOLUSDT | 8 | `wma453_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0567 | 0.5665 | 0.3186 | 0.0012 | 0.1618 | ok | RAN |
| SOLUSDT | 8 | `wma453_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.0214 | 0.5419 | 0.1221 | 0.0004 | 0.1006 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma453_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 0.9744 | 0.5400 | -0.1563 | -0.0005 | 0.1050 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma453_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8298 | 0.5340 | -1.0561 | -0.0069 | 0.0995 | ok | RAN |
| ETHUSDT | 8 | `wma453_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 0.8194 | 0.5410 | -1.1383 | -0.0074 | 0.0929 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma453_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma453_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma453_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma453_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma453_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma453_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma453_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma453_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma453_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma453_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma453_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma453_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma453_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma453_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma453_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma453_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
