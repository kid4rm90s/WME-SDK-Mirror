---
title: SDK.MapProblems class
source: classes/index.SDK.MapProblems.html
created: 2026-04-22
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class MapProblems

```typescript
getAll () : MapProblem []
```
Methods for dealing with MapProblems.
## Methods
### `getAll`

```typescript
getAll () : MapProblem []
```
an array of all the map problems in the WME data model
### `getById`

```typescript
getById ( args: { mapProblemId: string } ) : null | MapProblem
```
map problem with id, or null if not found in the WME data model
