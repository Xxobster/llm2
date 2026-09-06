# Autonomy public-indicator hunt gen 2525

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T034506Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret418_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 1.3135 | 0.6242 | 1.5731 | 0.0087 | 0.1911 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret418_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1854 | 0.5989 | 1.0731 | 0.0056 | 0.1758 | ok | RAN |
| SOLUSDT | 4 | `ret418_pos_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.0788 | 0.5304 | 0.4304 | 0.0015 | 0.1381 | ok | RAN |
| SOLUSDT | 8 | `ret418_pos_at_h` | one_head_filter_pi_star | 152 | 12.4648 | 1.0451 | 0.5263 | 0.2322 | 0.0009 | 0.1382 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret418_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 0.9212 | 0.5482 | -0.4516 | -0.0017 | 0.1506 | ok | RAN |
| SOLUSDT | 4 | `ret418_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 0.8550 | 0.5444 | -0.8685 | -0.0032 | 0.1420 | ok | RAN |
| ETHUSDT | 8 | `ret418_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.8136 | 0.5314 | -1.1276 | -0.0083 | 0.1200 | ok | RAN |
| ETHUSDT | 4 | `ret418_pos_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 0.8094 | 0.5389 | -1.1431 | -0.0083 | 0.1198 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret418_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret418_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4688 | 0.2778 | -1.1839 | -0.0565 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret418_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret418_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret418_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret418_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret418_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret418_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret418_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret418_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret418_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret418_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret418_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret418_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret418_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret418_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
