# Local Database Schema

The local database should store case metadata, source metadata, and generated drafts without requiring a remote service.

## Storage goals

- local-first operation
- no real case data in Git
- source metadata cache
- reproducible draft history
- safe separation between case material and public legal sources

## Suggested SQLite tables

### cases

| column | type | note |
|---|---|---|
| id | text primary key | local case id |
| jurisdiction | text | KR, US, JP, etc. |
| user_mode | text | citizen, business, public_official, researcher |
| case_type | text | privacy_leak, telecom_dispute, etc. |
| summary | text | masked or user-approved summary |
| created_at | text | ISO timestamp |
| updated_at | text | ISO timestamp |

### facts

| column | type | note |
|---|---|---|
| id | text primary key | fact id |
| case_id | text | parent case |
| event_date | text | date or partial date |
| text | text | fact statement |
| confidence | text | low, medium, high |
| created_at | text | ISO timestamp |

### materials

| column | type | note |
|---|---|---|
| id | text primary key | material id |
| case_id | text | parent case |
| title | text | material title |
| material_type | text | screenshot, contract, notice, call_note, etc. |
| file_path | text | local path only |
| note | text | short note |
| created_at | text | ISO timestamp |

### fact_material_links

| column | type | note |
|---|---|---|
| fact_id | text | linked fact |
| material_id | text | linked material |
| relation | text | supports, contradicts, contextual |

### source_cache

| column | type | note |
|---|---|---|
| id | text primary key | local source id |
| jurisdiction | text | country code |
| source_type | text | statute, case, agency_decision |
| source_authority | text | source authority |
| title | text | source title |
| identifier | text | article, case number, source id |
| official_url | text | URL if available |
| retrieved_at | text | ISO timestamp |
| effective_date | text | date if available |
| reliability_grade | text | A, B, C, D, X |
| text_hash | text | hash of source text |
| text_excerpt | text | short excerpt |

### drafts

| column | type | note |
|---|---|---|
| id | text primary key | draft id |
| case_id | text | parent case |
| draft_type | text | petition, demand_letter, complaint, memo |
| status | text | draft, needs_review, ready_for_review |
| content | text | markdown content |
| created_at | text | ISO timestamp |

## Rule

Store private case material locally. Store only public source metadata in reusable caches.
