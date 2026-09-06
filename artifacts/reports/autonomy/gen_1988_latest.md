# Autonomy public-indicator hunt gen 1988

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T074533Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1041_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.2439 | 0.6116 | 0.9935 | 0.0042 | 0.1240 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1041_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.1592 | 0.5833 | 0.6952 | 0.0029 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1041_below_at_h` | one_head_filter_pi_star | 262 | 21.3142 | 0.9680 | 0.5382 | -0.2231 | -0.0007 | 0.1260 | ok | RAN |
| SOLUSDT | 4 | `ema1041_below_at_h` | one_head_filter_pi_star | 272 | 22.1277 | 0.9502 | 0.5368 | -0.3567 | -0.0011 | 0.1324 | ok | RAN |
| ETHUSDT | 8 | `ema1041_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 0.9629 | 0.5570 | -0.2609 | -0.0012 | 0.1491 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1041_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 0.9210 | 0.5381 | -0.5486 | -0.0025 | 0.1525 | ok | RAN |
| ETHUSDT | 8 | `ema1041_above_at_h` | one_head_filter_pi_star | 122 | 10.0685 | 0.9014 | 0.5328 | -0.4757 | -0.0043 | 0.1230 | ok | RAN |
| ETHUSDT | 4 | `ema1041_above_at_h` | one_head_filter_pi_star | 121 | 9.9460 | 0.8472 | 0.5372 | -0.7500 | -0.0068 | 0.1240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1041_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1041_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1041_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1041_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1041_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1041_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1041_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1041_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1041_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1041_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1041_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1041_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1041_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1041_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1041_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1041_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
