# Autonomy public-indicator hunt gen 1283

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T183508Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma641_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9352 | 0.6737 | 4.1536 | 0.0225 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma641_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8602 | 0.6684 | 3.9268 | 0.0209 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma641_below_at_h` | one_head_filter_pi_star | 202 | 16.4331 | 1.8608 | 0.6733 | 3.6414 | 0.0131 | 0.3218 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma641_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.7074 | 0.6615 | 3.1524 | 0.0111 | 0.3281 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma641_above_at_h` | one_head_filter_pi_star | 114 | 9.3491 | 1.7526 | 0.6404 | 2.4517 | 0.0100 | 0.3246 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma641_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.2676 | 0.6226 | 1.2779 | 0.0097 | 0.2327 | ok | RAN |
| ETHUSDT | 4 | `sma641_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 1.2628 | 0.6127 | 1.2120 | 0.0091 | 0.2113 | ok | RAN |
| SOLUSDT | 4 | `sma641_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.4999 | 0.6115 | 2.0300 | 0.0081 | 0.3094 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma641_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0409 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma641_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma641_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma641_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma641_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma641_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma641_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma641_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma641_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma641_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma641_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma641_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma641_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma641_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma641_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma641_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
