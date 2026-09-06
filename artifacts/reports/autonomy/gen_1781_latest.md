# Autonomy public-indicator hunt gen 1781

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T124013Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret298_neg_at_h` | one_head_filter_pi_star | 151 | 12.3353 | 1.3698 | 0.6291 | 1.7015 | 0.0098 | 0.1921 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret298_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.1311 | 0.6023 | 0.7754 | 0.0043 | 0.1932 | ok | RAN |
| SOLUSDT | 8 | `ret298_pos_at_h` | one_head_filter_pi_star | 163 | 13.3668 | 1.2071 | 0.5644 | 1.0241 | 0.0036 | 0.1104 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret298_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.1398 | 0.5862 | 0.7340 | 0.0027 | 0.1437 | ok | RAN |
| SOLUSDT | 4 | `ret298_pos_at_h` | one_head_filter_pi_star | 163 | 13.2911 | 1.1414 | 0.5644 | 0.7118 | 0.0026 | 0.1043 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret298_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 0.9603 | 0.5488 | -0.2208 | -0.0009 | 0.1524 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret298_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8720 | 0.5372 | -0.7601 | -0.0049 | 0.1011 | ok | RAN |
| ETHUSDT | 4 | `ret298_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 0.8639 | 0.5437 | -0.7848 | -0.0051 | 0.0938 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret298_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0727 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret298_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0747 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret298_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret298_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret298_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret298_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret298_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret298_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret298_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret298_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret298_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret298_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret298_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret298_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret298_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret298_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
