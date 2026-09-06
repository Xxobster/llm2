# Autonomy public-indicator hunt gen 2094

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T212110Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma504_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.2146 | 0.6066 | 1.2018 | 0.0062 | 0.1803 | GATE_CAND | RAN |
| ETHUSDT | 4 | `wma504_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1225 | 0.5892 | 0.7376 | 0.0038 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `wma504_above_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.1207 | 0.5536 | 0.6299 | 0.0021 | 0.1012 | ok | RAN |
| SOLUSDT | 4 | `wma504_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0401 | 0.5640 | 0.2285 | 0.0008 | 0.1512 | ok | RAN |
| SOLUSDT | 8 | `wma504_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0280 | 0.5632 | 0.1619 | 0.0006 | 0.1552 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma504_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 0.9716 | 0.5238 | -0.1689 | -0.0005 | 0.1058 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma504_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 0.8083 | 0.5330 | -1.2192 | -0.0079 | 0.0934 | ok | RAN |
| ETHUSDT | 4 | `wma504_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 0.7802 | 0.5222 | -1.4056 | -0.0094 | 0.0889 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma504_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma504_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma504_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma504_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma504_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma504_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma504_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma504_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma504_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma504_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma504_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma504_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma504_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma504_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma504_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma504_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
