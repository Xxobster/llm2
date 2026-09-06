# Autonomy public-indicator hunt gen 1269

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T171718Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret225_neg_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.3252 | 0.7127 | 5.0658 | 0.0291 | 0.3923 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret225_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 2.1940 | 0.7151 | 4.6856 | 0.0281 | 0.4186 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret225_neg_at_h` | one_head_filter_pi_star | 185 | 15.1429 | 1.9605 | 0.6703 | 3.8811 | 0.0138 | 0.3838 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret225_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.8347 | 0.6489 | 3.5767 | 0.0126 | 0.3670 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret225_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.6300 | 0.6392 | 2.8474 | 0.0093 | 0.2732 | ok | RAN |
| SOLUSDT | 8 | `ret225_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.5252 | 0.6237 | 2.4231 | 0.0080 | 0.2742 | ok | RAN |
| ETHUSDT | 4 | `ret225_pos_at_h` | one_head_filter_pi_star | 203 | 16.6863 | 1.1595 | 0.5862 | 0.8365 | 0.0056 | 0.2315 | ok | RAN |
| ETHUSDT | 8 | `ret225_pos_at_h` | one_head_filter_pi_star | 202 | 16.6041 | 1.1385 | 0.5842 | 0.7426 | 0.0049 | 0.2327 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret225_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret225_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret225_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret225_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret225_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret225_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret225_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret225_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret225_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret225_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret225_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret225_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret225_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret225_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret225_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret225_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
