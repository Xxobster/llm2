# Autonomy public-indicator hunt gen 2365

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T090128Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret381_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.2193 | 0.5843 | 1.1738 | 0.0062 | 0.1867 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret381_neg_at_h` | one_head_filter_pi_star | 150 | 12.2536 | 1.1765 | 0.6000 | 0.9082 | 0.0054 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `ret381_pos_at_h` | one_head_filter_pi_star | 169 | 13.7803 | 1.1149 | 0.5503 | 0.5988 | 0.0022 | 0.1006 | ok | RAN |
| SOLUSDT | 4 | `ret381_pos_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.0102 | 0.5232 | 0.0535 | 0.0002 | 0.0993 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret381_neg_at_h` | one_head_filter_pi_star | 189 | 15.3755 | 0.9641 | 0.5556 | -0.2212 | -0.0008 | 0.1481 | ok | RAN |
| SOLUSDT | 8 | `ret381_neg_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9518 | 0.5423 | -0.3017 | -0.0010 | 0.1343 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret381_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 0.8472 | 0.5412 | -0.9533 | -0.0065 | 0.1134 | ok | RAN |
| ETHUSDT | 4 | `ret381_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 0.8418 | 0.5495 | -0.9930 | -0.0069 | 0.1209 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret381_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0683 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret381_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0720 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret381_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret381_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret381_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret381_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret381_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret381_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret381_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret381_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret381_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret381_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret381_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret381_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret381_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret381_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
