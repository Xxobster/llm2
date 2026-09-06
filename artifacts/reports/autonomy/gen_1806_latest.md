# Autonomy public-indicator hunt gen 1806

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T145727Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma459_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1489 | 0.5924 | 0.8872 | 0.0046 | 0.2011 | ok | RAN |
| ETHUSDT | 8 | `wma459_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1198 | 0.5806 | 0.7183 | 0.0038 | 0.1935 | ok | RAN |
| SOLUSDT | 8 | `wma459_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0877 | 0.5756 | 0.4835 | 0.0018 | 0.1628 | ok | RAN |
| SOLUSDT | 4 | `wma459_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 1.0430 | 0.5614 | 0.2416 | 0.0009 | 0.1579 | ok | RAN |
| SOLUSDT | 8 | `wma459_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.0330 | 0.5435 | 0.1895 | 0.0006 | 0.0978 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma459_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 0.9142 | 0.5276 | -0.5404 | -0.0016 | 0.1055 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma459_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8224 | 0.5319 | -1.1290 | -0.0071 | 0.1011 | ok | RAN |
| ETHUSDT | 8 | `wma459_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8004 | 0.5430 | -1.2795 | -0.0083 | 0.0860 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma459_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma459_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma459_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma459_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma459_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma459_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma459_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma459_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma459_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma459_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma459_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma459_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma459_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma459_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma459_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma459_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
