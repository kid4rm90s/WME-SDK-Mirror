# index.SDK.BBox

---
title: SDK.BBox type
source: types/index.SDK.BBox.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias BBox

```typescript
BBox: 
  | [ number , number , number , number ]
  | [ number , number , number , number , number , number ]
```

---

# index.SDK.CameraType

---
title: SDK.CameraType type
source: types/index.SDK.CameraType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias CameraType

```typescript
CameraType: 
  | "BUS_LANE"
  | "CARPOOL_LANE"
  | "DISTANCE"
  | "DUMMY"
  | "HOV_LANE"
  | "MOBILE_PHONE"
  | "NOISE"
  | "RED_LIGHT"
  | "SEATBELT"
  | "SPEED"
  | "STOP"
```

---

# index.SDK.ChargersAccessType

---
title: SDK.ChargersAccessType type
source: types/index.SDK.ChargersAccessType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ChargersAccessType

```typescript
ChargersAccessType: 
  | "CHARGERS_ACCESS_TYPE_UNKNOWN"
  | "PRIVATE"
  | "PUBLIC"
  | "RESTRICTED"
```

---

# index.SDK.ChargingStationCostType

---
title: SDK.ChargingStationCostType type
source: types/index.SDK.ChargingStationCostType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ChargingStationCostType

```typescript
ChargingStationCostType: "COST_TYPE_UNSPECIFIED" | "FEE" | "FREE"
```

---

# index.SDK.ClosureStatus

---
title: SDK.ClosureStatus type
source: types/index.SDK.ClosureStatus.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ClosureStatus

```typescript
ClosureStatus: 
  | "ACTIVE"
  | "FINISHED"
  | "FINISHED_EARLY_DUE_TO_DELETION"
  | "FINISHED_EARLY_DUE_TO_OVERLAPPING_CLOSURES"
  | "NOT_STARTED"
  | "SUSPENDED"
  | "UNVERIFIED"
  | "FAILED"
  | "UNKNOWN"
```

---

# index.SDK.DataModelName

---
title: SDK.DataModelName type
source: types/index.SDK.DataModelName.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias DataModelName

```typescript
DataModelName: Values < typeof DATA_MODEL_NAMES >
```

---

# index.SDK.DriveProfiles

---
title: SDK.DriveProfiles type
source: types/index.SDK.DriveProfiles.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias DriveProfiles

```typescript
DriveProfiles: { [ key in RESTRICTION_TYPE ] : DriveProfile [] }
```

---

# index.SDK.EditSuggestionSource

---
title: SDK.EditSuggestionSource type
source: types/index.SDK.EditSuggestionSource.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias EditSuggestionSource

```typescript
EditSuggestionSource: "CLIENT" | "GEO" | "OTHER" | "WME" | "SYSTEM"
```

---

# index.SDK.EditSuggestionStatus

---
title: SDK.EditSuggestionStatus type
source: types/index.SDK.EditSuggestionStatus.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias EditSuggestionStatus

```typescript
EditSuggestionStatus: Values < typeof EditSuggestionStatus >
```

---

# index.SDK.Extract

---
title: SDK.Extract type
source: types/index.SDK.Extract.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Extract<T, U>

```typescript
Extract: T extends U ? T: never
```

---

# index.SDK.GENERAL_SERVICE_TYPE

---
title: SDK.GENERAL_SERVICE_TYPE type
source: types/index.SDK.GENERAL_SERVICE_TYPE.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias GENERAL_SERVICE_TYPE

```typescript
GENERAL_SERVICE_TYPE: Values < typeof GENERAL_SERVICE_TYPE >
```

---

# index.SDK.InstructionOpCode

---
title: SDK.InstructionOpCode type
source: types/index.SDK.InstructionOpCode.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias InstructionOpCode

```typescript
InstructionOpCode: 
  | typeof CONTINUE
  | typeof EXIT_LEFT
  | typeof EXIT_RIGHT
  | typeof KEEP_LEFT
  | typeof KEEP_RIGHT
  | typeof NONE
  | typeof ROUNDABOUT_ENTER
  | typeof TURN_LEFT
  | typeof TURN_RIGHT
  | typeof UTURN
```

---

# index.SDK.IssueSeverity

---
title: SDK.IssueSeverity type
source: types/index.SDK.IssueSeverity.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias IssueSeverity

```typescript
IssueSeverity: "low" | "medium" | "high"
```

---

# index.SDK.LaneGuidanceMode

---
title: SDK.LaneGuidanceMode type
source: types/index.SDK.LaneGuidanceMode.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias LaneGuidanceMode

