# Autonomy public-indicator hunt gen 731

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T092532Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma448_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0411 | 0.6961 | 4.4228 | 0.0242 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma448_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8391 | 0.6788 | 3.9733 | 0.0208 | 0.3834 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma448_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.0411 | 0.6848 | 4.0513 | 0.0148 | 0.3641 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma448_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8856 | 0.6702 | 3.7215 | 0.0133 | 0.3455 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma448_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.6141 | 0.6077 | 2.7241 | 0.0098 | 0.2818 | ok | RAN |
| ETHUSDT | 4 | `sma448_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2819 | 0.5968 | 1.4458 | 0.0097 | 0.2258 | ok | RAN |
| SOLUSDT | 4 | `sma448_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.5568 | 0.6096 | 2.5615 | 0.0086 | 0.2727 | ok | RAN |
| ETHUSDT | 8 | `sma448_above_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.2103 | 0.5909 | 1.0726 | 0.0075 | 0.2102 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma448_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma448_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma448_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma448_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
