# Autonomy public-indicator hunt gen 1364

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T021923Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema952_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.9944 | 0.6742 | 4.2567 | 0.0217 | 0.3620 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema952_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 1.8204 | 0.6565 | 3.8609 | 0.0191 | 0.3435 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema952_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 1.8013 | 0.6522 | 3.9214 | 0.0122 | 0.3083 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema952_above_at_h` | one_head_filter_pi_star | 121 | 10.0567 | 1.6336 | 0.6364 | 2.2846 | 0.0098 | 0.3223 | ok | RAN |
| SOLUSDT | 4 | `ema952_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 1.5862 | 0.6284 | 3.1360 | 0.0097 | 0.3065 | ok | RAN |
| ETHUSDT | 8 | `ema952_above_at_h` | one_head_filter_pi_star | 139 | 11.4256 | 1.2107 | 0.5971 | 0.9644 | 0.0078 | 0.2086 | ok | RAN |
| SOLUSDT | 8 | `ema952_above_at_h` | one_head_filter_pi_star | 128 | 10.4372 | 1.5046 | 0.6172 | 1.9968 | 0.0077 | 0.3047 | ok | RAN |
| ETHUSDT | 4 | `ema952_above_at_h` | one_head_filter_pi_star | 126 | 10.3570 | 1.0824 | 0.5714 | 0.3771 | 0.0033 | 0.2063 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema952_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema952_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema952_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema952_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema952_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema952_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema952_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema952_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema952_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema952_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema952_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema952_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema952_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema952_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema952_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema952_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
