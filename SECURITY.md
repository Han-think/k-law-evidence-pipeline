# Security Policy

K-Law Evidence Pipeline is designed for local-first handling of sensitive case materials.

## Do not commit

- real case files
- private messages
- identity documents
- private contact details
- API values
- local database files
- exported drafts containing private facts

## API values

Store API values only in local environment files such as `.env`.

## External processing

Before using an external AI API:

1. mask private details,
2. preview outgoing text,
3. confirm user approval,
4. record that an external tool was used if needed.

## Reporting issues

For security concerns, open a GitHub issue only if it does not contain private data. If private data is involved, remove or mask it before reporting.

## Design position

The project should fail safely. If a source cannot be verified, it should return an error or limitation note instead of generating missing legal text.
