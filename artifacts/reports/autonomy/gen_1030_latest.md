# Autonomy public-indicator hunt gen 1030

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T141822Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma550_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9657 | 0.6915 | 4.2745 | 0.0226 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma550_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.9321 | 0.6940 | 4.1420 | 0.0223 | 0.3934 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma550_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8859 | 0.6618 | 3.7844 | 0.0138 | 0.3480 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma550_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.9047 | 0.6634 | 3.8448 | 0.0134 | 0.3610 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma550_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2571 | 0.6000 | 1.3418 | 0.0087 | 0.2211 | ok | RAN |
| ETHUSDT | 4 | `wma550_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2136 | 0.5989 | 1.1314 | 0.0077 | 0.2299 | ok | RAN |
| SOLUSDT | 8 | `wma550_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4889 | 0.6054 | 2.3178 | 0.0077 | 0.2541 | ok | RAN |
| SOLUSDT | 4 | `wma550_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.4525 | 0.6066 | 2.1504 | 0.0071 | 0.2623 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma550_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma550_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma550_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma550_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma550_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma550_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma550_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma550_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma550_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma550_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma550_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma550_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma550_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma550_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma550_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma550_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
