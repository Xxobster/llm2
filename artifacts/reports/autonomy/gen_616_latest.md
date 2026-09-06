# Autonomy public-indicator hunt gen 616

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T013236Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1140_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 2.1079 | 0.6833 | 4.5851 | 0.0247 | 0.3529 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1140_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0525 | 0.6952 | 4.1871 | 0.0228 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1140_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.8144 | 0.6446 | 3.8359 | 0.0125 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1140_below_at_h` | one_head_filter_pi_star | 261 | 21.2329 | 1.7601 | 0.6398 | 3.8057 | 0.0118 | 0.3142 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1140_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.8494 | 0.6696 | 2.7232 | 0.0118 | 0.2957 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma1140_above_at_h` | one_head_filter_pi_star | 111 | 9.1025 | 1.5511 | 0.6306 | 1.9129 | 0.0082 | 0.2793 | ok | RAN |
| ETHUSDT | 8 | `sma1140_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 1.0722 | 0.5703 | 0.3343 | 0.0029 | 0.2031 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1140_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 1.0071 | 0.5455 | 0.0332 | 0.0003 | 0.1970 | ok | RAN |
| BTCUSDT | 8 | `sma1140_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0521 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1140_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
