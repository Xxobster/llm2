# Autonomy public-indicator hunt gen 2041

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T135719Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4660_above_at_h` | one_head_filter_pi_star | 63 | 5.1790 | 1.7614 | 0.6349 | 1.6291 | 0.0106 | 0.0952 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4660_above_at_h` | one_head_filter_pi_star | 53 | 4.4618 | 1.4453 | 0.5849 | 0.9764 | 0.0068 | 0.0566 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4660_below_at_h` | one_head_filter_pi_star | 305 | 24.9401 | 0.9701 | 0.5311 | -0.2289 | -0.0006 | 0.1344 | ok | RAN |
| SOLUSDT | 4 | `ema4660_below_at_h` | one_head_filter_pi_star | 328 | 26.8208 | 0.9649 | 0.5396 | -0.2767 | -0.0007 | 0.1372 | ok | RAN |
| ETHUSDT | 8 | `ema4660_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9517 | 0.5543 | -0.3925 | -0.0016 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `ema4660_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9499 | 0.5536 | -0.4037 | -0.0016 | 0.1339 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4660_above_at_h` | one_head_filter_pi_star | 38 | 11.0914 | 0.9010 | 0.5263 | -0.4885 | -0.0049 | 0.1842 | ok | RAN |
| ETHUSDT | 4 | `ema4660_above_at_h` | one_head_filter_pi_star | 31 | 9.3547 | 0.8259 | 0.5161 | -0.8393 | -0.0085 | 0.0968 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4660_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4660_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
