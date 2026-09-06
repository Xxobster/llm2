# Autonomy public-indicator hunt gen 2419

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T160210Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma795_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.2321 | 0.5886 | 1.3007 | 0.0066 | 0.1771 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma795_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.2002 | 0.5856 | 1.1212 | 0.0056 | 0.1713 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma795_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.1916 | 0.5827 | 0.8647 | 0.0033 | 0.1181 | ok | RAN |
| SOLUSDT | 4 | `sma795_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.0926 | 0.5659 | 0.4281 | 0.0017 | 0.1163 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma795_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 0.9763 | 0.5583 | -0.1469 | -0.0005 | 0.1359 | ok | RAN |
| SOLUSDT | 8 | `sma795_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9471 | 0.5622 | -0.3292 | -0.0011 | 0.1393 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma795_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 0.8843 | 0.5658 | -0.5924 | -0.0047 | 0.0987 | ok | RAN |
| ETHUSDT | 8 | `sma795_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 0.8271 | 0.5357 | -0.9954 | -0.0071 | 0.1071 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma795_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma795_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0601 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma795_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma795_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
