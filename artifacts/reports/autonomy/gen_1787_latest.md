# Autonomy public-indicator hunt gen 1787

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T131346Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma712_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.2479 | 0.5955 | 1.3758 | 0.0068 | 0.1910 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma712_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.2094 | 0.5829 | 1.1694 | 0.0061 | 0.1943 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma712_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.0849 | 0.5468 | 0.4161 | 0.0016 | 0.1223 | ok | RAN |
| SOLUSDT | 4 | `sma712_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.0633 | 0.5517 | 0.3199 | 0.0012 | 0.1172 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma712_below_at_h` | one_head_filter_pi_star | 199 | 16.1890 | 0.9584 | 0.5578 | -0.2557 | -0.0009 | 0.1307 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma712_below_at_h` | one_head_filter_pi_star | 206 | 16.7585 | 0.8947 | 0.5388 | -0.6728 | -0.0023 | 0.1311 | ok | RAN |
| ETHUSDT | 8 | `sma712_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 0.8755 | 0.5641 | -0.6931 | -0.0050 | 0.1154 | ok | RAN |
| ETHUSDT | 4 | `sma712_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 0.8371 | 0.5570 | -0.9064 | -0.0070 | 0.1139 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma712_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma712_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma712_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma712_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma712_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma712_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma712_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma712_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma712_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma712_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma712_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma712_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma712_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma712_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma712_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma712_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
