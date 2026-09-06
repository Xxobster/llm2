# Autonomy public-indicator hunt gen 1460

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T225140Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema967_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 2.0567 | 0.6786 | 4.4550 | 0.0229 | 0.3571 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema967_below_at_h` | one_head_filter_pi_star | 239 | 19.5241 | 1.8600 | 0.6653 | 4.1046 | 0.0203 | 0.3389 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema967_above_at_h` | one_head_filter_pi_star | 118 | 9.6992 | 1.7678 | 0.6780 | 2.5115 | 0.0117 | 0.3390 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema967_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 1.7343 | 0.6403 | 3.6762 | 0.0117 | 0.3202 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema967_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.7422 | 0.6459 | 3.6983 | 0.0115 | 0.3035 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema967_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.6608 | 0.6441 | 2.2752 | 0.0095 | 0.3220 | ok | RAN |
| ETHUSDT | 4 | `ema967_above_at_h` | one_head_filter_pi_star | 130 | 10.6858 | 1.2235 | 0.5846 | 1.0178 | 0.0086 | 0.2231 | ok | RAN |
| ETHUSDT | 8 | `ema967_above_at_h` | one_head_filter_pi_star | 127 | 10.4392 | 1.2031 | 0.5984 | 0.8761 | 0.0074 | 0.2126 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema967_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6020 | 0.2941 | -0.7739 | -0.0347 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema967_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema967_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema967_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema967_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema967_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema967_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema967_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema967_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema967_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema967_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema967_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema967_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema967_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema967_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema967_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
