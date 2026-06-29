"""Evidence and source schemas."""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class ReliabilityGrade(str, Enum):
    A = "A"  # official direct source
    B = "B"  # official explanation or agency material
    C = "C"  # trusted public institution material
    D = "D"  # secondary source
    X = "X"  # unverified


class SourceEnvelope(BaseModel):
    source_type: str
    source_authority: str
    jurisdiction: str = "KR"
    title: str
    identifier: str | None = None
    effective_date: date | None = None
    retrieved_at: datetime = Field(default_factory=datetime.utcnow)
    official_url: str | None = None
    text_excerpt: str | None = None
    reliability_grade: ReliabilityGrade = ReliabilityGrade.X
    limitation_note: str | None = None
    raw: dict[str, Any] | None = None


class Fact(BaseModel):
    id: str
    date: date | None = None
    text: str
    evidence_refs: list[str] = Field(default_factory=list)
    confidence: str = "medium"


class EvidenceItem(BaseModel):
    id: str
    title: str
    date: date | None = None
    source_type: str | None = None
    file_path: str | None = None
    proves: list[str] = Field(default_factory=list)
    note: str | None = None


class CaseFile(BaseModel):
    case_id: str
    case_type: str
    user_role: str | None = None
    jurisdiction: str = "KR"
    language: str = "ko"
    summary: str | None = None
    facts: list[Fact] = Field(default_factory=list)
    evidence: list[EvidenceItem] = Field(default_factory=list)
    legal_issues: list[str] = Field(default_factory=list)
    requested_outcomes: list[str] = Field(default_factory=list)
