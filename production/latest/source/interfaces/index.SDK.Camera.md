---
title: SDK.Camera interface
source: interfaces/index.SDK.Camera.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Camera

```typescript
interface Camera {
  direction: null | RestrictionSegmentDirection ;
  geometry: Point ;
  id: number ;
  lockRank: null | number ;
  modificationData: ModificationMetadata ;
  segmentId: null | number ;
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
