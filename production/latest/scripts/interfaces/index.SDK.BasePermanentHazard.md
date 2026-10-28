---
title: SDK.BasePermanentHazard interface
source: interfaces/index.SDK.BasePermanentHazard.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface BasePermanentHazard

```typescript
interface BasePermanentHazard {
  direction: RestrictionSegmentDirection | null ;
  geometry: Point | Polygon ;
  id: number ;
  lockRank: number | null ;
  modificationData: ModificationMetadata ;
  segmentId: number | null ;
  subTypes: PermanentHazardSubType [] ;
}
```
## Properties
### `direction`

```typescript
direction: RestrictionSegmentDirection | null
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
lockRank: number | null
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `segmentId`

```typescript
segmentId: number | null
```
### `subTypes`

```typescript
subTypes: PermanentHazardSubType []
```
