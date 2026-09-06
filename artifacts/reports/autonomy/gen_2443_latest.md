# Autonomy public-indicator hunt gen 2443

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T185256Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma798_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.2737 | 0.5906 | 1.4271 | 0.0077 | 0.1930 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma798_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1908 | 0.5906 | 1.0653 | 0.0052 | 0.1813 | ok | RAN |
| SOLUSDT | 8 | `sma798_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.1245 | 0.5608 | 0.6232 | 0.0023 | 0.1149 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma798_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.0032 | 0.5319 | 0.0161 | 0.0001 | 0.1277 | ok | RAN |
| SOLUSDT | 4 | `sma798_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 0.9460 | 0.5566 | -0.3428 | -0.0011 | 0.1321 | ok | RAN |
| SOLUSDT | 8 | `sma798_below_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 0.9396 | 0.5467 | -0.3938 | -0.0013 | 0.1215 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma798_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 0.9131 | 0.5580 | -0.4234 | -0.0037 | 0.1159 | ok | RAN |
| ETHUSDT | 8 | `sma798_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 0.8731 | 0.5606 | -0.6154 | -0.0054 | 0.1061 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma798_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma798_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma798_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma798_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma798_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma798_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma798_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma798_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma798_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma798_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma798_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma798_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma798_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma798_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma798_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma798_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
