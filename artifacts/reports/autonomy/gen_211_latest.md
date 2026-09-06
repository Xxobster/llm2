# Autonomy public-indicator hunt gen 211

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T231750Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma42_cross_up` | one_head_filter_pi_star | 15 | 1.5311 | 16.3670 | 0.8000 | 3.4124 | 0.0646 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma42_cross_up` | one_head_filter_pi_star | 20 | 2.0242 | 1.9597 | 0.6000 | 1.3982 | 0.0280 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma42_cross_down` | one_head_filter_pi_star | 29 | 2.4031 | 1.7435 | 0.5862 | 1.2111 | 0.0261 | 0.2414 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma42_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8298 | 0.6833 | 3.9573 | 0.0216 | 0.3710 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma42_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.8274 | 0.6773 | 3.9435 | 0.0213 | 0.3773 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma42_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2271 | 0.6909 | 4.2080 | 0.0184 | 0.4121 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma42_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1738 | 0.6957 | 4.0361 | 0.0178 | 0.4224 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma42_cross_down` | one_head_filter_pi_star | 25 | 2.1337 | 1.5957 | 0.6400 | 0.9353 | 0.0138 | 0.1600 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma42_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2074 | 0.5975 | 0.9578 | 0.0063 | 0.2075 | ok | RAN |
| ETHUSDT | 8 | `sma42_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.1941 | 0.5987 | 0.8992 | 0.0060 | 0.1975 | ok | RAN |
| SOLUSDT | 4 | `sma42_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3242 | 0.5935 | 1.7733 | 0.0048 | 0.2477 | ok | RAN |
| SOLUSDT | 8 | `sma42_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3176 | 0.5849 | 1.7358 | 0.0047 | 0.2453 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma42_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma42_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma42_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma42_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `sma42_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma42_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma42_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma42_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma42_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma42_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma42_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma42_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
