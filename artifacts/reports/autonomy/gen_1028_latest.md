# Autonomy public-indicator hunt gen 1028

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T140231Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema903_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.9874 | 0.6756 | 4.2744 | 0.0219 | 0.3511 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema903_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.7051 | 0.6533 | 3.4469 | 0.0174 | 0.3511 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema903_below_at_h` | one_head_filter_pi_star | 239 | 19.5432 | 1.7830 | 0.6569 | 3.7537 | 0.0123 | 0.3054 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema903_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 1.7684 | 0.6468 | 3.7961 | 0.0121 | 0.2976 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema903_above_at_h` | one_head_filter_pi_star | 131 | 10.6818 | 1.7360 | 0.6336 | 2.5785 | 0.0104 | 0.2901 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema903_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.6750 | 0.6385 | 2.5201 | 0.0102 | 0.3231 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema903_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 1.1585 | 0.5915 | 0.7379 | 0.0062 | 0.2324 | ok | RAN |
| ETHUSDT | 4 | `ema903_above_at_h` | one_head_filter_pi_star | 119 | 9.7816 | 1.1590 | 0.6050 | 0.6763 | 0.0059 | 0.2101 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema903_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0511 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema903_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema903_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema903_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema903_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema903_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema903_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema903_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema903_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema903_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema903_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema903_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema903_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema903_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema903_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema903_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
