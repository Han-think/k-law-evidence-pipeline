# K-Law Evidence Pipeline

**K-Law Evidence Pipeline** is a local-first legal evidence and document drafting assistant for ordinary people.

It helps users organize facts, timelines, evidence, official legal sources, and draft documents before they contact a lawyer, public legal aid office, court, agency, consumer protection body, or media outlet.

> This project does **not** replace lawyers, courts, public legal aid, or licensed legal advice. It is a document preparation and evidence organization tool.

한국어 문서는 [README.ko.md](./README.ko.md)를 보세요.  
English documentation is available at [README.en.md](./README.en.md).

---

## Why this project exists

Legal help can be expensive, slow, and difficult to access. Many people face real harm but cannot clearly organize what happened, when it happened, what evidence exists, and which official legal sources may be relevant.

This project aims to reduce that burden by providing a free, local-first, source-focused workflow.

The goal is simple:

**Help ordinary people turn scattered memories, screenshots, messages, calls, notices, and documents into a structured evidence pack and a draft document.**

---

## Core principles

1. **Local-first privacy**  
   Case notes, evidence files, and personal information should remain on the user's machine by default.

2. **Official-source evidence**  
   Legal references should come from official statutes, court decisions, administrative decisions, or trusted public legal databases whenever possible.

3. **No fake certainty**  
   The system must not say "you will win", "you are guaranteed compensation", or "this is final legal advice".

4. **Facts first**  
   Separate facts, assumptions, emotions, evidence, claims, and missing materials.

5. **Country-adaptable architecture**  
   The first implementation targets Korean legal materials, but the pipeline is designed so other countries can replace the legal-source adapter with their own official law and case databases.

---

## Initial focus

The first MVP focuses on Korean cases where ordinary people often need structured documents:

- personal data leaks and privacy compensation claims
- telecom service disputes and service interruption compensation
- e-commerce refund / contract non-performance disputes
- basic small civil claim preparation
- public petition / complaint / demand letter drafting

---

## Planned workflow

```text
User notes / memories / files
→ privacy masking
→ fact extraction
→ timeline building
→ evidence list generation
→ legal issue extraction
→ official law / case source retrieval
→ citation verification
→ draft document generation
→ missing evidence checklist
→ opposing argument review
```

---

## MCP direction

This repository includes an early MCP-oriented design.

The MCP server should act as an **official evidence retrieval and citation verification layer**, not as a legal judgment engine.

Planned MCP tools:

- `search_law`
- `get_article`
- `search_case`
- `verify_citation`
- `make_evidence_pack`
- `mask_sensitive_text`

The LLM should write and organize.  
The MCP should retrieve and verify official sources.  
The human user should make final decisions.

---

## Security notice

Do not send private case files or sensitive personal details to external APIs without review and masking.

External LLM APIs may be useful for cost reduction and drafting quality, but they should be optional. The default mode should be local storage and local processing where possible.

---

## Legal notice

This project is for legal information organization and document drafting assistance only. It does not provide legal advice, legal representation, or guaranteed legal outcomes. Users should verify all legal citations and consult a qualified legal professional or public legal aid service before official submission.

---

## Status

Early planning / scaffold stage.  
The repository will grow into a local-first CLI and MCP-based legal evidence pipeline.
