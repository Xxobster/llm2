# Autonomy public-indicator hunt gen 2340

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T054956Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1087_above_at_h` | one_head_filter_pi_star | 104 | 8.4802 | 1.3039 | 0.6250 | 1.1265 | 0.0048 | 0.1346 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1087_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.1508 | 0.5841 | 0.6244 | 0.0027 | 0.1416 | ok | RAN |
| SOLUSDT | 8 | `ema1087_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.0040 | 0.5451 | 0.0269 | 0.0001 | 0.1294 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1087_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 0.9684 | 0.5397 | -0.2146 | -0.0007 | 0.1270 | ok | RAN |
| ETHUSDT | 8 | `ema1087_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.9691 | 0.5466 | -0.2193 | -0.0010 | 0.1525 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1087_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 0.9361 | 0.5398 | -0.4359 | -0.0020 | 0.1504 | ok | RAN |
| ETHUSDT | 4 | `ema1087_above_at_h` | one_head_filter_pi_star | 115 | 9.4908 | 0.8816 | 0.5478 | -0.5405 | -0.0052 | 0.1304 | ok | RAN |
| ETHUSDT | 8 | `ema1087_above_at_h` | one_head_filter_pi_star | 107 | 8.7953 | 0.8737 | 0.5327 | -0.5792 | -0.0055 | 0.1308 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1087_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1087_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1087_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1087_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1087_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1087_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1087_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1087_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1087_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1087_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1087_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1087_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1087_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1087_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1087_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1087_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
