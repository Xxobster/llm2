# Autonomy public-indicator hunt gen 2173

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T083311Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret354_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.2315 | 0.5966 | 1.2745 | 0.0069 | 0.1875 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret354_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.2167 | 0.5978 | 1.2611 | 0.0067 | 0.1902 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret354_pos_at_h` | one_head_filter_pi_star | 154 | 12.6288 | 1.2834 | 0.5974 | 1.3086 | 0.0049 | 0.1104 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret354_pos_at_h` | one_head_filter_pi_star | 162 | 13.2095 | 1.2598 | 0.5864 | 1.2540 | 0.0047 | 0.1235 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret354_neg_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 0.9190 | 0.5441 | -0.5304 | -0.0018 | 0.1422 | ok | RAN |
| SOLUSDT | 8 | `ret354_neg_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 0.9148 | 0.5500 | -0.5667 | -0.0018 | 0.1450 | ok | RAN |
| ETHUSDT | 4 | `ret354_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.7885 | 0.5405 | -1.3002 | -0.0091 | 0.0919 | ok | RAN |
| ETHUSDT | 8 | `ret354_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.7573 | 0.5316 | -1.5298 | -0.0108 | 0.0947 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret354_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0759 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret354_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0768 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret354_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret354_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret354_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret354_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret354_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret354_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret354_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret354_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret354_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret354_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret354_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret354_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret354_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret354_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
