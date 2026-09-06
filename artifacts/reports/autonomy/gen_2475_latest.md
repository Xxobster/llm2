# Autonomy public-indicator hunt gen 2475

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T223020Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma803_below_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.2630 | 0.6036 | 1.3908 | 0.0073 | 0.1716 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma803_below_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.1742 | 0.5964 | 0.9460 | 0.0049 | 0.1867 | ok | RAN |
| SOLUSDT | 8 | `sma803_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.1556 | 0.5547 | 0.6942 | 0.0028 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `sma803_above_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.0649 | 0.5436 | 0.3281 | 0.0012 | 0.1141 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma803_below_at_h` | one_head_filter_pi_star | 217 | 17.7443 | 0.9823 | 0.5622 | -0.1129 | -0.0004 | 0.1382 | ok | RAN |
| SOLUSDT | 8 | `sma803_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9625 | 0.5572 | -0.2309 | -0.0008 | 0.1294 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma803_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 0.8292 | 0.5419 | -0.9408 | -0.0076 | 0.1032 | ok | RAN |
| ETHUSDT | 4 | `sma803_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 0.8140 | 0.5399 | -1.0649 | -0.0078 | 0.1043 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma803_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma803_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0546 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma803_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma803_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma803_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma803_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma803_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma803_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma803_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma803_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma803_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma803_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma803_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma803_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma803_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma803_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
