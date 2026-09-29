---
title: SDK.RoadClosures class
source: classes/index.SDK.RoadClosures.html
created: 2026-09-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class RoadClosures

```typescript
addClosure (
  args: {
  description: string ;
  endDate: number ;
  fromNodeClosed: boolean ;
  isForward: boolean ;
  isPermanent: boolean ;
  segmentId: number ;
  startDate: number ;
  trafficEventId: string | null ;
} ,
  ) : RoadClosure
```
Methods for dealing with RoadClosures. Add/Delete methods don't automatically save changes like the UI closures.
## Methods
### `addClosure`

```typescript
addClosure (
  args: {
  description: string ;
  endDate: number ;
  fromNodeClosed: boolean ;
  isForward: boolean ;
  isPermanent: boolean ;
  segmentId: number ;
  startDate: number ;
  trafficEventId: string | null ;
} ,
  ) : RoadClosure
```
the created road closure.
### `deleteClosure`

```typescript
deleteClosure ( args: { roadClosureId: string } ) : void
```

### `getAll`

```typescript
getAll () : RoadClosure []
```
an array of all the road closures in the WME data model
### `getById`

```typescript
getById ( args: { roadClosureId: string } ) : RoadClosure | null
```
road closure with id, or null if not found in the WME data model
