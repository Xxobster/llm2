# Autonomy public-indicator hunt gen 2499

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T010323Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma806_below_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 1.3541 | 0.6087 | 1.7823 | 0.0091 | 0.1863 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma806_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.2149 | 0.5866 | 1.1824 | 0.0061 | 0.1620 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma806_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.1598 | 0.5662 | 0.7432 | 0.0029 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `sma806_above_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.0685 | 0.5497 | 0.3461 | 0.0013 | 0.1126 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma806_below_at_h` | one_head_filter_pi_star | 218 | 17.8260 | 0.9873 | 0.5550 | -0.0805 | -0.0003 | 0.1376 | ok | RAN |
| SOLUSDT | 4 | `sma806_below_at_h` | one_head_filter_pi_star | 217 | 17.7443 | 0.9720 | 0.5484 | -0.1779 | -0.0006 | 0.1336 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma806_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.9465 | 0.5646 | -0.2677 | -0.0022 | 0.1088 | ok | RAN |
| ETHUSDT | 4 | `sma806_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 0.8143 | 0.5357 | -1.0796 | -0.0082 | 0.1071 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma806_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma806_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma806_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma806_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma806_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma806_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma806_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma806_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma806_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma806_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma806_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma806_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma806_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma806_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma806_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma806_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
