"""Simple source ranking helpers."""

from __future__ import annotations

from klep.evidence.schema import ReliabilityGrade, SourceEnvelope


GRADE_SCORE = {
    ReliabilityGrade.A: 100,
    ReliabilityGrade.B: 80,
    ReliabilityGrade.C: 60,
    ReliabilityGrade.D: 30,
    ReliabilityGrade.X: 0,
}


def score_source(source: SourceEnvelope, query: str = "") -> int:
    """Score a source candidate.

    This is intentionally simple. It favors official reliability and title matches.
    """
    score = GRADE_SCORE.get(source.reliability_grade, 0)
    q = query.strip().lower()
    title = source.title.lower()
    excerpt = (source.text_excerpt or "").lower()

    if q and q in title:
        score += 30
    if q and q in excerpt:
        score += 10
    if source.official_url:
        score += 5
    if source.identifier:
        score += 5
    if source.effective_date:
        score += 5
    return score


def rank_sources(sources: list[SourceEnvelope], query: str = "") -> list[SourceEnvelope]:
    return sorted(sources, key=lambda s: score_source(s, query), reverse=True)
