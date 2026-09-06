# Autonomy public-indicator hunt gen 2157

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T061209Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret351_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.2709 | 0.6023 | 1.4447 | 0.0082 | 0.1988 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret351_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.1747 | 0.6000 | 0.9791 | 0.0053 | 0.1882 | ok | RAN |
| SOLUSDT | 8 | `ret351_pos_at_h` | one_head_filter_pi_star | 154 | 12.6288 | 1.2504 | 0.5714 | 1.1731 | 0.0043 | 0.1234 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret351_pos_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.2011 | 0.5652 | 0.9843 | 0.0037 | 0.1056 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret351_neg_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 0.9699 | 0.5495 | -0.1941 | -0.0007 | 0.1386 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret351_neg_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.9108 | 0.5492 | -0.5467 | -0.0019 | 0.1399 | ok | RAN |
| ETHUSDT | 8 | `ret351_pos_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 0.8591 | 0.5542 | -0.7985 | -0.0061 | 0.0964 | ok | RAN |
| ETHUSDT | 4 | `ret351_pos_at_h` | one_head_filter_pi_star | 196 | 16.0581 | 0.7978 | 0.5306 | -1.2622 | -0.0085 | 0.0969 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret351_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0692 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret351_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0736 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret351_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret351_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret351_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret351_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret351_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret351_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret351_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret351_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret351_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret351_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret351_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret351_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret351_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret351_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
