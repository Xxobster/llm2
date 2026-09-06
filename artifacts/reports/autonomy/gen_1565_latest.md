# Autonomy public-indicator hunt gen 1565

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T171018Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret267_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 2.2131 | 0.7178 | 4.5092 | 0.0270 | 0.4049 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret267_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.0507 | 0.6951 | 4.2249 | 0.0242 | 0.3963 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret267_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 1.9140 | 0.6687 | 3.5500 | 0.0138 | 0.3494 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret267_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.8271 | 0.6596 | 3.4744 | 0.0125 | 0.3457 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret267_pos_at_h` | one_head_filter_pi_star | 184 | 15.0889 | 1.5992 | 0.6196 | 2.7112 | 0.0093 | 0.2880 | ok | RAN |
| ETHUSDT | 4 | `ret267_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 1.2362 | 0.6057 | 1.1513 | 0.0082 | 0.2114 | ok | RAN |
| SOLUSDT | 8 | `ret267_pos_at_h` | one_head_filter_pi_star | 188 | 15.4169 | 1.4694 | 0.6064 | 2.2131 | 0.0076 | 0.2766 | ok | RAN |
| ETHUSDT | 8 | `ret267_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.1803 | 0.5856 | 0.9224 | 0.0061 | 0.2044 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret267_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret267_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret267_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret267_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret267_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret267_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret267_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret267_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret267_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret267_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret267_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret267_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret267_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret267_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret267_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret267_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
