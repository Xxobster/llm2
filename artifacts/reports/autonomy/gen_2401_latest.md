# Autonomy public-indicator hunt gen 2401

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T135705Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5560_above_at_h` | one_head_filter_pi_star | 35 | 3.2862 | 2.5502 | 0.6857 | 2.0193 | 0.0165 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema5560_above_at_h` | one_head_filter_pi_star | 48 | 4.4505 | 1.3889 | 0.6042 | 0.9169 | 0.0058 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5560_below_at_h` | one_head_filter_pi_star | 326 | 26.6573 | 0.9861 | 0.5399 | -0.1087 | -0.0003 | 0.1319 | ok | RAN |
| SOLUSDT | 4 | `ema5560_below_at_h` | one_head_filter_pi_star | 301 | 24.6130 | 0.9460 | 0.5282 | -0.4096 | -0.0011 | 0.1262 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5560_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9445 | 0.5526 | -0.4739 | -0.0019 | 0.1345 | ok | RAN |
| ETHUSDT | 8 | `ema5560_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9339 | 0.5503 | -0.5553 | -0.0022 | 0.1361 | ok | RAN |
| ETHUSDT | 8 | `ema5560_above_at_h` | one_head_filter_pi_star | 41 | 6.9835 | 0.7915 | 0.5122 | -0.9075 | -0.0110 | 0.1463 | ok | RAN |
| ETHUSDT | 4 | `ema5560_above_at_h` | one_head_filter_pi_star | 47 | 7.6624 | 0.7636 | 0.4894 | -1.1084 | -0.0128 | 0.1489 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5560_above_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.5417 | 0.2857 | -1.1090 | -0.0569 | 0.0476 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5560_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0628 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
