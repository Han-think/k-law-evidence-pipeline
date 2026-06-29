"""Jurisdiction profile models.

A jurisdiction profile keeps country-specific rules outside the core pipeline.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class JurisdictionProfile(BaseModel):
    code: str
    name: str
    language: str
    primary_statute_source: str | None = None
    primary_case_source: str | None = None
    citation_style: str | None = None
    supported_templates: list[str] = Field(default_factory=list)
    unsupported_features: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)
