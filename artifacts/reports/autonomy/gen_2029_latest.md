# Autonomy public-indicator hunt gen 2029

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T123452Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret333_neg_at_h` | one_head_filter_pi_star | 156 | 12.7438 | 1.2140 | 0.6090 | 1.1512 | 0.0065 | 0.2051 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret333_pos_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.2481 | 0.5733 | 1.1491 | 0.0044 | 0.1200 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret333_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.1384 | 0.5729 | 0.8379 | 0.0043 | 0.1875 | ok | RAN |
| SOLUSDT | 4 | `ret333_pos_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 1.2220 | 0.5705 | 1.0714 | 0.0038 | 0.1154 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret333_neg_at_h` | one_head_filter_pi_star | 208 | 16.9212 | 0.9719 | 0.5625 | -0.1794 | -0.0006 | 0.1394 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret333_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 0.9212 | 0.5608 | -0.5002 | -0.0017 | 0.1429 | ok | RAN |
| ETHUSDT | 8 | `ret333_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8469 | 0.5574 | -0.8990 | -0.0064 | 0.0984 | ok | RAN |
| ETHUSDT | 4 | `ret333_pos_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 0.8375 | 0.5576 | -0.9112 | -0.0067 | 0.0970 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret333_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0729 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret333_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0754 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret333_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret333_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret333_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret333_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret333_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret333_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret333_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret333_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret333_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret333_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret333_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret333_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret333_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret333_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
