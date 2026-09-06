# Autonomy public-indicator hunt gen 730

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T092058Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret584_neg_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.2414 | 0.7181 | 4.7442 | 0.0259 | 0.3723 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret584_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.0715 | 0.7006 | 4.1688 | 0.0233 | 0.3772 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret584_neg_at_h` | one_head_filter_pi_star | 220 | 17.9896 | 1.8003 | 0.6682 | 3.6805 | 0.0129 | 0.3182 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret584_neg_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.8079 | 0.6667 | 3.4887 | 0.0127 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret584_pos_at_h` | one_head_filter_pi_star | 113 | 9.3923 | 1.6459 | 0.6549 | 2.1998 | 0.0094 | 0.3186 | ok | RAN |
| SOLUSDT | 4 | `ret584_pos_at_h` | one_head_filter_pi_star | 104 | 8.6442 | 1.6020 | 0.6442 | 2.0968 | 0.0089 | 0.3365 | ok | RAN |
| ETHUSDT | 8 | `ret584_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.1781 | 0.5902 | 0.9234 | 0.0068 | 0.2186 | ok | RAN |
| ETHUSDT | 4 | `ret584_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.1485 | 0.5806 | 0.7877 | 0.0058 | 0.2151 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret584_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0585 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret584_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0596 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret584_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret584_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret584_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret584_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret584_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret584_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret584_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret584_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret584_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret584_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret584_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret584_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret584_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret584_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
