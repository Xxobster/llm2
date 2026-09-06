# Autonomy public-indicator hunt gen 890

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T002524Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret744_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.0978 | 0.7048 | 3.9883 | 0.0222 | 0.3675 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret744_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 2.0766 | 0.7006 | 3.9626 | 0.0220 | 0.4013 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret744_neg_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 2.0693 | 0.6806 | 3.9261 | 0.0161 | 0.3508 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret744_pos_at_h` | one_head_filter_pi_star | 78 | 6.4110 | 2.2057 | 0.6923 | 2.9759 | 0.0143 | 0.3205 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret744_neg_at_h` | one_head_filter_pi_star | 230 | 18.8073 | 1.8669 | 0.6652 | 3.6736 | 0.0139 | 0.3217 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret744_pos_at_h` | one_head_filter_pi_star | 79 | 6.4417 | 1.5625 | 0.6329 | 1.7336 | 0.0080 | 0.2785 | ok | RAN |
| ETHUSDT | 4 | `ret744_pos_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.1303 | 0.5614 | 0.6649 | 0.0055 | 0.2456 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret744_pos_at_h` | one_head_filter_pi_star | 123 | 10.1104 | 0.9848 | 0.5610 | -0.0710 | -0.0007 | 0.2439 | ok | RAN |
| BTCUSDT | 8 | `ret744_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4677 | 0.2353 | -1.1523 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret744_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3413 | 0.2308 | -1.4046 | -0.0785 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret744_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret744_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret744_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret744_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret744_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret744_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret744_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret744_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret744_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret744_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret744_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret744_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret744_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret744_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
