# Autonomy public-indicator hunt gen 672

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T051239Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1280_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.9447 | 0.6780 | 3.9791 | 0.0218 | 0.3512 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1280_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.9468 | 0.6842 | 4.0291 | 0.0215 | 0.3541 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1280_below_at_h` | one_head_filter_pi_star | 271 | 22.1599 | 1.7922 | 0.6384 | 4.0106 | 0.0122 | 0.3247 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1280_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.6931 | 0.6312 | 3.5891 | 0.0110 | 0.3042 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1280_above_at_h` | one_head_filter_pi_star | 68 | 5.5900 | 1.7396 | 0.6912 | 1.9679 | 0.0098 | 0.2794 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1280_above_at_h` | one_head_filter_pi_star | 90 | 7.3386 | 1.5039 | 0.6333 | 1.5562 | 0.0076 | 0.2667 | ok | RAN |
| ETHUSDT | 4 | `sma1280_above_at_h` | one_head_filter_pi_star | 125 | 10.3160 | 1.0921 | 0.5600 | 0.4219 | 0.0038 | 0.2080 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma1280_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 1.0179 | 0.5547 | 0.0854 | 0.0007 | 0.2188 | ok | RAN |
| BTCUSDT | 8 | `sma1280_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1280_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0580 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
