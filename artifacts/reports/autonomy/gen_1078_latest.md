# Autonomy public-indicator hunt gen 1078

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T201401Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma580_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0070 | 0.7016 | 4.4961 | 0.0231 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma580_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8186 | 0.6736 | 3.8362 | 0.0203 | 0.3679 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma580_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8486 | 0.6667 | 3.5936 | 0.0129 | 0.3538 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma580_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.8657 | 0.6617 | 3.6857 | 0.0129 | 0.3383 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma580_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.5634 | 0.6170 | 2.6448 | 0.0088 | 0.2660 | ok | RAN |
| SOLUSDT | 4 | `wma580_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.5574 | 0.6223 | 2.6158 | 0.0085 | 0.2606 | ok | RAN |
| ETHUSDT | 8 | `wma580_above_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.2199 | 0.6010 | 1.1823 | 0.0076 | 0.2172 | ok | RAN |
| ETHUSDT | 4 | `wma580_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.1787 | 0.5922 | 0.9467 | 0.0066 | 0.2235 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma580_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma580_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
