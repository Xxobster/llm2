# Autonomy public-indicator hunt gen 2285

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T225244Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret370_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.1972 | 0.5868 | 1.0765 | 0.0059 | 0.1976 | ok | RAN |
| ETHUSDT | 4 | `ret370_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.1910 | 0.5864 | 1.0060 | 0.0056 | 0.1790 | ok | RAN |
| SOLUSDT | 8 | `ret370_pos_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.0901 | 0.5417 | 0.4776 | 0.0018 | 0.1012 | ok | RAN |
| SOLUSDT | 4 | `ret370_pos_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.0864 | 0.5643 | 0.4210 | 0.0017 | 0.1214 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret370_neg_at_h` | one_head_filter_pi_star | 172 | 14.1577 | 0.9322 | 0.5465 | -0.4079 | -0.0015 | 0.1570 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret370_neg_at_h` | one_head_filter_pi_star | 184 | 15.1454 | 0.9128 | 0.5543 | -0.5400 | -0.0019 | 0.1467 | ok | RAN |
| ETHUSDT | 4 | `ret370_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.9241 | 0.5598 | -0.4520 | -0.0032 | 0.0978 | ok | RAN |
| ETHUSDT | 8 | `ret370_pos_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 0.8145 | 0.5492 | -1.1152 | -0.0079 | 0.0933 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret370_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6493 | 0.2632 | -0.7123 | -0.0360 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret370_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0625 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret370_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret370_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret370_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret370_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret370_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret370_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret370_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret370_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret370_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret370_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret370_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret370_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret370_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret370_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
