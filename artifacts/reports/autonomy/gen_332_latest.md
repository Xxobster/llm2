# Autonomy public-indicator hunt gen 332

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T115908Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema185_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1714 | 0.7143 | 4.9363 | 0.0257 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema185_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0471 | 0.6974 | 4.7010 | 0.0236 | 0.3692 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema185_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.1782 | 0.6983 | 4.2837 | 0.0170 | 0.3799 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema185_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.1723 | 0.6954 | 4.1743 | 0.0169 | 0.3736 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema185_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1703 | 0.5957 | 0.8893 | 0.0060 | 0.2234 | ok | RAN |
| SOLUSDT | 8 | `ema185_above_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.3084 | 0.5882 | 1.6434 | 0.0048 | 0.2696 | ok | RAN |
| SOLUSDT | 4 | `ema185_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3013 | 0.5800 | 1.5976 | 0.0047 | 0.2650 | ok | RAN |
| ETHUSDT | 8 | `ema185_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.1223 | 0.5879 | 0.6473 | 0.0044 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema185_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema185_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema185_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema185_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
