---
title: SDK.RestrictedDrivingAreas class
source: classes/index.SDK.RestrictedDrivingAreas.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class RestrictedDrivingAreas

```typescript
getAll () : RestrictedDrivingArea []
```
Methods for dealing with RestrictedDrivingAreas.
## Methods
### `getAll`

```typescript
getAll () : RestrictedDrivingArea []
```
an array of all the restricted driving areas in the WME data model
### `getById`

```typescript
getById ( args: { restrictedDrivingAreaId: number } ) : null | RestrictedDrivingArea
```
restricted driving area with id, or null if not found in the WME data model
