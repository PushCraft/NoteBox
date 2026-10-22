# Planned REST API (not implemented yet)

All endpoints require a verified Cognito JWT access token. The backend derives the user identity from verified token context.

| Method | Route | Purpose |
|---|---|---|
| GET | `/notes?limit=30&cursor=...` | List current user's messages |
| POST | `/notes` | Add message `{ "body": "..." }` |
| PATCH | `/notes/{noteId}` | Edit body or pin status |
| DELETE | `/notes/{noteId}` | Delete a message |

Future request validation: reject empty and oversized notes, paginate queries, avoid logging note text. The frontend may locally filter fetched notes for first-version search.
