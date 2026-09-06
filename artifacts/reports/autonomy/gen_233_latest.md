# Autonomy public-indicator hunt gen 233

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T004921Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema120_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0802 | 0.7010 | 4.8076 | 0.0250 | 0.3711 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema120_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0534 | 0.6979 | 4.6777 | 0.0241 | 0.3698 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema120_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.2359 | 0.6971 | 4.3523 | 0.0179 | 0.3771 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema120_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1999 | 0.6901 | 4.2310 | 0.0174 | 0.3860 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema120_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2386 | 0.6033 | 1.1966 | 0.0077 | 0.2174 | ok | RAN |
| SOLUSDT | 8 | `ema120_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3493 | 0.5952 | 1.8278 | 0.0054 | 0.2667 | ok | RAN |
| SOLUSDT | 4 | `ema120_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.2923 | 0.5871 | 1.5586 | 0.0045 | 0.2637 | ok | RAN |
| ETHUSDT | 4 | `ema120_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.0942 | 0.5846 | 0.5079 | 0.0034 | 0.2205 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema120_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema120_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
