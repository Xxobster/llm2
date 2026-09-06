# Autonomy public-indicator hunt gen 418

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T062658Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret272_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 2.2341 | 0.7125 | 4.4328 | 0.0273 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret272_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 2.1379 | 0.7143 | 4.3378 | 0.0254 | 0.4099 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret272_neg_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.9542 | 0.6802 | 3.6865 | 0.0139 | 0.3488 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret272_neg_at_h` | one_head_filter_pi_star | 165 | 13.5815 | 1.8565 | 0.6727 | 3.2628 | 0.0134 | 0.3394 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret272_pos_at_h` | one_head_filter_pi_star | 185 | 15.1709 | 1.6933 | 0.6324 | 2.9585 | 0.0098 | 0.2811 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret272_pos_at_h` | one_head_filter_pi_star | 167 | 13.6948 | 1.6496 | 0.6228 | 2.6886 | 0.0096 | 0.2814 | ok | RAN |
| ETHUSDT | 4 | `ret272_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2605 | 0.5968 | 1.2959 | 0.0088 | 0.2204 | ok | RAN |
| ETHUSDT | 8 | `ret272_pos_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 1.2009 | 0.5894 | 0.9423 | 0.0071 | 0.2318 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret272_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6154 | 0.3500 | -0.7982 | -0.0383 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret272_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0393 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret272_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret272_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
