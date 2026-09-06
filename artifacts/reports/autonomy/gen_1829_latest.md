# Autonomy public-indicator hunt gen 1829

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T170155Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret305_neg_at_h` | one_head_filter_pi_star | 148 | 12.0902 | 1.3316 | 0.6216 | 1.6100 | 0.0098 | 0.2027 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret305_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 1.2115 | 0.5987 | 1.0885 | 0.0063 | 0.1847 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret305_pos_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.1155 | 0.5479 | 0.5582 | 0.0022 | 0.1027 | ok | RAN |
| SOLUSDT | 4 | `ret305_pos_at_h` | one_head_filter_pi_star | 164 | 13.4488 | 1.0285 | 0.5305 | 0.1564 | 0.0006 | 0.1037 | ok | RAN |
| SOLUSDT | 4 | `ret305_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.0236 | 0.5657 | 0.1333 | 0.0005 | 0.1543 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret305_neg_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 0.9909 | 0.5528 | -0.0513 | -0.0002 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret305_pos_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 0.8824 | 0.5638 | -0.6437 | -0.0045 | 0.0940 | ok | RAN |
| ETHUSDT | 8 | `ret305_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 0.8064 | 0.5330 | -1.1836 | -0.0079 | 0.1044 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret305_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0678 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret305_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4309 | 0.2632 | -1.3328 | -0.0697 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret305_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret305_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret305_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret305_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret305_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret305_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret305_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret305_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret305_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret305_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret305_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret305_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret305_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret305_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
