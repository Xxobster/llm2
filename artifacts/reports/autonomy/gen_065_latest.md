# Autonomy public-indicator hunt gen 065

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T134849Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `racc_neg_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 2.0008 | 0.5000 | 1.0407 | 0.0618 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 4 | `racc_neg_at_h` | one_head_filter_pi_star | 13 | 1.3947 | 1.6046 | 0.4615 | 0.7793 | 0.0337 | 0.0769 | TPM<MIN | RAN |
| ETHUSDT | 4 | `racc_pos_at_h` | one_head_filter_pi_star | 161 | 13.0977 | 1.8070 | 0.6584 | 3.2334 | 0.0210 | 0.2981 | GATE_CAND | RAN |
| ETHUSDT | 8 | `racc_pos_at_h` | one_head_filter_pi_star | 177 | 14.4945 | 1.6470 | 0.6554 | 2.8362 | 0.0189 | 0.3390 | GATE_CAND | RAN |
| ETHUSDT | 4 | `racc_cross_down_0` | one_head_filter_pi_star | 375 | 30.5070 | 1.5719 | 0.6453 | 3.6827 | 0.0160 | 0.2987 | GATE_CAND | RAN |
| ETHUSDT | 4 | `racc_cross_up_0` | one_head_filter_pi_star | 379 | 30.8324 | 1.5787 | 0.6438 | 3.7822 | 0.0158 | 0.3061 | GATE_CAND | RAN |
| ETHUSDT | 8 | `racc_cross_up_0` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 8 | `racc_cross_down_0` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `racc_pos_at_h` | one_head_filter_pi_star | 143 | 11.6932 | 1.9933 | 0.6643 | 3.5621 | 0.0146 | 0.3706 | EBR>35% | RAN |
| SOLUSDT | 8 | `racc_pos_at_h` | one_head_filter_pi_star | 143 | 11.9204 | 1.9281 | 0.6643 | 3.5099 | 0.0143 | 0.3007 | GATE_CAND | RAN |
| ETHUSDT | 4 | `racc_neg_at_h` | one_head_filter_pi_star | 178 | 14.8592 | 1.3955 | 0.6292 | 1.9551 | 0.0130 | 0.2584 | ok | RAN |
| ETHUSDT | 8 | `racc_neg_at_h` | one_head_filter_pi_star | 183 | 15.0585 | 1.3245 | 0.6066 | 1.6075 | 0.0109 | 0.2350 | ok | RAN |
| SOLUSDT | 4 | `racc_cross_down_0` | one_head_filter_pi_star | 369 | 30.0189 | 1.7489 | 0.6423 | 4.5676 | 0.0107 | 0.3144 | GATE_CAND | RAN |
| SOLUSDT | 4 | `racc_cross_up_0` | one_head_filter_pi_star | 373 | 30.3443 | 1.7006 | 0.6434 | 4.3638 | 0.0104 | 0.3190 | GATE_CAND | RAN |
| SOLUSDT | 8 | `racc_cross_down_0` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 8 | `racc_cross_up_0` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `racc_neg_at_h` | one_head_filter_pi_star | 196 | 16.0730 | 1.4496 | 0.6071 | 2.4172 | 0.0076 | 0.2908 | ok | RAN |
| BTCUSDT | 4 | `racc_cross_up_0` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 4 | `racc_cross_down_0` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 8 | `racc_cross_up_0` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 8 | `racc_cross_down_0` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| SOLUSDT | 4 | `racc_neg_at_h` | one_head_filter_pi_star | 131 | 10.7583 | 1.3341 | 0.5954 | 1.4656 | 0.0061 | 0.2595 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `racc_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `racc_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
