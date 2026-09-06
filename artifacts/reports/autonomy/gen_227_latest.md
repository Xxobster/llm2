# Autonomy public-indicator hunt gen 227

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T002344Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma52_cross_up` | one_head_filter_pi_star | 19 | 1.6104 | 9.7341 | 0.7368 | 3.0304 | 0.0563 | 0.3158 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma52_cross_up` | one_head_filter_pi_star | 12 | 1.2473 | 1.8699 | 0.5833 | 1.0204 | 0.0285 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma52_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 1.8391 | 0.6791 | 3.9657 | 0.0219 | 0.3721 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma52_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.7459 | 0.6729 | 3.7110 | 0.0202 | 0.3645 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma52_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1878 | 0.6871 | 4.1667 | 0.0181 | 0.4049 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma52_below_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.0555 | 0.6772 | 3.7787 | 0.0163 | 0.4114 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma52_cross_down` | one_head_filter_pi_star | 33 | 2.8165 | 1.4529 | 0.6364 | 0.8697 | 0.0090 | 0.1515 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma52_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2591 | 0.6000 | 1.1808 | 0.0077 | 0.2125 | ok | RAN |
| ETHUSDT | 4 | `sma52_above_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.2189 | 0.5949 | 1.0106 | 0.0068 | 0.2152 | ok | RAN |
| SOLUSDT | 4 | `sma52_above_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3584 | 0.5991 | 1.9015 | 0.0053 | 0.2535 | ok | RAN |
| SOLUSDT | 8 | `sma52_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3009 | 0.5924 | 1.6554 | 0.0045 | 0.2417 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma52_cross_up` | one_head_filter_pi_star | 19 | 1.9230 | 1.0040 | 0.4737 | 0.0087 | 0.0002 | 0.1579 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma52_cross_down` | one_head_filter_pi_star | 14 | 1.2149 | 0.7853 | 0.5000 | -0.3509 | -0.0077 | 0.3571 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma52_cross_down` | one_head_filter_pi_star | 17 | 1.4752 | 0.6829 | 0.5294 | -0.7129 | -0.0119 | 0.2941 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma52_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma52_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma52_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma52_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma52_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma52_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma52_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma52_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma52_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma52_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
