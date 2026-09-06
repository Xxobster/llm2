# Autonomy public-indicator hunt gen 140

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T184032Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema80_cross_up` | one_head_filter_pi_star | 12 | 1.0883 | 5.9897 | 0.7500 | 2.2813 | 0.0353 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema80_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9698 | 0.6990 | 4.4922 | 0.0237 | 0.3724 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema80_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.8747 | 0.6850 | 4.1733 | 0.0215 | 0.3650 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema80_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2682 | 0.6946 | 4.3218 | 0.0186 | 0.4012 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema80_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2191 | 0.6928 | 4.1567 | 0.0182 | 0.4036 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema80_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2945 | 0.6099 | 1.3782 | 0.0094 | 0.2198 | ok | RAN |
| ETHUSDT | 8 | `ema80_above_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 1.2071 | 0.5989 | 1.0110 | 0.0068 | 0.2198 | ok | RAN |
| SOLUSDT | 4 | `ema80_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3276 | 0.5915 | 1.7461 | 0.0049 | 0.2535 | ok | RAN |
| SOLUSDT | 8 | `ema80_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3154 | 0.5902 | 1.6558 | 0.0048 | 0.2634 | ok | RAN |
| ETHUSDT | 8 | `ema80_cross_down` | one_head_filter_pi_star | 20 | 1.8653 | 1.0319 | 0.5000 | 0.0651 | 0.0016 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema80_cross_up` | one_head_filter_pi_star | 14 | 1.2149 | 0.7787 | 0.5000 | -0.4235 | -0.0109 | 0.4286 | EBR>35% | RAN |
| BTCUSDT | 4 | `ema80_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema80_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema80_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema80_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
