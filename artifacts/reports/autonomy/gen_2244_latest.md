# Autonomy public-indicator hunt gen 2244

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T175758Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1074_above_at_h` | one_head_filter_pi_star | 97 | 8.0620 | 1.4032 | 0.6495 | 1.4506 | 0.0061 | 0.1546 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1074_above_at_h` | one_head_filter_pi_star | 110 | 8.9694 | 1.1953 | 0.6000 | 0.7849 | 0.0034 | 0.1364 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1074_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 0.9784 | 0.5437 | -0.1501 | -0.0005 | 0.1331 | ok | RAN |
| ETHUSDT | 4 | `ema1074_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 0.9513 | 0.5438 | -0.3246 | -0.0015 | 0.1521 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1074_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 0.9421 | 0.5516 | -0.4004 | -0.0018 | 0.1570 | ok | RAN |
| SOLUSDT | 4 | `ema1074_below_at_h` | one_head_filter_pi_star | 262 | 21.4240 | 0.9071 | 0.5305 | -0.6716 | -0.0020 | 0.1336 | ok | RAN |
| ETHUSDT | 8 | `ema1074_above_at_h` | one_head_filter_pi_star | 120 | 9.8638 | 0.8864 | 0.5333 | -0.5243 | -0.0049 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `ema1074_above_at_h` | one_head_filter_pi_star | 122 | 10.0685 | 0.8420 | 0.5410 | -0.7900 | -0.0075 | 0.1311 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1074_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1074_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1074_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1074_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1074_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1074_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1074_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1074_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1074_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1074_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1074_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1074_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1074_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1074_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1074_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1074_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
