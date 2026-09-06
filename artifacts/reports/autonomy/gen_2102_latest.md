# Autonomy public-indicator hunt gen 2102

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T223138Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma506_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1260 | 0.5902 | 0.7371 | 0.0039 | 0.1803 | ok | RAN |
| ETHUSDT | 4 | `wma506_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1228 | 0.5882 | 0.7459 | 0.0038 | 0.1979 | ok | RAN |
| SOLUSDT | 8 | `wma506_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0919 | 0.5495 | 0.5059 | 0.0017 | 0.0989 | ok | RAN |
| SOLUSDT | 4 | `wma506_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.0494 | 0.5730 | 0.2916 | 0.0010 | 0.1514 | ok | RAN |
| SOLUSDT | 8 | `wma506_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.0179 | 0.5503 | 0.1050 | 0.0004 | 0.1640 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma506_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 0.9754 | 0.5288 | -0.1464 | -0.0005 | 0.1047 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma506_above_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 0.8366 | 0.5419 | -1.0145 | -0.0068 | 0.0838 | ok | RAN |
| ETHUSDT | 4 | `wma506_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.7983 | 0.5238 | -1.3189 | -0.0086 | 0.0952 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma506_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma506_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma506_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma506_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma506_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma506_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma506_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma506_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma506_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma506_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma506_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma506_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma506_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma506_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma506_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma506_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
