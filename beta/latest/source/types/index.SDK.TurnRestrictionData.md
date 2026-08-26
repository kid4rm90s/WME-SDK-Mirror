---
title: SDK.TurnRestrictionData type
source: types/index.SDK.TurnRestrictionData.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias TurnRestrictionData

```typescript
TurnRestrictionData: Omit <
  TurnRestriction ,
  | "editable"
  | "isExpired"
  | "timeFrames"
  | "vehicleRules"
  | "defaultType"
  | "driveProfiles" ,
  > & {
  defaultType: UpdateableTurnRestrictionType ;
  timeFrames ?: Omit < TimeFrame , "daysOfMonth" > [] ;
  vehicleRules: AddableTurnVehicleRules ;
}
```
