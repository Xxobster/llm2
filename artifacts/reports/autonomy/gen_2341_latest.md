# Autonomy public-indicator hunt gen 2341

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T055750Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret378_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.2283 | 0.5954 | 1.2405 | 0.0065 | 0.1734 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret378_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.2074 | 0.5828 | 1.0778 | 0.0060 | 0.1840 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret378_pos_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.0716 | 0.5342 | 0.3556 | 0.0014 | 0.0959 | ok | RAN |
| SOLUSDT | 8 | `ret378_pos_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.0495 | 0.5419 | 0.2570 | 0.0010 | 0.0968 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret378_neg_at_h` | one_head_filter_pi_star | 186 | 15.3101 | 0.9534 | 0.5591 | -0.2886 | -0.0010 | 0.1505 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret378_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 0.8962 | 0.5372 | -0.6614 | -0.0023 | 0.1436 | ok | RAN |
| ETHUSDT | 8 | `ret378_pos_at_h` | one_head_filter_pi_star | 210 | 17.2617 | 0.8073 | 0.5381 | -1.2542 | -0.0081 | 0.1048 | ok | RAN |
| ETHUSDT | 4 | `ret378_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.7947 | 0.5288 | -1.3189 | -0.0091 | 0.1047 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret378_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4039 | 0.2105 | -1.4311 | -0.0721 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret378_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0726 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret378_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret378_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret378_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret378_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret378_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret378_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret378_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret378_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret378_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret378_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret378_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret378_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret378_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret378_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
