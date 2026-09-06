# Autonomy public-indicator hunt gen 409

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T041721Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema580_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0508 | 0.6885 | 4.0946 | 0.0229 | 0.3934 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema580_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9268 | 0.6850 | 4.0032 | 0.0216 | 0.3800 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema580_below_at_h` | one_head_filter_pi_star | 217 | 17.7443 | 1.9325 | 0.6636 | 4.0131 | 0.0133 | 0.3272 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema580_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 1.8242 | 0.6558 | 3.6808 | 0.0127 | 0.3302 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema580_above_at_h` | one_head_filter_pi_star | 163 | 13.3668 | 1.6591 | 0.6258 | 2.7189 | 0.0097 | 0.2883 | ok | RAN |
| ETHUSDT | 8 | `ema580_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.2204 | 0.6129 | 1.0389 | 0.0076 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `ema580_above_at_h` | one_head_filter_pi_star | 156 | 12.7203 | 1.4337 | 0.5897 | 1.8653 | 0.0069 | 0.2821 | ok | RAN |
| ETHUSDT | 4 | `ema580_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.1622 | 0.6013 | 0.7930 | 0.0060 | 0.1962 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema580_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema580_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
