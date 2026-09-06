# Autonomy public-indicator hunt gen 2267

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T204313Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma775_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1711 | 0.5882 | 0.9647 | 0.0049 | 0.1711 | ok | RAN |
| SOLUSDT | 8 | `sma775_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.2715 | 0.5878 | 1.1719 | 0.0046 | 0.1221 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma775_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.0558 | 0.5707 | 0.3561 | 0.0017 | 0.1717 | ok | RAN |
| SOLUSDT | 4 | `sma775_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.0252 | 0.5344 | 0.1215 | 0.0005 | 0.1145 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma775_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9955 | 0.5610 | -0.0278 | -0.0001 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma775_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 0.9088 | 0.5441 | -0.5788 | -0.0020 | 0.1275 | ok | RAN |
| ETHUSDT | 4 | `sma775_above_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 0.8612 | 0.5655 | -0.7254 | -0.0059 | 0.1103 | ok | RAN |
| ETHUSDT | 8 | `sma775_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 0.8182 | 0.5405 | -0.9968 | -0.0079 | 0.1216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma775_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma775_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma775_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma775_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
