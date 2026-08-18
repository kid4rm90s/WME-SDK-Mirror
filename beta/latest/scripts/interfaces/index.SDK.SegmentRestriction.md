---
title: SDK.SegmentRestriction interface
source: interfaces/index.SDK.SegmentRestriction.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentRestriction

```typescript
interface SegmentRestriction {
  defaultType: null | RESTRICTION_TYPE ;
  description: null | string ;
  direction: null | RestrictionSegmentDirection ;
  disposition: null | RestrictionSegmentDisposition ;
  driveProfiles: DriveProfiles ;
  editable: boolean ;
  isExpired: boolean ;
  laneType: null | RestrictionSegmentLaneType ;
  timeFrames: TimeFrame [] ;
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
disposition: null | RestrictionSegmentDisposition
```
### `laneType`

```typescript
laneType: null | RestrictionSegmentLaneType
```
