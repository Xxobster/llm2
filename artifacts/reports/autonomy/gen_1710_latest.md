# Autonomy public-indicator hunt gen 1710

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T055819Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma444_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1943 | 0.6043 | 1.1046 | 0.0059 | 0.1979 | ok | RAN |
| ETHUSDT | 4 | `wma444_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1333 | 0.5892 | 0.7849 | 0.0042 | 0.1946 | ok | RAN |
| SOLUSDT | 8 | `wma444_below_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 1.0865 | 0.5696 | 0.4539 | 0.0017 | 0.1456 | ok | RAN |
| SOLUSDT | 8 | `wma444_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.0527 | 0.5525 | 0.2944 | 0.0009 | 0.1105 | ok | RAN |
| SOLUSDT | 4 | `wma444_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.0392 | 0.5449 | 0.2213 | 0.0007 | 0.0955 | ok | RAN |
| SOLUSDT | 4 | `wma444_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.0218 | 0.5593 | 0.1216 | 0.0005 | 0.1582 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma444_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8494 | 0.5344 | -0.9283 | -0.0061 | 0.0952 | ok | RAN |
| ETHUSDT | 8 | `wma444_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 0.8378 | 0.5444 | -0.9940 | -0.0066 | 0.0889 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma444_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma444_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma444_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma444_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma444_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma444_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma444_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma444_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma444_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma444_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma444_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma444_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma444_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma444_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma444_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma444_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
