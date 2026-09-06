# Autonomy public-indicator hunt gen 1891

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T223608Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma726_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.2616 | 0.5934 | 1.4435 | 0.0074 | 0.1868 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma726_below_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 1.2554 | 0.5915 | 1.3426 | 0.0071 | 0.1951 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma726_above_at_h` | one_head_filter_pi_star | 116 | 9.5126 | 1.1415 | 0.5690 | 0.6107 | 0.0025 | 0.1293 | ok | RAN |
| SOLUSDT | 4 | `sma726_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.0444 | 0.5397 | 0.2075 | 0.0008 | 0.1190 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma726_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9933 | 0.5813 | -0.0402 | -0.0001 | 0.1429 | ok | RAN |
| SOLUSDT | 8 | `sma726_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 0.9242 | 0.5556 | -0.4619 | -0.0016 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma726_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 0.8784 | 0.5493 | -0.6264 | -0.0051 | 0.1197 | ok | RAN |
| ETHUSDT | 8 | `sma726_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 0.8184 | 0.5455 | -1.0143 | -0.0080 | 0.1104 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma726_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma726_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma726_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma726_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma726_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma726_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma726_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma726_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma726_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma726_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma726_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma726_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma726_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma726_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma726_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma726_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
