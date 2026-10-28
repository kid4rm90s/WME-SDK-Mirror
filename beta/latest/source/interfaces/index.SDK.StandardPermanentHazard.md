---
title: SDK.StandardPermanentHazard interface
source: interfaces/index.SDK.StandardPermanentHazard.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface StandardPermanentHazard

```typescript
interface StandardPermanentHazard {
  direction: RestrictionSegmentDirection | null ;
  geometry: Point | Polygon ;
  id: number ;
  lockRank: number | null ;
  modificationData: ModificationMetadata ;
  rank: number | null ;
  segmentId: number | null ;
  subTypes: PermanentHazardSubType [] ;
  type: 
  | "SPEED_BUMP"
  | "TOPES"
  | "TOLL_BOOTH"
  | "DANGEROUS_CURVE"
  | "DANGEROUS_INTERSECTION"
  | "DANGEROUS_MERGE"
  | "RAILROAD_CROSSING"
  | "TRAFFIC_LIGHT"
  | "SIGN"
  | "LANE_ENDING"
  | "RAISED_CROSSWALK"
  | "HIGHWAY_CROSSWALK"
  | "SHOULDER_ENDING"
  | "NARROW_BRIDGE" ;
}
```
## Properties
### `rank`

```typescript
rank: number | null
```
### `type`

```typescript
type: 
  | "SPEED_BUMP"
  | "TOPES"
  | "TOLL_BOOTH"
  | "DANGEROUS_CURVE"
  | "DANGEROUS_INTERSECTION"
  | "DANGEROUS_MERGE"
  | "RAILROAD_CROSSING"
  | "TRAFFIC_LIGHT"
  | "SIGN"
  | "LANE_ENDING"
  | "RAISED_CROSSWALK"
  | "HIGHWAY_CROSSWALK"
  | "SHOULDER_ENDING"
  | "NARROW_BRIDGE"
```
