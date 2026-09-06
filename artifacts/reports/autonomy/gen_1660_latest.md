# Autonomy public-indicator hunt gen 1660

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T000534Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema996_above_at_h` | one_head_filter_pi_star | 127 | 10.3556 | 1.1221 | 0.5748 | 0.5563 | 0.0022 | 0.1417 | ok | RAN |
| SOLUSDT | 8 | `ema996_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.0922 | 0.5798 | 0.4179 | 0.0017 | 0.1345 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema996_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 0.9930 | 0.5545 | -0.0468 | -0.0002 | 0.1545 | ok | RAN |
| SOLUSDT | 8 | `ema996_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 0.9866 | 0.5444 | -0.0896 | -0.0003 | 0.1290 | ok | RAN |
| ETHUSDT | 4 | `ema996_above_at_h` | one_head_filter_pi_star | 138 | 11.3889 | 0.9893 | 0.5652 | -0.0526 | -0.0005 | 0.1232 | ok | RAN |
| SOLUSDT | 4 | `ema996_below_at_h` | one_head_filter_pi_star | 237 | 19.3797 | 0.9779 | 0.5485 | -0.1437 | -0.0005 | 0.1181 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema996_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 0.8960 | 0.5346 | -0.7453 | -0.0033 | 0.1567 | ok | RAN |
| ETHUSDT | 8 | `ema996_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 0.8433 | 0.5391 | -0.7767 | -0.0067 | 0.1172 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema996_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema996_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema996_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema996_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema996_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema996_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema996_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema996_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema996_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema996_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema996_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema996_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema996_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema996_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema996_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema996_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
