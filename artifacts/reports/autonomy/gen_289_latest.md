# Autonomy public-indicator hunt gen 289

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T044152Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema280_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0248 | 0.7016 | 4.4072 | 0.0238 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema280_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.9112 | 0.6866 | 4.1986 | 0.0219 | 0.3831 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema280_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.2273 | 0.6935 | 4.4724 | 0.0168 | 0.3710 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema280_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 2.1582 | 0.6845 | 4.3442 | 0.0163 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema280_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2943 | 0.6154 | 1.4687 | 0.0098 | 0.2143 | ok | RAN |
| ETHUSDT | 4 | `ema280_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2215 | 0.6033 | 1.1611 | 0.0077 | 0.2174 | ok | RAN |
| SOLUSDT | 4 | `ema280_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4620 | 0.6053 | 2.2296 | 0.0071 | 0.2684 | ok | RAN |
| SOLUSDT | 8 | `ema280_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.4611 | 0.6077 | 2.2229 | 0.0071 | 0.2652 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema280_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema280_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
