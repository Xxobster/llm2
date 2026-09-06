# Autonomy public-indicator hunt gen 2115

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T000803Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma755_below_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.1475 | 0.5758 | 0.8314 | 0.0043 | 0.1818 | ok | RAN |
| ETHUSDT | 4 | `sma755_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.1486 | 0.5852 | 0.8408 | 0.0042 | 0.1818 | ok | RAN |
| SOLUSDT | 4 | `sma755_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.0937 | 0.5448 | 0.4343 | 0.0017 | 0.1119 | ok | RAN |
| SOLUSDT | 8 | `sma755_above_at_h` | one_head_filter_pi_star | 120 | 9.8406 | 1.0372 | 0.5333 | 0.1771 | 0.0007 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma755_below_at_h` | one_head_filter_pi_star | 221 | 17.9788 | 0.9925 | 0.5520 | -0.0471 | -0.0002 | 0.1312 | ok | RAN |
| SOLUSDT | 4 | `sma755_below_at_h` | one_head_filter_pi_star | 217 | 17.6534 | 0.9384 | 0.5484 | -0.3954 | -0.0013 | 0.1244 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma755_above_at_h` | one_head_filter_pi_star | 136 | 11.1790 | 0.8562 | 0.5515 | -0.7129 | -0.0062 | 0.0956 | ok | RAN |
| ETHUSDT | 8 | `sma755_above_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 0.8148 | 0.5444 | -1.0767 | -0.0077 | 0.1065 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma755_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma755_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0595 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma755_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma755_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
