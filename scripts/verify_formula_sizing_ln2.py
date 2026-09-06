"""Read-only health check after formula sizing + live_guards fix."""

from __future__ import annotations

import subprocess

SSH = "ln2"


def out(cmd: str) -> str:
    return subprocess.check_output(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=25", SSH, cmd],
        text=True,
    )


def main() -> int:
    print("ACTIVE", out("systemctl is-active llm2-quad-btc-1h.service llm2-fvg-sol-1h.service"))
    print("BTC_UNIT", out(
        "systemctl show llm2-quad-btc-1h.service -p ActiveState -p SubState -p NRestarts -p Result -p MainPID"
    ))
    print("SOL_UNIT", out(
        "systemctl show llm2-fvg-sol-1h.service -p ActiveState -p SubState -p NRestarts -p Result -p MainPID"
    ))
    print("LLM2_UNITS", out("systemctl list-units --type=service --all llm2* --no-legend --no-pager"))
    print("SIZING", out(
        "python3 - <<'PY'\n"
        "import json\n"
        "b=json.load(open('/opt/llm2-quad-btc-1h/pack/strategy.json'))\n"
        "s=json.load(open('/opt/llm2-fvg-sol-1h/pack/strategy.json'))\n"
        "print('btc', b['sizing'])\n"
        "print('sol', s['sizing'])\n"
        "PY"
    ))
    print("HASHES", out(
        "echo BTC; cat /opt/llm2-quad-btc-1h/pack/pack_hash.txt; echo; "
        "echo SOL; cat /opt/llm2-fvg-sol-1h/pack/pack_hash.txt"
    ))
    print("BTC_TAIL", out("tail -n 8 /opt/llm2-quad-btc-1h/logs/ema_live.log"))
    print("SOL_TAIL", out("tail -n 12 /opt/llm2-fvg-sol-1h/logs/ema_live.log"))
    print("POSTFIX_ERRORS", out(
        "python3 - <<'PY'\n"
        "from pathlib import Path\n"
        "cut='2026-09-04T09:56:50Z'\n"
        "for p in ('/opt/llm2-quad-btc-1h/logs/ema_live.log','/opt/llm2-fvg-sol-1h/logs/ema_live.log'):\n"
        "    hits=[]\n"
        "    for line in Path(p).read_text(errors='replace').splitlines():\n"
        "        if line[:20] >= cut[:20] and any(k in line for k in ('Traceback','ImportError','Error')):\n"
        "            hits.append(line[:240])\n"
        "    print(p, 'n=', len(hits))\n"
        "    for h in hits[-6:]:\n"
        "        print(' ', h)\n"
        "PY"
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
