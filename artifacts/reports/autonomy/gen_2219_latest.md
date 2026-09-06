# Autonomy public-indicator hunt gen 2219

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T150005Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma769_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.2186 | 0.6045 | 1.2101 | 0.0062 | 0.1921 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma769_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.1577 | 0.5812 | 0.9181 | 0.0046 | 0.1780 | ok | RAN |
| SOLUSDT | 8 | `sma769_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.1154 | 0.5500 | 0.5553 | 0.0021 | 0.1286 | ok | RAN |
| SOLUSDT | 4 | `sma769_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.0778 | 0.5504 | 0.3615 | 0.0015 | 0.1240 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma769_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9518 | 0.5567 | -0.2974 | -0.0010 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma769_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 0.8992 | 0.5381 | -0.6497 | -0.0022 | 0.1333 | ok | RAN |
| ETHUSDT | 8 | `sma769_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.9104 | 0.5667 | -0.4606 | -0.0036 | 0.1200 | ok | RAN |
| ETHUSDT | 4 | `sma769_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 0.8418 | 0.5541 | -0.8383 | -0.0066 | 0.1081 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma769_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma769_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0560 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma769_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma769_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma769_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma769_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma769_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma769_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma769_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma769_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma769_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma769_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma769_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma769_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma769_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma769_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
