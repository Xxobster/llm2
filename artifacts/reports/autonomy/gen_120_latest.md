# Autonomy public-indicator hunt gen 120

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T172149Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma40_cross_up` | one_head_filter_pi_star | 14 | 1.3803 | 13.2397 | 0.7857 | 3.0732 | 0.0537 | 0.3571 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma40_cross_down` | one_head_filter_pi_star | 22 | 1.9198 | 1.8374 | 0.6364 | 1.1872 | 0.0271 | 0.2727 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma40_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.8621 | 0.6852 | 4.0346 | 0.0218 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma40_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8147 | 0.6771 | 3.9706 | 0.0211 | 0.3767 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma40_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2674 | 0.6994 | 4.2789 | 0.0190 | 0.4294 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma40_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.2178 | 0.6914 | 4.1562 | 0.0184 | 0.4136 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma40_cross_down` | one_head_filter_pi_star | 26 | 2.2191 | 1.8509 | 0.6538 | 1.2323 | 0.0163 | 0.1923 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma40_cross_up` | one_head_filter_pi_star | 12 | 1.2145 | 1.2725 | 0.5000 | 0.4061 | 0.0112 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma40_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2303 | 0.6025 | 1.0436 | 0.0071 | 0.2112 | ok | RAN |
| ETHUSDT | 8 | `sma40_above_at_h` | one_head_filter_pi_star | 153 | 12.6258 | 1.1999 | 0.6078 | 0.9106 | 0.0062 | 0.2026 | ok | RAN |
| SOLUSDT | 8 | `sma40_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3348 | 0.5915 | 1.8249 | 0.0050 | 0.2488 | ok | RAN |
| SOLUSDT | 4 | `sma40_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3268 | 0.5924 | 1.7749 | 0.0048 | 0.2464 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma40_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma40_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma40_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma40_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
