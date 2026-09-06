# Autonomy public-indicator hunt gen 1820

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T161314Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1018_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.1621 | 0.5833 | 0.6893 | 0.0030 | 0.1417 | ok | RAN |
| SOLUSDT | 4 | `ema1018_above_at_h` | one_head_filter_pi_star | 132 | 10.7633 | 1.1382 | 0.5682 | 0.6287 | 0.0025 | 0.1212 | ok | RAN |
| SOLUSDT | 8 | `ema1018_below_at_h` | one_head_filter_pi_star | 240 | 19.6250 | 1.0297 | 0.5542 | 0.1935 | 0.0006 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `ema1018_above_at_h` | one_head_filter_pi_star | 124 | 10.2335 | 1.0079 | 0.5726 | 0.0360 | 0.0003 | 0.1371 | ok | RAN |
| ETHUSDT | 4 | `ema1018_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 1.0082 | 0.5560 | 0.0555 | 0.0003 | 0.1466 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1018_below_at_h` | one_head_filter_pi_star | 260 | 21.2604 | 0.9600 | 0.5423 | -0.2820 | -0.0009 | 0.1269 | ok | RAN |
| ETHUSDT | 8 | `ema1018_above_at_h` | one_head_filter_pi_star | 130 | 10.7287 | 0.9631 | 0.5538 | -0.1677 | -0.0016 | 0.1231 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1018_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 0.9445 | 0.5447 | -0.3945 | -0.0018 | 0.1489 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1018_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1018_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1018_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1018_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1018_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1018_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1018_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1018_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1018_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1018_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1018_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1018_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1018_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1018_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1018_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1018_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
