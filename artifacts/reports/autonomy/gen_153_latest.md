# Autonomy public-indicator hunt gen 153

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T193030Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema36_cross_up` | one_head_filter_pi_star | 13 | 1.1114 | 11.6882 | 0.7692 | 2.6148 | 0.0592 | 0.3846 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema36_cross_down` | one_head_filter_pi_star | 15 | 1.4555 | 3.5552 | 0.8000 | 1.9006 | 0.0261 | 0.1333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema36_cross_down` | one_head_filter_pi_star | 11 | 0.9492 | 2.6752 | 0.7273 | 1.3194 | 0.0231 | 0.1818 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema36_below_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.7961 | 0.6804 | 3.8642 | 0.0206 | 0.3699 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema36_below_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.7783 | 0.6758 | 3.8171 | 0.0205 | 0.3699 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema36_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1327 | 0.6832 | 3.9298 | 0.0173 | 0.4224 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema36_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1288 | 0.6810 | 3.9432 | 0.0173 | 0.4172 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema36_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2402 | 0.5976 | 1.1055 | 0.0074 | 0.2134 | ok | RAN |
| ETHUSDT | 4 | `ema36_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2140 | 0.5975 | 0.9773 | 0.0067 | 0.2075 | ok | RAN |
| SOLUSDT | 4 | `ema36_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3707 | 0.6000 | 1.9974 | 0.0054 | 0.2465 | ok | RAN |
| SOLUSDT | 8 | `ema36_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3423 | 0.5981 | 1.8568 | 0.0051 | 0.2523 | ok | RAN |
| ETHUSDT | 8 | `ema36_cross_up` | one_head_filter_pi_star | 16 | 1.4130 | 1.1278 | 0.5000 | 0.2071 | 0.0048 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema36_cross_down` | one_head_filter_pi_star | 12 | 1.4086 | 1.0644 | 0.4167 | 0.1022 | 0.0024 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema36_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema36_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema36_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema36_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema36_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema36_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema36_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema36_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema36_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema36_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema36_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
