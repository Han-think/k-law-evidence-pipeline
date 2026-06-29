"""Korea jurisdiction profile."""

from __future__ import annotations

from klep.jurisdictions.profile import JurisdictionProfile


KR_PROFILE = JurisdictionProfile(
    code="KR",
    name="Republic of Korea",
    language="ko",
    primary_statute_source="National Law Information Center",
    primary_case_source="National Law Information Center",
    citation_style="Korean statute article and case-number based citation",
    supported_templates=[
        "timeline",
        "material_list",
        "petition_draft",
        "demand_letter_draft",
        "civil_complaint_draft",
    ],
    unsupported_features=[
        "automatic court filing",
        "final legal outcome prediction",
    ],
    notes=[
        "Use official source metadata whenever possible.",
        "Keep private case material local by default.",
    ],
)
