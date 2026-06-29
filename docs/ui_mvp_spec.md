# UI MVP Specification

The first UI should be simple, local-first, and source-aware.

## MVP objective

Create a local search and drafting interface that lets users:

- search legal source candidates
- view source metadata
- select user mode
- create a structured answer
- create a draft outline
- export markdown

## MVP screens

### 1. Search screen

Required elements:

- search input
- jurisdiction selector
- user mode selector
- source type filters
- search button
- result cards

### 2. Result detail panel

Required elements:

- title
- source authority
- source type
- identifier
- date or effective date
- retrieved date
- reliability grade
- excerpt
- limitation note
- official source link when available

### 3. Structured answer panel

Required sections:

- question understood
- scope and limits
- short answer
- source candidates
- application notes
- risks and uncertainties
- next actions
- citation notes

### 4. Draft panel

Required draft types:

- timeline
- material list
- petition outline
- demand letter outline
- civil complaint outline
- internal memo outline

### 5. Privacy panel

Required elements:

- local-first notice
- external API toggle
- masking preview
- outgoing text preview
- user confirmation

## MVP technology options

### Fast prototype

- Streamlit
- Python backend
- local file storage
- MCP server or direct adapter call

### Durable app

- FastAPI
- SQLite
- React or Next.js
- local file storage
- MCP server as source layer

## UI rule

Never hide uncertainty. The UI should show whether a result is verified, partial, missing, or unverified.
