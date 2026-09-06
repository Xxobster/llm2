# Autonomy public-indicator hunt gen 922

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T035324Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret776_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.2518 | 0.7166 | 4.5872 | 0.0247 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret776_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.2073 | 0.7110 | 4.3882 | 0.0237 | 0.3757 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret776_neg_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 2.1706 | 0.6821 | 4.3114 | 0.0174 | 0.3436 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret776_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.0145 | 0.6649 | 3.6902 | 0.0149 | 0.3457 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret776_pos_at_h` | one_head_filter_pi_star | 66 | 5.3817 | 1.6101 | 0.6364 | 1.6684 | 0.0076 | 0.2273 | ok | RAN |
| SOLUSDT | 4 | `ret776_pos_at_h` | one_head_filter_pi_star | 39 | 3.2055 | 1.3918 | 0.5897 | 0.8424 | 0.0061 | 0.2564 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret776_pos_at_h` | one_head_filter_pi_star | 127 | 10.4392 | 1.1062 | 0.5669 | 0.4606 | 0.0045 | 0.2205 | ok | RAN |
| ETHUSDT | 4 | `ret776_pos_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 1.0858 | 0.5597 | 0.3920 | 0.0036 | 0.2388 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret776_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.6743 | 0.3077 | -0.5655 | -0.0261 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret776_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret776_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret776_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret776_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret776_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret776_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret776_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret776_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret776_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret776_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret776_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret776_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret776_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret776_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret776_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
