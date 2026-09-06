# Autonomy public-indicator hunt gen 574

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T224849Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma265_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0509 | 0.7033 | 4.5243 | 0.0239 | 0.3791 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma265_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0249 | 0.7016 | 4.5671 | 0.0237 | 0.3717 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma265_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.2410 | 0.6961 | 4.4500 | 0.0178 | 0.3812 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma265_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1802 | 0.6909 | 4.1175 | 0.0167 | 0.3818 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma265_above_at_h` | one_head_filter_pi_star | 196 | 16.1742 | 1.1718 | 0.5867 | 0.8881 | 0.0061 | 0.2245 | ok | RAN |
| SOLUSDT | 8 | `wma265_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3335 | 0.5874 | 1.7570 | 0.0053 | 0.2670 | ok | RAN |
| ETHUSDT | 4 | `wma265_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.1370 | 0.5838 | 0.7351 | 0.0049 | 0.2234 | ok | RAN |
| SOLUSDT | 4 | `wma265_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3147 | 0.5909 | 1.6462 | 0.0049 | 0.2626 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma265_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma265_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma265_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma265_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma265_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma265_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