```typescript
LaneGuidanceMode: "default" | "display" | "display-and-voice"
```

---

# index.SDK.LaneInstructionStrategy

---
title: SDK.LaneInstructionStrategy type
source: types/index.SDK.LaneInstructionStrategy.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias LaneInstructionStrategy

```typescript
LaneInstructionStrategy: "default" | "pull" | "push"
```

---

# index.SDK.LotType

---
title: SDK.LotType type
source: types/index.SDK.LotType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias LotType

```typescript
LotType: "MULTI_LEVEL" | "STREET_LEVEL" | "STREET_LEVEL_COVERED" | "UNDERGROUND"
```

---

# index.SDK.MajorTrafficEventCategory

---
title: SDK.MajorTrafficEventCategory type
source: types/index.SDK.MajorTrafficEventCategory.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias MajorTrafficEventCategory

```typescript
MajorTrafficEventCategory: 
  | "CONCERT"
  | "CONSTRUCTION"
  | "CRISIS"
  | "DEMONSTRATION"
  | "DRIVING_ADVISORY"
  | "HOLIDAY/FESTIVAL"
  | "OTHER"
  | "PARADE"
  | "SPORTING_EVENT"
  | "SUMMIT"
  | "PARTNER_USER_COMMS"
  | "UNPLANNED_DISRUPTION"
```

---

# index.SDK.MapProblemType

---
title: SDK.MapProblemType type
source: types/index.SDK.MapProblemType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias MapProblemType

```typescript
MapProblemType: "DATA" | "DISCONNECTION" | "ROAD_CLOSURE" | "TURN"
```

---

# index.SDK.OLMouseEventName

---
title: SDK.OLMouseEventName type
source: types/index.SDK.OLMouseEventName.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias OLMouseEventName

```typescript
OLMouseEventName: "click" | "mousedown" | "mouseup" | "mousemove" | "mouseout"
```

---

# index.SDK.ObjectType

---
title: SDK.ObjectType type
source: types/index.SDK.ObjectType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ObjectType

```typescript
ObjectType: Values < typeof ObjectType >
```

---

# index.SDK.PARKING_LOT_SERVICE_TYPE

---
title: SDK.PARKING_LOT_SERVICE_TYPE type
source: types/index.SDK.PARKING_LOT_SERVICE_TYPE.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PARKING_LOT_SERVICE_TYPE

```typescript
PARKING_LOT_SERVICE_TYPE: Values < typeof PARKING_LOT_SERVICE_TYPE >
```

---

# index.SDK.PLACE_UPDATE_ACTION

---
title: SDK.PLACE_UPDATE_ACTION type
source: types/index.SDK.PLACE_UPDATE_ACTION.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PLACE_UPDATE_ACTION

```typescript
PLACE_UPDATE_ACTION: Values < typeof PLACE_UPDATE_ACTION >
```

---

# index.SDK.PLACE_UPDATE_SUBJECT

---
title: SDK.PLACE_UPDATE_SUBJECT type
source: types/index.SDK.PLACE_UPDATE_SUBJECT.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PLACE_UPDATE_SUBJECT

```typescript
PLACE_UPDATE_SUBJECT: Values < typeof PLACE_UPDATE_SUBJECT >
```

---

# index.SDK.ParkingLotCostType

---
title: SDK.ParkingLotCostType type
source: types/index.SDK.ParkingLotCostType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ParkingLotCostType

```typescript
ParkingLotCostType: "FREE" | "LOW" | "MODERATE" | "EXPENSIVE" | "UNKNOWN"
```

---

# index.SDK.ParkingType

---
title: SDK.ParkingType type
source: types/index.SDK.ParkingType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ParkingType

```typescript
ParkingType: "PRIVATE" | "PUBLIC" | "RESTRICTED" | null
```

---

# index.SDK.Partial

---
title: SDK.Partial type
source: types/index.SDK.Partial.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Partial<T>

```typescript
Partial: { [ P in keyof T ] ?: T [ P ] }
```

---

# index.SDK.PaymentMethod

---
title: SDK.PaymentMethod type
source: types/index.SDK.PaymentMethod.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PaymentMethod

```typescript
PaymentMethod: 
  | "APP"
  | "CREDIT"
  | "DEBIT"
  | "MEMBERSHIP_CARD"
  | "ONLINE_PAYMENT"
  | "OTHER"
  | "PAYMENT_METHOD_UNKNOWN"
  | "PLUG_IN_AUTO_CHARGE"
```

---

# index.SDK.PaymentType

