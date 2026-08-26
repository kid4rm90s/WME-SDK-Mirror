---
title: SDK.Signs class
source: classes/index.SDK.Signs.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Signs

```typescript
getAll ( args ?: { type ?: SignType } ) : Sign []
```
Methods for dealing with Signs.
## Methods
### `getAll`

```typescript
getAll ( args ?: { type ?: SignType } ) : Sign []
```
an array of all the signs in the WME data model
### `getById`

```typescript
getById ( args: { signId: number } ) : null | Sign
```
sign with id, or null if not found in the WME data model
