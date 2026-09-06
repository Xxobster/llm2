# Autonomy public-indicator hunt gen 195

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T221417Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma32_cross_up` | one_head_filter_pi_star | 21 | 1.7337 | 2.8156 | 0.7143 | 1.9599 | 0.0504 | 0.1905 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma32_cross_up` | one_head_filter_pi_star | 15 | 1.2824 | 10.8458 | 0.7333 | 2.6159 | 0.0492 | 0.2667 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma32_cross_down` | one_head_filter_pi_star | 24 | 2.8637 | 1.7862 | 0.6250 | 1.3914 | 0.0238 | 0.2083 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma32_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.8441 | 0.6818 | 3.9628 | 0.0214 | 0.3773 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma32_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.7923 | 0.6787 | 3.8100 | 0.0206 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma32_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2313 | 0.6970 | 4.1812 | 0.0184 | 0.4242 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma32_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.1289 | 0.6875 | 3.8998 | 0.0172 | 0.4125 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma32_cross_down` | one_head_filter_pi_star | 22 | 2.1219 | 2.2943 | 0.6818 | 1.5313 | 0.0154 | 0.0909 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma32_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1890 | 0.5901 | 0.8787 | 0.0060 | 0.2050 | ok | RAN |
| ETHUSDT | 4 | `sma32_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1898 | 0.5901 | 0.9154 | 0.0060 | 0.1988 | ok | RAN |
| SOLUSDT | 8 | `sma32_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3641 | 0.5972 | 1.9668 | 0.0054 | 0.2407 | ok | RAN |
| SOLUSDT | 4 | `sma32_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3489 | 0.5915 | 1.8972 | 0.0052 | 0.2394 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma32_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma32_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma32_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma32_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
