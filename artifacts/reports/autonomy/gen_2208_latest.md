# Autonomy public-indicator hunt gen 2208

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T133309Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5120_above_at_h` | one_head_filter_pi_star | 41 | 3.8496 | 2.4876 | 0.6341 | 2.1891 | 0.0174 | 0.0976 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma5120_above_at_h` | one_head_filter_pi_star | 48 | 4.2331 | 2.1390 | 0.6042 | 1.9486 | 0.0150 | 0.1042 | ok | RAN |
| ETHUSDT | 8 | `sma5120_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.0157 | 0.5605 | 0.1264 | 0.0005 | 0.1357 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma5120_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 0.9718 | 0.5370 | -0.2120 | -0.0006 | 0.1350 | ok | RAN |
| SOLUSDT | 8 | `sma5120_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 0.9651 | 0.5370 | -0.2651 | -0.0007 | 0.1318 | ok | RAN |
| ETHUSDT | 4 | `sma5120_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9744 | 0.5569 | -0.2108 | -0.0008 | 0.1370 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5120_above_at_h` | one_head_filter_pi_star | 38 | 11.2124 | 0.7820 | 0.5000 | -1.3413 | -0.0123 | 0.1579 | ok | RAN |
| ETHUSDT | 8 | `sma5120_above_at_h` | one_head_filter_pi_star | 35 | 10.3272 | 0.7096 | 0.4857 | -1.5917 | -0.0163 | 0.1429 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
