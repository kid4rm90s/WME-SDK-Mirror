---
title: SDK.SchoolZone interface
source: interfaces/index.SDK.SchoolZone.html
created: 2026-09-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SchoolZone

```typescript
interface SchoolZone {
  direction: RestrictionSegmentDirection | null ;
  excludedRoadTypes: RoadTypeId [] | null ;
  geometry: Point | Polygon ;
  id: number ;
  lockRank: number | null ;
  modificationData: ModificationMetadata ;
  name: string | null ;
  scheduleId: string | null ;
  segmentId: number | null ;
  speedLimit: number | null ;
  subTypes: PermanentHazardSubType [] ;
  type: "SCHOOL_ZONE" ;
}
```
## Properties
### `excludedRoadTypes`

```typescript
excludedRoadTypes: RoadTypeId [] | null
```
### `name`

```typescript
name: string | null
```
### `scheduleId`

```typescript
scheduleId: string | null
```
### `speedLimit`

```typescript
speedLimit: number | null
```
### `type`

```typescript
type: "SCHOOL_ZONE"
```
