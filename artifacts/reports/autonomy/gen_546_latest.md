# Autonomy public-indicator hunt gen 546

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T205943Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret400_neg_at_h` | one_head_filter_pi_star | 152 | 12.4170 | 2.4984 | 0.7368 | 4.7384 | 0.0296 | 0.3947 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret400_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.0874 | 0.7006 | 4.4832 | 0.0249 | 0.3729 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret400_neg_at_h` | one_head_filter_pi_star | 194 | 15.7823 | 1.8562 | 0.6701 | 3.5697 | 0.0124 | 0.3351 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret400_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.7083 | 0.6561 | 3.1090 | 0.0117 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret400_pos_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.6700 | 0.6211 | 2.7798 | 0.0102 | 0.3043 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret400_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.2109 | 0.5899 | 1.0778 | 0.0074 | 0.2135 | ok | RAN |
| SOLUSDT | 8 | `ret400_pos_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.4508 | 0.6210 | 1.7797 | 0.0073 | 0.2823 | ok | RAN |
| ETHUSDT | 4 | `ret400_pos_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.1721 | 0.5949 | 0.9337 | 0.0060 | 0.2256 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret400_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5824 | 0.3158 | -0.9020 | -0.0420 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret400_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0445 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret400_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret400_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
