# Tool Contracts

This document defines stable MCP tool boundaries.

## Principle

Tools retrieve, normalize, and verify source material. They do not make final decisions.

## search_law

Purpose: find statute or regulation candidates.

Input fields:

- query: string
- jurisdiction: string, default KR
- limit: integer, default 10

Output fields:

- status
- results
- note

Each result should use SourceEnvelope.

## get_article

Purpose: retrieve a specific article from a resolved source.

Input fields:

- law_name
- article
- jurisdiction
- effective_date optional

Output fields:

- status
- result
- limitation_note

Rule: never fabricate article text. If source retrieval fails, return an explicit error or placeholder.

## search_case

Purpose: find case or decision candidates.

Input fields:

- query
- jurisdiction
- limit

Output fields:

- status
- results

## verify_citation

Purpose: check whether a citation has enough metadata for drafting.

Required metadata:

- title
- identifier
- source authority
- source URL
- date field

This is a metadata check unless direct source retrieval is available.

## make_evidence_pack

Purpose: create a draft evidence-pack outline from a case summary.

Output sections:

- facts timeline
- material list
- issue candidates
- official source candidates
- missing materials
- possible counterarguments
- drafting notes

## mask_sensitive_text

Purpose: mask common private patterns before optional external API use.

This is a helper only. Human review is still required.
