# Autonomy public-indicator hunt gen 2286

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T225956Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma534_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1581 | 0.5956 | 0.9243 | 0.0047 | 0.1858 | ok | RAN |
| ETHUSDT | 4 | `wma534_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1408 | 0.5889 | 0.8363 | 0.0043 | 0.1889 | ok | RAN |
| SOLUSDT | 4 | `wma534_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0531 | 0.5464 | 0.3029 | 0.0010 | 0.0984 | ok | RAN |
| SOLUSDT | 8 | `wma534_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.0109 | 0.5330 | 0.0666 | 0.0002 | 0.1015 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma534_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 0.9837 | 0.5500 | -0.0984 | -0.0003 | 0.1611 | ok | RAN |
| SOLUSDT | 8 | `wma534_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 0.9660 | 0.5479 | -0.2096 | -0.0007 | 0.1489 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma534_above_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 0.8144 | 0.5304 | -1.1764 | -0.0076 | 0.0939 | ok | RAN |
| ETHUSDT | 8 | `wma534_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.7969 | 0.5294 | -1.3146 | -0.0086 | 0.0909 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma534_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma534_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma534_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma534_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
