# Autonomy public-indicator hunt gen 1643

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T223112Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma693_below_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 1.1662 | 0.5776 | 0.9202 | 0.0049 | 0.1988 | ok | RAN |
| ETHUSDT | 8 | `sma693_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.0990 | 0.5674 | 0.5940 | 0.0032 | 0.1854 | ok | RAN |
| SOLUSDT | 4 | `sma693_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.1032 | 0.5504 | 0.4790 | 0.0019 | 0.1163 | ok | RAN |
| SOLUSDT | 8 | `sma693_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.0257 | 0.5391 | 0.1238 | 0.0005 | 0.1328 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma693_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 0.9424 | 0.5567 | -0.3552 | -0.0012 | 0.1340 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma693_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 0.8955 | 0.5497 | -0.6483 | -0.0023 | 0.1361 | ok | RAN |
| ETHUSDT | 8 | `sma693_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.8949 | 0.5600 | -0.5718 | -0.0042 | 0.1133 | ok | RAN |
| ETHUSDT | 4 | `sma693_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 0.8550 | 0.5423 | -0.7558 | -0.0061 | 0.1197 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma693_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma693_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma693_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma693_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma693_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma693_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma693_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma693_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma693_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma693_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma693_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma693_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma693_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma693_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma693_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma693_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
