---
title: SDK.Junctions class
source: classes/index.SDK.Junctions.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Junctions

```typescript
getAll () : Junction []
```
Methods for dealing with Junctions.
## Methods
### `getAll`

```typescript
getAll () : Junction []
```
an array of all the junctions in the WME data model
### `getById`

```typescript
getById ( args: { junctionId: number } ) : null | Junction
```
junctions with id, or null if not found in the WME data model
