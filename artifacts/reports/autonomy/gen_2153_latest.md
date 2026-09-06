# Autonomy public-indicator hunt gen 2153

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T053004Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4940_above_at_h` | one_head_filter_pi_star | 62 | 5.7485 | 1.9545 | 0.6613 | 1.9939 | 0.0121 | 0.0968 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4940_above_at_h` | one_head_filter_pi_star | 48 | 4.4505 | 1.6271 | 0.6458 | 1.2758 | 0.0089 | 0.0833 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4940_below_at_h` | one_head_filter_pi_star | 316 | 25.8396 | 0.9868 | 0.5316 | -0.1009 | -0.0003 | 0.1361 | ok | RAN |
| SOLUSDT | 4 | `ema4940_below_at_h` | one_head_filter_pi_star | 326 | 26.6573 | 0.9752 | 0.5337 | -0.1950 | -0.0005 | 0.1288 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4940_below_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 0.9502 | 0.5546 | -0.4164 | -0.0017 | 0.1408 | ok | RAN |
| ETHUSDT | 8 | `ema4940_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9359 | 0.5513 | -0.5299 | -0.0022 | 0.1378 | ok | RAN |
| ETHUSDT | 8 | `ema4940_above_at_h` | one_head_filter_pi_star | 37 | 10.9173 | 0.8859 | 0.5135 | -0.5671 | -0.0055 | 0.1622 | ok | RAN |
| ETHUSDT | 4 | `ema4940_above_at_h` | one_head_filter_pi_star | 27 | 8.4145 | 0.7919 | 0.4815 | -0.9545 | -0.0099 | 0.1481 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4940_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4940_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4940_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4940_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
