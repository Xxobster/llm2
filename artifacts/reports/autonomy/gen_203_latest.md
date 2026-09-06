# Autonomy public-indicator hunt gen 203

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T224755Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma38_cross_up` | one_head_filter_pi_star | 12 | 1.2249 | 19.4994 | 0.8333 | 3.1075 | 0.0628 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma38_cross_up` | one_head_filter_pi_star | 19 | 1.9230 | 1.8034 | 0.5789 | 1.1951 | 0.0297 | 0.2105 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma38_cross_down` | one_head_filter_pi_star | 26 | 2.2191 | 2.2862 | 0.6538 | 1.6432 | 0.0229 | 0.1538 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma38_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.8251 | 0.6774 | 3.9270 | 0.0213 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma38_cross_down` | one_head_filter_pi_star | 27 | 2.2374 | 1.6736 | 0.5926 | 1.0898 | 0.0212 | 0.2593 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma38_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.7943 | 0.6773 | 3.8322 | 0.0207 | 0.3773 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma38_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2768 | 0.6988 | 4.3234 | 0.0190 | 0.4157 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma38_below_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.1318 | 0.6899 | 3.8971 | 0.0173 | 0.4304 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma38_above_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.2393 | 0.6012 | 1.0878 | 0.0074 | 0.2147 | ok | RAN |
| ETHUSDT | 8 | `sma38_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2050 | 0.5938 | 0.9560 | 0.0064 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `sma38_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3233 | 0.5896 | 1.7639 | 0.0048 | 0.2453 | ok | RAN |
| SOLUSDT | 4 | `sma38_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3123 | 0.5877 | 1.7079 | 0.0046 | 0.2512 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma38_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma38_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma38_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma38_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `sma38_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma38_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma38_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma38_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma38_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma38_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma38_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma38_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
