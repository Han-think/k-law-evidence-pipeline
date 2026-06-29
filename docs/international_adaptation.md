# International Adaptation

This project starts with Korean public legal sources, but the pipeline is not Korea-only.

The reusable structure is:

```text
facts
→ timeline
→ evidence list
→ issue candidates
→ official source lookup
→ citation check
→ draft document
→ checklist
```

## To adapt it to another country

Replace:

- statute source adapter
- case source adapter
- citation format
- document templates
- public filing terms
- language style rules

## What should stay the same

- local-first storage
- separation of fact, claim, and material
- official-source metadata
- no fake certainty
- draft-first output
- missing material checklist
- counterargument review

## Source envelope

Each country adapter should return:

- source type
- source authority
- title
- identifier
- date
- retrieved date
- official URL if available
- text excerpt
- reliability grade

The goal is not to export Korean law. The goal is to export a safer structure for civic legal preparation.
