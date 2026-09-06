# Autonomy public-indicator hunt gen 2043

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T141049Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma746_below_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.2439 | 0.5864 | 1.2589 | 0.0067 | 0.2037 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma746_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.2054 | 0.5833 | 1.1987 | 0.0060 | 0.1722 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma746_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.0026 | 0.5397 | 0.0124 | 0.0000 | 0.1270 | ok | RAN |
| SOLUSDT | 4 | `sma746_above_at_h` | one_head_filter_pi_star | 118 | 9.6766 | 0.9912 | 0.5254 | -0.0417 | -0.0002 | 0.1186 | ok | RAN |
| SOLUSDT | 8 | `sma746_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9434 | 0.5512 | -0.3548 | -0.0012 | 0.1268 | ok | RAN |
| SOLUSDT | 4 | `sma746_below_at_h` | one_head_filter_pi_star | 204 | 16.5958 | 0.9254 | 0.5539 | -0.4686 | -0.0016 | 0.1324 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma746_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8756 | 0.5646 | -0.6515 | -0.0051 | 0.1020 | ok | RAN |
| ETHUSDT | 8 | `sma746_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 0.8377 | 0.5490 | -0.8844 | -0.0069 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma746_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma746_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma746_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma746_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma746_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma746_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma746_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma746_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma746_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma746_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma746_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma746_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma746_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma746_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma746_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma746_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
