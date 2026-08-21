#!/usr/bin/env python3
"""Backward-compatible entry → ``ops_fleet_live_signal_parity``.

Prefer the named gate::

  python scripts/ops_fleet_live_signal_parity.py
"""

from __future__ import annotations

from scripts.ops_fleet_live_signal_parity import main

if __name__ == "__main__":
    raise SystemExit(main())
