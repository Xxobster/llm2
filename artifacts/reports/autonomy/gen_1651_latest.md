# Autonomy public-indicator hunt gen 1651

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T231434Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma694_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1565 | 0.5824 | 0.9135 | 0.0047 | 0.1923 | ok | RAN |
| SOLUSDT | 8 | `sma694_above_at_h` | one_head_filter_pi_star | 105 | 8.6105 | 1.2661 | 0.5905 | 1.0290 | 0.0044 | 0.1238 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma694_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.0901 | 0.5667 | 0.5358 | 0.0027 | 0.1778 | ok | RAN |
| SOLUSDT | 4 | `sma694_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.0998 | 0.5620 | 0.4834 | 0.0019 | 0.1095 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma694_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9383 | 0.5561 | -0.3841 | -0.0013 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma694_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.8806 | 0.5492 | -0.7444 | -0.0026 | 0.1451 | ok | RAN |
| ETHUSDT | 4 | `sma694_above_at_h` | one_head_filter_pi_star | 133 | 10.9753 | 0.8969 | 0.5489 | -0.5192 | -0.0042 | 0.1053 | ok | RAN |
| ETHUSDT | 8 | `sma694_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 0.8740 | 0.5577 | -0.7019 | -0.0051 | 0.1090 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma694_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma694_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma694_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma694_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma694_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma694_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma694_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma694_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma694_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma694_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma694_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma694_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma694_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma694_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma694_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma694_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
