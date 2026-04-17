---
title: SDK.BigJunctions class
source: classes/index.SDK.BigJunctions.html
created: 2026-04-17
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class BigJunctions

```typescript
getAll () : BigJunction []
```
Methods for dealing with BigJunctions.
## Methods
### `getAll`

```typescript
getAll () : BigJunction []
```
an array of all the bigJunctions in the WME data model
### `getAllPossibleTurns`

```typescript
getAllPossibleTurns ( args: { bigJunctionId: number } ) : Turn []
```
all possible turns for the bigJunction
### `getById`

```typescript
getById ( args: { bigJunctionId: number } ) : null | BigJunction
```
bigJunction with id, or null if not found in the WME data model
