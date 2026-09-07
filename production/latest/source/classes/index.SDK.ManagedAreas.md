---
title: SDK.ManagedAreas class
source: classes/index.SDK.ManagedAreas.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class ManagedAreas

```typescript
getAll () : ManagedArea []
```
Methods for dealing with ManagedAreas.
## Methods
### `getAll`

```typescript
getAll () : ManagedArea []
```
an array of all the managed areas in the WME data model
### `getById`

```typescript
getById ( args: { managedAreaId: string } ) : null | ManagedArea
```
managed area with id, or null if not found in the WME data model
