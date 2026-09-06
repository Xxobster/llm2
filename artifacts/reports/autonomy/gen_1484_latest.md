# Autonomy public-indicator hunt gen 1484

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T011806Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema970_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 2.0117 | 0.6818 | 4.3121 | 0.0224 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema970_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.7382 | 0.6555 | 3.6313 | 0.0181 | 0.3361 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema970_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 1.7719 | 0.6457 | 3.8454 | 0.0122 | 0.3071 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema970_above_at_h` | one_head_filter_pi_star | 117 | 9.6164 | 1.7722 | 0.6581 | 2.5688 | 0.0109 | 0.3162 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema970_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.6716 | 0.6475 | 3.3659 | 0.0108 | 0.3033 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema970_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.6697 | 0.6504 | 2.3960 | 0.0098 | 0.3089 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema970_above_at_h` | one_head_filter_pi_star | 133 | 10.9324 | 1.2437 | 0.5940 | 1.0773 | 0.0093 | 0.2256 | ok | RAN |
| ETHUSDT | 8 | `ema970_above_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 1.1890 | 0.5929 | 0.8646 | 0.0070 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema970_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema970_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema970_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema970_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema970_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema970_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema970_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema970_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema970_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema970_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema970_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema970_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema970_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema970_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema970_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema970_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
