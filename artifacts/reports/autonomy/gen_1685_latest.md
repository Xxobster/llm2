# Autonomy public-indicator hunt gen 1685

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T030350Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret284_neg_at_h` | one_head_filter_pi_star | 151 | 12.3353 | 1.2763 | 0.6159 | 1.3944 | 0.0083 | 0.2185 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret284_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.1118 | 0.5926 | 0.6575 | 0.0035 | 0.1914 | ok | RAN |
| SOLUSDT | 8 | `ret284_pos_at_h` | one_head_filter_pi_star | 179 | 14.6789 | 1.1086 | 0.5642 | 0.5838 | 0.0020 | 0.1061 | ok | RAN |
| SOLUSDT | 8 | `ret284_neg_at_h` | one_head_filter_pi_star | 144 | 11.7750 | 1.0516 | 0.5694 | 0.2681 | 0.0012 | 0.1528 | ok | RAN |
| SOLUSDT | 4 | `ret284_neg_at_h` | one_head_filter_pi_star | 154 | 12.5927 | 1.0543 | 0.5714 | 0.2776 | 0.0011 | 0.1558 | ok | RAN |
| SOLUSDT | 4 | `ret284_pos_at_h` | one_head_filter_pi_star | 190 | 15.5809 | 1.0155 | 0.5421 | 0.0885 | 0.0003 | 0.1105 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret284_pos_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 0.9047 | 0.5535 | -0.5390 | -0.0036 | 0.0943 | ok | RAN |
| ETHUSDT | 4 | `ret284_pos_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 0.8630 | 0.5519 | -0.7746 | -0.0053 | 0.0909 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret284_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5207 | 0.3158 | -1.0568 | -0.0464 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret284_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0726 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret284_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret284_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret284_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret284_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret284_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret284_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret284_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret284_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret284_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret284_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret284_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret284_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret284_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret284_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
