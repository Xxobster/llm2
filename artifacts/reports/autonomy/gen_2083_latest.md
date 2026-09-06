# Autonomy public-indicator hunt gen 2083

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T195037Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma751_below_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.2131 | 0.5872 | 1.1859 | 0.0060 | 0.1744 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma751_below_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.1490 | 0.5941 | 0.8147 | 0.0041 | 0.1882 | ok | RAN |
| SOLUSDT | 8 | `sma751_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.0214 | 0.5317 | 0.1027 | 0.0004 | 0.1270 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma751_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 0.9925 | 0.5312 | -0.0361 | -0.0001 | 0.1328 | ok | RAN |
| SOLUSDT | 8 | `sma751_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 0.9819 | 0.5535 | -0.1139 | -0.0004 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma751_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 0.8503 | 0.5361 | -0.9391 | -0.0033 | 0.1237 | ok | RAN |
| ETHUSDT | 8 | `sma751_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8717 | 0.5510 | -0.6810 | -0.0055 | 0.1156 | ok | RAN |
| ETHUSDT | 4 | `sma751_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 0.8190 | 0.5479 | -0.9510 | -0.0078 | 0.1027 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma751_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma751_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma751_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma751_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma751_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma751_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma751_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma751_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma751_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma751_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma751_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma751_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma751_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma751_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma751_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma751_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
