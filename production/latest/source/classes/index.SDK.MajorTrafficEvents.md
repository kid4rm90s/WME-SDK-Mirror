---
title: SDK.MajorTrafficEvents class
source: classes/index.SDK.MajorTrafficEvents.html
created: 2026-06-10
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class MajorTrafficEvents

```typescript
getAll () : MajorTrafficEvent []
```
Methods for dealing with MajorTrafficEvents.
## Methods
### `getAll`

```typescript
getAll () : MajorTrafficEvent []
```
an array of all the major traffic event in the WME data model
### `getById`

```typescript
getById ( args: { majorTrafficEventId: string } ) : null | MajorTrafficEvent
```
major traffic event with id, or null if not found in the WME data model
