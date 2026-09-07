---
title: SDK.SegmentRestrictionData type
source: types/index.SDK.SegmentRestrictionData.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SegmentRestrictionData

```typescript
SegmentRestrictionData: Omit <
  SegmentRestriction ,
  | "editable"
  | "isExpired"
  | "laneScope"
  | "timeFrames"
  | "vehicleRules"
  | "defaultType"
  | "disposition"
  | "driveProfiles"
  | "direction" ,
  > & {
  defaultType: UpdateableRestrictionType ;
  direction: RestrictionSegmentDirection ;
  laneScope: UpdateableRestrictionSegmentLaneScope ;
  timeFrames ?: Omit < TimeFrame , "daysOfMonth" > [] ;
  vehicleRules: AddableVehicleRules ;
}
```
