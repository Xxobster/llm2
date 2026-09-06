# Autonomy public-indicator hunt gen 037

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T115741Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `chop_low_at_h` | one_head_filter_pi_star | 31 | 2.7504 | 3.9229 | 0.8065 | 3.0631 | 0.0528 | 0.5806 | EBR>35% | RAN |
| ETHUSDT | 4 | `chop_low_at_h` | one_head_filter_pi_star | 95 | 7.9153 | 2.3828 | 0.7158 | 3.3856 | 0.0309 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `chop_cross_down_382` | one_head_filter_pi_star | 70 | 5.7248 | 1.6966 | 0.6857 | 1.9268 | 0.0239 | 0.2571 | GATE_CAND | RAN |
| ETHUSDT | 8 | `chop_cross_down_382` | one_head_filter_pi_star | 54 | 4.4162 | 1.5951 | 0.7222 | 1.4403 | 0.0205 | 0.2593 | GATE_CAND | RAN |
| SOLUSDT | 8 | `chop_low_at_h` | one_head_filter_pi_star | 39 | 3.4094 | 1.8159 | 0.6923 | 1.6674 | 0.0204 | 0.5641 | EBR>35% | RAN |
| SOLUSDT | 4 | `chop_low_at_h` | one_head_filter_pi_star | 113 | 9.4644 | 1.9838 | 0.6372 | 3.1483 | 0.0174 | 0.4336 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `chop_cross_down_382` | one_head_filter_pi_star | 44 | 3.6336 | 1.3100 | 0.6136 | 0.8179 | 0.0059 | 0.2955 | TPM<MIN | RAN |
| SOLUSDT | 8 | `chop_cross_down_382` | one_head_filter_pi_star | 43 | 3.5510 | 1.0855 | 0.5814 | 0.2579 | 0.0016 | 0.2558 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `chop_low_at_h` | one_head_filter_pi_star | 21 | 2.0246 | 1.0006 | 0.4286 | 0.0014 | 0.0001 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `chop_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `chop_cross_up_618` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `chop_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `chop_cross_up_618` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `chop_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `chop_cross_up_618` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `chop_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `chop_cross_up_618` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `chop_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `chop_cross_down_382` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `chop_cross_up_618` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `chop_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `chop_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `chop_cross_down_382` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `chop_cross_up_618` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
