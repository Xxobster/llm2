# Autonomy public-indicator hunt gen 1955

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T043530Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma734_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.3136 | 0.6011 | 1.6496 | 0.0086 | 0.1910 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma734_below_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.1642 | 0.5824 | 0.9274 | 0.0047 | 0.1941 | ok | RAN |
| SOLUSDT | 8 | `sma734_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.1353 | 0.5588 | 0.6230 | 0.0025 | 0.1176 | ok | RAN |
| SOLUSDT | 4 | `sma734_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.0773 | 0.5556 | 0.3649 | 0.0014 | 0.1185 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma734_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9160 | 0.5419 | -0.5318 | -0.0018 | 0.1379 | ok | RAN |
| SOLUSDT | 4 | `sma734_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.9050 | 0.5596 | -0.5889 | -0.0021 | 0.1347 | ok | RAN |
| ETHUSDT | 4 | `sma734_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 0.8986 | 0.5797 | -0.4942 | -0.0041 | 0.1014 | ok | RAN |
| ETHUSDT | 8 | `sma734_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 0.8621 | 0.5536 | -0.7767 | -0.0056 | 0.1012 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma734_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma734_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma734_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma734_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma734_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma734_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma734_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma734_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma734_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma734_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma734_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma734_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma734_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma734_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma734_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma734_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
