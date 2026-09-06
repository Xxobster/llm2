# Autonomy public-indicator hunt gen 1667

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T004200Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma696_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.1636 | 0.5829 | 0.9182 | 0.0048 | 0.1886 | ok | RAN |
| ETHUSDT | 8 | `sma696_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.0640 | 0.5676 | 0.3791 | 0.0020 | 0.1784 | ok | RAN |
| SOLUSDT | 4 | `sma696_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.0812 | 0.5407 | 0.3869 | 0.0015 | 0.1185 | ok | RAN |
| SOLUSDT | 8 | `sma696_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.0041 | 0.5294 | 0.0206 | 0.0001 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma696_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9396 | 0.5616 | -0.3765 | -0.0013 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma696_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 0.9364 | 0.5671 | -0.3487 | -0.0024 | 0.1037 | ok | RAN |
| SOLUSDT | 8 | `sma696_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 0.8653 | 0.5445 | -0.8446 | -0.0030 | 0.1257 | ok | RAN |
| ETHUSDT | 4 | `sma696_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 0.8251 | 0.5556 | -0.9211 | -0.0076 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma696_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma696_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma696_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma696_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma696_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma696_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma696_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma696_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma696_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma696_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma696_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma696_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma696_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma696_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma696_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma696_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
