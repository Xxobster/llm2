# sol_1h_power_ema_stack_long

Solana 1-hour `power_ema_stack_long`. Post-Only entry, cancel if no touch. Stop = clip(1.5 × Average True Range %, 0.4%, 3%). Leverage 13× from the 3% cap. Size = 5% of equity at that bar's stop, floored to Bybit qty_step 0.1. Not Shadow-Ready.
