# Autonomy public-indicator hunt gen 1140

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T034124Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema919_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 1.8862 | 0.6667 | 4.1230 | 0.0207 | 0.3419 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema919_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 1.8425 | 0.6624 | 4.0082 | 0.0200 | 0.3547 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema919_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 1.7570 | 0.6429 | 3.7286 | 0.0118 | 0.3016 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema919_below_at_h` | one_head_filter_pi_star | 221 | 18.0714 | 1.7485 | 0.6561 | 3.4618 | 0.0115 | 0.3167 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema919_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.7292 | 0.6532 | 2.4968 | 0.0106 | 0.3065 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema919_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.6426 | 0.6333 | 2.2670 | 0.0097 | 0.3000 | ok | RAN |
| ETHUSDT | 8 | `ema919_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 1.2180 | 0.6016 | 0.9537 | 0.0084 | 0.2188 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema919_above_at_h` | one_head_filter_pi_star | 119 | 9.7816 | 1.0118 | 0.5546 | 0.0541 | 0.0005 | 0.2101 | ok | RAN |
| BTCUSDT | 4 | `ema919_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema919_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema919_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema919_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema919_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema919_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema919_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema919_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema919_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema919_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema919_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema919_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema919_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema919_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema919_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema919_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
