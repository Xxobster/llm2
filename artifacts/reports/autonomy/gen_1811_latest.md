# Autonomy public-indicator hunt gen 1811

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T152442Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma715_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.3236 | 0.5977 | 1.7053 | 0.0088 | 0.1897 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma715_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1738 | 0.5778 | 0.9949 | 0.0051 | 0.1889 | ok | RAN |
| SOLUSDT | 8 | `sma715_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.0922 | 0.5344 | 0.4210 | 0.0017 | 0.1221 | ok | RAN |
| SOLUSDT | 4 | `sma715_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.0354 | 0.5420 | 0.1703 | 0.0007 | 0.1145 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma715_below_at_h` | one_head_filter_pi_star | 211 | 17.1653 | 0.9824 | 0.5592 | -0.1085 | -0.0004 | 0.1327 | ok | RAN |
| SOLUSDT | 8 | `sma715_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 0.9227 | 0.5604 | -0.4789 | -0.0016 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma715_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 0.8764 | 0.5580 | -0.6527 | -0.0051 | 0.1087 | ok | RAN |
| ETHUSDT | 8 | `sma715_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 0.8283 | 0.5528 | -0.9686 | -0.0071 | 0.1118 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma715_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma715_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma715_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma715_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
