# Autonomy public-indicator hunt gen 2493

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T002542Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret406_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.2992 | 0.6108 | 1.5504 | 0.0084 | 0.1737 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret406_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1130 | 0.5848 | 0.6396 | 0.0035 | 0.1813 | ok | RAN |
| SOLUSDT | 4 | `ret406_pos_at_h` | one_head_filter_pi_star | 143 | 11.7267 | 1.0619 | 0.5524 | 0.2988 | 0.0012 | 0.1119 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret406_pos_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 0.9998 | 0.5217 | -0.0010 | -0.0000 | 0.1087 | ok | RAN |
| SOLUSDT | 8 | `ret406_neg_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 0.9907 | 0.5556 | -0.0556 | -0.0002 | 0.1364 | ok | RAN |
| SOLUSDT | 4 | `ret406_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 0.9863 | 0.5556 | -0.0824 | -0.0003 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret406_pos_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 0.8447 | 0.5472 | -0.9060 | -0.0067 | 0.1132 | ok | RAN |
| ETHUSDT | 4 | `ret406_pos_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.8294 | 0.5400 | -0.9619 | -0.0077 | 0.1267 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret406_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret406_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0581 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret406_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret406_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret406_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret406_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret406_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret406_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret406_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret406_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret406_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret406_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret406_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret406_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret406_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret406_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
