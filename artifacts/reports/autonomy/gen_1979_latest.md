# Autonomy public-indicator hunt gen 1979

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T064650Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma737_below_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.2639 | 0.5904 | 1.3847 | 0.0074 | 0.1867 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma737_below_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.2264 | 0.6012 | 1.2570 | 0.0064 | 0.2024 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma737_above_at_h` | one_head_filter_pi_star | 122 | 10.0046 | 1.1814 | 0.5738 | 0.8106 | 0.0032 | 0.1230 | ok | RAN |
| SOLUSDT | 4 | `sma737_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.0961 | 0.5448 | 0.4746 | 0.0017 | 0.1034 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma737_below_at_h` | one_head_filter_pi_star | 216 | 17.5720 | 0.9646 | 0.5556 | -0.2229 | -0.0007 | 0.1296 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma737_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 0.9501 | 0.5732 | -0.2679 | -0.0019 | 0.1098 | ok | RAN |
| SOLUSDT | 4 | `sma737_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 0.9026 | 0.5573 | -0.6044 | -0.0021 | 0.1302 | ok | RAN |
| ETHUSDT | 4 | `sma737_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.9428 | 0.5714 | -0.2912 | -0.0022 | 0.1020 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma737_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma737_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma737_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma737_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma737_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma737_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma737_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma737_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma737_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma737_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma737_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma737_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma737_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma737_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma737_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma737_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
