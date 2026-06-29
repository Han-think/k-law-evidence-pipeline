"""Structured answer schemas."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field

from klep.evidence.schema import SourceEnvelope


class UserMode(str, Enum):
    CITIZEN = "citizen"
    PUBLIC_OFFICIAL = "public_official"
    BUSINESS = "business"
    RESEARCHER = "researcher"
    CIVIC_GROUP = "civic_group"


class AnswerStatus(str, Enum):
    DRAFT = "draft"
    NEEDS_SOURCE_VERIFICATION = "needs_source_verification"
    NEEDS_MATERIAL_SUPPORT = "needs_material_support"
    READY_FOR_REVIEW = "ready_for_review"


class StructuredAnswer(BaseModel):
    user_mode: UserMode = UserMode.CITIZEN
    status: AnswerStatus = AnswerStatus.DRAFT
    question_understood: str
    scope_and_limits: str
    short_answer: str
    source_candidates: list[SourceEnvelope] = Field(default_factory=list)
    application_notes: list[str] = Field(default_factory=list)
    risks_and_uncertainties: list[str] = Field(default_factory=list)
    next_actions: list[str] = Field(default_factory=list)
    citation_notes: list[str] = Field(default_factory=list)
