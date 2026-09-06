# Autonomy public-indicator hunt gen 530

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T195556Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret384_neg_at_h` | one_head_filter_pi_star | 148 | 12.0902 | 2.3049 | 0.7162 | 4.2505 | 0.0273 | 0.4189 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret384_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 2.0307 | 0.7019 | 3.9154 | 0.0229 | 0.3913 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret384_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.6895 | 0.6575 | 2.9597 | 0.0115 | 0.3481 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret384_neg_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.6403 | 0.6535 | 3.0526 | 0.0108 | 0.3317 | ok | RAN |
| SOLUSDT | 8 | `ret384_pos_at_h` | one_head_filter_pi_star | 163 | 13.3668 | 1.6859 | 0.6258 | 2.8327 | 0.0102 | 0.2883 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret384_pos_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.5507 | 0.6115 | 2.3171 | 0.0089 | 0.2930 | ok | RAN |
| ETHUSDT | 8 | `ret384_pos_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.1526 | 0.5907 | 0.8287 | 0.0059 | 0.2383 | ok | RAN |
| ETHUSDT | 4 | `ret384_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.1162 | 0.5810 | 0.6180 | 0.0045 | 0.2235 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret384_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.7059 | 0.3158 | -0.5806 | -0.0239 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret384_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0432 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret384_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret384_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
