# Autonomy public-indicator hunt gen 1403

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T060934Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma659_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0350 | 0.6940 | 4.2591 | 0.0236 | 0.3934 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma659_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9464 | 0.6809 | 4.0218 | 0.0229 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma659_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.7774 | 0.6683 | 3.4029 | 0.0121 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma659_below_at_h` | one_head_filter_pi_star | 202 | 16.4331 | 1.7853 | 0.6584 | 3.4761 | 0.0119 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma659_above_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 1.2604 | 0.6174 | 1.2388 | 0.0093 | 0.2148 | ok | RAN |
| SOLUSDT | 8 | `sma659_above_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.5123 | 0.6159 | 2.1647 | 0.0084 | 0.3113 | ok | RAN |
| SOLUSDT | 4 | `sma659_above_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.4795 | 0.5890 | 1.9759 | 0.0077 | 0.3082 | ok | RAN |
| ETHUSDT | 4 | `sma659_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.1652 | 0.5987 | 0.8012 | 0.0062 | 0.2171 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma659_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma659_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma659_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma659_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma659_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma659_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma659_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma659_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma659_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma659_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma659_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma659_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma659_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma659_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma659_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma659_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
