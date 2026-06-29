# Contributing

Thank you for your interest in K-Law Evidence Pipeline.

## Contribution goals

Good contributions should improve one of these areas:

- source reliability
- privacy and local-first handling
- jurisdiction adapter quality
- document templates
- tests and fixtures
- documentation clarity
- MCP compatibility

## Safety-first rule

Do not add features that claim final legal advice, guaranteed outcomes, or automatic official filing.

## Source rule

When adding legal source logic, include:

- source authority
- source URL pattern
- expected response fields
- reliability grade
- limitations
- sanitized test fixture if possible

## Pull request checklist

- [ ] No real user case data included
- [ ] No private API value included
- [ ] Output remains structured
- [ ] Missing source text is not generated
- [ ] Tests or documentation added
- [ ] Safety boundary preserved

## Development setup

```bash
git clone https://github.com/Han-think/k-law-evidence-pipeline.git
cd k-law-evidence-pipeline
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
pytest
```
