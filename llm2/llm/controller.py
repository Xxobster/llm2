"""Phase B LLM research-controller layer.

Architecture (deliberately non-autonomous for trading decisions):
1. Store prompts / model answers / human corrections in SQLite.
2. Retrieve similar past mistakes by keyword overlap (local RAG light).
3. Optionally call a local Ollama OpenAI-compatible endpoint.
4. Periodically prepare LoRA training datasets from *verified* corrections only.
5. Promotion of any adapter requires a frozen evaluation suite + human approval.
   The LLM never receives a reward for profitable backtests alone.
"""

from __future__ import annotations

import json
import re
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from llm2.paths import ARTIFACTS
from llm2.registry.db import ResearchDB

PROMOTION_GATE = (
    "RESEARCH_ONLY — LLM output cannot change frozen params, relax gates, "
    "or enable live trading. Promotion requires frozen eval suite + human authorization."
)

LORA_MIN_VERIFIED = 50
LORA_DIR = ARTIFACTS / "llm" / "lora_candidates"


@dataclass
class LLMResponse:
    text: str
    retrieved: list[str]
    promotion_blocked: bool = True
    interaction_id: str = ""


class LLMController:
    def __init__(
        self,
        db: ResearchDB | None = None,
        *,
        ollama_url: str = "http://localhost:11434/v1",
        model: str = "qwen2.5:7b",
    ) -> None:
        self.db = db or ResearchDB()
        self.ollama_url = ollama_url
        self.model = model

    def _keywords(self, text: str) -> set[str]:
        return {w.lower() for w in re.findall(r"[a-zA-Z_]{3,}", text)}

    def retrieve_similar_mistakes(self, query: str, *, limit: int = 5) -> list[str]:
        q_kw = self._keywords(query)
        with self.db._connect() as conn:
            rows = conn.execute(
                "SELECT content, tags FROM interactions "
                "WHERE tags LIKE '%mistake%' OR tags LIKE '%feedback%' "
                "ORDER BY created_at DESC LIMIT 400"
            ).fetchall()
        scored: list[tuple[int, str]] = []
        for row in rows:
            content = row["content"]
            overlap = len(q_kw & self._keywords(content))
            if overlap:
                scored.append((overlap, content))
        scored.sort(reverse=True)
        return [c for _, c in scored[:limit]]

    def log_mistake(
        self,
        prompt: str,
        bad_answer: str,
        correction: str,
        *,
        evidence: str = "",
        verified_by: str = "human",
    ) -> str:
        """Store a verified correction for RAG + future LoRA."""
        payload = json.dumps(
            {
                "prompt": prompt,
                "bad_answer": bad_answer,
                "correction": correction,
                "evidence": evidence,
                "verified_by": verified_by,
            },
            ensure_ascii=False,
        )
        iid = self.db.log_interaction("correction", payload, tags="mistake,feedback,verified")
        self.log_feedback(iid, label="verified_correction", notes=evidence[:500])
        return iid

    def log_feedback(self, interaction_id: str, label: str, notes: str = "") -> None:
        fid = str(uuid.uuid4())
        with self.db._connect() as conn:
            conn.execute(
                "INSERT INTO feedback (feedback_id, interaction_id, label, notes, created_at) "
                "VALUES (?, ?, ?, ?, ?)",
                (fid, interaction_id, label, notes, datetime.now(timezone.utc).isoformat()),
            )
            conn.commit()

    def count_verified_corrections(self) -> int:
        with self.db._connect() as conn:
            row = conn.execute(
                "SELECT COUNT(*) AS n FROM interactions WHERE tags LIKE '%verified%'"
            ).fetchone()
        return int(row["n"] if row else 0)

    def export_lora_sft_jsonl(self, path: Path | None = None) -> Path | None:
        """Export verified corrections as SFT chat records. Returns path or None if too few."""
        n = self.count_verified_corrections()
        if n < LORA_MIN_VERIFIED:
            return None
        LORA_DIR.mkdir(parents=True, exist_ok=True)
        out = path or (LORA_DIR / f"sft_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.jsonl")
        with self.db._connect() as conn:
            rows = conn.execute(
                "SELECT content FROM interactions WHERE tags LIKE '%verified%' ORDER BY created_at"
            ).fetchall()
        with out.open("w", encoding="utf-8") as f:
            for row in rows:
                try:
                    obj = json.loads(row["content"])
                except json.JSONDecodeError:
                    continue
                rec = {
                    "messages": [
                        {"role": "user", "content": obj.get("prompt", "")},
                        {"role": "assistant", "content": obj.get("correction", "")},
                    ]
                }
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        return out

    def complete(self, prompt: str, *, use_ollama: bool = False) -> LLMResponse:
        retrieved = self.retrieve_similar_mistakes(prompt)
        context = "\n".join(f"- {r[:400]}" for r in retrieved)
        full_prompt = f"{PROMOTION_GATE}\n\nPast mistakes:\n{context}\n\nUser:\n{prompt}"

        if use_ollama:
            text = self._ollama_chat(full_prompt)
        else:
            text = (
                f"[stub] Acknowledged under {PROMOTION_GATE} "
                f"retrieved={len(retrieved)} verified={self.count_verified_corrections()}."
            )

        self.db.log_interaction("user", prompt, tags="llm")
        iid = self.db.log_interaction("assistant", text, tags="llm,response")
        return LLMResponse(text=text, retrieved=retrieved, promotion_blocked=True, interaction_id=iid)

    def _ollama_chat(self, prompt: str) -> str:
        try:
            import httpx

            payload = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": PROMOTION_GATE},
                    {"role": "user", "content": prompt},
                ],
                "stream": False,
            }
            r = httpx.post(f"{self.ollama_url}/chat/completions", json=payload, timeout=120.0)
            r.raise_for_status()
            data: dict[str, Any] = r.json()
            return data["choices"][0]["message"]["content"]
        except Exception as exc:  # noqa: BLE001
            return f"[ollama unavailable: {exc}] {PROMOTION_GATE}"
