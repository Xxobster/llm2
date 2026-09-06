# Autonomy public-indicator hunt gen 894

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T004946Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma465_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0212 | 0.6947 | 4.5053 | 0.0245 | 0.3947 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma465_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0403 | 0.6974 | 4.5804 | 0.0243 | 0.3846 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma465_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.2066 | 0.7000 | 4.3868 | 0.0167 | 0.3722 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma465_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1502 | 0.6882 | 4.1407 | 0.0162 | 0.3824 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma465_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2403 | 0.6073 | 1.2548 | 0.0083 | 0.2199 | ok | RAN |
| SOLUSDT | 4 | `wma465_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.4149 | 0.6031 | 2.0587 | 0.0066 | 0.2577 | ok | RAN |
| SOLUSDT | 8 | `wma465_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.4233 | 0.6022 | 2.0595 | 0.0065 | 0.2688 | ok | RAN |
| ETHUSDT | 8 | `wma465_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.1391 | 0.5928 | 0.7596 | 0.0050 | 0.2165 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma465_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma465_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma465_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma465_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
