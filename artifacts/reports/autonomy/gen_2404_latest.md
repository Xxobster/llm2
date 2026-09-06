# Autonomy public-indicator hunt gen 2404

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T141836Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1095_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1095_above_at_h` | one_head_filter_pi_star | 102 | 8.3171 | 1.3626 | 0.5980 | 1.3136 | 0.0055 | 0.1373 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1095_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.0459 | 0.5664 | 0.2032 | 0.0009 | 0.1327 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1095_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 0.9760 | 0.5516 | -0.1611 | -0.0007 | 0.1525 | ok | RAN |
| ETHUSDT | 4 | `ema1095_above_at_h` | one_head_filter_pi_star | 127 | 10.4392 | 0.9754 | 0.5669 | -0.1099 | -0.0010 | 0.1260 | ok | RAN |
| SOLUSDT | 8 | `ema1095_below_at_h` | one_head_filter_pi_star | 268 | 21.9146 | 0.9246 | 0.5336 | -0.5484 | -0.0017 | 0.1306 | ok | RAN |
| SOLUSDT | 4 | `ema1095_below_at_h` | one_head_filter_pi_star | 269 | 21.9964 | 0.9230 | 0.5316 | -0.5616 | -0.0017 | 0.1264 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1095_below_at_h` | one_head_filter_pi_star | 246 | 20.0959 | 0.9168 | 0.5366 | -0.6281 | -0.0027 | 0.1463 | ok | RAN |
| ETHUSDT | 8 | `ema1095_above_at_h` | one_head_filter_pi_star | 105 | 8.6655 | 0.9132 | 0.5429 | -0.3883 | -0.0038 | 0.1333 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1095_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6250 | 0.3125 | -0.7038 | -0.0335 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1095_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1095_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1095_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1095_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1095_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1095_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1095_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1095_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1095_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1095_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1095_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1095_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1095_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1095_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
