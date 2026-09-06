# Autonomy public-indicator hunt gen 390

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T000338Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma150_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0359 | 0.6990 | 4.6661 | 0.0242 | 0.3776 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma150_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9590 | 0.6900 | 4.4406 | 0.0231 | 0.3700 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma150_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.3323 | 0.6983 | 4.6410 | 0.0186 | 0.3799 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma150_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2370 | 0.6923 | 4.2688 | 0.0180 | 0.3964 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma150_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2834 | 0.6108 | 1.3604 | 0.0090 | 0.2324 | ok | RAN |
| ETHUSDT | 4 | `wma150_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1757 | 0.5957 | 0.9120 | 0.0060 | 0.2234 | ok | RAN |
| SOLUSDT | 4 | `wma150_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.2735 | 0.5961 | 1.4777 | 0.0043 | 0.2562 | ok | RAN |
| SOLUSDT | 8 | `wma150_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.2774 | 0.5825 | 1.4886 | 0.0043 | 0.2573 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma150_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma150_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma150_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma150_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
