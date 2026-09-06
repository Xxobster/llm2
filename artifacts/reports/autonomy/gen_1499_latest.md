# Autonomy public-indicator hunt gen 1499

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T024229Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma674_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.1676 | 0.6919 | 4.6101 | 0.0259 | 0.3946 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma674_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9769 | 0.6788 | 4.1064 | 0.0230 | 0.3938 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma674_below_at_h` | one_head_filter_pi_star | 205 | 16.6772 | 1.8192 | 0.6634 | 3.5494 | 0.0122 | 0.3171 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma674_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.6633 | 0.6546 | 3.0337 | 0.0108 | 0.3247 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma674_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.5098 | 0.6074 | 2.0449 | 0.0082 | 0.3259 | ok | RAN |
| SOLUSDT | 4 | `sma674_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.4898 | 0.6077 | 1.8909 | 0.0077 | 0.3308 | ok | RAN |
| ETHUSDT | 8 | `sma674_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 1.1363 | 0.5890 | 0.6708 | 0.0049 | 0.2192 | ok | RAN |
| ETHUSDT | 4 | `sma674_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.1215 | 0.5932 | 0.6460 | 0.0046 | 0.2147 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma674_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma674_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma674_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma674_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma674_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma674_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma674_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma674_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma674_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma674_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma674_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma674_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma674_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma674_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma674_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma674_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
