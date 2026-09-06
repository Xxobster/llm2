# Autonomy public-indicator hunt gen 410

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T043212Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret264_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.2525 | 0.7152 | 4.7574 | 0.0270 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret264_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.0248 | 0.6923 | 4.2522 | 0.0244 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret264_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 1.9776 | 0.6807 | 3.6964 | 0.0146 | 0.3675 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret264_neg_at_h` | one_head_filter_pi_star | 162 | 13.3346 | 1.8750 | 0.6728 | 3.5132 | 0.0140 | 0.3642 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret264_pos_at_h` | one_head_filter_pi_star | 183 | 15.0069 | 1.6711 | 0.6339 | 2.8500 | 0.0101 | 0.2842 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret264_pos_at_h` | one_head_filter_pi_star | 171 | 14.0228 | 1.5797 | 0.6199 | 2.5124 | 0.0089 | 0.2807 | ok | RAN |
| ETHUSDT | 4 | `ret264_pos_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 1.2425 | 0.6069 | 1.1908 | 0.0083 | 0.2254 | ok | RAN |
| ETHUSDT | 8 | `ret264_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 1.1959 | 0.6000 | 0.9836 | 0.0066 | 0.2114 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret264_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0408 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret264_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret264_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret264_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
