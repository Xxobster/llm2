# Autonomy public-indicator hunt gen 2237

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T170836Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret363_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.3035 | 0.6092 | 1.5954 | 0.0087 | 0.1839 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret363_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.2619 | 0.6033 | 1.4637 | 0.0077 | 0.1848 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret363_pos_at_h` | one_head_filter_pi_star | 161 | 13.1280 | 1.1945 | 0.5652 | 0.9507 | 0.0035 | 0.1180 | ok | RAN |
| SOLUSDT | 4 | `ret363_pos_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.1277 | 0.5491 | 0.6614 | 0.0023 | 0.1040 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret363_neg_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 0.9525 | 0.5650 | -0.2996 | -0.0010 | 0.1500 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret363_neg_at_h` | one_head_filter_pi_star | 188 | 15.6399 | 0.8942 | 0.5479 | -0.6524 | -0.0023 | 0.1489 | ok | RAN |
| ETHUSDT | 8 | `ret363_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.8282 | 0.5543 | -0.9952 | -0.0070 | 0.0971 | ok | RAN |
| ETHUSDT | 4 | `ret363_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.7842 | 0.5185 | -1.3413 | -0.0093 | 0.1005 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret363_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0613 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret363_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0726 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret363_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret363_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret363_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret363_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret363_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret363_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret363_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret363_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret363_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret363_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret363_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret363_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret363_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret363_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
