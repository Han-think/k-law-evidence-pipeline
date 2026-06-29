"""Korean public legal information adapter.

This is an early best-effort adapter for the National Law Information Center API.
Users must provide their own Open Law API OC value in OPENLAW_OC.

Official portals:
- https://www.law.go.kr
- https://open.law.go.kr
"""

from __future__ import annotations

import os
from typing import Any

import httpx

from klep.evidence.schema import ReliabilityGrade, SourceEnvelope
from klep.law_sources.base import LawSourceAdapter


class KoreaOpenLawAdapter(LawSourceAdapter):
    jurisdiction = "KR"

    def __init__(self, oc: str | None = None, base_url: str | None = None) -> None:
        self.oc = oc or os.getenv("OPENLAW_OC", "")
        self.base_url = (base_url or os.getenv("OPENLAW_BASE_URL", "https://www.law.go.kr")).rstrip("/")

    async def search_law(self, query: str, limit: int = 10) -> list[SourceEnvelope]:
        if not self.oc:
            return [self._missing_key_envelope("OPENLAW_OC is not configured.")]

        params: dict[str, Any] = {
            "OC": self.oc,
            "target": "law",
            "type": "JSON",
            "query": query,
        }
        url = f"{self.base_url}/DRF/lawSearch.do"
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

        items = data.get("LawSearch", {}).get("law", [])
        if isinstance(items, dict):
            items = [items]

        results: list[SourceEnvelope] = []
        for item in items[:limit]:
            title = item.get("법령명한글") or item.get("법령명") or item.get("lawName") or query
            identifier = str(item.get("법령일련번호") or item.get("MST") or item.get("lawId") or "")
            results.append(
                SourceEnvelope(
                    source_type="statute_search_result",
                    source_authority="National Law Information Center",
                    jurisdiction="KR",
                    title=title,
                    identifier=identifier or None,
                    official_url=self.base_url,
                    text_excerpt=str(item)[:500],
                    reliability_grade=ReliabilityGrade.A,
                    limitation_note="Search result only. Fetch article text separately before citation.",
                    raw=item,
                )
            )
        return results

    async def get_article(self, law_name: str, article: str) -> SourceEnvelope | None:
        # Full article retrieval requires a resolved law identifier from search_law.
        # This placeholder intentionally avoids fabricating statute text.
        return SourceEnvelope(
            source_type="statute_article_placeholder",
            source_authority="National Law Information Center",
            jurisdiction="KR",
            title=law_name,
            identifier=article,
            official_url=self.base_url,
            text_excerpt=None,
            reliability_grade=ReliabilityGrade.X,
            limitation_note="Article retrieval is not implemented yet. Use official source verification before citation.",
        )

    async def search_case(self, query: str, limit: int = 10) -> list[SourceEnvelope]:
        if not self.oc:
            return [self._missing_key_envelope("OPENLAW_OC is not configured.")]

        params: dict[str, Any] = {
            "OC": self.oc,
            "target": "prec",
            "type": "JSON",
            "query": query,
        }
        url = f"{self.base_url}/DRF/lawSearch.do"
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

        items = data.get("PrecSearch", {}).get("prec", [])
        if isinstance(items, dict):
            items = [items]

        results: list[SourceEnvelope] = []
        for item in items[:limit]:
            title = item.get("사건명") or item.get("판례일련번호") or query
            identifier = str(item.get("사건번호") or item.get("판례일련번호") or "")
            results.append(
                SourceEnvelope(
                    source_type="case_search_result",
                    source_authority="National Law Information Center",
                    jurisdiction="KR",
                    title=title,
                    identifier=identifier or None,
                    official_url=self.base_url,
                    text_excerpt=str(item)[:500],
                    reliability_grade=ReliabilityGrade.A,
                    limitation_note="Search result only. Fetch full decision before citation.",
                    raw=item,
                )
            )
        return results

    def _missing_key_envelope(self, message: str) -> SourceEnvelope:
        return SourceEnvelope(
            source_type="configuration_notice",
            source_authority="local",
            jurisdiction="KR",
            title="Configuration required",
            text_excerpt=message,
            reliability_grade=ReliabilityGrade.X,
            limitation_note="Set OPENLAW_OC in .env before using official API calls.",
        )
