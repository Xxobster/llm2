# Autonomy public-indicator hunt gen 1058

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T173727Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret912_neg_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 2.0587 | 0.7073 | 4.3743 | 0.0234 | 0.3805 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret912_neg_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 1.9272 | 0.6930 | 4.1217 | 0.0208 | 0.3674 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret912_neg_at_h` | one_head_filter_pi_star | 241 | 20.0490 | 2.1464 | 0.6763 | 4.6419 | 0.0161 | 0.3278 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret912_neg_at_h` | one_head_filter_pi_star | 238 | 19.4615 | 2.0634 | 0.6807 | 4.4934 | 0.0151 | 0.3193 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret912_pos_at_h` | one_head_filter_pi_star | 74 | 6.0728 | 1.6788 | 0.6622 | 1.9323 | 0.0093 | 0.2568 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret912_pos_at_h` | one_head_filter_pi_star | 73 | 6.0672 | 1.5030 | 0.6575 | 1.5733 | 0.0080 | 0.2466 | ok | RAN |
| ETHUSDT | 8 | `ret912_pos_at_h` | one_head_filter_pi_star | 55 | 4.8367 | 1.0544 | 0.5636 | 0.1820 | 0.0028 | 0.2727 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret912_pos_at_h` | one_head_filter_pi_star | 50 | 4.3970 | 0.9766 | 0.5400 | -0.0797 | -0.0013 | 0.2800 | ok | RAN |
| BTCUSDT | 8 | `ret912_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3027 | 0.3077 | -1.4856 | -0.0534 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret912_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3828 | 0.3077 | -1.2499 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret912_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret912_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret912_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret912_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret912_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret912_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret912_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret912_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret912_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret912_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret912_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret912_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret912_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret912_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
