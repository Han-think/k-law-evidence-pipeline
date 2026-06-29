# Jurisdiction Adapter Contract

The project starts with Korea, but the architecture should allow other countries to add their own legal source adapters.

## Adapter goals

A jurisdiction adapter connects the pipeline to country-specific public legal information sources.

It must not change the core safety model:

- no fake certainty
- source metadata required
- local-first case handling
- draft-first output
- human final decision

## Required adapter methods

```python
async def search_law(query: str, limit: int = 10) -> list[SourceEnvelope]: ...
async def get_article(law_name: str, article: str) -> SourceEnvelope | None: ...
async def search_case(query: str, limit: int = 10) -> list[SourceEnvelope]: ...
```

## Recommended optional methods

```python
async def get_case_detail(identifier: str) -> SourceEnvelope | None: ...
async def search_regulation(query: str, limit: int = 10) -> list[SourceEnvelope]: ...
async def search_agency_decision(query: str, limit: int = 10) -> list[SourceEnvelope]: ...
async def compare_article_by_date(law_name: str, article: str, date_a: str, date_b: str) -> dict: ...
```

## Required source metadata

Every source result should include:

- jurisdiction
- source type
- source authority
- title
- identifier
- date or effective date when available
- retrieved date
- official URL when available
- text excerpt
- reliability grade
- limitation note

## Country profile

Each jurisdiction should also define:

- primary legal database
- case database
- citation style
- official language
- supported document templates
- privacy rules for local handling
- unsupported features

## Rule

If an adapter cannot retrieve official text, it must return a clear limitation note. It must not generate missing legal text.
