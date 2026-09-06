# Autonomy public-indicator hunt gen 2195

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T115128Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma766_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.2683 | 0.6034 | 1.4184 | 0.0072 | 0.1839 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma766_below_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.1021 | 0.5621 | 0.6021 | 0.0031 | 0.1834 | ok | RAN |
| SOLUSDT | 4 | `sma766_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.0557 | 0.5481 | 0.2683 | 0.0011 | 0.1333 | ok | RAN |
| SOLUSDT | 8 | `sma766_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.0416 | 0.5429 | 0.2083 | 0.0008 | 0.1214 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma766_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9360 | 0.5578 | -0.3949 | -0.0014 | 0.1307 | ok | RAN |
| SOLUSDT | 4 | `sma766_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 0.9312 | 0.5524 | -0.4332 | -0.0015 | 0.1286 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma766_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 0.9205 | 0.5706 | -0.4423 | -0.0032 | 0.1059 | ok | RAN |
| ETHUSDT | 4 | `sma766_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 0.8816 | 0.5556 | -0.6130 | -0.0051 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma766_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma766_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma766_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma766_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma766_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma766_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma766_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma766_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma766_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma766_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma766_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma766_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma766_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma766_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma766_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma766_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
