# Autonomy public-indicator hunt gen 1875

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T210947Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma724_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.2137 | 0.5829 | 1.2026 | 0.0060 | 0.1886 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma724_below_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.1193 | 0.5833 | 0.6796 | 0.0036 | 0.1845 | ok | RAN |
| SOLUSDT | 4 | `sma724_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.0568 | 0.5496 | 0.2723 | 0.0011 | 0.1298 | ok | RAN |
| SOLUSDT | 8 | `sma724_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.0516 | 0.5462 | 0.2433 | 0.0010 | 0.1154 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma724_below_at_h` | one_head_filter_pi_star | 214 | 17.4093 | 0.9791 | 0.5561 | -0.1313 | -0.0004 | 0.1355 | ok | RAN |
| SOLUSDT | 4 | `sma724_below_at_h` | one_head_filter_pi_star | 211 | 17.1653 | 0.9715 | 0.5498 | -0.1788 | -0.0006 | 0.1232 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma724_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 0.9246 | 0.5652 | -0.4144 | -0.0030 | 0.0994 | ok | RAN |
| ETHUSDT | 4 | `sma724_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.7848 | 0.5450 | -1.3248 | -0.0094 | 0.1005 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma724_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma724_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0701 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma724_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma724_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma724_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma724_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma724_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma724_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma724_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma724_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma724_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma724_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma724_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma724_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma724_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma724_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
