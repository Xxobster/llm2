# Autonomy public-indicator hunt gen 2051

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T151648Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma747_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.2628 | 0.5879 | 1.4262 | 0.0072 | 0.1703 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma747_below_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.1111 | 0.5756 | 0.6353 | 0.0032 | 0.2035 | ok | RAN |
| SOLUSDT | 8 | `sma747_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.1761 | 0.5547 | 0.8003 | 0.0031 | 0.1172 | ok | RAN |
| SOLUSDT | 4 | `sma747_above_at_h` | one_head_filter_pi_star | 132 | 10.8247 | 1.0341 | 0.5379 | 0.1635 | 0.0006 | 0.1212 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma747_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 0.9448 | 0.5598 | -0.3455 | -0.0012 | 0.1388 | ok | RAN |
| SOLUSDT | 8 | `sma747_below_at_h` | one_head_filter_pi_star | 192 | 15.6196 | 0.9395 | 0.5625 | -0.3684 | -0.0013 | 0.1302 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma747_above_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 0.8547 | 0.5500 | -0.7444 | -0.0060 | 0.1143 | ok | RAN |
| ETHUSDT | 8 | `sma747_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 0.8387 | 0.5556 | -0.9303 | -0.0068 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma747_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma747_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma747_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma747_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma747_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma747_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma747_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma747_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma747_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma747_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma747_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma747_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma747_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma747_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma747_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma747_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
