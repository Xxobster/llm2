# Autonomy public-indicator hunt gen 2116

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T001511Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1057_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.2708 | 0.6106 | 1.1251 | 0.0044 | 0.1327 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1057_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.1988 | 0.5862 | 0.8342 | 0.0035 | 0.1379 | ok | RAN |
| ETHUSDT | 4 | `ema1057_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.0157 | 0.5546 | 0.1074 | 0.0005 | 0.1485 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1057_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.0018 | 0.5475 | 0.0124 | 0.0000 | 0.1331 | ok | RAN |
| ETHUSDT | 8 | `ema1057_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 1.0006 | 0.5419 | 0.0042 | 0.0000 | 0.1542 | ok | RAN |
| SOLUSDT | 8 | `ema1057_below_at_h` | one_head_filter_pi_star | 262 | 21.4240 | 0.9618 | 0.5382 | -0.2682 | -0.0008 | 0.1298 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1057_above_at_h` | one_head_filter_pi_star | 129 | 10.6462 | 0.9581 | 0.5581 | -0.1921 | -0.0017 | 0.1163 | ok | RAN |
| ETHUSDT | 4 | `ema1057_above_at_h` | one_head_filter_pi_star | 122 | 10.0685 | 0.9526 | 0.5574 | -0.2152 | -0.0021 | 0.1230 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1057_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1057_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1057_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1057_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1057_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1057_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1057_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1057_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1057_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1057_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1057_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1057_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1057_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1057_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1057_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1057_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
