# Autonomy public-indicator hunt gen 072

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T141653Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `adx_cross_up_25` | one_head_filter_pi_star | 13 | 1.4770 | 1.5638 | 0.4615 | 0.7090 | 0.0435 | 0.1538 | TPM<MIN | RAN |
| BTCUSDT | 8 | `adx_cross_up_25` | one_head_filter_pi_star | 14 | 1.3752 | 1.5412 | 0.4286 | 0.6421 | 0.0410 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `adx_low_at_h` | one_head_filter_pi_star | 34 | 2.8327 | 1.8392 | 0.6176 | 1.4273 | 0.0341 | 0.1765 | TPM<MIN | RAN |
| ETHUSDT | 8 | `adx_high_at_h` | one_head_filter_pi_star | 268 | 21.8023 | 1.6514 | 0.6493 | 3.6637 | 0.0181 | 0.3246 | GATE_CAND | RAN |
| ETHUSDT | 4 | `adx_high_at_h` | one_head_filter_pi_star | 251 | 20.5044 | 1.6293 | 0.6494 | 3.5594 | 0.0176 | 0.3307 | GATE_CAND | RAN |
| ETHUSDT | 4 | `adx_cross_up_25` | one_head_filter_pi_star | 79 | 6.6361 | 1.4855 | 0.6329 | 1.5388 | 0.0165 | 0.2785 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `adx_cross_up_25` | one_head_filter_pi_star | 109 | 9.0818 | 1.4324 | 0.5963 | 1.5760 | 0.0144 | 0.3028 | ok | RAN |
| SOLUSDT | 4 | `adx_high_at_h` | one_head_filter_pi_star | 272 | 22.1277 | 2.0042 | 0.6765 | 4.8324 | 0.0140 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `adx_cross_up_25` | one_head_filter_pi_star | 99 | 8.3026 | 1.8733 | 0.6768 | 2.8389 | 0.0139 | 0.2929 | GATE_CAND | RAN |
| SOLUSDT | 8 | `adx_cross_up_25` | one_head_filter_pi_star | 121 | 10.1476 | 1.9088 | 0.6860 | 3.1491 | 0.0136 | 0.2975 | GATE_CAND | RAN |
| SOLUSDT | 8 | `adx_high_at_h` | one_head_filter_pi_star | 284 | 23.1040 | 1.8655 | 0.6655 | 4.5456 | 0.0128 | 0.3556 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `adx_low_at_h` | one_head_filter_pi_star | 59 | 4.8631 | 1.4973 | 0.6271 | 1.2082 | 0.0078 | 0.1525 | ok | RAN |
| SOLUSDT | 8 | `adx_low_at_h` | one_head_filter_pi_star | 46 | 4.0962 | 1.4649 | 0.6087 | 1.0450 | 0.0073 | 0.1522 | ok | RAN |
| BTCUSDT | 4 | `adx_high_at_h` | one_head_filter_pi_star | 24 | 2.3138 | 1.0704 | 0.4583 | 0.1491 | 0.0070 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 8 | `adx_high_at_h` | one_head_filter_pi_star | 25 | 2.4103 | 1.0655 | 0.4400 | 0.1395 | 0.0063 | 0.1600 | TPM<MIN | RAN |
| SOLUSDT | 8 | `adx_cross_down_20` | one_head_filter_pi_star | 13 | 1.2112 | 1.1444 | 0.5385 | 0.2174 | 0.0049 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `adx_low_at_h` | one_head_filter_pi_star | 55 | 4.5823 | 0.9744 | 0.4909 | -0.0808 | -0.0011 | 0.1636 | ok | RAN |
| ETHUSDT | 8 | `adx_cross_down_20` | one_head_filter_pi_star | 13 | 1.1281 | 0.7324 | 0.4615 | -0.5086 | -0.0133 | 0.3077 | TPM<MIN | RAN |
| ETHUSDT | 4 | `adx_cross_down_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `adx_cross_down_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `adx_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `adx_cross_down_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `adx_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `adx_cross_down_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
