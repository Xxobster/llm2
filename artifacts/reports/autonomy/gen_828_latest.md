# Autonomy public-indicator hunt gen 828

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T181909Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema795_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.9779 | 0.6818 | 4.3919 | 0.0227 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema795_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.8547 | 0.6714 | 3.7404 | 0.0201 | 0.3568 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema795_below_at_h` | one_head_filter_pi_star | 239 | 19.5432 | 1.9174 | 0.6653 | 4.1752 | 0.0134 | 0.3138 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema795_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.7922 | 0.6502 | 3.7965 | 0.0121 | 0.3128 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema795_above_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.7432 | 0.6435 | 2.4232 | 0.0109 | 0.3391 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema795_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.5622 | 0.6220 | 2.1313 | 0.0084 | 0.3071 | ok | RAN |
| ETHUSDT | 4 | `ema795_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.2198 | 0.5868 | 1.0364 | 0.0078 | 0.1976 | ok | RAN |
| ETHUSDT | 8 | `ema795_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 1.1923 | 0.5918 | 0.9012 | 0.0069 | 0.2177 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema795_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0393 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema795_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema795_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema795_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
