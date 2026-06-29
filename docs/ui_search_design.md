# UI and Search Design

The UI should make legal-source lookup simple without hiding uncertainty.

## Main screen

The first screen should have:

- search box
- jurisdiction selector
- user type selector
- source type filters
- result confidence filter
- local privacy notice

## Search box

The search box should support natural language and keyword search.

Examples:

- 개인정보 유출 배상
- 통신 장애 보상
- 환불 거부 내용증명
- 사업자 개인정보 처리방침 확인
- 공무원 민원 회신 근거 확인

## User type selector

Suggested options:

- citizen
- public_official
- business
- researcher
- civic_group

The selector changes answer style, not source truth.

## Source filters

Suggested filters:

- statutes
- articles
- cases
- agency decisions
- administrative rules
- local ordinances
- official explanations
- secondary materials

## Result card

Each result card should show:

- title
- source authority
- source type
- identifier
- date or effective date
- reliability grade
- short excerpt
- limitation note
- open official source button

## Answer panel

The answer panel should show:

1. short answer
2. source candidates
3. application notes
4. missing materials
5. possible counterarguments
6. next steps

## Draft panel

The draft panel should generate:

- timeline
- material list
- petition draft
- demand letter draft
- civil complaint draft outline
- internal memo draft

## Safety UI

Before external API use, show:

- outgoing text preview
- masking status
- external provider name
- user approval button

## MVP UI stack options

### Fastest local prototype

- Streamlit
- local Python backend
- MCP server as source layer

### More durable web app

- FastAPI backend
- React or Next.js frontend
- SQLite local database
- optional local file store

## Rule

The UI should make source uncertainty visible. It should not make draft text look like a final legal judgment.
