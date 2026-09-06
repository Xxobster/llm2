# Autonomy public-indicator hunt gen 688

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T061908Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1320_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.9215 | 0.6864 | 4.0131 | 0.0214 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1320_below_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.8032 | 0.6667 | 3.6814 | 0.0188 | 0.3425 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1320_below_at_h` | one_head_filter_pi_star | 270 | 22.0781 | 1.7528 | 0.6333 | 3.8961 | 0.0118 | 0.3037 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1320_below_at_h` | one_head_filter_pi_star | 266 | 21.7510 | 1.7196 | 0.6353 | 3.7670 | 0.0117 | 0.3083 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1320_above_at_h` | one_head_filter_pi_star | 81 | 6.7321 | 1.6566 | 0.6667 | 1.9386 | 0.0098 | 0.2963 | ok | RAN |
| SOLUSDT | 4 | `sma1320_above_at_h` | one_head_filter_pi_star | 66 | 5.4855 | 1.4793 | 0.6515 | 1.4600 | 0.0075 | 0.2727 | ok | RAN |
| ETHUSDT | 8 | `sma1320_above_at_h` | one_head_filter_pi_star | 139 | 11.4714 | 1.1399 | 0.5827 | 0.6492 | 0.0056 | 0.1942 | ok | RAN |
| ETHUSDT | 4 | `sma1320_above_at_h` | one_head_filter_pi_star | 107 | 8.7953 | 1.1049 | 0.5701 | 0.4463 | 0.0040 | 0.2150 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1320_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1320_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0557 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
