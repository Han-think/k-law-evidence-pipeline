# Output Schema

Public MCP clients need predictable output.

## Standard response

```json
{
  "status": "ok",
  "results": [],
  "errors": [],
  "warnings": [],
  "notice": "draft or source-candidate notice"
}
```

## Status values

- ok
- partial
- not_configured
- unsupported_jurisdiction
- source_unavailable
- validation_error
- error

## SourceEnvelope result

```json
{
  "source_type": "statute_search_result",
  "source_authority": "National Law Information Center",
  "jurisdiction": "KR",
  "title": "source title",
  "identifier": "source id",
  "effective_date": null,
  "retrieved_at": "timestamp",
  "official_url": "url",
  "text_excerpt": "short excerpt",
  "reliability_grade": "A",
  "limitation_note": "search result only",
  "raw": {}
}
```

## Error object

```json
{
  "code": "not_configured",
  "message": "OPENLAW_OC is not configured.",
  "retryable": false
}
```

## Rule

If source retrieval fails, return a structured error. Do not replace missing source text with generated text.
