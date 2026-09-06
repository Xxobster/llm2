# Autonomy public-indicator hunt gen 2069

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T180204Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret339_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.2430 | 0.5988 | 1.2930 | 0.0074 | 0.2036 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret339_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.2299 | 0.6059 | 1.2418 | 0.0068 | 0.1941 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret339_pos_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.1464 | 0.5548 | 0.7131 | 0.0027 | 0.1097 | ok | RAN |
| SOLUSDT | 4 | `ret339_pos_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 1.1404 | 0.5686 | 0.6844 | 0.0025 | 0.1176 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret339_neg_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9492 | 0.5678 | -0.3176 | -0.0010 | 0.1457 | ok | RAN |
| SOLUSDT | 4 | `ret339_neg_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9383 | 0.5628 | -0.3949 | -0.0013 | 0.1508 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret339_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.7661 | 0.5272 | -1.4522 | -0.0098 | 0.0978 | ok | RAN |
| ETHUSDT | 8 | `ret339_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 0.7363 | 0.5196 | -1.6416 | -0.0115 | 0.1061 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret339_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret339_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0683 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret339_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret339_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret339_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret339_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret339_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret339_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret339_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret339_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret339_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret339_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret339_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret339_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret339_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret339_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
