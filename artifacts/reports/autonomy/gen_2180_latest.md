# Autonomy public-indicator hunt gen 2180

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T095301Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1066_above_at_h` | one_head_filter_pi_star | 98 | 8.1451 | 1.3113 | 0.6327 | 1.1500 | 0.0049 | 0.1633 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1066_above_at_h` | one_head_filter_pi_star | 112 | 9.2060 | 1.2738 | 0.6250 | 1.0893 | 0.0047 | 0.1339 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1066_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 0.9628 | 0.5446 | -0.2489 | -0.0012 | 0.1562 | ok | RAN |
| SOLUSDT | 8 | `ema1066_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 0.9370 | 0.5341 | -0.4517 | -0.0013 | 0.1288 | ok | RAN |
| SOLUSDT | 4 | `ema1066_below_at_h` | one_head_filter_pi_star | 266 | 21.7510 | 0.9348 | 0.5376 | -0.4665 | -0.0014 | 0.1353 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1066_below_at_h` | one_head_filter_pi_star | 254 | 20.7495 | 0.9461 | 0.5472 | -0.4069 | -0.0017 | 0.1457 | ok | RAN |
| ETHUSDT | 4 | `ema1066_above_at_h` | one_head_filter_pi_star | 137 | 11.3054 | 0.9410 | 0.5547 | -0.2950 | -0.0025 | 0.1241 | ok | RAN |
| ETHUSDT | 8 | `ema1066_above_at_h` | one_head_filter_pi_star | 121 | 9.9859 | 0.9206 | 0.5455 | -0.3658 | -0.0034 | 0.1157 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1066_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1066_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1066_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1066_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1066_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1066_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1066_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1066_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1066_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1066_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1066_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1066_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1066_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1066_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1066_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1066_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
