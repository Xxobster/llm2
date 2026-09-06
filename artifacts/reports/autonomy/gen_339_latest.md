# Autonomy public-indicator hunt gen 339

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T130003Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma124_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9540 | 0.6888 | 4.3845 | 0.0230 | 0.3776 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma124_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.8743 | 0.6842 | 4.0826 | 0.0213 | 0.3737 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma124_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.2228 | 0.6914 | 4.1702 | 0.0175 | 0.3951 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma124_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.1400 | 0.6833 | 4.1662 | 0.0166 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma124_above_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 1.3038 | 0.6145 | 1.4649 | 0.0097 | 0.2123 | ok | RAN |
| ETHUSDT | 4 | `sma124_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2093 | 0.6010 | 1.1045 | 0.0071 | 0.2228 | ok | RAN |
| SOLUSDT | 4 | `sma124_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.3311 | 0.5990 | 1.7334 | 0.0052 | 0.2741 | ok | RAN |
| SOLUSDT | 8 | `sma124_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.2911 | 0.5902 | 1.5482 | 0.0046 | 0.2732 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma124_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma124_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma124_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma124_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma124_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma124_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma124_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma124_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma124_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma124_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma124_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma124_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma124_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma124_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma124_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma124_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
