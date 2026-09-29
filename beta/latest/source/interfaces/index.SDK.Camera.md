---
title: SDK.Camera interface
source: interfaces/index.SDK.Camera.html
created: 2026-09-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Camera

```typescript
interface Camera {
  direction: RestrictionSegmentDirection | null ;
  geometry: Point ;
  id: number ;
  lockRank: number | null ;
  modificationData: ModificationMetadata ;
  segmentId: number | null ;
  subTypes: PermanentHazardSubType [] ;
  type: "CAMERA" ;
  types: CameraType [] ;
}
```
## Properties
### `geometry`

```typescript
geometry: Point
```
### `type`

```typescript
type: "CAMERA"
```
### `types`

```typescript
types: CameraType []
```
