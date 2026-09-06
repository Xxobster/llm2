# Autonomy public-indicator hunt gen 707

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T074023Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma430_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0997 | 0.7027 | 4.6295 | 0.0250 | 0.3946 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma430_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8292 | 0.6839 | 3.9540 | 0.0213 | 0.3886 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma430_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.9503 | 0.6758 | 3.8051 | 0.0142 | 0.3736 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma430_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.8265 | 0.6649 | 3.4427 | 0.0128 | 0.3568 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma430_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2619 | 0.5957 | 1.3548 | 0.0093 | 0.2234 | ok | RAN |
| SOLUSDT | 4 | `sma430_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.5002 | 0.6085 | 2.3564 | 0.0080 | 0.2751 | ok | RAN |
| SOLUSDT | 8 | `sma430_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.5129 | 0.6053 | 2.4370 | 0.0080 | 0.2737 | ok | RAN |
| ETHUSDT | 8 | `sma430_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.2164 | 0.5932 | 1.1011 | 0.0078 | 0.2147 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma430_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma430_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma430_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma430_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
