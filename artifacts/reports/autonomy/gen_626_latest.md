# Autonomy public-indicator hunt gen 626

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T021104Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret480_neg_at_h` | one_head_filter_pi_star | 149 | 12.1719 | 2.2006 | 0.7047 | 4.3810 | 0.0260 | 0.4161 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret480_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.9608 | 0.6852 | 3.7927 | 0.0228 | 0.3765 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret480_neg_at_h` | one_head_filter_pi_star | 209 | 17.0026 | 1.8425 | 0.6651 | 3.6786 | 0.0127 | 0.3301 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret480_neg_at_h` | one_head_filter_pi_star | 219 | 17.8161 | 1.7074 | 0.6575 | 3.2601 | 0.0111 | 0.3242 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret480_pos_at_h` | one_head_filter_pi_star | 125 | 10.2748 | 1.2283 | 0.6000 | 1.0759 | 0.0085 | 0.2480 | ok | RAN |
| SOLUSDT | 4 | `ret480_pos_at_h` | one_head_filter_pi_star | 156 | 12.8821 | 1.5028 | 0.5962 | 2.1335 | 0.0083 | 0.2692 | ok | RAN |
| ETHUSDT | 8 | `ret480_pos_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.2066 | 0.5975 | 1.0099 | 0.0082 | 0.2453 | ok | RAN |
| SOLUSDT | 8 | `ret480_pos_at_h` | one_head_filter_pi_star | 149 | 12.2466 | 1.5001 | 0.5906 | 2.1248 | 0.0079 | 0.3087 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret480_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6020 | 0.2941 | -0.7739 | -0.0315 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret480_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret480_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret480_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
