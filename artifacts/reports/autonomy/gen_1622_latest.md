# Autonomy public-indicator hunt gen 1622

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T201147Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma431_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.1394 | 0.6000 | 0.8100 | 0.0042 | 0.1943 | ok | RAN |
| ETHUSDT | 8 | `wma431_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1375 | 0.5882 | 0.8213 | 0.0042 | 0.1872 | ok | RAN |
| SOLUSDT | 8 | `wma431_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.1224 | 0.5698 | 0.6667 | 0.0024 | 0.1564 | ok | RAN |
| SOLUSDT | 4 | `wma431_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.0928 | 0.5763 | 0.5026 | 0.0019 | 0.1525 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma431_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 0.9688 | 0.5410 | -0.1840 | -0.0006 | 0.0984 | ok | RAN |
| SOLUSDT | 4 | `wma431_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 0.9563 | 0.5357 | -0.2678 | -0.0008 | 0.1071 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma431_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8490 | 0.5359 | -0.9336 | -0.0061 | 0.0994 | ok | RAN |
| ETHUSDT | 8 | `wma431_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8043 | 0.5340 | -1.2150 | -0.0081 | 0.0890 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma431_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma431_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma431_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma431_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma431_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma431_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma431_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma431_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma431_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma431_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma431_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma431_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma431_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma431_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma431_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma431_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
