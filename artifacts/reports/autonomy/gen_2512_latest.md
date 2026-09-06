# Autonomy public-indicator hunt gen 2512

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T022429Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5880_above_at_h` | one_head_filter_pi_star | 64 | 5.9339 | 2.0558 | 0.6562 | 2.2098 | 0.0135 | 0.0781 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma5880_above_at_h` | one_head_filter_pi_star | 53 | 4.5131 | 1.8397 | 0.6415 | 1.7190 | 0.0128 | 0.1132 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5880_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9731 | 0.5556 | -0.2221 | -0.0009 | 0.1345 | ok | RAN |
| SOLUSDT | 4 | `sma5880_below_at_h` | one_head_filter_pi_star | 353 | 28.7172 | 0.9526 | 0.5382 | -0.3899 | -0.0009 | 0.1303 | ok | RAN |
| SOLUSDT | 8 | `sma5880_below_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 0.9452 | 0.5278 | -0.4323 | -0.0011 | 0.1265 | ok | RAN |
| ETHUSDT | 8 | `sma5880_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9550 | 0.5546 | -0.3743 | -0.0015 | 0.1327 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5880_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.6980 | 0.4688 | -1.6009 | -0.0159 | 0.1250 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `sma5880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
