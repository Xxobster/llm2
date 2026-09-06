# Autonomy public-indicator hunt gen 643

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T031652Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma376_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.1055 | 0.7053 | 4.7457 | 0.0246 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma376_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9159 | 0.6935 | 4.1875 | 0.0224 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma376_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.9796 | 0.6703 | 3.8601 | 0.0144 | 0.3622 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma376_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.8489 | 0.6686 | 3.4250 | 0.0130 | 0.3663 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma376_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2323 | 0.5969 | 1.2034 | 0.0081 | 0.2199 | ok | RAN |
| SOLUSDT | 4 | `sma376_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.5006 | 0.5989 | 2.3361 | 0.0080 | 0.2857 | ok | RAN |
| SOLUSDT | 8 | `sma376_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.4715 | 0.6056 | 2.1793 | 0.0075 | 0.2667 | ok | RAN |
| ETHUSDT | 8 | `sma376_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.1745 | 0.5867 | 0.9590 | 0.0062 | 0.2245 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma376_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma376_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma376_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma376_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma376_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma376_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma376_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma376_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma376_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma376_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma376_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma376_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma376_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma376_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma376_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma376_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
