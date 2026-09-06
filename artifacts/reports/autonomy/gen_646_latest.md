# Autonomy public-indicator hunt gen 646

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T032822Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma310_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0422 | 0.7090 | 4.5297 | 0.0244 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma310_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9988 | 0.6984 | 4.4275 | 0.0233 | 0.3757 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma310_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.2789 | 0.6989 | 4.4529 | 0.0176 | 0.3864 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma310_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1739 | 0.6864 | 4.0913 | 0.0169 | 0.3787 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma310_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2299 | 0.5916 | 1.1510 | 0.0080 | 0.2251 | ok | RAN |
| SOLUSDT | 4 | `wma310_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3814 | 0.5960 | 1.9472 | 0.0059 | 0.2576 | ok | RAN |
| ETHUSDT | 8 | `wma310_above_at_h` | one_head_filter_pi_star | 203 | 16.6863 | 1.1619 | 0.5911 | 0.8764 | 0.0058 | 0.2266 | ok | RAN |
| SOLUSDT | 8 | `wma310_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3053 | 0.5871 | 1.6172 | 0.0049 | 0.2637 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma310_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma310_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma310_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma310_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
