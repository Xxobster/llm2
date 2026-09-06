# Autonomy public-indicator hunt gen 2480

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T230119Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5800_above_at_h` | one_head_filter_pi_star | 42 | 3.9434 | 2.0640 | 0.6429 | 1.8188 | 0.0154 | 0.0952 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma5800_above_at_h` | one_head_filter_pi_star | 53 | 4.9763 | 1.8635 | 0.6415 | 1.8805 | 0.0130 | 0.1132 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma5800_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9774 | 0.5569 | -0.1810 | -0.0007 | 0.1317 | ok | RAN |
| ETHUSDT | 4 | `sma5800_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9754 | 0.5569 | -0.2026 | -0.0008 | 0.1287 | ok | RAN |
| SOLUSDT | 4 | `sma5800_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9495 | 0.5369 | -0.4078 | -0.0010 | 0.1298 | ok | RAN |
| SOLUSDT | 8 | `sma5800_below_at_h` | one_head_filter_pi_star | 311 | 25.4307 | 0.9500 | 0.5305 | -0.3891 | -0.0010 | 0.1350 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5800_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.7641 | 0.5000 | -1.1795 | -0.0123 | 0.1471 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5800_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.6600 | 0.4706 | -1.8757 | -0.0171 | 0.1176 | ok | RAN |
| ETHUSDT | 4 | `sma5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5800_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5800_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
