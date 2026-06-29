---
title: SDK.TurnClosures class
source: classes/index.SDK.TurnClosures.html
created: 2026-06-29
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class TurnClosures

```typescript
addClosure (
  args: {
  description: string ;
  endDate: number ;
  majorTrafficEventId ?: string ;
  startDate: number ;
  turnId: string ;
} ,
  ) : TurnClosure
```
Methods for dealing with TurnClosures.
## Methods
### `addClosure`

```typescript
addClosure (
  args: {
  description: string ;
  endDate: number ;
  majorTrafficEventId ?: string ;
  startDate: number ;
  turnId: string ;
} ,
  ) : TurnClosure
```
The newly created turn closure object.
### `getAll`

```typescript
getAll () : TurnClosure []
```
an array of all the turn closures in the WME data model
### `getById`

```typescript
getById ( args: { turnClosureId: string } ) : null | TurnClosure
```
turn closure with id, or null if not found in the WME data model
