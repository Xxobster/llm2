# Autonomy public-indicator hunt gen 2387

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T121404Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma791_below_at_h` | one_head_filter_pi_star | 156 | 12.7438 | 1.2012 | 0.5833 | 1.0715 | 0.0056 | 0.1795 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma791_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1155 | 0.5659 | 0.6655 | 0.0034 | 0.1758 | ok | RAN |
| SOLUSDT | 8 | `sma791_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.1225 | 0.5620 | 0.5492 | 0.0023 | 0.1322 | ok | RAN |
| SOLUSDT | 4 | `sma791_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.0634 | 0.5468 | 0.3092 | 0.0012 | 0.1223 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma791_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 0.9300 | 0.5472 | -0.4455 | -0.0015 | 0.1321 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma791_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 0.9224 | 0.5455 | -0.4951 | -0.0017 | 0.1244 | ok | RAN |
| ETHUSDT | 8 | `sma791_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 0.8700 | 0.5556 | -0.7431 | -0.0053 | 0.0994 | ok | RAN |
| ETHUSDT | 4 | `sma791_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 0.8700 | 0.5625 | -0.6676 | -0.0054 | 0.0972 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma791_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma791_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma791_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma791_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma791_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma791_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma791_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma791_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma791_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma791_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma791_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma791_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma791_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma791_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma791_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma791_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
