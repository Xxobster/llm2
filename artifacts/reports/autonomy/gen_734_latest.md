# Autonomy public-indicator hunt gen 734

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T093828Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma365_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0723 | 0.7017 | 4.5216 | 0.0241 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma365_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.8839 | 0.6878 | 4.1549 | 0.0216 | 0.3862 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma365_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2100 | 0.6919 | 4.2410 | 0.0170 | 0.3779 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma365_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1434 | 0.6882 | 4.0400 | 0.0160 | 0.3647 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma365_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2750 | 0.6085 | 1.4251 | 0.0094 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `wma365_above_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.2350 | 0.5959 | 1.2381 | 0.0082 | 0.2176 | ok | RAN |
| SOLUSDT | 8 | `wma365_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3711 | 0.5990 | 1.9161 | 0.0057 | 0.2574 | ok | RAN |
| SOLUSDT | 4 | `wma365_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3115 | 0.5909 | 1.6144 | 0.0049 | 0.2626 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma365_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma365_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma365_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma365_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
