# Autonomy public-indicator hunt gen 1733

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T081615Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret291_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.2103 | 0.6061 | 1.1280 | 0.0063 | 0.1879 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret291_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1066 | 0.5955 | 0.6491 | 0.0034 | 0.1798 | ok | RAN |
| SOLUSDT | 4 | `ret291_neg_at_h` | one_head_filter_pi_star | 135 | 11.0391 | 1.0871 | 0.5704 | 0.4223 | 0.0018 | 0.1630 | ok | RAN |
| SOLUSDT | 8 | `ret291_pos_at_h` | one_head_filter_pi_star | 174 | 14.2689 | 1.0648 | 0.5632 | 0.3470 | 0.0011 | 0.1092 | ok | RAN |
| SOLUSDT | 8 | `ret291_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 1.0297 | 0.5562 | 0.1650 | 0.0006 | 0.1538 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret291_pos_at_h` | one_head_filter_pi_star | 162 | 13.2095 | 0.9600 | 0.5309 | -0.2170 | -0.0008 | 0.0988 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret291_pos_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 0.9276 | 0.5636 | -0.4153 | -0.0028 | 0.1091 | ok | RAN |
| ETHUSDT | 4 | `ret291_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8367 | 0.5359 | -1.0042 | -0.0065 | 0.1105 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret291_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4194 | 0.3000 | -1.4074 | -0.0686 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret291_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0727 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret291_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret291_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret291_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret291_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret291_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret291_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret291_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret291_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret291_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret291_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret291_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret291_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret291_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret291_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
