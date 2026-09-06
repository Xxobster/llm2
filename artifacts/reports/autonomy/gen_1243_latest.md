# Autonomy public-indicator hunt gen 1243

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T144323Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma634_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0000 | 0.6811 | 4.2106 | 0.0235 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma634_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9553 | 0.6809 | 4.1120 | 0.0226 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma634_below_at_h` | one_head_filter_pi_star | 201 | 16.3517 | 1.7978 | 0.6567 | 3.4692 | 0.0123 | 0.3234 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma634_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.7747 | 0.6667 | 3.3502 | 0.0120 | 0.3281 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma634_above_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.5508 | 0.6107 | 2.2680 | 0.0085 | 0.3154 | ok | RAN |
| SOLUSDT | 8 | `sma634_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.5010 | 0.6043 | 2.0411 | 0.0082 | 0.3165 | ok | RAN |
| ETHUSDT | 8 | `sma634_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.1820 | 0.6051 | 0.9029 | 0.0066 | 0.2038 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma634_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.0131 | 0.5806 | 0.0708 | 0.0005 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `sma634_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma634_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma634_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma634_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma634_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma634_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma634_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma634_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma634_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma634_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma634_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma634_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma634_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma634_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma634_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma634_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
