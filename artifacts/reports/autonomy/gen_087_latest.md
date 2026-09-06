# Autonomy public-indicator hunt gen 087

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T151412Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `hlc3_above_at_h` | one_head_filter_pi_star | 25 | 2.1332 | 3.9958 | 0.7600 | 2.6036 | 0.0240 | 0.5200 | EBR>35% | RAN |
| ETHUSDT | 4 | `hlc3_above_at_h` | one_head_filter_pi_star | 67 | 5.5421 | 1.7289 | 0.6866 | 2.0208 | 0.0208 | 0.4478 | EBR>35% | RAN |
| ETHUSDT | 4 | `hlc3_cross_up` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 4 | `hlc3_cross_down` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 8 | `hlc3_cross_up` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 8 | `hlc3_cross_down` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `hlc3_cross_up` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 4 | `hlc3_cross_down` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 8 | `hlc3_cross_up` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 8 | `hlc3_cross_down` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `hlc3_cross_up` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 4 | `hlc3_cross_down` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 8 | `hlc3_cross_up` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 8 | `hlc3_cross_down` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `hlc3_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `hlc3_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `hlc3_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `hlc3_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `hlc3_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `hlc3_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `hlc3_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `hlc3_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `hlc3_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `hlc3_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
