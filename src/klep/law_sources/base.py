"""Base interface for public legal source adapters."""

from __future__ import annotations

from abc import ABC, abstractmethod

from klep.evidence.schema import SourceEnvelope


class LawSourceAdapter(ABC):
    jurisdiction: str

    @abstractmethod
    async def search_law(self, query: str, limit: int = 10) -> list[SourceEnvelope]:
        pass

    @abstractmethod
    async def get_article(self, law_name: str, article: str) -> SourceEnvelope | None:
        pass

    @abstractmethod
    async def search_case(self, query: str, limit: int = 10) -> list[SourceEnvelope]:
        pass
