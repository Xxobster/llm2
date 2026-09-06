# Autonomy public-indicator hunt gen 1917

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T005824Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret317_neg_at_h` | one_head_filter_pi_star | 155 | 12.6621 | 1.3500 | 0.6194 | 1.6971 | 0.0098 | 0.2000 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret317_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.2271 | 0.6061 | 1.2412 | 0.0067 | 0.1879 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret317_pos_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.2173 | 0.5590 | 1.0731 | 0.0037 | 0.0994 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret317_pos_at_h` | one_head_filter_pi_star | 178 | 14.5969 | 1.1398 | 0.5618 | 0.7392 | 0.0025 | 0.1067 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret317_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 0.9705 | 0.5574 | -0.1814 | -0.0006 | 0.1475 | ok | RAN |
| SOLUSDT | 4 | `ret317_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 0.9373 | 0.5455 | -0.3966 | -0.0014 | 0.1497 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret317_pos_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 0.8455 | 0.5405 | -0.8281 | -0.0065 | 0.1014 | ok | RAN |
| ETHUSDT | 4 | `ret317_pos_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 0.7606 | 0.5202 | -1.4842 | -0.0106 | 0.0925 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret317_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4039 | 0.2105 | -1.4311 | -0.0707 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret317_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0747 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret317_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret317_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret317_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret317_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret317_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret317_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret317_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret317_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret317_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret317_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret317_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret317_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret317_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret317_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
