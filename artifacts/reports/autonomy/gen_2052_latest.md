# Autonomy public-indicator hunt gen 2052

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T152650Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1049_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0727 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1049_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.2034 | 0.6018 | 0.8379 | 0.0035 | 0.1327 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1049_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.1274 | 0.5772 | 0.5558 | 0.0024 | 0.1301 | ok | RAN |
| ETHUSDT | 8 | `ema1049_below_at_h` | one_head_filter_pi_star | 241 | 19.6875 | 1.0211 | 0.5560 | 0.1445 | 0.0007 | 0.1577 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1049_below_at_h` | one_head_filter_pi_star | 240 | 19.6250 | 0.9876 | 0.5500 | -0.0822 | -0.0003 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `ema1049_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 0.9809 | 0.5476 | -0.1290 | -0.0004 | 0.1270 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1049_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 0.9438 | 0.5450 | -0.3816 | -0.0018 | 0.1532 | ok | RAN |
| ETHUSDT | 4 | `ema1049_above_at_h` | one_head_filter_pi_star | 130 | 10.6858 | 0.9543 | 0.5538 | -0.2187 | -0.0020 | 0.1154 | ok | RAN |
| ETHUSDT | 8 | `ema1049_above_at_h` | one_head_filter_pi_star | 125 | 10.2748 | 0.8778 | 0.5360 | -0.5966 | -0.0055 | 0.1360 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1049_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0506 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1049_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1049_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1049_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1049_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1049_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1049_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1049_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1049_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1049_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1049_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1049_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1049_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1049_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1049_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
