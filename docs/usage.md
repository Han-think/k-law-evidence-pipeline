# Usage

## Install for local development

```bash
git clone https://github.com/Han-think/k-law-evidence-pipeline.git
cd k-law-evidence-pipeline
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
```

On macOS or Linux:

```bash
source .venv/bin/activate
pip install -e .[dev]
```

## CLI

```bash
klep status
klep mask "contact test@example.com"
klep new-case sample-001 --case-type privacy_leak --output case.json
```

## MCP server

```bash
klep-mcp
```

Set `OPENLAW_OC` in `.env` before official Korean API calls.

## Development note

The current MCP implementation is a scaffold. It returns source candidates and metadata. It intentionally avoids fabricating full statute text when the adapter cannot retrieve it.
