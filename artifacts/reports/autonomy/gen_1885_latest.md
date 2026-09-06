# Autonomy public-indicator hunt gen 1885

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T220349Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret313_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.2369 | 0.5988 | 1.2725 | 0.0071 | 0.1976 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret313_neg_at_h` | one_head_filter_pi_star | 148 | 12.0902 | 1.1450 | 0.6081 | 0.7471 | 0.0042 | 0.2027 | ok | RAN |
| SOLUSDT | 4 | `ret313_pos_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.1200 | 0.5503 | 0.5907 | 0.0023 | 0.1074 | ok | RAN |
| SOLUSDT | 8 | `ret313_pos_at_h` | one_head_filter_pi_star | 184 | 15.0889 | 1.1018 | 0.5543 | 0.5596 | 0.0020 | 0.1087 | ok | RAN |
| SOLUSDT | 8 | `ret313_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 1.0375 | 0.5602 | 0.2122 | 0.0007 | 0.1506 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret313_neg_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 0.8939 | 0.5449 | -0.6092 | -0.0024 | 0.1538 | ok | RAN |
| ETHUSDT | 4 | `ret313_pos_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 0.8838 | 0.5443 | -0.6586 | -0.0046 | 0.0886 | ok | RAN |
| ETHUSDT | 8 | `ret313_pos_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 0.8274 | 0.5370 | -1.0115 | -0.0073 | 0.0926 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret313_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5435 | 0.2941 | -0.9587 | -0.0453 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret313_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4309 | 0.2632 | -1.3328 | -0.0712 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret313_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret313_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret313_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret313_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret313_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret313_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret313_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret313_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret313_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret313_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret313_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret313_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret313_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret313_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
