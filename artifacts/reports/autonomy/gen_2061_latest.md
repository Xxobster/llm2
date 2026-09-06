# Autonomy public-indicator hunt gen 2061

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T165108Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret338_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.1680 | 0.6012 | 0.9453 | 0.0052 | 0.1964 | ok | RAN |
| ETHUSDT | 4 | `ret338_neg_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1541 | 0.5912 | 0.9160 | 0.0049 | 0.1823 | ok | RAN |
| SOLUSDT | 4 | `ret338_pos_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.2026 | 0.5732 | 0.9673 | 0.0036 | 0.1146 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret338_pos_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.0627 | 0.5350 | 0.3318 | 0.0012 | 0.1019 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret338_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 0.9006 | 0.5417 | -0.6281 | -0.0022 | 0.1406 | ok | RAN |
| SOLUSDT | 4 | `ret338_neg_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.8949 | 0.5468 | -0.6885 | -0.0023 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `ret338_pos_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 0.8100 | 0.5417 | -1.1505 | -0.0081 | 0.1071 | ok | RAN |
| ETHUSDT | 8 | `ret338_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.7783 | 0.5410 | -1.3615 | -0.0095 | 0.0929 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret338_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0729 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret338_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0740 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret338_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret338_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret338_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret338_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret338_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret338_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret338_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret338_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret338_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret338_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret338_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret338_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret338_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret338_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
