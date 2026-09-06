# Autonomy public-indicator hunt gen 2132

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T020942Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1059_above_at_h` | one_head_filter_pi_star | 110 | 8.9694 | 1.2426 | 0.6000 | 0.9782 | 0.0041 | 0.1364 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1059_above_at_h` | one_head_filter_pi_star | 105 | 8.7269 | 1.1779 | 0.6095 | 0.7422 | 0.0032 | 0.1429 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema1059_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 0.9878 | 0.5531 | -0.0820 | -0.0004 | 0.1504 | ok | RAN |
| SOLUSDT | 8 | `ema1059_below_at_h` | one_head_filter_pi_star | 234 | 19.1344 | 0.9719 | 0.5427 | -0.1829 | -0.0006 | 0.1239 | ok | RAN |
| SOLUSDT | 4 | `ema1059_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 0.9335 | 0.5382 | -0.4621 | -0.0014 | 0.1285 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1059_above_at_h` | one_head_filter_pi_star | 114 | 9.4082 | 0.9547 | 0.5439 | -0.2045 | -0.0019 | 0.1228 | ok | RAN |
| ETHUSDT | 4 | `ema1059_below_at_h` | one_head_filter_pi_star | 239 | 19.5241 | 0.9377 | 0.5397 | -0.4447 | -0.0020 | 0.1464 | ok | RAN |
| ETHUSDT | 4 | `ema1059_above_at_h` | one_head_filter_pi_star | 125 | 10.3160 | 0.9200 | 0.5680 | -0.3762 | -0.0035 | 0.1360 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1059_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1059_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1059_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1059_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1059_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1059_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1059_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1059_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1059_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1059_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1059_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1059_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1059_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1059_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1059_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1059_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
