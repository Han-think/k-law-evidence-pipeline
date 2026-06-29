# Evidence Schema

The evidence schema is the internal contract between intake, timeline, source lookup, and draft generation.

## Case object

```yaml
case_id: sample-case-001
case_type: privacy_leak
user_role: affected_user
jurisdiction: KR
language: ko
summary: "Short case summary"

parties:
  claimant:
    display_name: "masked user"
  respondent:
    display_name: "company or agency"

facts:
  - id: F-001
    date: "2025-12-30"
    text: "A public notice discussed the incident."
    evidence_refs: [EV-001]
    confidence: medium

evidence:
  - id: EV-001
    title: "Report or notice capture"
    date: "2025-12-30"
    source_type: public_report
    file_path: ./evidence/ev001.png
    proves: [F-001]
    note: "Do not commit real files to Git."

legal_issues:
  - privacy_compensation
  - notice_sufficiency

requested_outcomes:
  - cash compensation
  - protective measures
  - public explanation
```

## Evidence reliability

Suggested values:

- `official`: official source or formal document
- `direct`: direct user-held material
- `indirect`: article, third-party note, or summary
- `uncertain`: needs verification

## Source envelope

```yaml
source_type: statute
source_authority: National Law Information Center
jurisdiction: KR
title: Personal Information Protection Act
identifier: article-39
effective_date: "YYYY-MM-DD"
retrieved_at: "YYYY-MM-DD"
official_url: "https://www.law.go.kr/..."
text_excerpt: "..."
reliability_grade: A
```
