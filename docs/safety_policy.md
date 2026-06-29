# Safety Policy

This project handles legal and dispute-related materials. Safety must be designed into the workflow from the beginning.

## Core safety rules

1. The tool must not claim to be a lawyer.
2. The tool must not guarantee winning, compensation, or any official result.
3. The tool must not submit documents automatically without explicit user action.
4. Case materials should be stored locally by default.
5. External API use must be optional.
6. Before external API use, private details should be masked and the outgoing text should be previewed.
7. Every legal citation should include source metadata whenever possible.
8. Drafts should include a reminder that official submission requires user review.

## Recommended output labels

The system should label outputs clearly:

- `draft`: not ready for submission without review
- `source_candidate`: requires official source verification
- `verified_source`: checked against an official or trusted source
- `missing_evidence`: weak point that needs support
- `counterargument`: possible opposing argument
- `user_decision_required`: the tool must not decide automatically

## Legal disclaimer

The project provides legal information organization and document drafting assistance only. It is not legal advice, legal representation, or an official public service.
