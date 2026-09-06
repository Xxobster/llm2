# Autonomy public-indicator hunt gen 954

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T072754Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret808_neg_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.2162 | 0.7047 | 4.4887 | 0.0245 | 0.3627 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret808_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.9341 | 0.6932 | 3.5695 | 0.0200 | 0.3693 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret808_neg_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 2.1250 | 0.6806 | 4.1923 | 0.0174 | 0.3717 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret808_neg_at_h` | one_head_filter_pi_star | 221 | 18.0714 | 2.0146 | 0.6742 | 4.1401 | 0.0161 | 0.3484 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret808_pos_at_h` | one_head_filter_pi_star | 63 | 5.1370 | 1.5526 | 0.6508 | 1.5505 | 0.0082 | 0.2698 | ok | RAN |
| ETHUSDT | 8 | `ret808_pos_at_h` | one_head_filter_pi_star | 127 | 10.4392 | 1.1776 | 0.5748 | 0.7572 | 0.0077 | 0.2362 | ok | RAN |
| SOLUSDT | 4 | `ret808_pos_at_h` | one_head_filter_pi_star | 59 | 4.8418 | 1.3204 | 0.6271 | 0.9320 | 0.0052 | 0.2203 | ok | RAN |
| ETHUSDT | 4 | `ret808_pos_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 1.1140 | 0.5682 | 0.5158 | 0.0049 | 0.2197 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret808_pos_at_h` | one_head_filter_pi_star | 11 | 2.0201 | 0.4902 | 0.2727 | -1.3134 | -0.0433 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret808_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4982 | 0.3125 | -1.0382 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret808_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret808_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret808_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret808_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret808_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret808_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret808_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret808_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret808_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret808_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret808_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret808_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret808_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret808_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
