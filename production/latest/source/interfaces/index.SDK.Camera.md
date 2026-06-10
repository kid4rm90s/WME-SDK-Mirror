---
title: SDK.Camera interface
source: interfaces/index.SDK.Camera.html
created: 2026-06-10
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
  types: CameraType [] ;
}
```
## Properties
### `direction`

```typescript
direction: null | RestrictionSegmentDirection
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```
### `lockRank`

```typescript
lockRank: null | number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `segmentId`

```typescript
segmentId: null | number
```
### `types`

```typescript
types: CameraType []
```