---
title: SDK.PaymentType type
source: types/index.SDK.PaymentType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PaymentType

```typescript
PaymentType: 
  | "CASH"
  | "CHECKS"
  | "CREDIT"
  | "DEBIT_CARD"
  | "DIGITAL_WALLET"
  | "ELECTRONIC_PASS"
  | "MEMBERSHIP"
  | "PARKING_APP"
  | "PERMIT"
  | "PREPAID"
  | "SMS_CALL"
```

---

# index.SDK.Pick

---
title: SDK.Pick type
source: types/index.SDK.Pick.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Pick<T, K>

```typescript
Pick: { [ P in K ] : T [ P ] }
```

---

# index.SDK.PlaceUpdateType

---
title: SDK.PlaceUpdateType type
source: types/index.SDK.PlaceUpdateType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PlaceUpdateType

```typescript
PlaceUpdateType: ` ${ PLACE_UPDATE_ACTION } _ ${ PLACE_UPDATE_SUBJECT } ` | "flag"
```

---

# index.SDK.Position

---
title: SDK.Position type
source: types/index.SDK.Position.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Position

```typescript
Position: number []
```

---

# index.SDK.RESTRICTION_TYPE

---
title: SDK.RESTRICTION_TYPE type
source: types/index.SDK.RESTRICTION_TYPE.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias RESTRICTION_TYPE

```typescript
RESTRICTION_TYPE: Values < typeof RESTRICTION_TYPE >
```

---

# index.SDK.Record

---
title: SDK.Record type
source: types/index.SDK.Record.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Record<K, T>

```typescript
Record: { [ P in K ] : T }
```

---

# index.SDK.RegionCode

---
title: SDK.RegionCode type
source: types/index.SDK.RegionCode.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias RegionCode

```typescript
RegionCode: 
  | typeof REGION_CODE_USA
  | typeof REGION_CODE_ROW
  | typeof REGION_CODE_IL
```

---

# index.SDK.RestrictionSegmentDirection

---
title: SDK.RestrictionSegmentDirection type
source: types/index.SDK.RestrictionSegmentDirection.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias RestrictionSegmentDirection

```typescript
RestrictionSegmentDirection: "BOTH" | "FWD" | "REV"
```

---

# index.SDK.RoadTypeId

---
title: SDK.RoadTypeId type
source: types/index.SDK.RoadTypeId.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias RoadTypeId

```typescript
RoadTypeId: Values < typeof ROAD_TYPE >
```

---

# index.SDK.SaveMode

---
title: SDK.SaveMode type
source: types/index.SDK.SaveMode.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SaveMode

```typescript
SaveMode: "DISALLOWED" | "EDITING" | "IDLE" | "SUGGESTING"
```

---

# index.SDK.SdkFeatureGeometry

---
title: SDK.SdkFeatureGeometry type
source: types/index.SDK.SdkFeatureGeometry.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SdkFeatureGeometry

```typescript
SdkFeatureGeometry: Point | LineString | Polygon
```

---

# index.SDK.SdkFeatureProperties

---
title: SDK.SdkFeatureProperties type
source: types/index.SDK.SdkFeatureProperties.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SdkFeatureProperties

```typescript
SdkFeatureProperties: Record <
  string ,
  string
  | number
  | null
  | undefined
  | SdkFeatureGeometry ,
  >
```

---

# index.SDK.SdkFeatureStyleContext

---
title: SDK.SdkFeatureStyleContext type
source: types/index.SDK.SdkFeatureStyleContext.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SdkFeatureStyleContext

```typescript
SdkFeatureStyleContext: Record <
  string ,
  (
  context: { feature ?: SdkWazeFeature ; zoomLevel: number } ,
  ) = > string | number | undefined ,
  >
```

---

# index.SDK.SdkFeatureStylePredicate

---
title: SDK.SdkFeatureStylePredicate type
source: types/index.SDK.SdkFeatureStylePredicate.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SdkFeatureStylePredicate

```typescript
SdkFeatureStylePredicate: (
  properties: SdkFeatureProperties ,
  zoomLevel: number ,
  ) = > boolean
```

---

# index.SDK.SdkMouseEventName

---
title: SDK.SdkMouseEventName type
source: types/index.SDK.SdkMouseEventName.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SdkMouseEventName

```typescript
SdkMouseEventName: 
  | typeof SDK_EVENT_NAME.MAP_MOUSE_CLICK
  | typeof SDK_EVENT_NAME.MAP_MOUSE_DOWN
  | typeof SDK_EVENT_NAME.MAP_MOUSE_UP
  | typeof SDK_EVENT_NAME.MAP_MOUSE_MOVE
  | typeof SDK_EVENT_NAME.MAP_MOUSE_OUT
```

