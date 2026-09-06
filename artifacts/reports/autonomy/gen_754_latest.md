# Autonomy public-indicator hunt gen 754

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T110617Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret608_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.2565 | 0.7166 | 4.7900 | 0.0255 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret608_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0925 | 0.7120 | 4.4221 | 0.0234 | 0.3696 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret608_neg_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.7916 | 0.6493 | 3.6194 | 0.0132 | 0.3270 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret608_neg_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.8335 | 0.6612 | 3.9741 | 0.0131 | 0.3099 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret608_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.2381 | 0.5754 | 1.1901 | 0.0090 | 0.2291 | ok | RAN |
| SOLUSDT | 4 | `ret608_pos_at_h` | one_head_filter_pi_star | 128 | 10.6385 | 1.6110 | 0.6406 | 2.1483 | 0.0087 | 0.2812 | ok | RAN |
| ETHUSDT | 4 | `ret608_pos_at_h` | one_head_filter_pi_star | 183 | 14.9930 | 1.1833 | 0.5792 | 0.9398 | 0.0077 | 0.2404 | ok | RAN |
| SOLUSDT | 8 | `ret608_pos_at_h` | one_head_filter_pi_star | 130 | 10.6849 | 1.4817 | 0.6077 | 1.9009 | 0.0074 | 0.2692 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret608_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5942 | 0.2500 | -0.7892 | -0.0369 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret608_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5541 | 0.2632 | -0.9865 | -0.0497 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret608_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret608_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
