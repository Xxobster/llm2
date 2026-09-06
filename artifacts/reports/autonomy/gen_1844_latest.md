# Autonomy public-indicator hunt gen 1844

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T182311Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1022_above_at_h` | one_head_filter_pi_star | 125 | 10.2740 | 1.2015 | 0.5920 | 0.8684 | 0.0036 | 0.1200 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1022_above_at_h` | one_head_filter_pi_star | 116 | 9.5126 | 1.1130 | 0.5776 | 0.4961 | 0.0020 | 0.1293 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1022_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 0.9857 | 0.5545 | -0.0958 | -0.0004 | 0.1545 | ok | RAN |
| SOLUSDT | 4 | `ema1022_below_at_h` | one_head_filter_pi_star | 240 | 19.6250 | 0.9672 | 0.5417 | -0.2174 | -0.0007 | 0.1167 | ok | RAN |
| ETHUSDT | 8 | `ema1022_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 0.9667 | 0.5455 | -0.2318 | -0.0010 | 0.1515 | ok | RAN |
| SOLUSDT | 8 | `ema1022_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 0.9244 | 0.5333 | -0.5398 | -0.0017 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1022_above_at_h` | one_head_filter_pi_star | 127 | 10.4802 | 0.9246 | 0.5591 | -0.3717 | -0.0031 | 0.1181 | ok | RAN |
| ETHUSDT | 8 | `ema1022_above_at_h` | one_head_filter_pi_star | 111 | 9.1607 | 0.8565 | 0.5495 | -0.6788 | -0.0064 | 0.1171 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1022_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1022_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1022_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1022_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1022_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1022_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1022_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1022_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1022_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1022_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1022_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1022_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1022_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1022_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1022_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1022_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
