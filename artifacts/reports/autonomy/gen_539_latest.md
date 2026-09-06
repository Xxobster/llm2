# Autonomy public-indicator hunt gen 539

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T203208Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma292_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9391 | 0.6931 | 4.2984 | 0.0228 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma292_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.8670 | 0.6825 | 4.0875 | 0.0219 | 0.3810 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma292_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1132 | 0.6805 | 4.0587 | 0.0164 | 0.3787 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma292_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.0452 | 0.6784 | 3.8963 | 0.0154 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma292_above_at_h` | one_head_filter_pi_star | 201 | 16.5219 | 1.2786 | 0.6070 | 1.4432 | 0.0094 | 0.2289 | ok | RAN |
| ETHUSDT | 8 | `sma292_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2458 | 0.5979 | 1.2783 | 0.0086 | 0.2268 | ok | RAN |
| SOLUSDT | 4 | `sma292_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3810 | 0.6030 | 1.9271 | 0.0059 | 0.2563 | ok | RAN |
| SOLUSDT | 8 | `sma292_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3274 | 0.5959 | 1.6969 | 0.0052 | 0.2539 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma292_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma292_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma292_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma292_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma292_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma292_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma292_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma292_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma292_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma292_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma292_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma292_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma292_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma292_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma292_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma292_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
