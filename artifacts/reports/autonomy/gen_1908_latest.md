# Autonomy public-indicator hunt gen 1908

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T000820Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1030_above_at_h` | one_head_filter_pi_star | 113 | 9.2877 | 1.2978 | 0.6018 | 1.1711 | 0.0048 | 0.1416 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1030_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.2000 | 0.5868 | 0.8331 | 0.0035 | 0.1157 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1030_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.0337 | 0.5537 | 0.2193 | 0.0007 | 0.1281 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1030_above_at_h` | one_head_filter_pi_star | 130 | 10.7287 | 0.9970 | 0.5692 | -0.0140 | -0.0001 | 0.1308 | ok | RAN |
| ETHUSDT | 4 | `ema1030_below_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 0.9582 | 0.5434 | -0.2821 | -0.0013 | 0.1553 | ok | RAN |
| SOLUSDT | 4 | `ema1030_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 0.9379 | 0.5363 | -0.4304 | -0.0013 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1030_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9404 | 0.5459 | -0.4139 | -0.0019 | 0.1485 | ok | RAN |
| ETHUSDT | 8 | `ema1030_above_at_h` | one_head_filter_pi_star | 130 | 10.6858 | 0.9521 | 0.5538 | -0.2242 | -0.0020 | 0.1154 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1030_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0288 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1030_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1030_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1030_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1030_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1030_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1030_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1030_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1030_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1030_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1030_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1030_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1030_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1030_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1030_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1030_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
