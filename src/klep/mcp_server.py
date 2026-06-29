"""MCP server for K-Law Evidence Pipeline.

Run:
    klep-mcp

This server exposes safe, source-oriented tools. It does not provide final legal advice.
"""

from __future__ import annotations

import asyncio
from typing import Any

from mcp.server.fastmcp import FastMCP

from klep.law_sources.korea_openlaw import KoreaOpenLawAdapter
from klep.security.pii_masker import mask_sensitive_text as _mask_sensitive_text

mcp = FastMCP("k-law-evidence-pipeline")
adapter = KoreaOpenLawAdapter()


@mcp.tool()
def mask_sensitive_text(text: str) -> str:
    """Mask common private details before optional external API use."""
    return _mask_sensitive_text(text)


@mcp.tool()
def search_law(query: str, jurisdiction: str = "KR", limit: int = 10) -> dict[str, Any]:
    """Search official legal source candidates.

    This returns candidates and metadata. It does not provide final legal advice.
    """
    if jurisdiction != "KR":
        return {
            "status": "unsupported_jurisdiction",
            "message": "Only KR adapter scaffold is available in MVP.",
            "results": [],
        }
    results = asyncio.run(adapter.search_law(query=query, limit=limit))
    return {"status": "ok", "results": [r.model_dump(mode="json") for r in results]}


@mcp.tool()
def search_case(query: str, jurisdiction: str = "KR", limit: int = 10) -> dict[str, Any]:
    """Search public case or decision candidates."""
    if jurisdiction != "KR":
        return {
            "status": "unsupported_jurisdiction",
            "message": "Only KR adapter scaffold is available in MVP.",
            "results": [],
        }
    results = asyncio.run(adapter.search_case(query=query, limit=limit))
    return {"status": "ok", "results": [r.model_dump(mode="json") for r in results]}


@mcp.tool()
def get_article(law_name: str, article: str, jurisdiction: str = "KR") -> dict[str, Any]:
    """Return a statute article envelope when implemented by the adapter.

    MVP currently returns a placeholder instead of fabricating article text.
    """
    if jurisdiction != "KR":
        return {
            "status": "unsupported_jurisdiction",
            "message": "Only KR adapter scaffold is available in MVP.",
            "result": None,
        }
    result = asyncio.run(adapter.get_article(law_name=law_name, article=article))
    return {"status": "ok", "result": result.model_dump(mode="json") if result else None}


@mcp.tool()
def verify_citation(
    title: str,
    identifier: str | None = None,
    source_authority: str | None = None,
    official_url: str | None = None,
    effective_date: str | None = None,
) -> dict[str, Any]:
    """Check whether a citation has minimum metadata for safe drafting."""
    missing: list[str] = []
    if not title:
        missing.append("title")
    if not identifier:
        missing.append("identifier")
    if not source_authority:
        missing.append("source_authority")
    if not official_url:
        missing.append("official_url")
    if not effective_date:
        missing.append("effective_date_or_decision_date")

    return {
        "verified": len(missing) == 0,
        "missing": missing,
        "note": "Metadata check only. Official source text still needs direct verification.",
    }


@mcp.tool()
def make_evidence_pack(summary: str, jurisdiction: str = "KR") -> dict[str, Any]:
    """Create a lightweight evidence-pack outline from a case summary."""
    masked_summary = _mask_sensitive_text(summary)
    return {
        "jurisdiction": jurisdiction,
        "summary_masked": masked_summary,
        "sections": [
            "facts_timeline",
            "evidence_list",
            "legal_issue_candidates",
            "official_source_candidates",
            "missing_materials",
            "possible_counterarguments",
            "draft_document_notes",
        ],
        "notice": "This is an outline. It is not legal advice or a final filing document.",
    }


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
