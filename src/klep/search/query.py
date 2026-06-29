"""Search query models."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field

from klep.answering.schema import UserMode


class SourceType(str, Enum):
    STATUTE = "statute"
    ARTICLE = "article"
    CASE = "case"
    AGENCY_DECISION = "agency_decision"
    ADMIN_RULE = "admin_rule"
    LOCAL_ORDINANCE = "local_ordinance"
    OFFICIAL_EXPLANATION = "official_explanation"
    SECONDARY = "secondary"


class SearchQuery(BaseModel):
    query: str
    jurisdiction: str = "KR"
    user_mode: UserMode = UserMode.CITIZEN
    source_types: list[SourceType] = Field(default_factory=list)
    limit: int = 10
    include_secondary: bool = False
    require_official: bool = True

    def normalized_query(self) -> str:
        return " ".join(self.query.split())