---

# index.SDK.SegmentDirection

---
title: SDK.SegmentDirection type
source: types/index.SDK.SegmentDirection.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SegmentDirection

```typescript
SegmentDirection: Values < typeof SegmentDirection >
```

---

# index.SDK.SegmentLaneGuidanceDirection

---
title: SDK.SegmentLaneGuidanceDirection type
source: types/index.SDK.SegmentLaneGuidanceDirection.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SegmentLaneGuidanceDirection

```typescript
SegmentLaneGuidanceDirection: Extract < SegmentDirection , "A_TO_B" | "B_TO_A" >
```

---

# index.SDK.SegmentPermission

---
title: SDK.SegmentPermission type
source: types/index.SDK.SegmentPermission.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SegmentPermission

```typescript
SegmentPermission: Values < typeof SegmentPermission >
```

---

# index.SDK.Selection

---
title: SDK.Selection type
source: types/index.SDK.Selection.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Selection

```typescript
Selection: 
  | { ids: number [] ; objectType: typeof SEGMENT }
  | { ids: string [] ; objectType: typeof VENUE }
  | { ids: number [] ; objectType: typeof BIG_JUNCTION }
  | { ids: number [] ; objectType: typeof CITY }
  | { ids: string [] ; objectType: typeof MAP_COMMENT }
  | { ids: number [] ; objectType: typeof NODE }
  | { ids: number [] ; objectType: typeof PERMANENT_HAZARD }
  | { ids: number [] ; objectType: typeof RESTRICTED_DRIVING_AREA }
  | { ids: number [] ; objectType: typeof SEGMENT_SUGGESTION }
```

---

# index.SDK.SelectionWithLocalizedTypeName

---
title: SDK.SelectionWithLocalizedTypeName type
source: types/index.SDK.SelectionWithLocalizedTypeName.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SelectionWithLocalizedTypeName

```typescript
SelectionWithLocalizedTypeName: Selection & { localizedTypeName: string }
```

---

# index.SDK.ServiceType

---
title: SDK.ServiceType type
source: types/index.SDK.ServiceType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ServiceType

```typescript
ServiceType: GENERAL_SERVICE_TYPE | PARKING_LOT_SERVICE_TYPE
```

---

# index.SDK.SidebarTabName

---
title: SDK.SidebarTabName type
source: types/index.SDK.SidebarTabName.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SidebarTabName

```typescript
SidebarTabName: Values < typeof SidebarTabName >
```

---

# index.SDK.SnapTo

---
title: SDK.SnapTo type
source: types/index.SDK.SnapTo.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SnapTo

```typescript
SnapTo: "segment" | "none"
```

---

# index.SDK.SpotsEstimate

---
title: SDK.SpotsEstimate type
source: types/index.SDK.SpotsEstimate.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SpotsEstimate

```typescript
SpotsEstimate: 
  | "R_1_TO_10"
  | "R_11_TO_30"
  | "R_31_TO_60"
  | "R_61_TO_100"
  | "R_101_TO_300"
  | "R_301_TO_600"
  | "R_600_PLUS"
```

---

# index.SDK.SuggestibleActionType

---
title: SDK.SuggestibleActionType type
source: types/index.SDK.SuggestibleActionType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SuggestibleActionType

```typescript
SuggestibleActionType: "ADD" | "DELETE" | "UPDATE" | "SPLIT"
```

---

# index.SDK.SuggestionResolutionRejectionReason

---
title: SDK.SuggestionResolutionRejectionReason type
source: types/index.SDK.SuggestionResolutionRejectionReason.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SuggestionResolutionRejectionReason

```typescript
SuggestionResolutionRejectionReason: 
  | "EDIT_IS_WRONG"
  | "EDIT_NOT_ALIGNED_TO_GUIDELINES"
  | "GENERAL_NO_LONGER_RELEVANT"
  | "GENERAL_OTHER"
  | "EDIT_ABUSE"
  | "EDIT_LOW_QUALITY"
```

---

# index.SDK.SuggestionResolutionStatus

---
title: SDK.SuggestionResolutionStatus type
source: types/index.SDK.SuggestionResolutionStatus.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SuggestionResolutionStatus

```typescript
SuggestionResolutionStatus: 
  | "ACCEPTED"
  | "OPEN"
  | "REJECTED"
  | "REJECTED_APPEALABLE"
```

---

# index.SDK.UnpavedRoadsSetting

