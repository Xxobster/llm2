# Autonomy public-indicator hunt gen 2133

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T021651Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret348_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.2264 | 0.5968 | 1.2931 | 0.0067 | 0.1774 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret348_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1454 | 0.5778 | 0.8571 | 0.0044 | 0.1778 | ok | RAN |
| SOLUSDT | 8 | `ret348_pos_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.1606 | 0.5762 | 0.7817 | 0.0030 | 0.1258 | ok | RAN |
| SOLUSDT | 4 | `ret348_pos_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.1490 | 0.5576 | 0.7603 | 0.0027 | 0.1152 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret348_neg_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 0.9903 | 0.5652 | -0.0616 | -0.0002 | 0.1401 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret348_neg_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.8894 | 0.5510 | -0.7163 | -0.0024 | 0.1480 | ok | RAN |
| ETHUSDT | 8 | `ret348_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.8037 | 0.5257 | -1.1954 | -0.0081 | 0.0914 | ok | RAN |
| ETHUSDT | 4 | `ret348_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 0.7721 | 0.5424 | -1.3688 | -0.0099 | 0.0960 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret348_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0706 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret348_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0759 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret348_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret348_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret348_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret348_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret348_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret348_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret348_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret348_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret348_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret348_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret348_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret348_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret348_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret348_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
