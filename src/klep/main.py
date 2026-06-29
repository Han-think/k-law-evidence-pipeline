"""CLI entry point."""

from __future__ import annotations

import json
from pathlib import Path

import typer
from rich import print

from klep.security.pii_masker import mask_sensitive_text

app = typer.Typer(help="K-Law Evidence Pipeline CLI")


@app.command()
def mask(text: str) -> None:
    print(mask_sensitive_text(text))


@app.command("new-case")
def new_case(case_id: str, case_type: str = "general", output: Path = Path("case.json")) -> None:
    data = {
        "case_id": case_id,
        "case_type": case_type,
        "jurisdiction": "KR",
        "language": "ko",
        "summary": "",
        "facts": [],
        "evidence": [],
        "legal_issues": [],
        "requested_outcomes": [],
    }
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"created {output}")


@app.command("status")
def status() -> None:
    print("K-Law Evidence Pipeline CLI is ready.")
    print("MCP server entry point: klep-mcp")


if __name__ == "__main__":
    app()
