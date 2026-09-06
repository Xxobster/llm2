# Autonomy public-indicator hunt gen 1341

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T001028Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret235_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.3007 | 0.7160 | 4.8581 | 0.0284 | 0.3905 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret235_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 2.1272 | 0.6994 | 4.3030 | 0.0262 | 0.3926 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret235_neg_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.9802 | 0.6762 | 4.1987 | 0.0142 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret235_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.8681 | 0.6508 | 3.5860 | 0.0132 | 0.3386 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret235_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5329 | 0.6193 | 2.3943 | 0.0082 | 0.2841 | ok | RAN |
| ETHUSDT | 8 | `ret235_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2229 | 0.5989 | 1.1430 | 0.0080 | 0.2246 | ok | RAN |
| ETHUSDT | 4 | `ret235_pos_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.1875 | 0.5897 | 1.0027 | 0.0068 | 0.2308 | ok | RAN |
| SOLUSDT | 4 | `ret235_pos_at_h` | one_head_filter_pi_star | 171 | 13.9434 | 1.4210 | 0.6023 | 1.9139 | 0.0066 | 0.2690 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret235_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret235_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret235_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret235_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret235_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret235_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret235_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret235_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret235_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret235_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret235_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret235_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret235_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret235_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret235_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret235_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
