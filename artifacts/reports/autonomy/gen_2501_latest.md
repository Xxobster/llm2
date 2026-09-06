# Autonomy public-indicator hunt gen 2501

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T011546Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret410_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.2907 | 0.6114 | 1.5458 | 0.0085 | 0.1829 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret410_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.1438 | 0.5988 | 0.7788 | 0.0045 | 0.1790 | ok | RAN |
| SOLUSDT | 4 | `ret410_pos_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.0928 | 0.5316 | 0.4771 | 0.0018 | 0.1203 | ok | RAN |
| SOLUSDT | 8 | `ret410_pos_at_h` | one_head_filter_pi_star | 168 | 13.7768 | 1.0780 | 0.5417 | 0.4140 | 0.0016 | 0.1131 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret410_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 0.9395 | 0.5740 | -0.3452 | -0.0012 | 0.1479 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret410_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 0.9027 | 0.5491 | -0.5763 | -0.0022 | 0.1387 | ok | RAN |
| ETHUSDT | 8 | `ret410_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.8020 | 0.5314 | -1.2211 | -0.0087 | 0.1143 | ok | RAN |
| ETHUSDT | 4 | `ret410_pos_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 0.7999 | 0.5342 | -1.2143 | -0.0089 | 0.1180 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret410_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4688 | 0.2778 | -1.1839 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret410_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0683 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret410_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret410_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret410_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret410_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret410_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret410_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret410_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret410_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret410_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret410_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret410_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret410_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret410_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret410_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
