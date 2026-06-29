"""Local probe for OpenLaw API responses.

Usage:
    python scripts/openlaw_probe.py "개인정보 보호법"

Do not commit real API values. Set OPENLAW_OC in your local .env or shell.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys

import httpx
from dotenv import load_dotenv


async def main() -> None:
    load_dotenv()
    query = sys.argv[1] if len(sys.argv) > 1 else "개인정보 보호법"
    oc = os.getenv("OPENLAW_OC", "")
    if not oc:
        raise SystemExit("OPENLAW_OC is not set")

    url = "https://www.law.go.kr/DRF/lawSearch.do"
    params = {"OC": oc, "target": "law", "type": "JSON", "query": query}
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    print(json.dumps(data, ensure_ascii=False, indent=2)[:8000])


if __name__ == "__main__":
    asyncio.run(main())
