# Autonomy public-indicator hunt gen 1451

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T220057Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma667_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9997 | 0.6804 | 4.1841 | 0.0233 | 0.3814 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma667_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9063 | 0.6738 | 3.9525 | 0.0216 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma667_below_at_h` | one_head_filter_pi_star | 208 | 16.9212 | 1.7608 | 0.6538 | 3.4455 | 0.0116 | 0.3221 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma667_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.6628 | 0.6519 | 2.9396 | 0.0107 | 0.3370 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma667_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.6628 | 0.6148 | 2.5187 | 0.0099 | 0.3111 | ok | RAN |
| SOLUSDT | 8 | `sma667_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.6054 | 0.6286 | 2.3658 | 0.0094 | 0.3429 | ok | RAN |
| ETHUSDT | 8 | `sma667_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.1615 | 0.5924 | 0.7990 | 0.0060 | 0.2229 | ok | RAN |
| ETHUSDT | 4 | `sma667_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 1.1530 | 0.5915 | 0.7286 | 0.0056 | 0.2254 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma667_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma667_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0561 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma667_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma667_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma667_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma667_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma667_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma667_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma667_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma667_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma667_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma667_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma667_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma667_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma667_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma667_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
