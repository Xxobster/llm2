# Autonomy public-indicator hunt gen 496

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T173901Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma840_below_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.3822 | 0.7110 | 4.8402 | 0.0276 | 0.3873 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma840_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.8543 | 0.6791 | 3.7445 | 0.0203 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma840_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.7986 | 0.6571 | 3.5439 | 0.0126 | 0.3190 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma840_below_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.6885 | 0.6493 | 3.2068 | 0.0113 | 0.3175 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma840_above_at_h` | one_head_filter_pi_star | 133 | 10.8449 | 1.6868 | 0.6391 | 2.4692 | 0.0098 | 0.3083 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma840_above_at_h` | one_head_filter_pi_star | 150 | 12.2311 | 1.4824 | 0.5933 | 1.9950 | 0.0075 | 0.3067 | ok | RAN |
| ETHUSDT | 8 | `sma840_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.1106 | 0.5909 | 0.5427 | 0.0043 | 0.2208 | ok | RAN |
| ETHUSDT | 4 | `sma840_above_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.0752 | 0.5740 | 0.3811 | 0.0029 | 0.1953 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma840_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma840_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
