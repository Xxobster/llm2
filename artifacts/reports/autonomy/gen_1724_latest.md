# Autonomy public-indicator hunt gen 1724

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T072220Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1006_above_at_h` | one_head_filter_pi_star | 124 | 10.1110 | 1.1254 | 0.5806 | 0.5578 | 0.0022 | 0.1371 | ok | RAN |
| SOLUSDT | 8 | `ema1006_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.0896 | 0.5659 | 0.4087 | 0.0017 | 0.1240 | ok | RAN |
| ETHUSDT | 8 | `ema1006_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.0292 | 0.5602 | 0.1920 | 0.0009 | 0.1528 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1006_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 0.9882 | 0.5470 | -0.0808 | -0.0004 | 0.1496 | ok | RAN |
| SOLUSDT | 8 | `ema1006_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.9741 | 0.5402 | -0.1809 | -0.0006 | 0.1264 | ok | RAN |
| SOLUSDT | 4 | `ema1006_below_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 0.9728 | 0.5447 | -0.1847 | -0.0006 | 0.1341 | ok | RAN |
| ETHUSDT | 8 | `ema1006_above_at_h` | one_head_filter_pi_star | 127 | 10.4811 | 0.9720 | 0.5512 | -0.1317 | -0.0012 | 0.1260 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1006_above_at_h` | one_head_filter_pi_star | 139 | 11.4705 | 0.9569 | 0.5540 | -0.2167 | -0.0018 | 0.1151 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1006_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0283 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1006_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1006_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1006_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1006_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1006_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1006_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1006_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1006_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1006_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1006_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1006_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1006_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1006_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1006_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1006_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
