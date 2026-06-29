from klep.evidence.schema import ReliabilityGrade, SourceEnvelope


def test_source_envelope_minimal():
    source = SourceEnvelope(
        source_type="test",
        source_authority="local",
        title="sample",
        reliability_grade=ReliabilityGrade.X,
    )
    assert source.jurisdiction == "KR"
    assert source.title == "sample"
