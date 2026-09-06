# Autonomy public-indicator hunt gen 1987

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T073818Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma738_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.2708 | 0.5943 | 1.4988 | 0.0075 | 0.1829 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma738_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.2443 | 0.5833 | 1.3545 | 0.0066 | 0.1889 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma738_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.0958 | 0.5532 | 0.4666 | 0.0017 | 0.1064 | ok | RAN |
| SOLUSDT | 8 | `sma738_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.0826 | 0.5407 | 0.3961 | 0.0016 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma738_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 0.9904 | 0.5625 | -0.0593 | -0.0002 | 0.1298 | ok | RAN |
| SOLUSDT | 8 | `sma738_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.9292 | 0.5590 | -0.4388 | -0.0015 | 0.1333 | ok | RAN |
| ETHUSDT | 8 | `sma738_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 0.9582 | 0.5797 | -0.2154 | -0.0016 | 0.1159 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma738_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 0.8668 | 0.5616 | -0.7056 | -0.0057 | 0.1164 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma738_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma738_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0561 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma738_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma738_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma738_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma738_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma738_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma738_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma738_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma738_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma738_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma738_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma738_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma738_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma738_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma738_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
