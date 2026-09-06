# Autonomy public-indicator hunt gen 2067

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T174444Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma749_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.1898 | 0.5943 | 1.0588 | 0.0054 | 0.1943 | ok | RAN |
| SOLUSDT | 8 | `sma749_above_at_h` | one_head_filter_pi_star | 123 | 10.0866 | 1.1568 | 0.5691 | 0.6773 | 0.0028 | 0.1301 | ok | RAN |
| ETHUSDT | 8 | `sma749_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.0801 | 0.5611 | 0.4783 | 0.0025 | 0.1833 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma749_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 0.9692 | 0.5197 | -0.1522 | -0.0006 | 0.1181 | ok | RAN |
| SOLUSDT | 4 | `sma749_below_at_h` | one_head_filter_pi_star | 215 | 17.4907 | 0.9438 | 0.5488 | -0.3585 | -0.0012 | 0.1302 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma749_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.8726 | 0.5366 | -0.8289 | -0.0028 | 0.1317 | ok | RAN |
| ETHUSDT | 8 | `sma749_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 0.8745 | 0.5669 | -0.7005 | -0.0052 | 0.1083 | ok | RAN |
| ETHUSDT | 4 | `sma749_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8418 | 0.5578 | -0.8216 | -0.0066 | 0.0884 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma749_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma749_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma749_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma749_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma749_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma749_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma749_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma749_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma749_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma749_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma749_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma749_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma749_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma749_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma749_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma749_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
