# Autonomy public-indicator hunt gen 1122

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T013917Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret976_neg_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.8946 | 0.6806 | 3.9094 | 0.0212 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret976_neg_at_h` | one_head_filter_pi_star | 267 | 21.8115 | 1.6931 | 0.6517 | 3.8262 | 0.0173 | 0.3408 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret976_neg_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 1.9686 | 0.6553 | 4.4606 | 0.0140 | 0.3409 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret976_neg_at_h` | one_head_filter_pi_star | 273 | 22.3234 | 1.9030 | 0.6520 | 4.4866 | 0.0134 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret976_pos_at_h` | one_head_filter_pi_star | 75 | 6.2259 | 1.3179 | 0.5867 | 1.0056 | 0.0128 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `ret976_pos_at_h` | one_head_filter_pi_star | 51 | 4.1918 | 1.8410 | 0.6863 | 1.7814 | 0.0102 | 0.2745 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret976_pos_at_h` | one_head_filter_pi_star | 84 | 6.9730 | 1.0834 | 0.6071 | 0.3225 | 0.0039 | 0.1905 | ok | RAN |
| SOLUSDT | 4 | `ret976_pos_at_h` | one_head_filter_pi_star | 46 | 3.8232 | 1.0896 | 0.6087 | 0.2485 | 0.0017 | 0.2609 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret976_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4406 | 0.2857 | -1.1310 | -0.0534 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret976_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3255 | 0.2143 | -1.5000 | -0.0805 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret976_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret976_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret976_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret976_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret976_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret976_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret976_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret976_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret976_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret976_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret976_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret976_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret976_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret976_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
