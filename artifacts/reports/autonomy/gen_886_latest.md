# Autonomy public-indicator hunt gen 886

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T000136Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma460_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0731 | 0.7031 | 4.6202 | 0.0246 | 0.3958 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma460_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.8795 | 0.6856 | 4.1318 | 0.0214 | 0.3814 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma460_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.1831 | 0.6885 | 4.3320 | 0.0163 | 0.3716 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma460_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.9908 | 0.6739 | 3.8971 | 0.0150 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma460_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2430 | 0.6094 | 1.2844 | 0.0084 | 0.2240 | ok | RAN |
| ETHUSDT | 4 | `wma460_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2163 | 0.5990 | 1.1619 | 0.0075 | 0.2188 | ok | RAN |
| SOLUSDT | 8 | `wma460_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4771 | 0.6085 | 2.3182 | 0.0072 | 0.2593 | ok | RAN |
| SOLUSDT | 4 | `wma460_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3922 | 0.6020 | 1.9774 | 0.0063 | 0.2602 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma460_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma460_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
