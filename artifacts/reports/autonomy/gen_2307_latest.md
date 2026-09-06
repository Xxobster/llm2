# Autonomy public-indicator hunt gen 2307

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T013054Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma781_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.2544 | 0.5989 | 1.4091 | 0.0071 | 0.1808 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma781_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1996 | 0.5906 | 1.0571 | 0.0056 | 0.1930 | ok | RAN |
| SOLUSDT | 8 | `sma781_above_at_h` | one_head_filter_pi_star | 113 | 9.3918 | 1.3221 | 0.6106 | 1.2925 | 0.0055 | 0.1416 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma781_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.0872 | 0.5635 | 0.4026 | 0.0016 | 0.1190 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma781_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 0.9527 | 0.5545 | -0.2913 | -0.0010 | 0.1238 | ok | RAN |
| SOLUSDT | 8 | `sma781_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9453 | 0.5528 | -0.3373 | -0.0012 | 0.1357 | ok | RAN |
| ETHUSDT | 8 | `sma781_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 0.9607 | 0.5669 | -0.2029 | -0.0015 | 0.1019 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma781_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 0.8595 | 0.5526 | -0.7427 | -0.0060 | 0.0987 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma781_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma781_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0583 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma781_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma781_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma781_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma781_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma781_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma781_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma781_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma781_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma781_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma781_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma781_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma781_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma781_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma781_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
