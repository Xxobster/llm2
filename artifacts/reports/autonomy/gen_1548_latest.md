# Autonomy public-indicator hunt gen 1548

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T071814Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema979_below_at_h` | one_head_filter_pi_star | 242 | 19.7692 | 1.8265 | 0.6653 | 3.9692 | 0.0199 | 0.3430 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema979_below_at_h` | one_head_filter_pi_star | 243 | 19.8509 | 1.7300 | 0.6502 | 3.7093 | 0.0176 | 0.3374 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema979_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.7947 | 0.6420 | 3.9820 | 0.0121 | 0.2957 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema979_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 1.7587 | 0.6468 | 3.7685 | 0.0118 | 0.2937 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema979_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 1.3016 | 0.6054 | 1.3837 | 0.0115 | 0.2313 | ok | RAN |
| ETHUSDT | 4 | `ema979_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.3211 | 0.6170 | 1.4406 | 0.0115 | 0.2340 | ok | RAN |
| SOLUSDT | 4 | `ema979_above_at_h` | one_head_filter_pi_star | 123 | 10.0866 | 1.6492 | 0.6504 | 2.3209 | 0.0101 | 0.3171 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema979_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.5787 | 0.6279 | 2.1867 | 0.0088 | 0.3178 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema979_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0288 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema979_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema979_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema979_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema979_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema979_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema979_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema979_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema979_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema979_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema979_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema979_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema979_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema979_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema979_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema979_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
