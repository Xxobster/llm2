# Autonomy public-indicator hunt gen 1972

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T060846Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1038_above_at_h` | one_head_filter_pi_star | 110 | 9.0416 | 1.1376 | 0.5909 | 0.5839 | 0.0025 | 0.1455 | ok | RAN |
| SOLUSDT | 4 | `ema1038_above_at_h` | one_head_filter_pi_star | 124 | 10.1110 | 1.1158 | 0.5726 | 0.5040 | 0.0021 | 0.1290 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema1038_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 0.9821 | 0.5507 | -0.1201 | -0.0006 | 0.1498 | ok | RAN |
| SOLUSDT | 8 | `ema1038_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 0.9311 | 0.5341 | -0.4954 | -0.0015 | 0.1326 | ok | RAN |
| ETHUSDT | 8 | `ema1038_above_at_h` | one_head_filter_pi_star | 125 | 10.2748 | 0.9621 | 0.5600 | -0.1737 | -0.0016 | 0.1280 | ok | RAN |
| SOLUSDT | 4 | `ema1038_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 0.9247 | 0.5363 | -0.5218 | -0.0016 | 0.1290 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1038_below_at_h` | one_head_filter_pi_star | 242 | 19.7692 | 0.9295 | 0.5372 | -0.5213 | -0.0023 | 0.1488 | ok | RAN |
| ETHUSDT | 4 | `ema1038_above_at_h` | one_head_filter_pi_star | 133 | 10.9763 | 0.9140 | 0.5414 | -0.4202 | -0.0039 | 0.1278 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1038_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1038_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1038_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1038_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1038_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1038_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1038_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1038_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1038_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1038_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1038_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1038_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1038_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1038_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1038_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1038_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
