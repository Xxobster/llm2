# Autonomy public-indicator hunt gen 1989

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T075233Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret327_neg_at_h` | one_head_filter_pi_star | 149 | 12.1719 | 1.3152 | 0.6107 | 1.5469 | 0.0088 | 0.2013 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret327_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.2299 | 0.5989 | 1.3029 | 0.0070 | 0.1921 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret327_pos_at_h` | one_head_filter_pi_star | 165 | 13.4542 | 1.1928 | 0.5576 | 0.9306 | 0.0034 | 0.1152 | ok | RAN |
| SOLUSDT | 8 | `ret327_pos_at_h` | one_head_filter_pi_star | 190 | 15.5809 | 1.1631 | 0.5632 | 0.8762 | 0.0029 | 0.1053 | ok | RAN |
| SOLUSDT | 8 | `ret327_neg_at_h` | one_head_filter_pi_star | 184 | 14.9688 | 1.0676 | 0.5707 | 0.3874 | 0.0014 | 0.1576 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret327_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 0.9434 | 0.5439 | -0.3337 | -0.0013 | 0.1520 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret327_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 0.8323 | 0.5475 | -0.9947 | -0.0067 | 0.1061 | ok | RAN |
| ETHUSDT | 4 | `ret327_pos_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 0.7614 | 0.5375 | -1.4089 | -0.0105 | 0.1125 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret327_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0596 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret327_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0720 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret327_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret327_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret327_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret327_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret327_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret327_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret327_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret327_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret327_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret327_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret327_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret327_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret327_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret327_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
