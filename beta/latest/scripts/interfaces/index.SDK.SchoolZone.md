---
title: SDK.SchoolZone interface
source: interfaces/index.SDK.SchoolZone.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SchoolZone

```typescript
interface SchoolZone {
  direction: null | RestrictionSegmentDirection ;
  excludedRoadTypes: null | RoadTypeId [] ;
  geometry: Point | Polygon ;
  id: number ;
  lockRank: null | number ;
  modificationData: ModificationMetadata ;
  name: null | string ;
  scheduleId: null | string ;
  segmentId: null | number ;
  speedLimit: null | number ;
  subTypes: PermanentHazardSubType [] ;
  type: "SCHOOL_ZONE" ;
}
```
## Properties
### `excludedRoadTypes`

```typescript
excludedRoadTypes: null | RoadTypeId []
```
### `name`

```typescript
name: null | string
```
### `scheduleId`

```typescript
scheduleId: null | string
```
### `speedLimit`

```typescript
speedLimit: null | number
```
### `type`

```typescript
type: "SCHOOL_ZONE"
```
