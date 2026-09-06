# Autonomy public-indicator hunt gen 515

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T185430Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma268_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9227 | 0.6898 | 4.2618 | 0.0225 | 0.3904 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma268_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9212 | 0.6848 | 4.0865 | 0.0224 | 0.3804 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma268_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2346 | 0.6897 | 4.3302 | 0.0174 | 0.3793 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma268_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1734 | 0.6886 | 4.0923 | 0.0170 | 0.3772 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma268_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2529 | 0.6041 | 1.3146 | 0.0086 | 0.2234 | ok | RAN |
| ETHUSDT | 4 | `sma268_above_at_h` | one_head_filter_pi_star | 199 | 16.3575 | 1.2415 | 0.5980 | 1.2458 | 0.0082 | 0.2211 | ok | RAN |
| SOLUSDT | 8 | `sma268_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3712 | 0.6071 | 1.8938 | 0.0059 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `sma268_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3674 | 0.5970 | 1.8800 | 0.0058 | 0.2587 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma268_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0208 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma268_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma268_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma268_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma268_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma268_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma268_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma268_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma268_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma268_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma268_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma268_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma268_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma268_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma268_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma268_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
