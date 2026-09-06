# Autonomy public-indicator hunt gen 2339

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T054226Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma785_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.2801 | 0.5978 | 1.5179 | 0.0078 | 0.1955 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma785_below_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.1788 | 0.5818 | 0.9765 | 0.0050 | 0.1818 | ok | RAN |
| SOLUSDT | 4 | `sma785_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.1221 | 0.5571 | 0.5806 | 0.0023 | 0.1214 | ok | RAN |
| SOLUSDT | 8 | `sma785_above_at_h` | one_head_filter_pi_star | 123 | 10.0866 | 1.1093 | 0.5772 | 0.4923 | 0.0020 | 0.1220 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma785_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 1.0005 | 0.5694 | 0.0030 | 0.0000 | 0.1340 | ok | RAN |
| SOLUSDT | 8 | `sma785_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9491 | 0.5567 | -0.3159 | -0.0011 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma785_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 0.9320 | 0.5577 | -0.3521 | -0.0028 | 0.1154 | ok | RAN |
| ETHUSDT | 4 | `sma785_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 0.8456 | 0.5513 | -0.8310 | -0.0064 | 0.0962 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma785_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma785_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4039 | 0.2105 | -1.4311 | -0.0694 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma785_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma785_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
