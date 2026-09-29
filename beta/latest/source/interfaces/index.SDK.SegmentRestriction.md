---
title: SDK.SegmentRestriction interface
source: interfaces/index.SDK.SegmentRestriction.html
created: 2026-09-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentRestriction

```typescript
interface SegmentRestriction {
  defaultType: RESTRICTION_TYPE | null ;
  description: string | null ;
  direction: RestrictionSegmentDirection | null ;
  disposition: RestrictionSegmentLaneScope | null ;
  driveProfiles: VehicleRules ;
  editable: boolean ;
  isExpired: boolean ;
  laneScope: RestrictionSegmentLaneScope | null ;
  laneType: RestrictionSegmentLaneType | null ;
  timeFrames: TimeFrame [] ;
  vehicleRules: VehicleRules ;
}
```
Represents restrictions applied to a segment.
## Properties
### `direction`

```typescript
direction: RestrictionSegmentDirection | null
```
### `disposition`

```typescript
disposition: RestrictionSegmentLaneScope | null
```
### `laneScope`

```typescript
laneScope: RestrictionSegmentLaneScope | null
```
### `laneType`

```typescript
laneType: RestrictionSegmentLaneType | null
```
