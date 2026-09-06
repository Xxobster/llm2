# Autonomy public-indicator hunt gen 232

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T004457Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma160_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.8384 | 0.6834 | 4.0188 | 0.0210 | 0.3668 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma160_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.7162 | 0.6684 | 3.5327 | 0.0187 | 0.3684 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma160_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.3283 | 0.7029 | 4.5223 | 0.0180 | 0.3771 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma160_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.1922 | 0.6936 | 4.1625 | 0.0167 | 0.3699 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma160_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 1.2819 | 0.6075 | 1.3830 | 0.0093 | 0.2258 | ok | RAN |
| ETHUSDT | 8 | `sma160_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2595 | 0.6066 | 1.2626 | 0.0087 | 0.2295 | ok | RAN |
| SOLUSDT | 8 | `sma160_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3388 | 0.5971 | 1.7887 | 0.0053 | 0.2621 | ok | RAN |
| SOLUSDT | 4 | `sma160_above_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.3042 | 0.5882 | 1.6155 | 0.0048 | 0.2598 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma160_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma160_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
