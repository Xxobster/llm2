# Autonomy public-indicator hunt gen 2155

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T055116Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma761_below_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.3282 | 0.6059 | 1.7051 | 0.0088 | 0.1941 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma761_below_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.1496 | 0.5723 | 0.8578 | 0.0045 | 0.1734 | ok | RAN |
| SOLUSDT | 8 | `sma761_above_at_h` | one_head_filter_pi_star | 147 | 12.0547 | 1.1083 | 0.5442 | 0.5363 | 0.0020 | 0.1293 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma761_above_at_h` | one_head_filter_pi_star | 132 | 10.8247 | 0.9787 | 0.5379 | -0.1049 | -0.0004 | 0.1212 | ok | RAN |
| SOLUSDT | 8 | `sma761_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 0.9637 | 0.5524 | -0.2262 | -0.0007 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `sma761_below_at_h` | one_head_filter_pi_star | 217 | 17.7443 | 0.9503 | 0.5530 | -0.3197 | -0.0011 | 0.1336 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma761_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 0.8493 | 0.5494 | -0.8321 | -0.0063 | 0.0988 | ok | RAN |
| ETHUSDT | 8 | `sma761_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 0.8378 | 0.5409 | -0.9196 | -0.0070 | 0.1132 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma761_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0535 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma761_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma761_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma761_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma761_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma761_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma761_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma761_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma761_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma761_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma761_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma761_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma761_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma761_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma761_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma761_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
