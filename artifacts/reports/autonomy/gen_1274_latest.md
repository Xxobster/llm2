# Autonomy public-indicator hunt gen 1274

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T174449Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1128_pos_at_h` | one_head_filter_pi_star | 18 | 1.9811 | 2.5288 | 0.6667 | 1.8479 | 0.0191 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1128_neg_at_h` | one_head_filter_pi_star | 323 | 26.2767 | 1.6580 | 0.6502 | 3.8459 | 0.0166 | 0.3096 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1128_neg_at_h` | one_head_filter_pi_star | 312 | 25.3818 | 1.6060 | 0.6442 | 3.5307 | 0.0158 | 0.3141 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1128_neg_at_h` | one_head_filter_pi_star | 308 | 25.0564 | 1.6969 | 0.6266 | 3.9029 | 0.0112 | 0.3214 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1128_neg_at_h` | one_head_filter_pi_star | 319 | 25.9513 | 1.6990 | 0.6301 | 3.8797 | 0.0107 | 0.3197 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1128_pos_at_h` | one_head_filter_pi_star | 40 | 3.6272 | 0.9078 | 0.5250 | -0.2611 | -0.0041 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1128_pos_at_h` | one_head_filter_pi_star | 44 | 3.9325 | 0.7497 | 0.5000 | -0.8070 | -0.0135 | 0.2045 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1128_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0512 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1128_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1128_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret1128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1128_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1128_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1128_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1128_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
