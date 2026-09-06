# Autonomy public-indicator hunt gen 1483

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T011238Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma671_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.1247 | 0.6889 | 4.5530 | 0.0248 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma671_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.0244 | 0.6857 | 4.0573 | 0.0231 | 0.3886 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma671_below_at_h` | one_head_filter_pi_star | 201 | 16.3517 | 1.6804 | 0.6468 | 2.9902 | 0.0104 | 0.3184 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma671_below_at_h` | one_head_filter_pi_star | 208 | 16.9212 | 1.6328 | 0.6442 | 3.0052 | 0.0103 | 0.3269 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma671_above_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.6389 | 0.6266 | 2.5846 | 0.0100 | 0.3165 | ok | RAN |
| ETHUSDT | 8 | `sma671_above_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 1.2476 | 0.6084 | 1.1560 | 0.0089 | 0.2238 | ok | RAN |
| SOLUSDT | 8 | `sma671_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.5525 | 0.6103 | 2.1816 | 0.0088 | 0.3162 | ok | RAN |
| ETHUSDT | 4 | `sma671_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.1062 | 0.5839 | 0.5376 | 0.0040 | 0.1988 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma671_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma671_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma671_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma671_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma671_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma671_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma671_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma671_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma671_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma671_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma671_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma671_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma671_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma671_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma671_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma671_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
