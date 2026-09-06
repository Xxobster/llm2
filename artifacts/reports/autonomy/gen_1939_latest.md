# Autonomy public-indicator hunt gen 1939

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T030628Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma732_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.2676 | 0.6023 | 1.4588 | 0.0073 | 0.1875 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma732_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.1677 | 0.5689 | 0.9341 | 0.0050 | 0.1796 | ok | RAN |
| SOLUSDT | 4 | `sma732_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.0232 | 0.5294 | 0.1138 | 0.0004 | 0.1176 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma732_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 0.9920 | 0.5286 | -0.0409 | -0.0002 | 0.1214 | ok | RAN |
| SOLUSDT | 4 | `sma732_below_at_h` | one_head_filter_pi_star | 218 | 17.8260 | 0.9668 | 0.5505 | -0.2116 | -0.0007 | 0.1284 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma732_below_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 0.9205 | 0.5545 | -0.5116 | -0.0017 | 0.1327 | ok | RAN |
| ETHUSDT | 4 | `sma732_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8833 | 0.5646 | -0.5986 | -0.0047 | 0.1088 | ok | RAN |
| ETHUSDT | 8 | `sma732_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 0.7778 | 0.5355 | -1.2551 | -0.0095 | 0.1097 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma732_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma732_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma732_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma732_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma732_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma732_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma732_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma732_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma732_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma732_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma732_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma732_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma732_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma732_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma732_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma732_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
