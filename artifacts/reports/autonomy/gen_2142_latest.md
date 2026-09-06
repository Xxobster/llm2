# Autonomy public-indicator hunt gen 2142

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T034150Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma512_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1231 | 0.5815 | 0.7353 | 0.0039 | 0.2011 | ok | RAN |
| ETHUSDT | 8 | `wma512_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.0991 | 0.5820 | 0.6070 | 0.0031 | 0.1905 | ok | RAN |
| SOLUSDT | 8 | `wma512_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0739 | 0.5640 | 0.4173 | 0.0015 | 0.1686 | ok | RAN |
| SOLUSDT | 4 | `wma512_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.0567 | 0.5674 | 0.3261 | 0.0012 | 0.1517 | ok | RAN |
| SOLUSDT | 8 | `wma512_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.0505 | 0.5426 | 0.2896 | 0.0009 | 0.0957 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma512_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 0.9760 | 0.5337 | -0.1440 | -0.0005 | 0.1036 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma512_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.8335 | 0.5393 | -1.0141 | -0.0070 | 0.0899 | ok | RAN |
| ETHUSDT | 4 | `wma512_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.7897 | 0.5323 | -1.3800 | -0.0089 | 0.0968 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma512_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma512_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma512_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma512_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma512_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma512_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma512_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma512_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma512_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma512_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma512_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma512_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma512_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma512_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma512_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma512_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
