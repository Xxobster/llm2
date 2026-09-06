# Autonomy public-indicator hunt gen 514

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T185002Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret368_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.3206 | 0.7169 | 4.7291 | 0.0280 | 0.3916 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret368_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.2714 | 0.7091 | 4.6043 | 0.0273 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret368_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.7274 | 0.6562 | 3.1835 | 0.0118 | 0.3385 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret368_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.6919 | 0.6596 | 3.0508 | 0.0109 | 0.3298 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret368_pos_at_h` | one_head_filter_pi_star | 165 | 13.4542 | 1.6809 | 0.6242 | 2.8032 | 0.0108 | 0.2848 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret368_pos_at_h` | one_head_filter_pi_star | 180 | 14.7609 | 1.6941 | 0.6222 | 2.9459 | 0.0108 | 0.2722 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret368_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2175 | 0.6011 | 1.0951 | 0.0081 | 0.2128 | ok | RAN |
| ETHUSDT | 4 | `ret368_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.0810 | 0.5862 | 0.4333 | 0.0033 | 0.2471 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret368_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret368_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0625 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret368_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret368_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
