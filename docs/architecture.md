# Architecture

The pipeline is designed around replaceable blocks. Each block has a narrow role, a clear input, and a clear output.

```text
Input
→ Privacy / masking block
→ Intake parser
→ Timeline builder
→ Evidence list builder
→ Legal issue extractor
→ Official source adapter
→ Citation verifier
→ Evidence pack builder
→ Draft generator
→ Review checklist
→ Exporter
```

## Block responsibilities

### Privacy / masking block

Masks private details before text is sent to optional external services.

### Intake parser

Splits user notes into facts, assumptions, emotions, requested outcomes, and materials.

### Timeline builder

Creates a date-based event table.

### Evidence list builder

Maps each piece of material to the fact it supports.

### Legal issue extractor

Suggests issue categories such as privacy leak, telecom dispute, refund dispute, contract non-performance, or small civil claim.

### Official source adapter

Retrieves legal sources from official or trusted public databases.

For Korea, this starts with public legal information sources such as law.go.kr / open.law.go.kr.

### Citation verifier

Checks whether a legal reference has enough citation metadata:

- law name
- article number
- effective date
- source authority
- retrieved date
- case number, if applicable

### Evidence pack builder

Creates a structured bundle of facts, evidence, legal source candidates, missing materials, and drafting notes.

### Draft generator

Generates draft documents such as complaints, petitions, demand letters, and evidence lists.

### Review checklist

Lists weak points, missing support, and possible counterarguments.

## Design rule

The LLM organizes and writes.  
The MCP retrieves and verifies.  
The user decides.
