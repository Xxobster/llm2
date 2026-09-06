# Autonomy public-indicator hunt gen 058

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T132110Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `rv_cross_up_p01` | one_head_filter_pi_star | 66 | 5.5416 | 5.5471 | 0.8333 | 5.1539 | 0.0751 | 0.5303 | EBR>35% | RAN |
| ETHUSDT | 4 | `rv_cross_up_p01` | one_head_filter_pi_star | 57 | 4.9069 | 3.7796 | 0.7895 | 3.9181 | 0.0655 | 0.4737 | EBR>35% | RAN |
| ETHUSDT | 4 | `rv_high_at_h` | one_head_filter_pi_star | 78 | 6.6765 | 3.8043 | 0.8077 | 4.6744 | 0.0513 | 0.5513 | EBR>35% | RAN |
| ETHUSDT | 8 | `rv_high_at_h` | one_head_filter_pi_star | 92 | 7.7235 | 3.4649 | 0.7826 | 4.7995 | 0.0484 | 0.5217 | EBR>35% | RAN |
| SOLUSDT | 4 | `rv_high_at_h` | one_head_filter_pi_star | 104 | 8.8199 | 2.9445 | 0.7500 | 4.9229 | 0.0276 | 0.6058 | EBR>35% | RAN |
| SOLUSDT | 8 | `rv_high_at_h` | one_head_filter_pi_star | 93 | 8.0865 | 2.8885 | 0.7419 | 4.6169 | 0.0260 | 0.6452 | EBR>35% | RAN |
| SOLUSDT | 4 | `rv_cross_up_p01` | one_head_filter_pi_star | 59 | 5.0036 | 2.5003 | 0.7119 | 3.0787 | 0.0258 | 0.4915 | EBR>35% | RAN |
| SOLUSDT | 8 | `rv_cross_up_p01` | one_head_filter_pi_star | 71 | 5.9614 | 2.1616 | 0.6901 | 2.8014 | 0.0204 | 0.5070 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `rv_low_at_h` | one_head_filter_pi_star | 132 | 10.7922 | 1.3462 | 0.5909 | 1.3755 | 0.0048 | 0.1364 | ok | RAN |
| SOLUSDT | 8 | `rv_low_at_h` | one_head_filter_pi_star | 105 | 8.5982 | 1.1147 | 0.5714 | 0.4529 | 0.0016 | 0.1048 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `rv_low_at_h` | one_head_filter_pi_star | 155 | 12.7523 | 0.9138 | 0.5419 | -0.4458 | -0.0029 | 0.1677 | ok | RAN |
| ETHUSDT | 8 | `rv_low_at_h` | one_head_filter_pi_star | 128 | 10.5327 | 0.7482 | 0.5156 | -1.3581 | -0.0084 | 0.1172 | ok | RAN |
| BTCUSDT | 4 | `rv_low_at_h` | one_head_filter_pi_star | 15 | 1.3765 | 0.4073 | 0.2667 | -1.2647 | -0.0492 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `rv_low_at_h` | one_head_filter_pi_star | 15 | 1.3765 | 0.4073 | 0.2667 | -1.2647 | -0.0524 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `rv_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `rv_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `rv_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `rv_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `rv_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rv_cross_up_p01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rv_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rv_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `rv_cross_up_p01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rv_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
