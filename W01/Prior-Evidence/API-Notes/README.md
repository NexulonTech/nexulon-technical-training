# Odoo API Notes

## Purpose

This folder contains the API documentation and study notes prepared as part of the W01 Prior Evidence for **NX-INT-QP-101 Stage One**.

The notes document the Odoo external API concepts used during the Odoo Contacts CRUD implementation in Postman and Python.

## Evidence

- `Odoo-JSON2-API-Notes.pdf` — Odoo API study and implementation notes.

## Topics Covered

The notes cover:

- Odoo External JSON-2 API
- JSON-2 endpoint structure
- HTTP request structure
- API key authentication
- Required HTTP headers
- `X-Odoo-Database`
- Odoo access rights and API security
- `res.partner` model
- `search_read` — Read
- `create` — Create
- `write` — Update
- `unlink` — Delete
- Request and response structures
- API key security and rotation
- JSON-2 vs legacy XML-RPC / JSON-RPC
- Transactions
- Webhooks vs polling
- Postman and Python usage

## Related W01 Evidence

The concepts documented here were applied in the following evidence:

- `../Odoo-CRUD-Postman/` — Postman collection demonstrating Odoo Contacts CRUD operations.
- `../Python-CRUD/` — Python implementation of the Odoo Contacts CRUD operations.

## Security

No real API keys or credentials are stored in this repository. Authentication secrets are represented using placeholders or environment variables.
