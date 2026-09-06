# Autonomy public-indicator hunt gen 2403

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T141133Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma793_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.2394 | 0.5862 | 1.2992 | 0.0067 | 0.1724 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma793_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1440 | 0.5761 | 0.8199 | 0.0042 | 0.1739 | ok | RAN |
| SOLUSDT | 8 | `sma793_above_at_h` | one_head_filter_pi_star | 128 | 10.6385 | 1.1189 | 0.5703 | 0.5503 | 0.0021 | 0.1172 | ok | RAN |
| SOLUSDT | 4 | `sma793_above_at_h` | one_head_filter_pi_star | 135 | 11.0080 | 1.0359 | 0.5333 | 0.1729 | 0.0007 | 0.1111 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma793_below_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 0.9533 | 0.5514 | -0.2956 | -0.0010 | 0.1308 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma793_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 0.9089 | 0.5500 | -0.5772 | -0.0020 | 0.1350 | ok | RAN |
| ETHUSDT | 4 | `sma793_above_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 0.8646 | 0.5455 | -0.7550 | -0.0057 | 0.1030 | ok | RAN |
| ETHUSDT | 8 | `sma793_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 0.8642 | 0.5535 | -0.7431 | -0.0058 | 0.1069 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma793_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma793_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma793_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma793_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma793_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma793_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma793_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma793_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma793_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma793_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma793_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma793_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma793_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma793_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma793_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma793_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
