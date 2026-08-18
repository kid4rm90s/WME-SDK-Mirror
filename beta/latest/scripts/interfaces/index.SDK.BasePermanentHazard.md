---
title: SDK.BasePermanentHazard interface
source: interfaces/index.SDK.BasePermanentHazard.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface BasePermanentHazard

```typescript
interface BasePermanentHazard {
  direction: null | RestrictionSegmentDirection ;
  geometry: Point | Polygon ;
  id: number ;
  lockRank: null | number ;
  modificationData: ModificationMetadata ;
  segmentId: null | number ;
  subTypes: PermanentHazardSubType [] ;
}
```
## Properties
### `direction`

```typescript
direction: null | RestrictionSegmentDirection
```
### `geometry`

```typescript
geometry: Point | Polygon
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
### `subTypes`

```typescript
subTypes: PermanentHazardSubType []
```
