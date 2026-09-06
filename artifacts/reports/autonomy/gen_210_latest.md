# Autonomy public-indicator hunt gen 210

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T231358Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret7_neg_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8028 | 0.6787 | 3.8436 | 0.0207 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret7_cross_up_0` | one_head_filter_pi_star | 165 | 13.4922 | 2.2740 | 0.7091 | 4.3281 | 0.0190 | 0.4121 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret7_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.2422 | 0.6914 | 4.1533 | 0.0184 | 0.4259 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret7_cross_up_0` | one_head_filter_pi_star | 213 | 17.4002 | 1.6365 | 0.6620 | 3.1533 | 0.0177 | 0.3662 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret7_pos_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2001 | 0.5926 | 0.9329 | 0.0065 | 0.2037 | ok | RAN |
| SOLUSDT | 4 | `ret7_pos_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3851 | 0.5991 | 2.0812 | 0.0057 | 0.2442 | ok | RAN |
| SOLUSDT | 8 | `ret7_cross_down_0` | one_head_filter_pi_star | 213 | 17.3681 | 1.3799 | 0.5962 | 2.0084 | 0.0055 | 0.2394 | ok | RAN |
| ETHUSDT | 8 | `ret7_cross_down_0` | one_head_filter_pi_star | 161 | 13.2859 | 1.1644 | 0.5901 | 0.7792 | 0.0052 | 0.1801 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret7_cross_down_0` | one_head_filter_pi_star | 20 | 1.7020 | 0.7748 | 0.3500 | -0.4429 | -0.0226 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret7_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret7_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ret7_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret7_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret7_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret7_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret7_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret7_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret7_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret7_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret7_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret7_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret7_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret7_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret7_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
