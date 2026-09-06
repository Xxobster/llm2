# Autonomy public-indicator hunt gen 1077

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T200549Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret196_neg_at_h` | one_head_filter_pi_star | 159 | 12.9888 | 2.2123 | 0.7044 | 4.5652 | 0.0275 | 0.3962 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret196_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.2301 | 0.7102 | 4.9743 | 0.0270 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret196_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1030 | 0.6765 | 3.8563 | 0.0152 | 0.3706 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret196_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.9954 | 0.6685 | 3.8195 | 0.0145 | 0.3591 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret196_pos_at_h` | one_head_filter_pi_star | 181 | 14.8429 | 1.5573 | 0.6298 | 2.5281 | 0.0085 | 0.2762 | ok | RAN |
| SOLUSDT | 8 | `ret196_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.4468 | 0.6075 | 2.1507 | 0.0071 | 0.2688 | ok | RAN |
| ETHUSDT | 8 | `ret196_pos_at_h` | one_head_filter_pi_star | 194 | 16.0092 | 1.1735 | 0.5928 | 0.9020 | 0.0060 | 0.2216 | ok | RAN |
| ETHUSDT | 4 | `ret196_pos_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.1334 | 0.5787 | 0.7299 | 0.0048 | 0.2183 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret196_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret196_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret196_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret196_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret196_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret196_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret196_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret196_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret196_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret196_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret196_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret196_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret196_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret196_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret196_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret196_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
