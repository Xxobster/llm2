# Autonomy public-indicator hunt gen 043

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T122105Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `hull_above_at_h` | one_head_filter_pi_star | 175 | 14.2983 | 2.0207 | 0.7143 | 4.2349 | 0.0239 | 0.3657 | EBR>35% | RAN |
| ETHUSDT | 4 | `hull_cross_up` | one_head_filter_pi_star | 210 | 17.1551 | 1.7864 | 0.6762 | 3.7133 | 0.0201 | 0.3619 | EBR>35% | RAN |
| ETHUSDT | 8 | `hull_above_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.7514 | 0.6743 | 3.6030 | 0.0196 | 0.3670 | EBR>35% | RAN |
| SOLUSDT | 4 | `hull_cross_up` | one_head_filter_pi_star | 150 | 12.2656 | 2.2720 | 0.7133 | 4.0251 | 0.0184 | 0.4333 | EBR>35% | RAN |
| SOLUSDT | 8 | `hull_above_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1535 | 0.6871 | 3.9629 | 0.0176 | 0.4172 | EBR>35% | RAN |
| ETHUSDT | 8 | `hull_cross_up` | one_head_filter_pi_star | 258 | 21.0762 | 1.5919 | 0.6512 | 3.2844 | 0.0163 | 0.3411 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `hull_above_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.0314 | 0.6981 | 3.7361 | 0.0152 | 0.3836 | EBR>35% | RAN |
| SOLUSDT | 8 | `hull_cross_up` | one_head_filter_pi_star | 228 | 18.6438 | 1.8990 | 0.6667 | 4.0423 | 0.0131 | 0.3377 | GATE_CAND | RAN |
| ETHUSDT | 8 | `hull_cross_down` | one_head_filter_pi_star | 238 | 19.4898 | 1.3698 | 0.6134 | 1.9715 | 0.0110 | 0.2143 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `hull_below_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.5393 | 0.6073 | 2.6946 | 0.0083 | 0.2565 | ok | RAN |
| SOLUSDT | 8 | `hull_cross_down` | one_head_filter_pi_star | 258 | 21.0374 | 1.4728 | 0.6202 | 2.6614 | 0.0070 | 0.2558 | ok | RAN |
| ETHUSDT | 8 | `hull_below_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| SOLUSDT | 4 | `hull_cross_down` | one_head_filter_pi_star | 211 | 17.2050 | 1.4208 | 0.6019 | 2.2143 | 0.0062 | 0.2417 | ok | RAN |
| SOLUSDT | 8 | `hull_below_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.4009 | 0.5943 | 2.1286 | 0.0059 | 0.2594 | ok | RAN |
| ETHUSDT | 4 | `hull_below_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.1196 | 0.5783 | 0.6127 | 0.0041 | 0.2108 | ok | RAN |
| ETHUSDT | 4 | `hull_cross_down` | one_head_filter_pi_star | 146 | 12.0481 | 1.1176 | 0.5753 | 0.5681 | 0.0037 | 0.1781 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `hull_cross_down` | one_head_filter_pi_star | 23 | 1.9572 | 0.9136 | 0.3913 | -0.1715 | -0.0081 | 0.0870 | TPM<MIN | RAN |
| BTCUSDT | 4 | `hull_below_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6456 | 0.3333 | -0.7081 | -0.0370 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `hull_cross_down` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `hull_below_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `hull_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `hull_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `hull_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `hull_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
