# Autonomy public-indicator hunt gen 2427

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T165757Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma796_below_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.2992 | 0.6047 | 1.5690 | 0.0080 | 0.1802 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma796_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.2496 | 0.5944 | 1.3980 | 0.0073 | 0.1833 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma796_above_at_h` | one_head_filter_pi_star | 122 | 10.0046 | 1.2067 | 0.5738 | 0.8789 | 0.0035 | 0.0984 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma796_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.1896 | 0.5746 | 0.8647 | 0.0033 | 0.1119 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma796_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 0.9407 | 0.5588 | -0.3716 | -0.0013 | 0.1324 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma796_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9034 | 0.5473 | -0.6071 | -0.0021 | 0.1294 | ok | RAN |
| ETHUSDT | 4 | `sma796_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 0.8763 | 0.5584 | -0.6747 | -0.0054 | 0.1039 | ok | RAN |
| ETHUSDT | 8 | `sma796_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 0.8471 | 0.5466 | -0.8434 | -0.0064 | 0.1056 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma796_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0546 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma796_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma796_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma796_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma796_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma796_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma796_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma796_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma796_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma796_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma796_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma796_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma796_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma796_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma796_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma796_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
