# Autonomy public-indicator hunt gen 202

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T224331Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret10_cross_down_0` | one_head_filter_pi_star | 26 | 2.2247 | 1.9418 | 0.6923 | 1.3595 | 0.0287 | 0.2308 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret10_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7855 | 0.6757 | 3.7904 | 0.0202 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret10_neg_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.7697 | 0.6771 | 3.7664 | 0.0201 | 0.3812 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret10_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2453 | 0.6933 | 4.1637 | 0.0184 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret10_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1540 | 0.6890 | 3.9650 | 0.0175 | 0.4146 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret10_cross_down_0` | one_head_filter_pi_star | 36 | 3.0493 | 2.3286 | 0.6944 | 1.9423 | 0.0147 | 0.0556 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret10_cross_up_0` | one_head_filter_pi_star | 17 | 1.4933 | 1.5239 | 0.6471 | 0.7413 | 0.0122 | 0.1765 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret10_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2143 | 0.5938 | 0.9885 | 0.0069 | 0.2062 | ok | RAN |
| ETHUSDT | 4 | `ret10_pos_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.2080 | 0.5886 | 0.9727 | 0.0066 | 0.1962 | ok | RAN |
| SOLUSDT | 4 | `ret10_pos_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3858 | 0.5935 | 2.0807 | 0.0057 | 0.2477 | ok | RAN |
| SOLUSDT | 8 | `ret10_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3731 | 0.5972 | 2.0299 | 0.0056 | 0.2454 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret10_cross_down_0` | one_head_filter_pi_star | 12 | 1.0832 | 0.9115 | 0.5833 | -0.1425 | -0.0054 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret10_cross_up_0` | one_head_filter_pi_star | 17 | 1.3989 | 0.8912 | 0.5294 | -0.2025 | -0.0054 | 0.1176 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret10_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.7748 | 0.3500 | -0.4429 | -0.0226 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret10_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret10_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret10_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret10_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret10_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret10_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret10_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret10_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret10_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret10_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
