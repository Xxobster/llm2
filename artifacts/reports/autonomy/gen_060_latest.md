# Autonomy public-indicator hunt gen 060

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T133104Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `atrpos_cross_up_08` | one_head_filter_pi_star | 33 | 2.8680 | 2.0841 | 0.6061 | 1.7590 | 0.0239 | 0.2424 | TPM<MIN | RAN |
| ETHUSDT | 8 | `atrpos_cross_up_08` | one_head_filter_pi_star | 41 | 3.4307 | 1.8912 | 0.6098 | 1.6475 | 0.0229 | 0.2439 | TPM<MIN | RAN |
| ETHUSDT | 8 | `atrpos_high_at_h` | one_head_filter_pi_star | 154 | 12.5282 | 1.7470 | 0.6558 | 3.0066 | 0.0223 | 0.3766 | EBR>35% | RAN |
| ETHUSDT | 4 | `atrpos_high_at_h` | one_head_filter_pi_star | 136 | 11.0639 | 1.6001 | 0.6618 | 2.4614 | 0.0188 | 0.3824 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `atrpos_cross_up_08` | one_head_filter_pi_star | 19 | 1.5809 | 1.9481 | 0.6842 | 1.1863 | 0.0151 | 0.1579 | TPM<MIN | RAN |
| SOLUSDT | 8 | `atrpos_high_at_h` | one_head_filter_pi_star | 155 | 12.7061 | 1.7638 | 0.6323 | 2.9914 | 0.0137 | 0.4516 | EBR>35% | RAN |
| SOLUSDT | 4 | `atrpos_high_at_h` | one_head_filter_pi_star | 144 | 11.9468 | 1.6479 | 0.6181 | 2.5806 | 0.0121 | 0.4375 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 8 | `atrpos_high_at_h` | one_head_filter_pi_star | 22 | 1.8721 | 1.0725 | 0.4091 | 0.1357 | 0.0089 | 0.1364 | TPM<MIN | RAN |
| SOLUSDT | 8 | `atrpos_cross_up_08` | one_head_filter_pi_star | 38 | 3.1241 | 1.4324 | 0.6579 | 0.9922 | 0.0083 | 0.2105 | TPM<MIN | RAN |
| SOLUSDT | 8 | `atrpos_cross_down_02` | one_head_filter_pi_star | 16 | 1.3323 | 1.2901 | 0.5625 | 0.4682 | 0.0080 | 0.1250 | TPM<MIN | RAN |
| SOLUSDT | 4 | `atrpos_low_at_h` | one_head_filter_pi_star | 39 | 3.3802 | 1.3658 | 0.5641 | 0.7829 | 0.0039 | 0.1026 | TPM<MIN | RAN |
| BTCUSDT | 4 | `atrpos_high_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 1.0226 | 0.3810 | 0.0425 | 0.0029 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `atrpos_low_at_h` | one_head_filter_pi_star | 29 | 2.6336 | 1.1173 | 0.4828 | 0.2612 | 0.0018 | 0.1379 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `atrpos_low_at_h` | one_head_filter_pi_star | 34 | 3.1684 | 0.5715 | 0.4706 | -1.3540 | -0.0130 | 0.0294 | TPM<MIN | RAN |
| ETHUSDT | 4 | `atrpos_low_at_h` | one_head_filter_pi_star | 49 | 4.2274 | 0.5983 | 0.4694 | -1.3755 | -0.0135 | 0.0408 | ok | RAN |
| ETHUSDT | 4 | `atrpos_cross_down_02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `atrpos_cross_down_02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `atrpos_cross_down_02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `atrpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `atrpos_cross_up_08` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `atrpos_cross_down_02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `atrpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `atrpos_cross_up_08` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `atrpos_cross_down_02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
