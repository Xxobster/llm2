# Autonomy public-indicator hunt gen 2268

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T205026Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1077_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.1890 | 0.5965 | 0.7966 | 0.0033 | 0.1404 | ok | RAN |
| SOLUSDT | 4 | `ema1077_above_at_h` | one_head_filter_pi_star | 113 | 9.2882 | 1.1279 | 0.6018 | 0.5551 | 0.0023 | 0.1327 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1077_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 0.9991 | 0.5437 | -0.0060 | -0.0000 | 0.1331 | ok | RAN |
| ETHUSDT | 4 | `ema1077_below_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 0.9583 | 0.5550 | -0.2820 | -0.0013 | 0.1606 | ok | RAN |
| ETHUSDT | 4 | `ema1077_above_at_h` | one_head_filter_pi_star | 113 | 9.3257 | 0.9660 | 0.5575 | -0.1518 | -0.0014 | 0.1062 | ok | RAN |
| SOLUSDT | 4 | `ema1077_below_at_h` | one_head_filter_pi_star | 260 | 21.2604 | 0.9343 | 0.5385 | -0.4664 | -0.0014 | 0.1346 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1077_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 0.9243 | 0.5495 | -0.5433 | -0.0024 | 0.1532 | ok | RAN |
| ETHUSDT | 8 | `ema1077_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 0.9343 | 0.5391 | -0.3115 | -0.0029 | 0.1250 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1077_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1077_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0557 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1077_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1077_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1077_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1077_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1077_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1077_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1077_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1077_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1077_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1077_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1077_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1077_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1077_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1077_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
