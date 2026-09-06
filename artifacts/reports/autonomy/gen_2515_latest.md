# Autonomy public-indicator hunt gen 2515

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T024315Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma808_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.3742 | 0.6108 | 1.9470 | 0.0100 | 0.1676 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma808_above_at_h` | one_head_filter_pi_star | 112 | 9.1851 | 1.1912 | 0.5893 | 0.7484 | 0.0033 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `sma808_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.0969 | 0.5792 | 0.5873 | 0.0028 | 0.1803 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma808_above_at_h` | one_head_filter_pi_star | 146 | 11.9049 | 0.9989 | 0.5274 | -0.0054 | -0.0000 | 0.1164 | ok | RAN |
| SOLUSDT | 8 | `sma808_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9243 | 0.5473 | -0.4756 | -0.0017 | 0.1343 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma808_below_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 0.9194 | 0.5607 | -0.5238 | -0.0018 | 0.1308 | ok | RAN |
| ETHUSDT | 4 | `sma808_above_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 0.8589 | 0.5455 | -0.7871 | -0.0061 | 0.1030 | ok | RAN |
| ETHUSDT | 8 | `sma808_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 0.7778 | 0.5253 | -1.2780 | -0.0097 | 0.1076 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma808_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma808_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma808_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma808_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma808_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma808_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma808_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma808_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma808_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma808_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma808_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma808_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma808_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma808_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma808_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma808_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
