"""Pipeline stage definitions.

These stages keep the project modular and jurisdiction-adaptable.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class PipelineStageName(str, Enum):
    INTAKE = "intake"
    PRIVACY_MASKING = "privacy_masking"
    FACT_EXTRACTION = "fact_extraction"
    TIMELINE_CREATION = "timeline_creation"
    MATERIAL_LIST_CREATION = "material_list_creation"
    ISSUE_CLASSIFICATION = "issue_classification"
    OFFICIAL_SOURCE_LOOKUP = "official_source_lookup"
    CITATION_VERIFICATION = "citation_verification"
    DRAFT_GENERATION = "draft_generation"
    REVIEW_CHECKLIST = "review_checklist"
    EXPORT = "export"


class PipelineStageResult(BaseModel):
    stage: PipelineStageName
    status: str = "pending"
    output_refs: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)


DEFAULT_PIPELINE = [stage for stage in PipelineStageName]
