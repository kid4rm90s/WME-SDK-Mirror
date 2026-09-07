---
title: SDK.SegmentRestriction interface
source: interfaces/index.SDK.SegmentRestriction.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentRestriction

```typescript
interface SegmentRestriction {
  defaultType: null | RESTRICTION_TYPE ;
  description: null | string ;
  direction: null | RestrictionSegmentDirection ;
  disposition: null | RestrictionSegmentLaneScope ;
  driveProfiles: VehicleRules ;
  editable: boolean ;
  isExpired: boolean ;
  laneScope: null | RestrictionSegmentLaneScope ;
  laneType: null | RestrictionSegmentLaneType ;
  timeFrames: TimeFrame [] ;
  vehicleRules: VehicleRules ;
}
```
Represents restrictions applied to a segment.
## Properties
### `direction`

```typescript
direction: null | RestrictionSegmentDirection
```
### `disposition`

```typescript
disposition: null | RestrictionSegmentLaneScope
```
### `laneScope`

```typescript
laneScope: null | RestrictionSegmentLaneScope
```
### `laneType`

```typescript
laneType: null | RestrictionSegmentLaneType
```
