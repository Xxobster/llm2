# Autonomy public-indicator hunt gen 1861

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T195248Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret309_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.2848 | 0.6012 | 1.4127 | 0.0077 | 0.2025 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret309_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.2368 | 0.5988 | 1.2861 | 0.0068 | 0.1977 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret309_pos_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.0690 | 0.5470 | 0.3723 | 0.0013 | 0.1050 | ok | RAN |
| SOLUSDT | 8 | `ret309_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.0339 | 0.5628 | 0.1989 | 0.0007 | 0.1475 | ok | RAN |
| SOLUSDT | 4 | `ret309_pos_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.0231 | 0.5287 | 0.1220 | 0.0005 | 0.1146 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret309_neg_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 0.9692 | 0.5500 | -0.1750 | -0.0007 | 0.1437 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret309_pos_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 0.8212 | 0.5361 | -1.0423 | -0.0079 | 0.1024 | ok | RAN |
| ETHUSDT | 4 | `ret309_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 0.7861 | 0.5287 | -1.3263 | -0.0092 | 0.0977 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret309_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0692 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret309_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret309_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret309_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret309_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret309_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret309_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret309_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret309_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret309_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret309_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret309_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret309_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret309_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret309_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret309_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
