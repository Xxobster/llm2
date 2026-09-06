# Autonomy public-indicator hunt gen 1677

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T014401Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret283_neg_at_h` | one_head_filter_pi_star | 158 | 12.9072 | 1.2041 | 0.6076 | 1.0427 | 0.0060 | 0.1899 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret283_pos_at_h` | one_head_filter_pi_star | 175 | 14.3509 | 1.2158 | 0.5886 | 1.0760 | 0.0036 | 0.1029 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret283_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.1007 | 0.5868 | 0.5905 | 0.0032 | 0.1856 | ok | RAN |
| SOLUSDT | 4 | `ret283_neg_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 1.0981 | 0.5696 | 0.5331 | 0.0021 | 0.1582 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret283_pos_at_h` | one_head_filter_pi_star | 181 | 14.8429 | 0.9997 | 0.5414 | -0.0017 | -0.0000 | 0.1160 | ok | RAN |
| SOLUSDT | 8 | `ret283_neg_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 0.9968 | 0.5581 | -0.0184 | -0.0001 | 0.1453 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret283_pos_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 0.9110 | 0.5590 | -0.5011 | -0.0034 | 0.0932 | ok | RAN |
| ETHUSDT | 8 | `ret283_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8366 | 0.5410 | -1.0088 | -0.0064 | 0.0929 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret283_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5504 | 0.3333 | -0.9442 | -0.0428 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret283_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret283_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret283_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret283_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret283_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret283_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret283_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret283_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret283_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret283_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret283_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret283_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret283_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret283_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret283_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
