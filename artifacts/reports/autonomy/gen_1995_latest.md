# Autonomy public-indicator hunt gen 1995

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T083749Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma739_below_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 1.2452 | 0.6000 | 1.3171 | 0.0069 | 0.2125 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma739_below_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.1592 | 0.5655 | 0.9003 | 0.0047 | 0.1845 | ok | RAN |
| SOLUSDT | 4 | `sma739_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.0836 | 0.5512 | 0.3934 | 0.0016 | 0.1181 | ok | RAN |
| SOLUSDT | 8 | `sma739_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.0246 | 0.5469 | 0.1157 | 0.0005 | 0.1328 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma739_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 0.9418 | 0.5736 | -0.3590 | -0.0013 | 0.1371 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma739_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 0.9210 | 0.5521 | -0.4847 | -0.0017 | 0.1302 | ok | RAN |
| ETHUSDT | 4 | `sma739_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 0.9443 | 0.5674 | -0.2792 | -0.0022 | 0.0993 | ok | RAN |
| ETHUSDT | 8 | `sma739_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 0.9127 | 0.5732 | -0.4768 | -0.0035 | 0.1098 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma739_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma739_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma739_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma739_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma739_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma739_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma739_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma739_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma739_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma739_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma739_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma739_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma739_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma739_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma739_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma739_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
