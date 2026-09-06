# Autonomy public-indicator hunt gen 1853

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T191032Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret308_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 1.2799 | 0.6242 | 1.4408 | 0.0080 | 0.1911 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret308_neg_at_h` | one_head_filter_pi_star | 155 | 12.6621 | 1.0876 | 0.5742 | 0.4778 | 0.0027 | 0.2000 | ok | RAN |
| SOLUSDT | 4 | `ret308_pos_at_h` | one_head_filter_pi_star | 160 | 13.1208 | 1.1056 | 0.5625 | 0.5488 | 0.0021 | 0.1125 | ok | RAN |
| SOLUSDT | 8 | `ret308_pos_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.0590 | 0.5478 | 0.3073 | 0.0011 | 0.1083 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret308_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 0.9928 | 0.5556 | -0.0412 | -0.0002 | 0.1520 | ok | RAN |
| SOLUSDT | 4 | `ret308_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 0.9756 | 0.5610 | -0.1378 | -0.0005 | 0.1585 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret308_pos_at_h` | one_head_filter_pi_star | 146 | 12.0481 | 0.9305 | 0.5479 | -0.3618 | -0.0027 | 0.0822 | ok | RAN |
| ETHUSDT | 4 | `ret308_pos_at_h` | one_head_filter_pi_star | 145 | 11.9656 | 0.8635 | 0.5517 | -0.7594 | -0.0052 | 0.0828 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret308_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5403 | 0.2778 | -0.9713 | -0.0459 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret308_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5225 | 0.2500 | -1.0038 | -0.0483 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret308_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret308_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret308_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret308_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret308_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret308_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret308_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret308_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret308_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret308_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret308_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret308_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret308_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret308_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
