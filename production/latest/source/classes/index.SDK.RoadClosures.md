---
title: SDK.RoadClosures class
source: classes/index.SDK.RoadClosures.html
created: 2026-05-15
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
  trafficEventId: null | string ;
} ,
  ) : RoadClosure
```
Methods for dealing with RoadClosures.
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
  trafficEventId: null | string ;
} ,
  ) : RoadClosure
```
the created road closure.
### `getAll`

```typescript
getAll () : RoadClosure []
```
an array of all the road closures in the WME data model
### `getById`

```typescript
getById ( args: { roadClosureId: string } ) : null | RoadClosure
```
road closure with id, or null if not found in the WME data model
