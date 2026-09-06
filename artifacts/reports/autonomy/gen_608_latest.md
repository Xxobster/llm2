# Autonomy public-indicator hunt gen 608

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T010230Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1120_below_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 2.0327 | 0.6887 | 4.3364 | 0.0235 | 0.3726 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1120_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0306 | 0.6989 | 4.0117 | 0.0228 | 0.3817 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1120_below_at_h` | one_head_filter_pi_star | 236 | 19.2979 | 1.9600 | 0.6653 | 4.1755 | 0.0140 | 0.3178 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1120_below_at_h` | one_head_filter_pi_star | 232 | 18.9708 | 1.7267 | 0.6509 | 3.4978 | 0.0116 | 0.3233 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1120_above_at_h` | one_head_filter_pi_star | 112 | 9.1846 | 1.6612 | 0.6518 | 2.2286 | 0.0095 | 0.2946 | ok | RAN |
| SOLUSDT | 4 | `sma1120_above_at_h` | one_head_filter_pi_star | 112 | 9.1846 | 1.5568 | 0.6250 | 1.9388 | 0.0082 | 0.2857 | ok | RAN |
| ETHUSDT | 8 | `sma1120_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 1.2148 | 0.5890 | 1.0126 | 0.0078 | 0.2123 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1120_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 1.0154 | 0.5548 | 0.0763 | 0.0006 | 0.2055 | ok | RAN |
| BTCUSDT | 4 | `sma1120_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0532 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1120_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
