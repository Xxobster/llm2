# Autonomy public-indicator hunt gen 788

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T143435Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema745_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 2.0789 | 0.6942 | 4.4238 | 0.0232 | 0.3786 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema745_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.0241 | 0.6818 | 4.1411 | 0.0230 | 0.3788 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema745_below_at_h` | one_head_filter_pi_star | 226 | 18.4802 | 1.9051 | 0.6637 | 4.0432 | 0.0133 | 0.3186 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema745_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 1.8382 | 0.6599 | 3.9826 | 0.0126 | 0.3036 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema745_above_at_h` | one_head_filter_pi_star | 116 | 9.6411 | 1.5856 | 0.6379 | 2.1370 | 0.0089 | 0.3190 | ok | RAN |
| ETHUSDT | 8 | `ema745_above_at_h` | one_head_filter_pi_star | 141 | 11.6355 | 1.2487 | 0.6028 | 1.1288 | 0.0087 | 0.2057 | ok | RAN |
| SOLUSDT | 4 | `ema745_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.5534 | 0.6269 | 2.2136 | 0.0086 | 0.3209 | ok | RAN |
| ETHUSDT | 4 | `ema745_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.1082 | 0.5928 | 0.5635 | 0.0039 | 0.2036 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema745_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0400 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema745_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema745_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema745_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
