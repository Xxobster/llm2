# Autonomy public-indicator hunt gen 1963

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T052007Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma735_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.2227 | 0.5843 | 1.2447 | 0.0065 | 0.1798 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma735_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.1427 | 0.5690 | 0.8190 | 0.0042 | 0.1954 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma735_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.0013 | 0.5255 | 0.0067 | 0.0000 | 0.1168 | ok | RAN |
| SOLUSDT | 4 | `sma735_above_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 0.9892 | 0.5359 | -0.0576 | -0.0002 | 0.1111 | ok | RAN |
| SOLUSDT | 4 | `sma735_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 0.9628 | 0.5598 | -0.2335 | -0.0008 | 0.1292 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma735_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.9053 | 0.5492 | -0.5815 | -0.0020 | 0.1295 | ok | RAN |
| ETHUSDT | 8 | `sma735_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 0.9272 | 0.5693 | -0.3603 | -0.0030 | 0.1168 | ok | RAN |
| ETHUSDT | 4 | `sma735_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 0.7577 | 0.5311 | -1.4805 | -0.0108 | 0.1073 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma735_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma735_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4039 | 0.2105 | -1.4311 | -0.0707 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma735_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma735_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
