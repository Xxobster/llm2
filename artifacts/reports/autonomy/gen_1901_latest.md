# Autonomy public-indicator hunt gen 1901

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T233039Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret315_neg_at_h` | one_head_filter_pi_star | 153 | 12.4987 | 1.2726 | 0.6144 | 1.3570 | 0.0079 | 0.1895 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret315_neg_at_h` | one_head_filter_pi_star | 152 | 12.4170 | 1.1588 | 0.5987 | 0.8397 | 0.0048 | 0.1974 | ok | RAN |
| SOLUSDT | 8 | `ret315_pos_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.2284 | 0.5638 | 1.0535 | 0.0042 | 0.1208 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret315_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.1248 | 0.5508 | 0.6720 | 0.0023 | 0.1123 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret315_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 0.9901 | 0.5690 | -0.0579 | -0.0002 | 0.1552 | ok | RAN |
| SOLUSDT | 8 | `ret315_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 0.9635 | 0.5569 | -0.2131 | -0.0008 | 0.1437 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret315_pos_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 0.8327 | 0.5506 | -0.9749 | -0.0069 | 0.0823 | ok | RAN |
| ETHUSDT | 8 | `ret315_pos_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 0.7858 | 0.5380 | -1.3055 | -0.0096 | 0.0994 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret315_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0715 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret315_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0783 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret315_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret315_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret315_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret315_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret315_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret315_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret315_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret315_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret315_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret315_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret315_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret315_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret315_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret315_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
