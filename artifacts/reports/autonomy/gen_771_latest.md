# Autonomy public-indicator hunt gen 771

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T125224Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma484_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0993 | 0.6989 | 4.6375 | 0.0249 | 0.3817 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma484_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0207 | 0.6915 | 4.3636 | 0.0233 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma484_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.9271 | 0.6720 | 3.8060 | 0.0137 | 0.3495 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma484_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.7807 | 0.6557 | 3.2218 | 0.0119 | 0.3443 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma484_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.6035 | 0.6167 | 2.6560 | 0.0093 | 0.2833 | ok | RAN |
| ETHUSDT | 8 | `sma484_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.2687 | 0.6051 | 1.2465 | 0.0092 | 0.2102 | ok | RAN |
| ETHUSDT | 4 | `sma484_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.2523 | 0.5989 | 1.2830 | 0.0087 | 0.2034 | ok | RAN |
| SOLUSDT | 4 | `sma484_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5245 | 0.6054 | 2.4007 | 0.0083 | 0.2757 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma484_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma484_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma484_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma484_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma484_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma484_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
