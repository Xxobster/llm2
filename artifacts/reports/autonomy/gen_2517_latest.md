# Autonomy public-indicator hunt gen 2517

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T025559Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret414_neg_at_h` | one_head_filter_pi_star | 145 | 11.8452 | 1.2541 | 0.6069 | 1.2279 | 0.0071 | 0.1931 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret414_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.2131 | 0.5988 | 1.1614 | 0.0060 | 0.1802 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret414_pos_at_h` | one_head_filter_pi_star | 167 | 13.6948 | 1.1128 | 0.5389 | 0.5887 | 0.0022 | 0.1198 | ok | RAN |
| SOLUSDT | 4 | `ret414_pos_at_h` | one_head_filter_pi_star | 162 | 13.2095 | 1.1037 | 0.5432 | 0.5261 | 0.0020 | 0.1235 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret414_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 0.9942 | 0.5690 | -0.0345 | -0.0001 | 0.1437 | ok | RAN |
| SOLUSDT | 4 | `ret414_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 0.9487 | 0.5706 | -0.2778 | -0.0011 | 0.1472 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret414_pos_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 0.8393 | 0.5298 | -0.9240 | -0.0069 | 0.1131 | ok | RAN |
| ETHUSDT | 4 | `ret414_pos_at_h` | one_head_filter_pi_star | 207 | 17.0151 | 0.7847 | 0.5169 | -1.4446 | -0.0090 | 0.1208 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret414_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5653 | 0.2778 | -0.8933 | -0.0353 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret414_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4904 | 0.2778 | -1.0918 | -0.0499 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret414_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret414_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret414_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret414_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret414_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret414_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret414_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret414_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret414_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret414_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret414_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret414_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret414_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret414_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
