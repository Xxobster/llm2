# Autonomy public-indicator hunt gen 2117

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T002222Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret346_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.2808 | 0.6036 | 1.4746 | 0.0080 | 0.1834 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret346_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.2710 | 0.5989 | 1.4808 | 0.0079 | 0.1921 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret346_pos_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.0522 | 0.5497 | 0.2673 | 0.0010 | 0.0993 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret346_pos_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.0004 | 0.5362 | 0.0020 | 0.0000 | 0.1232 | ok | RAN |
| SOLUSDT | 4 | `ret346_neg_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.9429 | 0.5590 | -0.3638 | -0.0012 | 0.1538 | ok | RAN |
| SOLUSDT | 8 | `ret346_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 0.9343 | 0.5484 | -0.4121 | -0.0014 | 0.1559 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret346_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.7877 | 0.5410 | -1.3018 | -0.0090 | 0.0929 | ok | RAN |
| ETHUSDT | 4 | `ret346_pos_at_h` | one_head_filter_pi_star | 175 | 14.3376 | 0.7719 | 0.5429 | -1.4168 | -0.0100 | 0.0914 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret346_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0706 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret346_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0783 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret346_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret346_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret346_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret346_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret346_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret346_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret346_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret346_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret346_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret346_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret346_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret346_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret346_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret346_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
