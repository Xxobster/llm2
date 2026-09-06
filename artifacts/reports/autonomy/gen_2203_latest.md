# Autonomy public-indicator hunt gen 2203

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T125526Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma767_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1818 | 0.5738 | 1.0556 | 0.0053 | 0.1803 | ok | RAN |
| ETHUSDT | 4 | `sma767_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1753 | 0.5955 | 0.9966 | 0.0051 | 0.1798 | ok | RAN |
| SOLUSDT | 8 | `sma767_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.0843 | 0.5504 | 0.3860 | 0.0015 | 0.1163 | ok | RAN |
| SOLUSDT | 4 | `sma767_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.0568 | 0.5441 | 0.2733 | 0.0010 | 0.1176 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma767_below_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 0.9582 | 0.5556 | -0.2621 | -0.0009 | 0.1353 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma767_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 0.8824 | 0.5340 | -0.7632 | -0.0026 | 0.1311 | ok | RAN |
| ETHUSDT | 8 | `sma767_above_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.8837 | 0.5657 | -0.6573 | -0.0048 | 0.0971 | ok | RAN |
| ETHUSDT | 4 | `sma767_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 0.8354 | 0.5528 | -0.9188 | -0.0069 | 0.1118 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma767_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma767_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma767_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma767_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma767_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma767_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma767_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma767_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma767_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma767_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma767_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma767_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma767_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma767_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma767_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma767_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
