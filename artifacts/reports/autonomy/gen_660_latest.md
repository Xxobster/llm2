# Autonomy public-indicator hunt gen 660

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T042415Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema585_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.2633 | 0.7056 | 4.7221 | 0.0256 | 0.4167 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema585_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.0196 | 0.6818 | 4.2959 | 0.0230 | 0.3788 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema585_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 1.8829 | 0.6605 | 3.8790 | 0.0131 | 0.3302 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema585_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.8543 | 0.6553 | 3.6941 | 0.0129 | 0.3252 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema585_above_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.6266 | 0.6190 | 2.6613 | 0.0097 | 0.3036 | ok | RAN |
| ETHUSDT | 8 | `ema585_above_at_h` | one_head_filter_pi_star | 139 | 11.4705 | 1.2726 | 0.6259 | 1.2319 | 0.0095 | 0.2014 | ok | RAN |
| SOLUSDT | 8 | `ema585_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.5139 | 0.6071 | 2.1313 | 0.0084 | 0.3000 | ok | RAN |
| ETHUSDT | 4 | `ema585_above_at_h` | one_head_filter_pi_star | 151 | 12.4607 | 1.2293 | 0.5960 | 1.0546 | 0.0083 | 0.1921 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema585_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema585_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema585_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema585_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
