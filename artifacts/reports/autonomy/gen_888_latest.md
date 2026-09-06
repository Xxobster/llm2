# Autonomy public-indicator hunt gen 888

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T001224Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma1820_above_at_h` | one_head_filter_pi_star | 47 | 3.9070 | 2.0912 | 0.7021 | 2.2367 | 0.0165 | 0.3191 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma1820_below_at_h` | one_head_filter_pi_star | 317 | 25.8960 | 1.6071 | 0.6498 | 3.6299 | 0.0163 | 0.3186 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma1820_below_at_h` | one_head_filter_pi_star | 296 | 24.1805 | 1.5925 | 0.6453 | 3.3026 | 0.0151 | 0.3142 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1820_above_at_h` | one_head_filter_pi_star | 61 | 5.0708 | 2.0914 | 0.6885 | 2.4756 | 0.0151 | 0.2951 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1820_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 1.7568 | 0.6334 | 4.0561 | 0.0113 | 0.3183 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1820_below_at_h` | one_head_filter_pi_star | 315 | 25.6259 | 1.7130 | 0.6349 | 3.9729 | 0.0106 | 0.3111 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1820_above_at_h` | one_head_filter_pi_star | 55 | 4.8367 | 1.1688 | 0.5455 | 0.4996 | 0.0067 | 0.2545 | ok | RAN |
| ETHUSDT | 4 | `sma1820_above_at_h` | one_head_filter_pi_star | 44 | 3.8529 | 1.1487 | 0.5682 | 0.4021 | 0.0066 | 0.2727 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1820_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0587 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1820_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3190 | 0.2000 | -1.5401 | -0.0760 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
