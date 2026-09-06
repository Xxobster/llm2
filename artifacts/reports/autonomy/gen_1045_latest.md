# Autonomy public-indicator hunt gen 1045

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T160043Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret186_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 2.0890 | 0.6941 | 4.4434 | 0.0263 | 0.3882 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret186_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.1199 | 0.7024 | 4.5155 | 0.0255 | 0.3810 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret186_neg_at_h` | one_head_filter_pi_star | 157 | 12.8380 | 2.1312 | 0.6688 | 3.8654 | 0.0165 | 0.3694 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret186_neg_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.0653 | 0.6744 | 3.9506 | 0.0156 | 0.3721 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret186_pos_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2342 | 0.5949 | 1.2304 | 0.0080 | 0.2308 | ok | RAN |
| SOLUSDT | 8 | `ret186_pos_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.5247 | 0.6154 | 2.4776 | 0.0079 | 0.2667 | ok | RAN |
| SOLUSDT | 4 | `ret186_pos_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.4508 | 0.6041 | 2.2110 | 0.0072 | 0.2741 | ok | RAN |
| ETHUSDT | 8 | `ret186_pos_at_h` | one_head_filter_pi_star | 200 | 16.5043 | 1.1987 | 0.5950 | 1.0411 | 0.0067 | 0.2200 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret186_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret186_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret186_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret186_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret186_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret186_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret186_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret186_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret186_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret186_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret186_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret186_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret186_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret186_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret186_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret186_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
