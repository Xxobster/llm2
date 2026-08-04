from pathlib import Path

import yaml

from llm2.live.certificate import pack_fingerprint

roots = {
    "ETH": Path("/opt/llm2-structure-eth"),
    "SOL": Path("/opt/llm2-structure-sol"),
    "BTC": Path("/opt/llm2-structure"),
}
for name, root in roots.items():
    pack = root / "pack"
    fp = pack_fingerprint(pack)
    print(name, fp)
    cert_path = root / ("certificate.yaml" if name != "BTC" else "structure_v1_lgbm_certificate.yaml")
    if not cert_path.is_file():
        print(" missing cert", cert_path)
        continue
    raw = yaml.safe_load(cert_path.read_text(encoding="utf-8"))
    old = raw.get("pack_hash")
    if fp and old != fp:
        raw["pack_hash"] = fp
        cert_path.write_text(
            yaml.safe_dump(raw, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        print("  cert restamped", old, "->", fp)
    else:
        print("  cert ok")
    (pack / "pack_hash.txt").write_text((fp or "") + "\n", encoding="utf-8")
