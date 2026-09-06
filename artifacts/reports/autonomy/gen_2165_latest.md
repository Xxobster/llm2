# Autonomy public-indicator hunt gen 2165

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T072015Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret353_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.2660 | 0.6084 | 1.3846 | 0.0080 | 0.2048 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret353_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1927 | 0.5848 | 1.0667 | 0.0061 | 0.1871 | ok | RAN |
| SOLUSDT | 8 | `ret353_pos_at_h` | one_head_filter_pi_star | 172 | 14.1048 | 1.2807 | 0.5872 | 1.3577 | 0.0048 | 0.1105 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret353_pos_at_h` | one_head_filter_pi_star | 146 | 11.9049 | 1.0302 | 0.5342 | 0.1537 | 0.0006 | 0.1301 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret353_neg_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9413 | 0.5512 | -0.3807 | -0.0013 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret353_neg_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 0.8465 | 0.5396 | -1.0190 | -0.0035 | 0.1386 | ok | RAN |
| ETHUSDT | 8 | `ret353_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.7723 | 0.5359 | -1.3954 | -0.0103 | 0.1050 | ok | RAN |
| ETHUSDT | 4 | `ret353_pos_at_h` | one_head_filter_pi_star | 187 | 15.3207 | 0.7621 | 0.5241 | -1.4615 | -0.0104 | 0.0963 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret353_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4688 | 0.2778 | -1.1839 | -0.0623 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret353_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0768 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret353_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret353_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret353_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret353_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret353_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret353_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret353_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret353_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret353_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret353_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret353_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret353_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret353_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret353_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
