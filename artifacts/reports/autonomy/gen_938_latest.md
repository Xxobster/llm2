# Autonomy public-indicator hunt gen 938

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T054047Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret792_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8046 | 0.6757 | 3.8647 | 0.0191 | 0.3468 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret792_neg_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.7874 | 0.6703 | 3.3458 | 0.0176 | 0.3676 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret792_neg_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.9779 | 0.6716 | 3.8970 | 0.0156 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret792_neg_at_h` | one_head_filter_pi_star | 235 | 19.2162 | 1.9488 | 0.6638 | 4.0917 | 0.0150 | 0.3404 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret792_pos_at_h` | one_head_filter_pi_star | 64 | 5.2186 | 2.0347 | 0.6562 | 2.5169 | 0.0122 | 0.2812 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret792_pos_at_h` | one_head_filter_pi_star | 60 | 4.8924 | 1.4909 | 0.6167 | 1.2440 | 0.0066 | 0.2167 | ok | RAN |
| ETHUSDT | 4 | `ret792_pos_at_h` | one_head_filter_pi_star | 136 | 11.1790 | 1.1476 | 0.5809 | 0.6610 | 0.0063 | 0.2426 | ok | RAN |
| ETHUSDT | 8 | `ret792_pos_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 1.1079 | 0.5530 | 0.4764 | 0.0045 | 0.2197 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret792_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6560 | 0.3333 | -0.6016 | -0.0258 | 0.0667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret792_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5020 | 0.3750 | -1.0196 | -0.0519 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret792_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret792_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret792_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret792_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret792_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret792_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret792_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret792_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret792_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret792_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret792_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret792_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret792_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret792_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
