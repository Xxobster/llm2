# Autonomy public-indicator hunt gen 2494

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T003153Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma567_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.2325 | 0.6089 | 1.3124 | 0.0067 | 0.1844 | GATE_CAND | RAN |
| ETHUSDT | 4 | `wma567_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1126 | 0.5838 | 0.6714 | 0.0035 | 0.1838 | ok | RAN |
| SOLUSDT | 4 | `wma567_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.1242 | 0.5537 | 0.6662 | 0.0023 | 0.1073 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma567_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0037 | 0.5401 | 0.0217 | 0.0001 | 0.0963 | ok | RAN |
| SOLUSDT | 8 | `wma567_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9525 | 0.5427 | -0.3017 | -0.0010 | 0.1558 | ok | RAN |
| SOLUSDT | 4 | `wma567_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 0.9474 | 0.5526 | -0.3188 | -0.0011 | 0.1474 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma567_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8735 | 0.5376 | -0.7768 | -0.0051 | 0.0968 | ok | RAN |
| ETHUSDT | 8 | `wma567_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.8308 | 0.5337 | -1.0500 | -0.0068 | 0.1011 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma567_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma567_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma567_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma567_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma567_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma567_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma567_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma567_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma567_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma567_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma567_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma567_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma567_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma567_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma567_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma567_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
