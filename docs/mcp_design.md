# MCP Design

The MCP server is the official-source evidence layer.

It should not act as a judge. It should not make final legal conclusions. It should retrieve, normalize, and verify source material.

## Tool list

### search_law

Search statutes or official legal materials by keyword.

Input:

```json
{
  "query": "개인정보보호법 손해배상",
  "jurisdiction": "KR"
}
```

Output:

```json
{
  "results": [
    {
      "title": "개인정보 보호법",
      "source_authority": "National Law Information Center",
      "official_url": "...",
      "reliability_grade": "A"
    }
  ]
}
```

### get_article

Get a specific statute article when the source adapter supports it.

### search_case

Search case law or decisions.

### verify_citation

Check whether a citation contains enough metadata.

### make_evidence_pack

Build a source-aware pack for a user case.

### mask_sensitive_text

Mask private details before optional external API usage.

## Output rule

Every legal source result should include:

- source type
- authority
- title
- identifier
- date or effective date
- retrieved date
- official URL if available
- source excerpt
- reliability grade
- limitation note

## Reliability grade

- A: official source direct result
- B: official explanation or agency material
- C: trusted public institution material
- D: media or secondary source
- X: unverified
