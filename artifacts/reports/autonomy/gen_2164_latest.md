# Autonomy public-indicator hunt gen 2164

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T071244Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1064_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.1430 | 0.6036 | 0.5935 | 0.0024 | 0.1261 | ok | RAN |
| SOLUSDT | 4 | `ema1064_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.1307 | 0.5789 | 0.5597 | 0.0023 | 0.1404 | ok | RAN |
| ETHUSDT | 4 | `ema1064_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 1.0122 | 0.5565 | 0.0817 | 0.0004 | 0.1565 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1064_below_at_h` | one_head_filter_pi_star | 236 | 19.2979 | 1.0039 | 0.5466 | 0.0255 | 0.0001 | 0.1271 | ok | RAN |
| SOLUSDT | 8 | `ema1064_below_at_h` | one_head_filter_pi_star | 266 | 21.7510 | 0.9292 | 0.5338 | -0.5087 | -0.0015 | 0.1316 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1064_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 0.9148 | 0.5422 | -0.5888 | -0.0027 | 0.1556 | ok | RAN |
| ETHUSDT | 4 | `ema1064_above_at_h` | one_head_filter_pi_star | 121 | 9.9859 | 0.8927 | 0.5455 | -0.5027 | -0.0047 | 0.1240 | ok | RAN |
| ETHUSDT | 8 | `ema1064_above_at_h` | one_head_filter_pi_star | 119 | 9.7816 | 0.8924 | 0.5294 | -0.5203 | -0.0047 | 0.1345 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1064_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1064_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1064_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1064_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1064_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1064_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1064_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1064_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1064_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1064_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1064_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1064_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1064_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1064_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1064_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1064_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
