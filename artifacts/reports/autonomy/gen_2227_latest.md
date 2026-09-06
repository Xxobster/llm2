# Autonomy public-indicator hunt gen 2227

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T155620Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma770_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.2084 | 0.5944 | 1.1307 | 0.0058 | 0.1667 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma770_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1676 | 0.5843 | 0.9743 | 0.0050 | 0.1798 | ok | RAN |
| SOLUSDT | 8 | `sma770_above_at_h` | one_head_filter_pi_star | 123 | 10.0866 | 1.1777 | 0.5691 | 0.7784 | 0.0033 | 0.1301 | ok | RAN |
| SOLUSDT | 4 | `sma770_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.0362 | 0.5403 | 0.1696 | 0.0007 | 0.1210 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma770_below_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 0.9327 | 0.5540 | -0.4268 | -0.0015 | 0.1408 | ok | RAN |
| SOLUSDT | 8 | `sma770_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9279 | 0.5468 | -0.4548 | -0.0016 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma770_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 0.9149 | 0.5704 | -0.4060 | -0.0035 | 0.1111 | ok | RAN |
| ETHUSDT | 8 | `sma770_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 0.8923 | 0.5603 | -0.5363 | -0.0046 | 0.1206 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma770_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma770_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0560 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma770_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma770_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
