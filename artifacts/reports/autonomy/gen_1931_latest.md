# Autonomy public-indicator hunt gen 1931

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T022213Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma731_below_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.2102 | 0.5828 | 1.1168 | 0.0056 | 0.1902 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma731_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1843 | 0.5879 | 1.0753 | 0.0053 | 0.1758 | ok | RAN |
| SOLUSDT | 4 | `sma731_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.0458 | 0.5391 | 0.2161 | 0.0009 | 0.1172 | ok | RAN |
| SOLUSDT | 8 | `sma731_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.0328 | 0.5373 | 0.1602 | 0.0006 | 0.1194 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma731_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 0.9829 | 0.5588 | -0.1053 | -0.0004 | 0.1373 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma731_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 0.8858 | 0.5381 | -0.7219 | -0.0025 | 0.1371 | ok | RAN |
| ETHUSDT | 4 | `sma731_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 0.8319 | 0.5548 | -0.8921 | -0.0071 | 0.0959 | ok | RAN |
| ETHUSDT | 8 | `sma731_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 0.8210 | 0.5460 | -1.0547 | -0.0074 | 0.1166 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma731_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma731_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma731_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma731_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma731_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma731_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma731_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma731_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma731_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma731_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma731_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma731_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma731_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma731_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma731_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma731_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
