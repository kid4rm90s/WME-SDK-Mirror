---
title: SDK.StandardPermanentHazard interface
source: interfaces/index.SDK.StandardPermanentHazard.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface StandardPermanentHazard

```typescript
interface StandardPermanentHazard {
  direction: null | RestrictionSegmentDirection ;
  geometry: Point | Polygon ;
  id: number ;
  lockRank: null | number ;
  modificationData: ModificationMetadata ;
  rank: null | number ;
  segmentId: null | number ;
  subTypes: PermanentHazardSubType [] ;
  type: 
  | "DANGEROUS_CURVE"
  | "DANGEROUS_INTERSECTION"
  | "DANGEROUS_MERGE"
  | "RAILROAD_CROSSING"
  | "SPEED_BUMP"
  | "TOLL_BOOTH"
  | "TOPES"
  | "TRAFFIC_LIGHT"
  | "SIGN"
  | "RAISED_CROSSWALK"
  | "HIGHWAY_CROSSWALK"
  | "NARROW_BRIDGE"
  | "LANE_ENDING"
  | "SHOULDER_ENDING" ;
}
```
## Properties
### `rank`

```typescript
rank: null | number
```
### `type`

```typescript
type: 
  | "DANGEROUS_CURVE"
  | "DANGEROUS_INTERSECTION"
  | "DANGEROUS_MERGE"
  | "RAILROAD_CROSSING"
  | "SPEED_BUMP"
  | "TOLL_BOOTH"
  | "TOPES"
  | "TRAFFIC_LIGHT"
  | "SIGN"
  | "RAISED_CROSSWALK"
  | "HIGHWAY_CROSSWALK"
  | "NARROW_BRIDGE"
  | "LANE_ENDING"
  | "SHOULDER_ENDING"
```
