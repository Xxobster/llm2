# Autonomy public-indicator hunt gen 558

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T214613Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma255_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1098 | 0.7074 | 4.7350 | 0.0249 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma255_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0042 | 0.6984 | 4.4885 | 0.0232 | 0.3704 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma255_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2123 | 0.6977 | 4.2211 | 0.0175 | 0.3837 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma255_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1968 | 0.6871 | 4.0991 | 0.0173 | 0.3926 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma255_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2564 | 0.6091 | 1.3090 | 0.0087 | 0.2284 | ok | RAN |
| ETHUSDT | 8 | `wma255_above_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.1763 | 0.5904 | 0.8932 | 0.0064 | 0.2287 | ok | RAN |
| SOLUSDT | 8 | `wma255_above_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.3523 | 0.5931 | 1.8353 | 0.0054 | 0.2647 | ok | RAN |
| SOLUSDT | 4 | `wma255_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.2734 | 0.5871 | 1.4595 | 0.0043 | 0.2587 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma255_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma255_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma255_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma255_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
