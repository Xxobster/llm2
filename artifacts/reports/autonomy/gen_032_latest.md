# Autonomy public-indicator hunt gen 032

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T113854Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `st_dn_at_h` | one_head_filter_pi_star | 211 | 17.2368 | 1.7995 | 0.6730 | 3.8086 | 0.0211 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 8 | `st_dn_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 1.7542 | 0.6744 | 3.6703 | 0.0201 | 0.3767 | EBR>35% | RAN |
| ETHUSDT | 8 | `st_flip_down` | one_head_filter_pi_star | 20 | 1.7113 | 1.8319 | 0.6500 | 1.1124 | 0.0197 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `st_dn_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2866 | 0.7076 | 4.3915 | 0.0190 | 0.4211 | EBR>35% | RAN |
| SOLUSDT | 8 | `st_dn_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2391 | 0.6946 | 4.2201 | 0.0185 | 0.4251 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `st_flip_up` | one_head_filter_pi_star | 16 | 1.6048 | 1.8120 | 0.6875 | 1.0622 | 0.0124 | 0.1250 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `st_up_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.3027 | 0.6266 | 1.3244 | 0.0090 | 0.2152 | ok | RAN |
| ETHUSDT | 8 | `st_up_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2868 | 0.6164 | 1.2751 | 0.0086 | 0.2138 | ok | RAN |
| SOLUSDT | 4 | `st_up_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3511 | 0.5990 | 1.8595 | 0.0051 | 0.2415 | ok | RAN |
| SOLUSDT | 8 | `st_up_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3335 | 0.5952 | 1.7987 | 0.0049 | 0.2429 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `st_flip_up` | one_head_filter_pi_star | 14 | 1.3022 | 0.8259 | 0.2857 | -0.3091 | -0.0097 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `st_up_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `st_up_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `st_flip_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `st_flip_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `st_flip_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `st_flip_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `st_flip_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `st_dn_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `st_flip_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `st_flip_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `st_dn_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `st_flip_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `st_flip_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
