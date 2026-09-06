# Autonomy public-indicator hunt gen 2371

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T100413Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma789_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.2136 | 0.5902 | 1.1646 | 0.0059 | 0.1749 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma789_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.2026 | 0.5815 | 1.1680 | 0.0058 | 0.1685 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma789_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.1254 | 0.5649 | 0.5810 | 0.0023 | 0.1221 | ok | RAN |
| SOLUSDT | 4 | `sma789_above_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 1.0621 | 0.5423 | 0.3061 | 0.0012 | 0.1197 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma789_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 0.9729 | 0.5535 | -0.1705 | -0.0006 | 0.1349 | ok | RAN |
| SOLUSDT | 8 | `sma789_below_at_h` | one_head_filter_pi_star | 222 | 18.1531 | 0.9432 | 0.5405 | -0.3715 | -0.0012 | 0.1306 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma789_above_at_h` | one_head_filter_pi_star | 124 | 10.2327 | 0.8993 | 0.5484 | -0.4777 | -0.0043 | 0.1129 | ok | RAN |
| ETHUSDT | 4 | `sma789_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 0.8701 | 0.5563 | -0.7091 | -0.0055 | 0.1187 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma789_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0561 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma789_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma789_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma789_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma789_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma789_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma789_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma789_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma789_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma789_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma789_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma789_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma789_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma789_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma789_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma789_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
