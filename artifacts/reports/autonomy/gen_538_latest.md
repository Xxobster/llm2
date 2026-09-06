# Autonomy public-indicator hunt gen 538

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T202812Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret392_neg_at_h` | one_head_filter_pi_star | 156 | 12.7438 | 2.6836 | 0.7500 | 5.2485 | 0.0329 | 0.4231 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret392_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.2287 | 0.7052 | 4.4899 | 0.0263 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret392_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.7803 | 0.6630 | 3.3312 | 0.0120 | 0.3533 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret392_neg_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.7925 | 0.6701 | 3.4127 | 0.0120 | 0.3144 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret392_pos_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.6324 | 0.6345 | 2.4750 | 0.0098 | 0.2897 | ok | RAN |
| SOLUSDT | 4 | `ret392_pos_at_h` | one_head_filter_pi_star | 117 | 9.5946 | 1.5847 | 0.6410 | 2.0576 | 0.0091 | 0.2821 | ok | RAN |
| ETHUSDT | 8 | `ret392_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.2415 | 0.6163 | 1.1795 | 0.0087 | 0.2267 | ok | RAN |
| ETHUSDT | 4 | `ret392_pos_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.2091 | 0.6014 | 0.9835 | 0.0077 | 0.2391 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret392_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5883 | 0.3500 | -0.8891 | -0.0407 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret392_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5883 | 0.3500 | -0.8891 | -0.0422 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret392_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret392_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
