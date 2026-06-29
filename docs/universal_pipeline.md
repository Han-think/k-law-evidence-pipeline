# Universal Legal Evidence Pipeline

This document describes the country-neutral structure.

## Universal stages

```text
1. Intake
2. Privacy masking
3. Fact extraction
4. Timeline creation
5. Material list creation
6. Issue classification
7. Official source lookup
8. Citation verification
9. Draft generation
10. Review checklist
11. Export
```

## Stage outputs

### Intake

Raw user notes and files.

### Privacy masking

A safer text version for optional external processing.

### Fact extraction

Structured facts separated from assumptions and requests.

### Timeline creation

Date-based events.

### Material list creation

Materials mapped to the facts they support.

### Issue classification

Country-neutral issue categories and country-specific legal categories.

### Official source lookup

Source candidates from official or trusted databases.

### Citation verification

Metadata check and source reliability grade.

### Draft generation

Draft document with source candidates and review notes.

### Review checklist

Missing material, weak support, and possible counterarguments.

### Export

Markdown first. DOCX or PDF may be added later.

## Rule

The universal pipeline should not assume one country's law. Country logic belongs in adapters and templates.
