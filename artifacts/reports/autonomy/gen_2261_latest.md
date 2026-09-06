# Autonomy public-indicator hunt gen 2261

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T195852Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret366_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.2040 | 0.5920 | 1.1320 | 0.0061 | 0.1839 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret366_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.2058 | 0.5917 | 1.1026 | 0.0059 | 0.1893 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret366_pos_at_h` | one_head_filter_pi_star | 142 | 11.5787 | 1.0571 | 0.5423 | 0.2837 | 0.0011 | 0.1056 | ok | RAN |
| SOLUSDT | 4 | `ret366_pos_at_h` | one_head_filter_pi_star | 146 | 11.9049 | 1.0127 | 0.5342 | 0.0654 | 0.0003 | 0.1164 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret366_neg_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.9689 | 0.5641 | -0.1868 | -0.0007 | 0.1385 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret366_neg_at_h` | one_head_filter_pi_star | 178 | 14.6516 | 0.9129 | 0.5506 | -0.5474 | -0.0020 | 0.1461 | ok | RAN |
| ETHUSDT | 8 | `ret366_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.8416 | 0.5506 | -0.9174 | -0.0066 | 0.1011 | ok | RAN |
| ETHUSDT | 4 | `ret366_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.7823 | 0.5397 | -1.3279 | -0.0095 | 0.0952 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret366_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret366_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0589 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret366_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret366_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret366_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret366_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret366_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret366_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret366_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret366_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret366_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret366_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret366_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret366_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret366_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret366_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
