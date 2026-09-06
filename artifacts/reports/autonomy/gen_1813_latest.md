# Autonomy public-indicator hunt gen 1813

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T153531Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret302_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 1.2145 | 0.6098 | 1.1818 | 0.0066 | 0.2134 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret302_neg_at_h` | one_head_filter_pi_star | 152 | 12.4170 | 1.2176 | 0.6053 | 1.1244 | 0.0062 | 0.1974 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret302_pos_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.2032 | 0.5570 | 0.9414 | 0.0037 | 0.1141 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret302_pos_at_h` | one_head_filter_pi_star | 152 | 12.4648 | 1.1937 | 0.5592 | 0.9279 | 0.0036 | 0.1184 | ok | RAN |
| SOLUSDT | 8 | `ret302_neg_at_h` | one_head_filter_pi_star | 157 | 12.8380 | 1.1366 | 0.5796 | 0.7121 | 0.0027 | 0.1529 | ok | RAN |
| SOLUSDT | 4 | `ret302_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0389 | 0.5665 | 0.2156 | 0.0008 | 0.1503 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret302_pos_at_h` | one_head_filter_pi_star | 174 | 14.3587 | 0.8768 | 0.5460 | -0.7158 | -0.0049 | 0.0977 | ok | RAN |
| ETHUSDT | 4 | `ret302_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.7908 | 0.5189 | -1.3261 | -0.0088 | 0.0973 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret302_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0727 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret302_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0742 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret302_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret302_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret302_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret302_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret302_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret302_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret302_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret302_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret302_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret302_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret302_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret302_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret302_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret302_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
