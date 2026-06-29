"""Draft document schemas."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class DraftType(str, Enum):
    TIMELINE = "timeline"
    MATERIAL_LIST = "material_list"
    PETITION = "petition"
    DEMAND_LETTER = "demand_letter"
    CIVIL_COMPLAINT_OUTLINE = "civil_complaint_outline"
    INTERNAL_MEMO = "internal_memo"
    BUSINESS_COMPLIANCE_MEMO = "business_compliance_memo"
    RESEARCH_SOURCE_NOTE = "research_source_note"


class DraftStatus(str, Enum):
    DRAFT = "draft"
    NEEDS_SOURCE_VERIFICATION = "needs_source_verification"
    NEEDS_MATERIAL_SUPPORT = "needs_material_support"
    READY_FOR_REVIEW = "ready_for_review"


class DraftDocument(BaseModel):
    draft_type: DraftType
    status: DraftStatus = DraftStatus.DRAFT
    jurisdiction: str = "KR"
    title: str
    sections: dict[str, str] = Field(default_factory=dict)
    source_candidate_ids: list[str] = Field(default_factory=list)
    material_ids: list[str] = Field(default_factory=list)
    review_warnings: list[str] = Field(default_factory=list)

    def to_markdown(self) -> str:
        lines = [f"# {self.title}", "", f"Status: {self.status.value}", f"Jurisdiction: {self.jurisdiction}", ""]
        for name, content in self.sections.items():
            lines.extend([f"## {name}", "", content, ""])
        if self.review_warnings:
            lines.extend(["## Review warnings", ""])
            lines.extend([f"- {warning}" for warning in self.review_warnings])
        return "\n".join(lines).strip() + "\n"