---
title: SDK.UnpavedRoadsSetting type
source: types/index.SDK.UnpavedRoadsSetting.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias UnpavedRoadsSetting

```typescript
UnpavedRoadsSetting: "ALLOW" | "DISALLOW" | "AVOID_LONG_ONES"
```

---

# index.SDK.UpdateRequestSource

---
title: SDK.UpdateRequestSource type
source: types/index.SDK.UpdateRequestSource.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias UpdateRequestSource

```typescript
UpdateRequestSource: "MOBILE_CLIENT" | "MOBILE_WEB" | "WEB" | "REPORTING_AGENT"
```

---

# index.SDK.UpdateRequestType

---
title: SDK.UpdateRequestType type
source: types/index.SDK.UpdateRequestType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias UpdateRequestType

```typescript
UpdateRequestType: 
  | "BLOCKED_ROAD"
  | "INCORRECT_ADDRESS"
  | "INCORRECT_GENERAL_ERROR"
  | "INCORRECT_JUNCTION"
  | "INCORRECT_MISSING_ROUNDABOUT"
  | "INCORRECT_ROUTE"
  | "INCORRECT_TURN"
  | "MISSING_BRIDGE_OVERPASS"
  | "MISSING_EXIT"
  | "MISSING_ROAD"
  | "TURN_NOT_ALLOWED"
  | "WRONG_DRIVING_DIRECTIONS"
```

---

# index.SDK.UpdateableMapProblemState

---
title: SDK.UpdateableMapProblemState type
source: types/index.SDK.UpdateableMapProblemState.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias UpdateableMapProblemState

```typescript
UpdateableMapProblemState: Values < typeof UpdateableMapProblemState >
```

---

# index.SDK.UserRank

---
title: SDK.UserRank type
source: types/index.SDK.UserRank.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias UserRank

```typescript
UserRank: 0 | 1 | 2 | 3 | 4 | 5 | 6
```

---

# index.SDK.VehicleType

---
title: SDK.VehicleType type
source: types/index.SDK.VehicleType.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VehicleType

```typescript
VehicleType: 
  | "BUS"
  | "CAV"
  | "CLEAN_FUEL"
  | "EV"
  | "HAZARDOUS_MATERIALS"
  | "HOV_2"
  | "HOV_3"
  | "HYBRID"
  | "MOTORCYCLE"
  | "PRIVATE"
  | "PUBLIC_TRANSPORTATION"
  | "RV"
  | "TAXI"
  | "TOWING_VEHICLE"
  | "TRUCK"
```

---

# index.SDK.VenueCategoryId

---
title: SDK.VenueCategoryId type
source: types/index.SDK.VenueCategoryId.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VenueCategoryId

```typescript
VenueCategoryId: VenueSubCategoryId | VenueResidentialId | VenueMainCategoryId
```

---

# index.SDK.VenueMainCategoryId

---
title: SDK.VenueMainCategoryId type
source: types/index.SDK.VenueMainCategoryId.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VenueMainCategoryId

```typescript
VenueMainCategoryId: Values < typeof VENUE_MAIN_CATEGORY >
```

---

# index.SDK.VenuePermission

---
title: SDK.VenuePermission type
source: types/index.SDK.VenuePermission.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VenuePermission

```typescript
VenuePermission: Values < typeof VenuePermission >
```

---

# index.SDK.VenueResidentialId

---
title: SDK.VenueResidentialId type
source: types/index.SDK.VenueResidentialId.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VenueResidentialId

```typescript
VenueResidentialId: typeof VENUE_RESIDENTIAL
```

---

# index.SDK.VenueSubCategoryId

---
title: SDK.VenueSubCategoryId type
source: types/index.SDK.VenueSubCategoryId.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VenueSubCategoryId

```typescript
VenueSubCategoryId: ArrayElement < Values < typeof VENUE_SUBCATEGORIES > >
```

---

# index.SDK.WME_LAYER_NAMES

---
title: SDK.WME_LAYER_NAMES type
source: types/index.SDK.WME_LAYER_NAMES.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias WME_LAYER_NAMES

```typescript
WME_LAYER_NAMES: Values < typeof WME_LAYER_NAMES >
```

---

# index.SDK.ZoomLevel

---
title: SDK.ZoomLevel type
source: types/index.SDK.ZoomLevel.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias ZoomLevel

```typescript
ZoomLevel: 
  | 4
  | 5
  | 6
  | 7
  | 8
  | 9
  | 10
  | 11
  | 12
  | 13
  | 14
  | 15
  | 16
  | 17
  | 18
  | 19
  | 20
  | 21
  | 22
```

---

