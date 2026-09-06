# Autonomy public-indicator hunt gen 2398

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T133625Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma552_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1672 | 0.5967 | 0.9758 | 0.0051 | 0.1823 | ok | RAN |
| ETHUSDT | 4 | `wma552_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1080 | 0.5829 | 0.6478 | 0.0033 | 0.1818 | ok | RAN |
| SOLUSDT | 4 | `wma552_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.0743 | 0.5492 | 0.4312 | 0.0014 | 0.1036 | ok | RAN |
| SOLUSDT | 8 | `wma552_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.0078 | 0.5408 | 0.0474 | 0.0001 | 0.0969 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma552_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 0.9536 | 0.5414 | -0.2823 | -0.0010 | 0.1492 | ok | RAN |
| SOLUSDT | 8 | `wma552_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.9510 | 0.5487 | -0.3005 | -0.0011 | 0.1538 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma552_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8488 | 0.5355 | -0.9385 | -0.0059 | 0.0929 | ok | RAN |
| ETHUSDT | 4 | `wma552_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8362 | 0.5344 | -1.0277 | -0.0070 | 0.0952 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma552_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma552_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma552_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma552_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
