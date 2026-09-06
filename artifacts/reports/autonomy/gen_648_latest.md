# Autonomy public-indicator hunt gen 648

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T033631Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1220_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 2.0424 | 0.6912 | 4.6040 | 0.0242 | 0.3548 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1220_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 2.1384 | 0.6995 | 4.4093 | 0.0242 | 0.3596 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1220_below_at_h` | one_head_filter_pi_star | 271 | 22.1599 | 1.8719 | 0.6458 | 4.3258 | 0.0131 | 0.3137 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1220_below_at_h` | one_head_filter_pi_star | 277 | 22.5345 | 1.7448 | 0.6354 | 3.8746 | 0.0116 | 0.3177 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1220_above_at_h` | one_head_filter_pi_star | 101 | 8.2356 | 1.7822 | 0.6733 | 2.3540 | 0.0110 | 0.2772 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1220_above_at_h` | one_head_filter_pi_star | 103 | 8.4465 | 1.7766 | 0.6699 | 2.3546 | 0.0105 | 0.2913 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1220_above_at_h` | one_head_filter_pi_star | 131 | 10.8112 | 1.0660 | 0.5573 | 0.3052 | 0.0027 | 0.2061 | ok | RAN |
| ETHUSDT | 4 | `sma1220_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.0533 | 0.5613 | 0.2767 | 0.0022 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1220_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1220_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4938 | 0.3125 | -1.0772 | -0.0564 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
