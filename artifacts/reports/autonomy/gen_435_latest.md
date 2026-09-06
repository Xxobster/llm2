# Autonomy public-indicator hunt gen 435

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T104011Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma202_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.1168 | 0.7056 | 4.7222 | 0.0248 | 0.3778 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma202_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0349 | 0.7065 | 4.5923 | 0.0245 | 0.3859 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma202_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2607 | 0.6970 | 4.2214 | 0.0175 | 0.3818 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma202_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.1896 | 0.6932 | 4.2703 | 0.0168 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma202_above_at_h` | one_head_filter_pi_star | 192 | 15.8441 | 1.2250 | 0.5938 | 1.1605 | 0.0079 | 0.2292 | ok | RAN |
| ETHUSDT | 4 | `sma202_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.1832 | 0.5918 | 0.9370 | 0.0064 | 0.2245 | ok | RAN |
| SOLUSDT | 4 | `sma202_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3487 | 0.5922 | 1.8249 | 0.0055 | 0.2573 | ok | RAN |
| SOLUSDT | 8 | `sma202_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3331 | 0.5920 | 1.7417 | 0.0053 | 0.2637 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma202_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma202_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma202_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma202_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma202_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma202_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma202_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma202_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma202_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma202_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma202_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma202_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma202_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma202_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma202_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma202_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
