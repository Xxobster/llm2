# Autonomy public-indicator hunt gen 526

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T193953Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma235_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0587 | 0.7043 | 4.6671 | 0.0244 | 0.3710 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma235_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.8831 | 0.6842 | 4.1160 | 0.0212 | 0.3684 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma235_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2080 | 0.6959 | 4.1968 | 0.0173 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma235_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.1871 | 0.6914 | 4.2111 | 0.0171 | 0.3714 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma235_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.3182 | 0.6066 | 1.5230 | 0.0103 | 0.2240 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma235_above_at_h` | one_head_filter_pi_star | 200 | 16.4397 | 1.2194 | 0.6050 | 1.1654 | 0.0078 | 0.2350 | ok | RAN |
| SOLUSDT | 8 | `wma235_above_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3543 | 0.5942 | 1.8621 | 0.0054 | 0.2609 | ok | RAN |
| SOLUSDT | 4 | `wma235_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.2599 | 0.5879 | 1.3945 | 0.0041 | 0.2613 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma235_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma235_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma235_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma235_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma235_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma235_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
