# Autonomy public-indicator hunt gen 1176

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T075821Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma2540_above_at_h` | one_head_filter_pi_star | 49 | 4.7268 | 1.5181 | 0.6327 | 1.3484 | 0.0194 | 0.2449 | ok | RAN |
| ETHUSDT | 4 | `sma2540_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.6409 | 0.6481 | 3.8364 | 0.0167 | 0.3050 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2540_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 1.5557 | 0.6390 | 3.5506 | 0.0153 | 0.3037 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma2540_below_at_h` | one_head_filter_pi_star | 280 | 22.7786 | 1.8910 | 0.6571 | 4.3282 | 0.0135 | 0.3321 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2540_above_at_h` | one_head_filter_pi_star | 33 | 3.2399 | 1.3478 | 0.6061 | 0.8036 | 0.0119 | 0.2727 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma2540_below_at_h` | one_head_filter_pi_star | 308 | 25.1854 | 1.7306 | 0.6494 | 3.9853 | 0.0115 | 0.3344 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2540_above_at_h` | one_head_filter_pi_star | 83 | 6.8231 | 1.8915 | 0.6747 | 2.2684 | 0.0108 | 0.2169 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2540_above_at_h` | one_head_filter_pi_star | 70 | 5.7544 | 1.8273 | 0.6429 | 2.0481 | 0.0105 | 0.2143 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2540_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2540_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
