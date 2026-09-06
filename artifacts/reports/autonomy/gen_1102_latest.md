# Autonomy public-indicator hunt gen 1102

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T232103Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma595_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0160 | 0.6882 | 4.4189 | 0.0235 | 0.3817 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma595_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.8087 | 0.6823 | 3.8504 | 0.0205 | 0.3802 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma595_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.9519 | 0.6736 | 3.8849 | 0.0140 | 0.3472 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma595_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8673 | 0.6649 | 3.6543 | 0.0132 | 0.3508 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma595_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2687 | 0.6000 | 1.4259 | 0.0091 | 0.2205 | ok | RAN |
| SOLUSDT | 8 | `wma595_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.5471 | 0.6114 | 2.5917 | 0.0083 | 0.2591 | ok | RAN |
| ETHUSDT | 8 | `wma595_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2432 | 0.6032 | 1.2922 | 0.0082 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `wma595_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.4824 | 0.6126 | 2.3092 | 0.0076 | 0.2565 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma595_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma595_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma595_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma595_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
