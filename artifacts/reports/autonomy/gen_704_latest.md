# Autonomy public-indicator hunt gen 704

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T072744Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1360_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.8488 | 0.6737 | 3.9868 | 0.0201 | 0.3517 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1360_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 1.7228 | 0.6509 | 3.4862 | 0.0174 | 0.3276 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1360_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 1.8986 | 0.6562 | 4.2676 | 0.0135 | 0.3047 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1360_below_at_h` | one_head_filter_pi_star | 285 | 23.3047 | 1.7400 | 0.6351 | 3.9483 | 0.0113 | 0.3193 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1360_above_at_h` | one_head_filter_pi_star | 88 | 7.2329 | 1.6436 | 0.6477 | 1.9557 | 0.0101 | 0.2727 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma1360_above_at_h` | one_head_filter_pi_star | 75 | 6.2335 | 1.3738 | 0.6533 | 1.2282 | 0.0060 | 0.2800 | ok | RAN |
| ETHUSDT | 4 | `sma1360_above_at_h` | one_head_filter_pi_star | 104 | 8.5830 | 1.0812 | 0.5577 | 0.3549 | 0.0036 | 0.2404 | ok | RAN |
| ETHUSDT | 8 | `sma1360_above_at_h` | one_head_filter_pi_star | 88 | 7.2625 | 1.0885 | 0.5682 | 0.3376 | 0.0034 | 0.2045 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1360_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1360_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
