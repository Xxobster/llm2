# Autonomy public-indicator hunt gen 2277

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T215520Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret369_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.2086 | 0.6000 | 1.1509 | 0.0062 | 0.1943 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret369_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.1445 | 0.5818 | 0.7919 | 0.0045 | 0.1939 | ok | RAN |
| SOLUSDT | 8 | `ret369_pos_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 1.0180 | 0.5493 | 0.0912 | 0.0004 | 0.1197 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret369_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 0.9425 | 0.5580 | -0.3473 | -0.0012 | 0.1492 | ok | RAN |
| SOLUSDT | 4 | `ret369_pos_at_h` | one_head_filter_pi_star | 143 | 11.7267 | 0.9389 | 0.5315 | -0.3216 | -0.0013 | 0.1259 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret369_neg_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.9194 | 0.5436 | -0.5152 | -0.0017 | 0.1436 | ok | RAN |
| ETHUSDT | 4 | `ret369_pos_at_h` | one_head_filter_pi_star | 207 | 16.9593 | 0.8463 | 0.5411 | -0.9708 | -0.0064 | 0.0918 | ok | RAN |
| ETHUSDT | 8 | `ret369_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8017 | 0.5351 | -1.2204 | -0.0087 | 0.0973 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret369_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0583 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret369_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4688 | 0.2778 | -1.1839 | -0.0598 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret369_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret369_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret369_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret369_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret369_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret369_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret369_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret369_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret369_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret369_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret369_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret369_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret369_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret369_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
