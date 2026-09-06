# Autonomy public-indicator hunt gen 1322

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T222410Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1176_neg_at_h` | one_head_filter_pi_star | 303 | 24.6496 | 1.6737 | 0.6502 | 3.7769 | 0.0167 | 0.3201 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret1176_neg_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 1.5673 | 0.6431 | 3.5659 | 0.0150 | 0.3108 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1176_neg_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.6498 | 0.6280 | 3.8667 | 0.0107 | 0.3333 | ok | RAN |
| SOLUSDT | 8 | `ret1176_neg_at_h` | one_head_filter_pi_star | 353 | 28.7172 | 1.6641 | 0.6346 | 4.0179 | 0.0103 | 0.3201 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret1176_pos_at_h` | one_head_filter_pi_star | 56 | 5.4980 | 1.0530 | 0.5179 | 0.1770 | 0.0025 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1176_pos_at_h` | one_head_filter_pi_star | 51 | 5.0071 | 0.9786 | 0.5294 | -0.0704 | -0.0011 | 0.2157 | ok | RAN |
| BTCUSDT | 4 | `ret1176_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3159 | 0.2353 | -1.5894 | -0.0674 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1176_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3159 | 0.2353 | -1.5894 | -0.0699 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1176_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret1176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1176_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret1176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1176_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1176_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
