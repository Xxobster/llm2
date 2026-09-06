# Autonomy public-indicator hunt gen 1964

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T052527Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1037_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.2507 | 0.6083 | 1.0088 | 0.0043 | 0.1417 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1037_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.1691 | 0.5917 | 0.7100 | 0.0030 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1037_below_at_h` | one_head_filter_pi_star | 242 | 19.7692 | 0.9890 | 0.5496 | -0.0771 | -0.0003 | 0.1488 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ema1037_below_at_h` | one_head_filter_pi_star | 269 | 21.9964 | 0.9219 | 0.5316 | -0.5699 | -0.0017 | 0.1301 | ok | RAN |
| ETHUSDT | 8 | `ema1037_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 0.9356 | 0.5439 | -0.4465 | -0.0020 | 0.1491 | ok | RAN |
| SOLUSDT | 4 | `ema1037_below_at_h` | one_head_filter_pi_star | 262 | 21.4240 | 0.9060 | 0.5305 | -0.6806 | -0.0021 | 0.1336 | ok | RAN |
| ETHUSDT | 8 | `ema1037_above_at_h` | one_head_filter_pi_star | 127 | 10.4811 | 0.9421 | 0.5512 | -0.2745 | -0.0024 | 0.1181 | ok | RAN |
| ETHUSDT | 4 | `ema1037_above_at_h` | one_head_filter_pi_star | 109 | 8.9956 | 0.8492 | 0.5413 | -0.6899 | -0.0067 | 0.1193 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1037_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1037_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1037_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1037_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1037_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1037_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1037_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1037_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1037_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1037_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1037_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1037_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1037_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1037_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1037_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1037_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
