# Autonomy public-indicator hunt gen 722

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T084632Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret576_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.1758 | 0.7191 | 4.5103 | 0.0250 | 0.3820 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret576_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.9466 | 0.6923 | 3.9370 | 0.0213 | 0.3669 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret576_neg_at_h` | one_head_filter_pi_star | 226 | 18.4802 | 1.8498 | 0.6593 | 3.8915 | 0.0131 | 0.3186 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret576_neg_at_h` | one_head_filter_pi_star | 216 | 17.6878 | 1.7487 | 0.6574 | 3.4135 | 0.0121 | 0.3102 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret576_pos_at_h` | one_head_filter_pi_star | 133 | 11.0540 | 1.5386 | 0.6241 | 2.0556 | 0.0082 | 0.3158 | ok | RAN |
| ETHUSDT | 4 | `ret576_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2118 | 0.5860 | 1.0930 | 0.0079 | 0.2419 | ok | RAN |
| ETHUSDT | 8 | `ret576_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.1691 | 0.5722 | 0.9536 | 0.0066 | 0.2353 | ok | RAN |
| SOLUSDT | 4 | `ret576_pos_at_h` | one_head_filter_pi_star | 133 | 10.9315 | 1.4146 | 0.5789 | 1.7499 | 0.0065 | 0.2857 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret576_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4075 | 0.2500 | -1.2442 | -0.0506 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret576_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0596 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret576_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret576_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret576_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret576_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret576_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret576_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret576_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret576_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret576_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret576_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret576_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret576_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret576_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret576_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
