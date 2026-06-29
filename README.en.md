# K-Law Evidence Pipeline

**K-Law Evidence Pipeline** is a local-first evidence and document drafting assistant for ordinary people facing legal or administrative disputes.

It starts with Korean public legal information, but the structure is designed so other countries can replace the source adapter with their own official legal databases.

This is not a lawyer replacement. It is a preparation tool.

---

## Purpose

Legal help can be expensive and slow. Many people need a way to organize their case before they ask for professional help.

This project helps users organize:

- what happened
- when it happened
- what materials exist
- what is still missing
- which official sources may be relevant
- what a draft document may look like

---

## Adaptable architecture

For another country, replace:

- statute source adapter
- case law source adapter
- citation format
- document templates
- privacy rules
- filing rules
- language style rules

The pipeline remains:

```text
user facts
→ timeline
→ evidence list
→ issue extraction
→ official source retrieval
→ citation verification
→ draft document
→ review checklist
```

---

## Safety model

The system must not provide fake certainty.

It should not say:

- "You will win."
- "You are guaranteed compensation."
- "This is final legal advice."

It should say:

- "This is a draft."
- "This citation needs verification."
- "This claim needs support."
- "This argument may face counterarguments."

---

## External AI APIs

External AI APIs can reduce cost and improve drafting quality. They should be optional. Local storage and local processing should be the default.

Before sending text to an external API, the user should be able to mask private details, preview the outgoing text, and approve the action.

---

## Social goal

This project is intended to be free and open so that people with limited resources can prepare clearer documents and better evidence packs before seeking help.
