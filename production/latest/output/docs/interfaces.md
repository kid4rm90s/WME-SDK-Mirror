# index.SDK.AddableVehicleRule

---
title: SDK.AddableVehicleRule interface
source: interfaces/index.SDK.AddableVehicleRule.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface AddableVehicleRule

```typescript
interface AddableVehicleRule {
  licensePlateRule: LicensePlateRule | null ;
  minPassengers: 0 | 2 | 3 | 4 ;
  subscriptions: string [] ;
  vehicleTypes: AddableVehicleType [] ;
}
```
Represents a vehicle rule when updating restrictions.
## Properties
### `minPassengers`

```typescript
minPassengers: 0 | 2 | 3 | 4
```
### `vehicleTypes`

```typescript
vehicleTypes: AddableVehicleType []
```

---

# index.SDK.AddressRawComponents

---
title: SDK.AddressRawComponents interface
source: interfaces/index.SDK.AddressRawComponents.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface AddressRawComponents

```typescript
interface AddressRawComponents {
  cityName ?: string ;
  countryId ?: number ;
  stateId ?: number ;
  streetName ?: string ;
}
```
## Properties
### **Optional** `cityName`

```typescript
cityName ?: string
```
### **Optional** `countryId`

```typescript
countryId ?: number
```
### **Optional** `stateId`

```typescript
stateId ?: number
```
### **Optional** `streetName`

```typescript
streetName ?: string
```

---

# index.SDK.AffectedObject

---
title: SDK.AffectedObject interface
source: interfaces/index.SDK.AffectedObject.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface AffectedObject

```typescript
interface AffectedObject {
  objectId: string | number | null ;
  objectType: ObjectType ;
}
```
## Properties
### `objectId`

```typescript
objectId: string | number | null
```
### `objectType`

```typescript
objectType: ObjectType
```

---

# index.SDK.BaseAddress

---
title: SDK.BaseAddress interface
source: interfaces/index.SDK.BaseAddress.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface BaseAddress

```typescript
interface BaseAddress {
  city: City | null ;
  country: Country | null ;
  isEmpty: boolean ;
  state: State | null ;
  street: Street | null ;
}
```
## Properties
### `city`

```typescript
city: City | null
```
### `country`

```typescript
country: Country | null
```
### `isEmpty`

```typescript
isEmpty: boolean
```
### `state`

```typescript
state: State | null
```
### `street`

```typescript
street: Street | null
```

---

# index.SDK.BasePermanentHazard

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

---

# index.SDK.BaseRestriction

---
title: SDK.BaseRestriction interface
source: interfaces/index.SDK.BaseRestriction.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface BaseRestriction

```typescript
interface BaseRestriction {
  defaultType: RESTRICTION_TYPE | null ;
  description: string | null ;
  driveProfiles: VehicleRules ;
  editable: boolean ;
  isExpired: boolean ;
  timeFrames: TimeFrame [] ;
  vehicleRules: VehicleRules ;
}
```
Base restriction contract shared by turn and segment restrictions.
## Properties
### `defaultType`

```typescript
defaultType: RESTRICTION_TYPE | null
```
### `description`

```typescript
description: string | null
```
### `driveProfiles`

```typescript
driveProfiles: VehicleRules
```
### `editable`

```typescript
editable: boolean
```
### `isExpired`

```typescript
isExpired: boolean
```
### `timeFrames`

```typescript
timeFrames: TimeFrame []
```
### `vehicleRules`

```typescript
vehicleRules: VehicleRules
```

---

# index.SDK.BaseVehicleRule

---
title: SDK.BaseVehicleRule interface
source: interfaces/index.SDK.BaseVehicleRule.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface BaseVehicleRule

```typescript
interface BaseVehicleRule {
  licensePlateRule: LicensePlateRule | null ;
  subscriptions: string [] ;
}
```
Represents a vehicle rule for specific vehicle exemptions or restrictions.
## Properties
### `licensePlateRule`

```typescript
licensePlateRule: LicensePlateRule | null
```
### `subscriptions`

```typescript
subscriptions: string []
```

---

# index.SDK.BigJunction

---
title: SDK.BigJunction interface
source: interfaces/index.SDK.BigJunction.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface BigJunction

```typescript
interface BigJunction {
  cityId: number | null ;
  geometry: Polygon ;
  id: number ;
  modificationData: ModificationMetadata ;
  name: string | null ;
  segmentIds: number [] ;
}
```
## Properties
### `cityId`

```typescript
cityId: number | null
```
### `geometry`

```typescript
geometry: Polygon
```
### `id`

```typescript
id: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string | null
```
### `segmentIds`

```typescript
segmentIds: number []
```

---

# index.SDK.CallSite

---
title: SDK.CallSite interface
source: interfaces/index.SDK.CallSite.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface CallSite

```typescript
interface CallSite {
  getColumnNumber () : number | null ;
  getEnclosingColumnNumber () : number | null ;
  getEnclosingLineNumber () : number | null ;
  getEvalOrigin () : string | undefined ;
  getFileName () : string | null ;
  getFunction () : Function | undefined ;
  getFunctionName () : string | null ;
  getLineNumber () : number | null ;
  getMethodName () : string | null ;
  getPosition () : number ;
  getPromiseIndex () : number | null ;
  getScriptHash () : string ;
  getScriptNameOrSourceURL () : string | null ;
  getThis () : unknown ;
  getTypeName () : string | null ;
  isAsync () : boolean ;
  isConstructor () : boolean ;
  isEval () : boolean ;
  isNative () : boolean ;
  isPromiseAll () : boolean ;
  isToplevel () : boolean ;
}
```
## Methods

---

# index.SDK.Camera

---
title: SDK.Camera interface
source: interfaces/index.SDK.Camera.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Camera

```typescript
interface Camera {
  direction: RestrictionSegmentDirection | null ;
  geometry: Point ;
  id: number ;
  lockRank: number | null ;
  modificationData: ModificationMetadata ;
  segmentId: number | null ;
  subTypes: PermanentHazardSubType [] ;
  type: "CAMERA" ;
  types: CameraType [] ;
}
```
## Properties
### `geometry`

```typescript
geometry: Point
```
### `type`

```typescript
type: "CAMERA"
```
### `types`

```typescript
types: CameraType []
```

---

# index.SDK.ChangedField

---
title: SDK.ChangedField interface
source: interfaces/index.SDK.ChangedField.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ChangedField

```typescript
interface ChangedField {
  fieldName: string | undefined ;
}
```
## Properties
### `fieldName`

```typescript
fieldName: string | undefined
```

---

# index.SDK.ChangedIDsInfo

---
title: SDK.ChangedIDsInfo interface
source: interfaces/index.SDK.ChangedIDsInfo.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ChangedIDsInfo

```typescript
interface ChangedIDsInfo {
  newID: string | number | null ;
  oldID: string | number | null ;
}
```
## Properties
### `newID`

```typescript
newID: string | number | null
```
### `oldID`

```typescript
oldID: string | number | null
```

---

# index.SDK.City

---
title: SDK.City interface
source: interfaces/index.SDK.City.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface City

```typescript
interface City {
  countryId: number | null ;
  geometry: Point ;
  id: number ;
  isEmpty: boolean ;
  modificationData: ModificationMetadata ;
  name: string | null ;
  stateId: number | null ;
}
```
## Properties
### `countryId`

```typescript
countryId: number | null
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```
### `isEmpty`

```typescript
isEmpty: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string | null
```
### `stateId`

```typescript
stateId: number | null
```

---

# index.SDK.ConversationElement

---
title: SDK.ConversationElement interface
source: interfaces/index.SDK.ConversationElement.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ConversationElement

```typescript
interface ConversationElement {
  createdOn: number ;
  text: string ;
  userName: string | null ;
}
```
## Properties
### `createdOn`

```typescript
createdOn: number
```
### `text`

```typescript
text: string
```
### `userName`

```typescript
userName: string | null
```

---

# index.SDK.Country

---
title: SDK.Country interface
source: interfaces/index.SDK.Country.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Country

```typescript
interface Country {
  abbr: string ;
  defaultLaneWidthPerRoadType: 
  | Partial <
  {
  "1": number ;
  "10": number ;
  "15": number ;
  "16": number ;
  "17": number ;
  "18": number ;
  "19": number ;
  "2": number ;
  "20": number ;
  "22": number ;
  "3": number ;
  "4": number ;
  "5": number ;
  "6": number ;
  "7": number ;
  "8": number ;
  "9": number ;
} ,
  >
  | null ;
  id: number ;
  isLeftHandTraffic: boolean ;
  modificationData: ModificationMetadata ;
  name: string ;
  regionCode: RegionCode
  | null ;
  restrictionSubscriptions: Subscription [] ;
}
```
## Properties
### `abbr`

```typescript
abbr: string
```
### `defaultLaneWidthPerRoadType`

```typescript
defaultLaneWidthPerRoadType: 
  | Partial <
  {
  "1": number ;
  "10": number ;
  "15": number ;
  "16": number ;
  "17": number ;
  "18": number ;
  "19": number ;
  "2": number ;
  "20": number ;
  "22": number ;
  "3": number ;
  "4": number ;
  "5": number ;
  "6": number ;
  "7": number ;
  "8": number ;
  "9": number ;
} ,
  >
  | null
```
### `id`

```typescript
id: number
```
### `isLeftHandTraffic`

```typescript
isLeftHandTraffic: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```
### `regionCode`

```typescript
regionCode: RegionCode | null
```
### `restrictionSubscriptions`

```typescript
restrictionSubscriptions: Subscription []
```

---

# index.SDK.DriveProfile

---
title: SDK.DriveProfile interface
source: interfaces/index.SDK.DriveProfile.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface DriveProfile

```typescript
interface DriveProfile {
  licensePlateNumber: string ;
  numPassengers: number ;
  subscriptions: string [] ;
  vehicleTypes: VehicleType [] ;
}
```
## Properties
### `licensePlateNumber`

```typescript
licensePlateNumber: string
```
### `numPassengers`

```typescript
numPassengers: number
```
### `subscriptions`

```typescript
subscriptions: string []
```
### `vehicleTypes`

```typescript
vehicleTypes: VehicleType []
```

---

# index.SDK.EditSuggestion

---
title: SDK.EditSuggestion interface
source: interfaces/index.SDK.EditSuggestion.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface EditSuggestion

```typescript
interface EditSuggestion {
  bbox: BBox ;
  id: string ;
  isRead: boolean ;
  isStarred: boolean ;
  modificationData: ModificationMetadata ;
  source: EditSuggestionSource ;
  status: EditSuggestionStatus ;
  suggestions: Suggestion [] ;
}
```
Represents an edit suggestion, potentially containing multiple individual suggestions.
## Properties
### `bbox`

```typescript
bbox: BBox
```
### `id`

```typescript
id: string
```
### `isRead`

```typescript
isRead: boolean
```
### `isStarred`

```typescript
isStarred: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `source`

```typescript
source: EditSuggestionSource
```
### `status`

```typescript
status: EditSuggestionStatus
```
### `suggestions`

```typescript
suggestions: Suggestion []
```

---

# index.SDK.EditSuggestionChange

---
title: SDK.EditSuggestionChange interface
source: interfaces/index.SDK.EditSuggestionChange.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface EditSuggestionChange

```typescript
interface EditSuggestionChange {
  attributeChanges: SuggestionAttributeChange < unknown > [] ;
  createdOn: number | null ;
  rejectionReason: SuggestionResolutionRejectionReason | null ;
  status: SuggestionResolutionStatus ;
  suggestionId: string ;
}
```
Represents a change suggested in an edit suggestion, containing an attribute change per each changed attribute.
## Properties
### `attributeChanges`

```typescript
attributeChanges: SuggestionAttributeChange < unknown > []
```
### `createdOn`

```typescript
createdOn: number | null
```
### `rejectionReason`

```typescript
rejectionReason: SuggestionResolutionRejectionReason | null
```
### `status`

```typescript
status: SuggestionResolutionStatus
```
### `suggestionId`

```typescript
suggestionId: string
```

---

# index.SDK.ErrorOptions

---
title: SDK.ErrorOptions interface
source: interfaces/index.SDK.ErrorOptions.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ErrorOptions

```typescript
interface ErrorOptions {
  cause ?: unknown ;
}
```
## Properties

---

# index.SDK.ExitSign

---
title: SDK.ExitSign interface
source: interfaces/index.SDK.ExitSign.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ExitSign

```typescript
interface ExitSign {
  description: string ;
  id: number | null ;
}
```
## Properties
### `description`

```typescript
description: string
```
### `id`

```typescript
id: number | null
```

---

# index.SDK.FeatureStyle

---
title: SDK.FeatureStyle interface
source: interfaces/index.SDK.FeatureStyle.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface FeatureStyle

```typescript
interface FeatureStyle {
  backgroundGraphic ?: string ;
  backgroundGraphicZIndex ?: number ;
  backgroundHeight ?: string | number ;
  backgroundWidth ?: string | number ;
  backgroundXOffset ?: string | number ;
  backgroundYOffset ?: string | number ;
  cursor ?: string ;
  display ?: string ;
  externalGraphic ?: string | null ;
  fill ?: boolean ;
  fillColor ?: string ;
  fillOpacity ?: number ;
  fontColor ?: string ;
  fontFamily ?: string ;
  fontOpacity ?: number ;
  fontSize ?: string ;
  fontStyle ?: string ;
  fontWeight ?: string ;
  graphic ?: boolean ;
  graphicHeight ?: string | number ;
  graphicName ?: string ;
  graphicOpacity ?: string | number ;
  graphicWidth ?: string | number ;
  graphicXOffset ?: number ;
  graphicYOffset ?: string | number ;
  graphicZIndex ?: string | number ;
  hoverFillColor ?: string ;
  hoverFillOpacity ?: number ;
  hoverPointRadius ?: number ;
  hoverPointUnit ?: string ;
  hoverStrokeColor ?: string ;
  hoverStrokeOpacity ?: number ;
  hoverStrokeWidth ?: number ;
  label ?: string ;
  labelAlign ?: string ;
  labelOutlineColor ?: string ;
  labelOutlineOpacity ?: number ;
  labelOutlineWidth ?: number ;
  labelSelect ?: boolean ;
  labelXOffset ?: number ;
  labelYOffset ?: number ;
  pointerEvents ?: string ;
  pointRadius ?: string | number ;
  rotation ?: string | number ;
  stroke ?: boolean ;
  strokeColor ?: string ;
  strokeDashstyle ?:
  | "dot"
  | "dash"
  | "dashdot"
  | "longdash"
  | "longdashdot"
  | "solid" ;
  strokeLinecap ?: "butt"
  | "round"
  | "square" ;
  strokeOpacity ?: string | number ;
  strokeWidth ?: string | number ;
  title ?: string ;
}
```
List of OpenLayers supported styles taken from OL 2 docs
Seehttps://amirn.users.x20web.corp.google.com/www/dev.openlayers.org/docs/files/OpenLayers/Feature/Vector-js.html#OpenLayers.Feature.Vector.OpenLayers.Feature.Vector.stylehttp://cs/waze-dev/web-common/packages/web-map/src/third_party/OpenLayers/Feature/Vector.js;l=373-434;rcl=b5d307754927a6944baa9bdd3f2ba802ebffdbc3Param: backgroundGraphicUrl to a graphic to be used as the background under an externalGraphic.Param: backgroundGraphicZIndexThe integer z-index value to use in rendering the background graphic.Param: backgroundHeightThe height of the background graphic. If not provided, the graphicHeight will be used.Param: backgroundWidthThe width of the background width. If not provided, the graphicWidth will be used.Param: backgroundXOffsetThe x offset (in pixels) for the background graphic.Param: backgroundYOffsetThe y offset (in pixels) for the background graphic.Param: cursorDefault is "".Param: displaySymbolizers will have no effect if display is set to "none".  All other values have no effect.Param: externalGraphicUrl to an external graphic that will be used for rendering points.Param: fillSet to false if no fill is desired.Param: fillColorHex fill color.  Default is "#ee9900".Param: fillOpacityFill opacity (0-1).  Default is 0.4Param: fontColorThe font color for the label, to be provided like CSS.Param: fontFamilyThe font family for the label, to be provided like in CSS.Param: fontOpacityOpacity (0-1) for the labelParam: fontSizeThe font size for the label, to be provided like in CSS.Param: fontStyleThe font style for the label, to be provided like in CSS.Param: fontWeightThe font weight for the label, to be provided like in CSS.Param: graphicSet to false if no graphic is desired.Param: graphicHeightPixel height for sizing an external graphic.Param: graphicNameNamed graphic to use when rendering points.  Supported values include "circle" (default), "square", "star", "x", "cross", "triangle".Param: graphicOpacityOpacity (0-1) for an external graphic.Param: graphicWidthPixel width for sizing an external graphic.Param: graphicXOffsetPixel offset along the positive x axis for displacing an external graphic.Param: graphicYOffsetPixel offset along the positive y axis for displacing an external graphic.Param: graphicZIndexThe integer z-index value to use in rendering.Param: labelThe text for an optional label. For browsers that use the canvas renderer, this requires either fillText or mozDrawText to be available.Param: labelAlignLabel alignment. This specifies the insertion point relative to the text. It is a string
composed of two characters. The first character is for the horizontal alignment, the second for the vertical
alignment. Valid values for horizontal alignment: "l"=left, "c"=center, "r"=right. Valid values for vertical
alignment: "t"=top, "m"=middle, "b"=bottom. Example values: "lt", "cm", "rb". Default is "cm".Param: labelOutlineColorThe color of the label outline. Default is 'white'. Only supported by the canvas & SVG renderers.Param: labelOutlineOpacityThe opacity (0-1) of the label outline. Default is fontOpacity. Only supported by the canvas & SVG renderers.Param: labelOutlineWidthThe width of the label outline. Default is 3, set to 0 or null to disable. Only supported by the  SVG renderers.Param: labelSelectIf set to true, labels will be selectable using SelectFeature or similar controls. Default is false.Param: labelXOffsetPixel offset along the positive x axis for displacing the label. Not supported by the canvas renderer.Param: labelYOffsetPixel offset along the positive y axis for displacing the label. Not supported by the canvas renderer.Param: pointRadiusPixel point radius.  Default is 6.Param: pointerEventsDefault is "visiblePainted".Param: rotationFor point symbolizers, this is the rotation of a graphic in the clockwise direction about its center point (or any point off center as specified by graphicXOffset and graphicYOffset).Param: strokeSet to false if no stroke is desired.Param: strokeColorHex stroke color.  Default is "#ee9900".Param: strokeDashstyleStroke dash style.  Default is "solid". [dot | dash | dashdot | longdash | longdashdot | solid]Param: strokeLinecapStroke cap type.  Default is "round".  [butt | round | square]Param: strokeOpacityStroke opacity (0-1).  Default is 1.Param: strokeWidthPixel stroke width.  Default is 1.Param: titleTooltip when hovering over a feature. Not supported by the canvas renderer.
## Properties

---

# index.SDK.GeoJsonObject

---
title: SDK.GeoJsonObject interface
source: interfaces/index.SDK.GeoJsonObject.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface GeoJsonObject

```typescript
interface GeoJsonObject {
  bbox ?: BBox ;
  type: 
  | "Point"
  | "LineString"
  | "Polygon"
  | "Feature"
  | "MultiLineString"
  | "MultiPolygon"
  | "MultiPoint"
  | "GeometryCollection"
  | "FeatureCollection" ;
}
```
The base GeoJSON object.https://tools.ietf.org/html/rfc7946#section-3The GeoJSON specification also allows foreign members
(https://tools.ietf.org/html/rfc7946#section-6.1)
Developers should use "&" type in TypeScript or extend the interface
to add these foreign members.
## Properties

---

# index.SDK.HouseNumber

---
title: SDK.HouseNumber interface
source: interfaces/index.SDK.HouseNumber.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface HouseNumber

```typescript
interface HouseNumber {
  fractionPoint: Point | null ;
  geometry: Point ;
  id: string ;
  isForced: boolean ;
  number: string ;
  segmentId: number ;
  updatedBy: string | null ;
}
```
Represents a house number associated with a segment.
It provides information about the house number itself, its location, and its relation to the segment.
## Properties
### `fractionPoint`

```typescript
fractionPoint: Point | null
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: string
```
### `isForced`

```typescript
isForced: boolean
```
### `number`

```typescript
number: string
```
### `segmentId`

```typescript
segmentId: number
```
### `updatedBy`

```typescript
updatedBy: string | null
```

---

# index.SDK.IssueTrackerFilters

---
title: SDK.IssueTrackerFilters interface
source: interfaces/index.SDK.IssueTrackerFilters.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface IssueTrackerFilters

```typescript
interface IssueTrackerFilters {
  mapProblems: MapProblemsFilterState | null ;
  mapSuggestions: MapSuggestionsFilterState | null ;
  placeUpdateRequests: PlaceUpdateRequestsFilterState | null ;
  updateRequests: UpdateRequestsFilterState | null ;
}
```
## Properties
### `mapProblems`

```typescript
mapProblems: MapProblemsFilterState | null
```
### `mapSuggestions`

```typescript
mapSuggestions: MapSuggestionsFilterState | null
```
### `placeUpdateRequests`

```typescript
placeUpdateRequests: PlaceUpdateRequestsFilterState | null
```
### `updateRequests`

```typescript
updateRequests: UpdateRequestsFilterState | null
```

---

# index.SDK.IssueTrackerPanelClosedEvent

---
title: SDK.IssueTrackerPanelClosedEvent interface
source: interfaces/index.SDK.IssueTrackerPanelClosedEvent.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface IssueTrackerPanelClosedEvent

```typescript
interface IssueTrackerPanelClosedEvent {
  type: IssueTrackerType | "unknown" ;
}
```
## Properties
### `type`

```typescript
type: IssueTrackerType | "unknown"
```

---

# index.SDK.IssueTrackerPanelOpenedEvent

---
title: SDK.IssueTrackerPanelOpenedEvent interface
source: interfaces/index.SDK.IssueTrackerPanelOpenedEvent.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface IssueTrackerPanelOpenedEvent

```typescript
interface IssueTrackerPanelOpenedEvent {
  id: string ;
  type: IssueTrackerType ;
}
```
## Properties
### `id`

```typescript
id: string
```
### `type`

```typescript
type: IssueTrackerType
```

---

# index.SDK.Junction

---
title: SDK.Junction interface
source: interfaces/index.SDK.Junction.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Junction

```typescript
interface Junction {
  geometry: Point ;
  id: number ;
  modificationData: ModificationMetadata ;
  segmentIds: number [] ;
}
```
## Properties
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `segmentIds`

```typescript
segmentIds: number []
```

---

# index.SDK.KeyboardShortcut

---
title: SDK.KeyboardShortcut interface
source: interfaces/index.SDK.KeyboardShortcut.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface KeyboardShortcut

```typescript
interface KeyboardShortcut {
  callback: () = > void ;
  description: string ;
  shortcutId: string ;
  shortcutKeys: string | null ;
}
```
A keyboard shortcut for userscript action.
## Properties
### `callback`

```typescript
callback: () = > void
```
### `description`

```typescript
description: string
```
### `shortcutId`

```typescript
shortcutId: string
```
### `shortcutKeys`

```typescript
shortcutKeys: string | null
```

---

# index.SDK.LineString

---
title: SDK.LineString interface
source: interfaces/index.SDK.LineString.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface LineString

```typescript
interface LineString {
  bbox ?: BBox ;
  coordinates: Position [] ;
  type: "LineString" ;
}
```
LineString geometry object.https://tools.ietf.org/html/rfc7946#section-3.1.4
## Properties

---

# index.SDK.LocalizedString

---
title: SDK.LocalizedString interface
source: interfaces/index.SDK.LocalizedString.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface LocalizedString

```typescript
interface LocalizedString {
  locale: string ;
  value: string ;
}
```
## Properties
### `locale`

```typescript
locale: string
```
### `value`

```typescript
value: string
```

---

# index.SDK.LonLat

---
title: SDK.LonLat interface
source: interfaces/index.SDK.LonLat.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface LonLat

```typescript
interface LonLat {
  lat: number ;
  lon: number ;
}
```
## Properties
### `lat`

```typescript
lat: number
```
### `lon`

```typescript
lon: number
```

---

# index.SDK.MajorTrafficEvent

---
title: SDK.MajorTrafficEvent interface
source: interfaces/index.SDK.MajorTrafficEvent.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MajorTrafficEvent

```typescript
interface MajorTrafficEvent {
  category: MajorTrafficEventCategory | null ;
  cityId: number | null ;
  endDate: string | null ;
  id: string ;
  isPublished: boolean ;
  isReady: boolean ;
  lockRank: UserRank | null ;
  modificationData: ModificationMetadata ;
  names: LocalizedString [] ;
  startDate: string | null ;
}
```
## Properties
### `category`

```typescript
category: MajorTrafficEventCategory | null
```
### `cityId`

```typescript
cityId: number | null
```
### `endDate`

```typescript
endDate: string | null
```
### `id`

```typescript
id: string
```
### `isPublished`

```typescript
isPublished: boolean
```
### `isReady`

```typescript
isReady: boolean
```
### `lockRank`

```typescript
lockRank: UserRank | null
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `names`

```typescript
names: LocalizedString []
```
### `startDate`

```typescript
startDate: string | null
```

---

# index.SDK.ManagedArea

---
title: SDK.ManagedArea interface
source: interfaces/index.SDK.ManagedArea.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ManagedArea

```typescript
interface ManagedArea {
  geometry: Polygon ;
  id: string ;
  userName: string ;
}
```
## Properties
### `geometry`

```typescript
geometry: Polygon
```
### `id`

```typescript
id: string
```
### `userName`

```typescript
userName: string
```

---

# index.SDK.ManagedAreaShort

---
title: SDK.ManagedAreaShort interface
source: interfaces/index.SDK.ManagedAreaShort.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ManagedAreaShort

```typescript
interface ManagedAreaShort {
  id: number ;
  name: string ;
}
```
## Properties
### `id`

```typescript
id: number
```
### `name`

```typescript
name: string
```

---

# index.SDK.MapComment

---
title: SDK.MapComment interface
source: interfaces/index.SDK.MapComment.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapComment

```typescript
interface MapComment {
  body: string ;
  conversation: ConversationElement [] ;
  endDate: string | null ;
  geometry: Point | Polygon ;
  id: string ;
  isFollowing: boolean ;
  isPoint: boolean ;
  lockRank: UserRank ;
  modificationData: ModificationMetadata ;
  subject: string ;
}
```
## Properties
### `body`

```typescript
body: string
```
### `conversation`

```typescript
conversation: ConversationElement []
```
### `endDate`

```typescript
endDate: string | null
```
### `geometry`

```typescript
geometry: Point | Polygon
```
### `id`

```typescript
id: string
```
### `isFollowing`

```typescript
isFollowing: boolean
```
### `isPoint`

```typescript
isPoint: boolean
```
### `lockRank`

```typescript
lockRank: UserRank
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `subject`

```typescript
subject: string
```

---

# index.SDK.MapProblem

---
title: SDK.MapProblem interface
source: interfaces/index.SDK.MapProblem.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapProblem

```typescript
interface MapProblem {
  geometry: Point ;
  id: string ;
  isEditable: boolean ;
  isOpen: boolean ;
  isRead: boolean ;
  isStarred: boolean ;
  problemType: MapProblemType ;
  resolvedOn: number | null ;
  severity: IssueSeverity ;
}
```
## Properties
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: string
```
### `isEditable`

```typescript
isEditable: boolean
```
### `isOpen`

```typescript
isOpen: boolean
```
### `isRead`

```typescript
isRead: boolean
```
### `isStarred`

```typescript
isStarred: boolean
```
### `problemType`

```typescript
problemType: MapProblemType
```
### `resolvedOn`

```typescript
resolvedOn: number | null
```
### `severity`

```typescript
severity: IssueSeverity
```

---

# index.SDK.MapProblemsFilterState

---
title: SDK.MapProblemsFilterState interface
source: interfaces/index.SDK.MapProblemsFilterState.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapProblemsFilterState

```typescript
interface MapProblemsFilterState {
  status: "OPEN" | "CLOSED" ;
}
```
## Properties
### `status`

```typescript
status: "OPEN" | "CLOSED"
```

---

# index.SDK.MapSuggestionsFilterState

---
title: SDK.MapSuggestionsFilterState interface
source: interfaces/index.SDK.MapSuggestionsFilterState.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapSuggestionsFilterState

```typescript
interface MapSuggestionsFilterState {
  status: 
  | "OPEN"
  | "ADDED_TO_MAP"
  | "APPROVED_BY_GOOGLE"
  | "CLOSED_ALL"
  | "NOT_APPROVED_BY_GOOGLE"
  | "PENDING_GOOGLE_REPLY"
  | "REJECTED_ALL" ;
}
```
## Properties
### `status`

```typescript
status: 
  | "OPEN"
  | "ADDED_TO_MAP"
  | "APPROVED_BY_GOOGLE"
  | "CLOSED_ALL"
  | "NOT_APPROVED_BY_GOOGLE"
  | "PENDING_GOOGLE_REPLY"
  | "REJECTED_ALL"
```

---

# index.SDK.MapUpdateRequest

---
title: SDK.MapUpdateRequest interface
source: interfaces/index.SDK.MapUpdateRequest.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapUpdateRequest

```typescript
interface MapUpdateRequest {
  description: string | null ;
  geometry: Point ;
  id: number ;
  isEditable: boolean ;
  isOpen: boolean ;
  isRead: boolean ;
  isStarred: boolean ;
  reportedOn: number ;
  resolutionState: string | null ;
  resolvedBy: string | null ;
  resolvedOn: number | null ;
  severity: IssueSeverity ;
  source: UpdateRequestSource ;
  updateRequestType: UpdateRequestType ;
  userPreferences: UpdateRequestUserPreferences ;
}
```
## Properties
### `description`

```typescript
description: string | null
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```
### `isEditable`

```typescript
isEditable: boolean
```
### `isOpen`

```typescript
isOpen: boolean
```
### `isRead`

```typescript
isRead: boolean
```
### `isStarred`

```typescript
isStarred: boolean
```
### `reportedOn`

```typescript
reportedOn: number
```
### `resolutionState`

```typescript
resolutionState: string | null
```
### `resolvedBy`

```typescript
resolvedBy: string | null
```
### `resolvedOn`

```typescript
resolvedOn: number | null
```
### `severity`

```typescript
severity: IssueSeverity
```
### `source`

```typescript
source: UpdateRequestSource
```
### `updateRequestType`

```typescript
updateRequestType: UpdateRequestType
```
### `userPreferences`

```typescript
userPreferences: UpdateRequestUserPreferences
```

---

# index.SDK.ModificationMetadata

---
title: SDK.ModificationMetadata interface
source: interfaces/index.SDK.ModificationMetadata.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface ModificationMetadata

```typescript
interface ModificationMetadata {
  createdBy: string | null ;
  createdOn: number | null ;
  updatedBy: string | null ;
  updatedOn: number | null ;
}
```
## Properties
### `createdBy`

```typescript
createdBy: string | null
```
### `createdOn`

```typescript
createdOn: number | null
```
### `updatedBy`

```typescript
updatedBy: string | null
```
### `updatedOn`

```typescript
updatedOn: number | null
```

---

# index.SDK.MultiLineString

---
title: SDK.MultiLineString interface
source: interfaces/index.SDK.MultiLineString.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MultiLineString

```typescript
interface MultiLineString {
  bbox ?: BBox ;
  coordinates: Position [] [] ;
  type: "MultiLineString" ;
}
```
MultiLineString geometry object.https://tools.ietf.org/html/rfc7946#section-3.1.5
## Properties

---

# index.SDK.MultiPolygon

---
title: SDK.MultiPolygon interface
source: interfaces/index.SDK.MultiPolygon.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MultiPolygon

```typescript
interface MultiPolygon {
  bbox ?: BBox ;
  coordinates: Position [] [] [] ;
  type: "MultiPolygon" ;
}
```
MultiPolygon geometry object.https://tools.ietf.org/html/rfc7946#section-3.1.7
## Properties

---

# index.SDK.NavigationPoint

---
title: SDK.NavigationPoint interface
source: interfaces/index.SDK.NavigationPoint.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface NavigationPoint

```typescript
interface NavigationPoint {
  isEntry: boolean ;
  isExit: boolean ;
  isPrimary: boolean ;
  name: string ;
  point: Point ;
}
```
## Properties
### `isEntry`

```typescript
isEntry: boolean
```
### `isExit`

```typescript
isExit: boolean
```
### `isPrimary`

```typescript
isPrimary: boolean
```
### `name`

```typescript
name: string
```
### `point`

```typescript
point: Point
```

---

# index.SDK.Node

---
title: SDK.Node interface
source: interfaces/index.SDK.Node.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Node

```typescript
interface Node {
  connectedSegmentIds: number [] ;
  geometry: Point ;
  id: number ;
}
```
## Properties
### `connectedSegmentIds`

```typescript
connectedSegmentIds: number []
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```

---

# index.SDK.OpeningHour

---
title: SDK.OpeningHour interface
source: interfaces/index.SDK.OpeningHour.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface OpeningHour

```typescript
interface OpeningHour {
  days: number [] ;
  fromHour: string ;
  toHour: string ;
}
```
## Properties
### `days`

```typescript
days: number []
```
### `fromHour`

```typescript
fromHour: string
```
### `toHour`

```typescript
toHour: string
```

---

# index.SDK.Pixel

---
title: SDK.Pixel interface
source: interfaces/index.SDK.Pixel.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Pixel

```typescript
interface Pixel {
  x: number ;
  y: number ;
}
```
## Properties
### `x`

```typescript
x: number
```
### `y`

```typescript
y: number
```

---

# index.SDK.PlaceUpdateRequestsFilterState

---
title: SDK.PlaceUpdateRequestsFilterState interface
source: interfaces/index.SDK.PlaceUpdateRequestsFilterState.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface PlaceUpdateRequestsFilterState

```typescript
interface PlaceUpdateRequestsFilterState {
  placeType: "RESIDENTIAL" | "PUBLIC" ;
}
```
## Properties
### `placeType`

```typescript
placeType: "RESIDENTIAL" | "PUBLIC"
```

---

# index.SDK.Point

---
title: SDK.Point interface
source: interfaces/index.SDK.Point.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Point

```typescript
interface Point {
  bbox ?: BBox ;
  coordinates: Position ;
  type: "Point" ;
}
```
Point geometry object.https://tools.ietf.org/html/rfc7946#section-3.1.2
## Properties

---

# index.SDK.Polygon

---
title: SDK.Polygon interface
source: interfaces/index.SDK.Polygon.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Polygon

```typescript
interface Polygon {
  bbox ?: BBox ;
  coordinates: Position [] [] ;
  type: "Polygon" ;
}
```
Polygon geometry object.https://tools.ietf.org/html/rfc7946#section-3.1.6
## Properties

---

# index.SDK.RegisterSidebarTabResult

---
title: SDK.RegisterSidebarTabResult interface
source: interfaces/index.SDK.RegisterSidebarTabResult.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RegisterSidebarTabResult

```typescript
interface RegisterSidebarTabResult {
  tabLabel: HTMLElement ;
  tabPane: HTMLElement ;
}
```
## Properties
### `tabLabel`

```typescript
tabLabel: HTMLElement
```
### `tabPane`

```typescript
tabPane: HTMLElement
```

---

# index.SDK.RestrictedDrivingArea

---
title: SDK.RestrictedDrivingArea interface
source: interfaces/index.SDK.RestrictedDrivingArea.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RestrictedDrivingArea

```typescript
interface RestrictedDrivingArea {
  center: Point ;
  geometry: Polygon ;
  id: number ;
  modificationData: ModificationMetadata ;
  name: string ;
  restrictionName: string ;
}
```
## Properties
### `center`

```typescript
center: Point
```
### `geometry`

```typescript
geometry: Polygon
```
### `id`

```typescript
id: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```
### `restrictionName`

```typescript
restrictionName: string
```

---

# index.SDK.RoadClosure

---
title: SDK.RoadClosure interface
source: interfaces/index.SDK.RoadClosure.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RoadClosure

```typescript
interface RoadClosure {
  attributions: RoadClosureAttribution [] ;
  description: string | null ;
  endDate: string | null ;
  id: string ;
  isForward: boolean ;
  isPermanent: boolean ;
  modificationData: ModificationMetadata ;
  segmentId: number ;
  startDate: string | null ;
  status: ClosureStatus ;
  trafficEventId: string | null ;
}
```
## Properties
### `attributions`

```typescript
attributions: RoadClosureAttribution []
```
### `description`

```typescript
description: string | null
```
### `endDate`

```typescript
endDate: string | null
```
### `id`

```typescript
id: string
```
### `isForward`

```typescript
isForward: boolean
```
### `isPermanent`

```typescript
isPermanent: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `segmentId`

```typescript
segmentId: number
```
### `startDate`

```typescript
startDate: string | null
```
### `status`

```typescript
status: ClosureStatus
```
### `trafficEventId`

```typescript
trafficEventId: string | null
```

---

# index.SDK.RoadClosureAttribution

---
title: SDK.RoadClosureAttribution interface
source: interfaces/index.SDK.RoadClosureAttribution.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RoadClosureAttribution

```typescript
interface RoadClosureAttribution {
  channel: RoadClosureAttributionChannel ;
  contributionTime: number | null ;
  contributorType: RoadClosureContributorType ;
  credit: string | null ;
}
```
## Properties
### `channel`

```typescript
channel: RoadClosureAttributionChannel
```
### `contributionTime`

```typescript
contributionTime: number | null
```
### `contributorType`

```typescript
contributorType: RoadClosureContributorType
```
### `credit`

```typescript
credit: string | null
```

---

# index.SDK.RoadShield

---
title: SDK.RoadShield interface
source: interfaces/index.SDK.RoadShield.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RoadShield

```typescript
interface RoadShield {
  direction: string | null ;
  id: number | null ;
  signText ?: string | null ;
}
```
## Properties
### `direction`

```typescript
direction: string | null
```
### `id`

```typescript
id: number | null
```
### **Optional** `signText`

```typescript
signText ?: string | null
```

---

# index.SDK.RoadType

---
title: SDK.RoadType interface
source: interfaces/index.SDK.RoadType.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RoadType

```typescript
interface RoadType {
  id: RoadTypeId ;
  localizedName: string ;
  name: string ;
}
```
## Properties
### `id`

```typescript
id: RoadTypeId
```
### `localizedName`

```typescript
localizedName: string
```
### `name`

```typescript
name: string
```

---

# index.SDK.SchoolZone

---
title: SDK.SchoolZone interface
source: interfaces/index.SDK.SchoolZone.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SchoolZone

```typescript
interface SchoolZone {
  direction: RestrictionSegmentDirection | null ;
  excludedRoadTypes: RoadTypeId [] | null ;
  geometry: Point | Polygon ;
  id: number ;
  lockRank: number | null ;
  modificationData: ModificationMetadata ;
  name: string | null ;
  scheduleId: string | null ;
  segmentId: number | null ;
  speedLimit: number | null ;
  subTypes: PermanentHazardSubType [] ;
  type: "SCHOOL_ZONE" ;
}
```
## Properties
### `excludedRoadTypes`

```typescript
excludedRoadTypes: RoadTypeId [] | null
```
### `name`

```typescript
name: string | null
```
### `scheduleId`

```typescript
scheduleId: string | null
```
### `speedLimit`

```typescript
speedLimit: number | null
```
### `type`

```typescript
type: "SCHOOL_ZONE"
```

---

# index.SDK.SdkEvents

---
title: SDK.SdkEvents interface
source: interfaces/index.SDK.SdkEvents.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkEvents

```typescript
interface SdkEvents {
  "wme-after-edit": { affectedObjects: AffectedObject [] } ;
  "wme-after-redo-clear": undefined ;
  "wme-after-undo": undefined ;
  "wme-data-model-object-changed-id": {
  dataModelName: DataModelName ;
  objectIds: ChangedIDsInfo ;
} ;
  "wme-data-model-object-state-deleted": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
} ;
  "wme-data-model-objects-added": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
} ;
  "wme-data-model-objects-changed": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
} ;
  "wme-data-model-objects-removed": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
} ;
  "wme-data-model-objects-saved": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
} ;
  "wme-editing-house-numbers": { isEditingHouseNumbers: false } ;
  "wme-feature-editor-opened": {
  featureType: 
  | "segment"
  | "bigJunction"
  | "city"
  | "googlePlace"
  | "mapComment"
  | "node"
  | "permanentHazard"
  | "restrictedDrivingArea"
  | "segmentSuggestion"
  | "venue" ;
} ;
  "wme-house-number-added": { houseNumberId: string } ;
  "wme-house-number-deleted": { houseNumberId: string } ;
  "wme-house-number-moved": { houseNumberId: string } ;
  "wme-house-number-updated": { houseNumberId: string } ;
  "wme-initialized": undefined ;
  "wme-issue-tracker-panel-closed": IssueTrackerPanelClosedEvent ;
  "wme-issue-tracker-panel-opened": IssueTrackerPanelOpenedEvent ;
  "wme-layer-checkbox-toggled": { checked: boolean ; name: string } ;
  "wme-layer-feature-clicked": {
  featureId: string | number ;
  layerName: string ;
} ;
  "wme-layer-feature-mouse-enter": {
  featureId: string
  | number ;
  layerName: string ;
} ;
  "wme-layer-feature-mouse-leave": {
  featureId: string
  | number ;
  layerName: string ;
} ;
  "wme-layer-visibility-changed": { layerName: string } ;
  "wme-logged-in": undefined ;
  "wme-logged-out": undefined ;
  "wme-map-data-loaded": undefined ;
  "wme-map-house-number-marker-added": undefined ;
  "wme-map-initial-data-loaded": undefined ;
  "wme-map-layer-added": { layerName: string } ;
  "wme-map-layer-changed": { layerName: string } ;
  "wme-map-layer-removed": { layerName: string } ;
  "wme-map-mouse-click": SdkMouseEvent ;
  "wme-map-mouse-down": SdkMouseEvent ;
  "wme-map-mouse-move": SdkMouseEvent ;
  "wme-map-mouse-out": SdkMouseEvent ;
  "wme-map-mouse-up": SdkMouseEvent ;
  "wme-map-move": undefined ;
  "wme-map-move-end": undefined ;
  "wme-map-zoom-changed": undefined ;
  "wme-no-edits": undefined ;
  "wme-ready": undefined ;
  "wme-save-finished": { success: boolean } ;
  "wme-save-mode-changed": { saveMode: SaveMode } ;
  "wme-selection-changed": undefined ;
  "wme-sidebar-tab-opened": { domId: string ; tabName: SidebarTabName } ;
  "wme-street-view-button-activated": undefined ;
  "wme-street-view-button-deactivated": undefined ;
  "wme-street-view-panel-visibility-changed": { isVisible: boolean } ;
  "wme-update-request-panel-opened": { updateRequestId: number } ;
  "wme-user-settings-changed": undefined ;
}
```
SDK events and their payload (if any).
## Properties
### `wme-after-edit`

```typescript
"wme-after-edit": { affectedObjects: AffectedObject [] }
```
### `wme-after-redo-clear`

```typescript
"wme-after-redo-clear": undefined
```
### `wme-after-undo`

```typescript
"wme-after-undo": undefined
```
### `wme-data-model-object-changed-id`

```typescript
"wme-data-model-object-changed-id": {
  dataModelName: DataModelName ;
  objectIds: ChangedIDsInfo ;
}
```
### `wme-data-model-object-state-deleted`

```typescript
"wme-data-model-object-state-deleted": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-added`

```typescript
"wme-data-model-objects-added": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-changed`

```typescript
"wme-data-model-objects-changed": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-removed`

```typescript
"wme-data-model-objects-removed": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-saved`

```typescript
"wme-data-model-objects-saved": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
}
```
### `wme-editing-house-numbers`

```typescript
"wme-editing-house-numbers": { isEditingHouseNumbers: false }
```
### `wme-feature-editor-opened`

```typescript
"wme-feature-editor-opened": {
  featureType: 
  | "segment"
  | "bigJunction"
  | "city"
  | "googlePlace"
  | "mapComment"
  | "node"
  | "permanentHazard"
  | "restrictedDrivingArea"
  | "segmentSuggestion"
  | "venue" ;
}
```
### `wme-house-number-added`

```typescript
"wme-house-number-added": { houseNumberId: string }
```
### `wme-house-number-deleted`

```typescript
"wme-house-number-deleted": { houseNumberId: string }
```
### `wme-house-number-moved`

```typescript
"wme-house-number-moved": { houseNumberId: string }
```
### `wme-house-number-updated`

```typescript
"wme-house-number-updated": { houseNumberId: string }
```
### `wme-initialized`

```typescript
"wme-initialized": undefined
```
### `wme-issue-tracker-panel-closed`

```typescript
"wme-issue-tracker-panel-closed": IssueTrackerPanelClosedEvent
```
### `wme-issue-tracker-panel-opened`

```typescript
"wme-issue-tracker-panel-opened": IssueTrackerPanelOpenedEvent
```
### `wme-layer-checkbox-toggled`

```typescript
"wme-layer-checkbox-toggled": { checked: boolean ; name: string }
```
### `wme-layer-feature-clicked`

```typescript
"wme-layer-feature-clicked": { featureId: string | number ; layerName: string }
```
### `wme-layer-feature-mouse-enter`

```typescript
"wme-layer-feature-mouse-enter": {
  featureId: string | number ;
  layerName: string ;
}
```
### `wme-layer-feature-mouse-leave`

```typescript
"wme-layer-feature-mouse-leave": {
  featureId: string | number ;
  layerName: string ;
}
```
### `wme-layer-visibility-changed`

```typescript
"wme-layer-visibility-changed": { layerName: string }
```
### `wme-logged-in`

```typescript
"wme-logged-in": undefined
```
### `wme-logged-out`

```typescript
"wme-logged-out": undefined
```
### `wme-map-data-loaded`

```typescript
"wme-map-data-loaded": undefined
```
### `wme-map-house-number-marker-added`

```typescript
"wme-map-house-number-marker-added": undefined
```
### `wme-map-initial-data-loaded`

```typescript
"wme-map-initial-data-loaded": undefined
```
### `wme-map-layer-added`

```typescript
"wme-map-layer-added": { layerName: string }
```
### `wme-map-layer-changed`

```typescript
"wme-map-layer-changed": { layerName: string }
```
### `wme-map-layer-removed`

```typescript
"wme-map-layer-removed": { layerName: string }
```
### `wme-map-mouse-click`

```typescript
"wme-map-mouse-click": SdkMouseEvent
```
### `wme-map-mouse-down`

```typescript
"wme-map-mouse-down": SdkMouseEvent
```
### `wme-map-mouse-move`

```typescript
"wme-map-mouse-move": SdkMouseEvent
```
### `wme-map-mouse-out`

```typescript
"wme-map-mouse-out": SdkMouseEvent
```
### `wme-map-mouse-up`

```typescript
"wme-map-mouse-up": SdkMouseEvent
```
### `wme-map-move`

```typescript
"wme-map-move": undefined
```
### `wme-map-move-end`

```typescript
"wme-map-move-end": undefined
```
### `wme-map-zoom-changed`

```typescript
"wme-map-zoom-changed": undefined
```
### `wme-no-edits`

```typescript
"wme-no-edits": undefined
```
### `wme-ready`

```typescript
"wme-ready": undefined
```
### `wme-save-finished`

```typescript
"wme-save-finished": { success: boolean }
```
### `wme-save-mode-changed`

```typescript
"wme-save-mode-changed": { saveMode: SaveMode }
```
### `wme-selection-changed`

```typescript
"wme-selection-changed": undefined
```
### `wme-sidebar-tab-opened`

```typescript
"wme-sidebar-tab-opened": { domId: string ; tabName: SidebarTabName }
```
### `wme-street-view-button-activated`

```typescript
"wme-street-view-button-activated": undefined
```
### `wme-street-view-button-deactivated`

```typescript
"wme-street-view-button-deactivated": undefined
```
### `wme-street-view-panel-visibility-changed`

```typescript
"wme-street-view-panel-visibility-changed": { isVisible: boolean }
```
### `wme-update-request-panel-opened`

```typescript
"wme-update-request-panel-opened": { updateRequestId: number }
```
### `wme-user-settings-changed`

```typescript
"wme-user-settings-changed": undefined
```

---

# index.SDK.SdkFeature

---
title: SDK.SdkFeature interface
source: interfaces/index.SDK.SdkFeature.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkFeature<G>

```typescript
interface SdkFeature < G extends SdkFeatureGeometry = SdkFeatureGeometry > {
  geometry: G ;
  id: string | number ;
  properties ?: SdkFeatureProperties ;
  type: "Feature" ;
}
```
## Properties
### `geometry`

```typescript
geometry: G
```
### `id`

```typescript
id: string | number
```
### **Optional** `properties`

```typescript
properties ?: SdkFeatureProperties
```
### `type`

```typescript
type: "Feature"
```

---

# index.SDK.SdkFeatureStyleRule

---
title: SDK.SdkFeatureStyleRule interface
source: interfaces/index.SDK.SdkFeatureStyleRule.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkFeatureStyleRule

```typescript
interface SdkFeatureStyleRule {
  predicate ?: SdkFeatureStylePredicate ;
  style: FeatureStyle ;
}
```
## Properties
### **Optional** `predicate`

```typescript
predicate ?: SdkFeatureStylePredicate
```
### `style`

```typescript
style: FeatureStyle
```

---

# index.SDK.SdkMouseEvent

---
title: SDK.SdkMouseEvent interface
source: interfaces/index.SDK.SdkMouseEvent.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkMouseEvent

```typescript
interface SdkMouseEvent {
  lat: number ;
  lon: number ;
  viewportX: number ;
  viewportY: number ;
  x: number ;
  y: number ;
}
```
## Properties
### `lat`

```typescript
lat: number
```
### `lon`

```typescript
lon: number
```
### `viewportX`

```typescript
viewportX: number
```
### `viewportY`

```typescript
viewportY: number
```
### `x`

```typescript
x: number
```
### `y`

```typescript
y: number
```

---

# index.SDK.SdkWazeFeature

---
title: SDK.SdkWazeFeature interface
source: interfaces/index.SDK.SdkWazeFeature.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkWazeFeature

```typescript
interface SdkWazeFeature {
  featureType: "SDKFeature" ;
  properties: SdkFeatureProperties ;
}
```
## Properties
### `featureType`

```typescript
featureType: "SDKFeature"
```
### `properties`

```typescript
properties: SdkFeatureProperties
```

---

# index.SDK.Segment

---
title: SDK.Segment interface
source: interfaces/index.SDK.Segment.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Segment

```typescript
interface Segment {
  allowNoDirection: boolean ;
  alternateStreetIds: number [] ;
  areFwdTurnsVerified: boolean ;
  areRevTurnsVerified: boolean ;
  elevationLevel: number | null ;
  flagAttributes: SegmentFlagAttributes ;
  fromLanesInfo: SegmentLanesInfo | null ;
  fromNodeId: number | null ;
  fromNodeLanesCount: number ;
  fwdSpeedLimit: number | null ;
  geometry: LineString ;
  hasClosures: boolean ;
  hasHouseNumbers: boolean ;
  hasRestrictions: boolean ;
  hasSeparator: boolean ;
  id: number ;
  isAtoB: boolean ;
  isBtoA: boolean ;
  isDrivable: boolean ;
  isFwdSpeedLimitVerified: boolean ;
  isRevSpeedLimitVerified: boolean ;
  isTwoWay: boolean ;
  junctionId: number | null ;
  length: number ;
  lockRank: UserRank ;
  modificationData: ModificationMetadata ;
  primaryStreetId: number | null ;
  rank: UserRank ;
  restrictions: SegmentRestriction [] ;
  revSpeedLimit: number | null ;
  roadType: RoadTypeId ;
  routingRoadType: 6 | 7 | 1 | 2 | 3 | null ;
  toLanesInfo: SegmentLanesInfo | null ;
  toNodeId: number | null ;
  toNodeLanesCount: number ;
}
```
## Properties
### `allowNoDirection`

```typescript
allowNoDirection: boolean
```
### `alternateStreetIds`

```typescript
alternateStreetIds: number []
```
### `areFwdTurnsVerified`

```typescript
areFwdTurnsVerified: boolean
```
### `areRevTurnsVerified`

```typescript
areRevTurnsVerified: boolean
```
### `elevationLevel`

```typescript
elevationLevel: number | null
```
### `flagAttributes`

```typescript
flagAttributes: SegmentFlagAttributes
```
### `fromLanesInfo`

```typescript
fromLanesInfo: SegmentLanesInfo | null
```
### `fromNodeId`

```typescript
fromNodeId: number | null
```
### `fromNodeLanesCount`

```typescript
fromNodeLanesCount: number
```
### `fwdSpeedLimit`

```typescript
fwdSpeedLimit: number | null
```
### `geometry`

```typescript
geometry: LineString
```
### `hasClosures`

```typescript
hasClosures: boolean
```
### `hasHouseNumbers`

```typescript
hasHouseNumbers: boolean
```
### `hasRestrictions`

```typescript
hasRestrictions: boolean
```
### `hasSeparator`

```typescript
hasSeparator: boolean
```
### `id`

```typescript
id: number
```
### `isAtoB`

```typescript
isAtoB: boolean
```
### `isBtoA`

```typescript
isBtoA: boolean
```
### `isDrivable`

```typescript
isDrivable: boolean
```
### `isFwdSpeedLimitVerified`

```typescript
isFwdSpeedLimitVerified: boolean
```
### `isRevSpeedLimitVerified`

```typescript
isRevSpeedLimitVerified: boolean
```
### `isTwoWay`

```typescript
isTwoWay: boolean
```
### `junctionId`

```typescript
junctionId: number | null
```
### `length`

```typescript
length: number
```
### `lockRank`

```typescript
lockRank: UserRank
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `primaryStreetId`

```typescript
primaryStreetId: number | null
```
### `rank`

```typescript
rank: UserRank
```
### `restrictions`

```typescript
restrictions: SegmentRestriction []
```
### `revSpeedLimit`

```typescript
revSpeedLimit: number | null
```
### `roadType`

```typescript
roadType: RoadTypeId
```
### `routingRoadType`

```typescript
routingRoadType: 6 | 7 | 1 | 2 | 3 | null
```
### `toLanesInfo`

```typescript
toLanesInfo: SegmentLanesInfo | null
```
### `toNodeId`

```typescript
toNodeId: number | null
```
### `toNodeLanesCount`

```typescript
toNodeLanesCount: number
```

---

# index.SDK.SegmentAddress

---
title: SDK.SegmentAddress interface
source: interfaces/index.SDK.SegmentAddress.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentAddress

```typescript
interface SegmentAddress {
  altStreets: SegmentAddress [] ;
  city: City | null ;
  country: Country | null ;
  isEmpty: boolean ;
  state: State | null ;
  street: Street | null ;
}
```
## Properties
### `altStreets`

```typescript
altStreets: SegmentAddress []
```

---

# index.SDK.SegmentFlagAttributes

---
title: SDK.SegmentFlagAttributes interface
source: interfaces/index.SDK.SegmentFlagAttributes.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentFlagAttributes

```typescript
interface SegmentFlagAttributes {
  beacons: boolean ;
  fwdLanesEnabled: boolean ;
  fwdSpeedCamera: boolean ;
  headlights: boolean ;
  nearbyHOV: boolean ;
  revLanesEnabled: boolean ;
  revSpeedCamera: boolean ;
  tunnel: boolean ;
  unpaved: boolean ;
}
```
## Properties
### `beacons`

```typescript
beacons: boolean
```
### `fwdLanesEnabled`

```typescript
fwdLanesEnabled: boolean
```
### `fwdSpeedCamera`

```typescript
fwdSpeedCamera: boolean
```
### `headlights`

```typescript
headlights: boolean
```
### `nearbyHOV`

```typescript
nearbyHOV: boolean
```
### `revLanesEnabled`

```typescript
revLanesEnabled: boolean
```
### `revSpeedCamera`

```typescript
revSpeedCamera: boolean
```
### `tunnel`

```typescript
tunnel: boolean
```
### `unpaved`

```typescript
unpaved: boolean
```

---

# index.SDK.SegmentLanesInfo

---
title: SDK.SegmentLanesInfo interface
source: interfaces/index.SDK.SegmentLanesInfo.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentLanesInfo

```typescript
interface SegmentLanesInfo {
  laneWidth: number | null ;
  numberOfLanes: number ;
}
```
## Properties
### `laneWidth`

```typescript
laneWidth: number | null
```
### `numberOfLanes`

```typescript
numberOfLanes: number
```

---

# index.SDK.SegmentRestriction

---
title: SDK.SegmentRestriction interface
source: interfaces/index.SDK.SegmentRestriction.html
created: 2026-10-28
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

---

# index.SDK.SegmentSuggestion

---
title: SDK.SegmentSuggestion interface
source: interfaces/index.SDK.SegmentSuggestion.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentSuggestion

```typescript
interface SegmentSuggestion {
  geometry: LineString ;
  id: number ;
  segmentId: number | null ;
  source: SegmentSuggestionSource ;
  status: SegmentSuggestionStatus ;
  streetName: string | null ;
}
```
## Properties
### `geometry`

```typescript
geometry: LineString
```
### `id`

```typescript
id: number
```
### `segmentId`

```typescript
segmentId: number | null
```
### `source`

```typescript
source: SegmentSuggestionSource
```
### `status`

```typescript
status: SegmentSuggestionStatus
```
### `streetName`

```typescript
streetName: string | null
```

---

# index.SDK.Sign

---
title: SDK.Sign interface
source: interfaces/index.SDK.Sign.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Sign

```typescript
interface Sign {
  countryId: number ;
  description: string ;
  id: number ;
  maxTextLength: number ;
  minTextLength: number ;
  type: SignType ;
}
```
## Properties
### `countryId`

```typescript
countryId: number
```
### `description`

```typescript
description: string
```
### `id`

```typescript
id: number
```
### `maxTextLength`

```typescript
maxTextLength: number
```
### `minTextLength`

```typescript
minTextLength: number
```
### `type`

```typescript
type: SignType
```

---

# index.SDK.StandardPermanentHazard

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

---

# index.SDK.State

---
title: SDK.State interface
source: interfaces/index.SDK.State.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface State

```typescript
interface State {
  geometry: Polygon | MultiPolygon | null ;
  id: number ;
  modificationData: ModificationMetadata ;
  name: string ;
}
```
## Properties
### `geometry`

```typescript
geometry: Polygon | MultiPolygon | null
```
### `id`

```typescript
id: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```

---

# index.SDK.Street

---
title: SDK.Street interface
source: interfaces/index.SDK.Street.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Street

```typescript
interface Street {
  cityId: number | null ;
  direction: string | null ;
  englishName: string | null ;
  id: number ;
  isEmpty: boolean ;
  modificationData: ModificationMetadata ;
  name: string | null ;
  signText: string | null ;
  signType: number | null ;
}
```
## Properties
### `cityId`

```typescript
cityId: number | null
```
### `direction`

```typescript
direction: string | null
```
### `englishName`

```typescript
englishName: string | null
```
### `id`

```typescript
id: number
```
### `isEmpty`

```typescript
isEmpty: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string | null
```
### `signText`

```typescript
signText: string | null
```
### `signType`

```typescript
signType: number | null
```

---

# index.SDK.Subscription

---
title: SDK.Subscription interface
source: interfaces/index.SDK.Subscription.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Subscription

```typescript
interface Subscription {
  id: string ;
  name: string ;
}
```
## Properties
### `id`

```typescript
id: string
```
### `name`

```typescript
name: string
```

---

# index.SDK.Suggestion

---
title: SDK.Suggestion interface
source: interfaces/index.SDK.Suggestion.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Suggestion

```typescript
interface Suggestion {
  createdOn: number | null ;
  edits: SuggestionEntityEdit [] ;
  id: string ;
  resolutionData: SuggestionResolution [] ;
}
```
Represents a suggestion for an edit.
## Properties
### `createdOn`

```typescript
createdOn: number | null
```
### `edits`

```typescript
edits: SuggestionEntityEdit []
```
### `id`

```typescript
id: string
```
### `resolutionData`

```typescript
resolutionData: SuggestionResolution []
```

---

# index.SDK.SuggestionAttributeChange

---
title: SDK.SuggestionAttributeChange interface
source: interfaces/index.SDK.SuggestionAttributeChange.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SuggestionAttributeChange<T>

```typescript
interface SuggestionAttributeChange < T = unknown > {
  id: string ;
  name: string ;
  newValue: T ;
  objectType: ObjectType ;
  oldValue: T ;
  timestamp: number | null ;
}
```
Represents a single attribute change in an edit suggestion change.
## Properties
### `id`

```typescript
id: string
```
### `name`

```typescript
name: string
```
### `newValue`

```typescript
newValue: T
```
### `objectType`

```typescript
objectType: ObjectType
```
### `oldValue`

```typescript
oldValue: T
```
### `timestamp`

```typescript
timestamp: number | null
```

---

# index.SDK.SuggestionEntityEdit

---
title: SDK.SuggestionEntityEdit interface
source: interfaces/index.SDK.SuggestionEntityEdit.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SuggestionEntityEdit

```typescript
interface SuggestionEntityEdit {
  actionType: SuggestibleActionType ;
  objectId: string | number | null ;
  objectType: ObjectType ;
}
```
Represents an edit to an entity within a suggestion.
## Properties
### `actionType`

```typescript
actionType: SuggestibleActionType
```
### `objectId`

```typescript
objectId: string | number | null
```
### `objectType`

```typescript
objectType: ObjectType
```

---

# index.SDK.SuggestionResolution

---
title: SDK.SuggestionResolution interface
source: interfaces/index.SDK.SuggestionResolution.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SuggestionResolution

```typescript
interface SuggestionResolution {
  createdBy: string | null ;
  createdOn: number ;
  rejectionReason: SuggestionResolutionRejectionReason | null ;
  resolution: SuggestionResolutionStatus ;
}
```
Represents the resolution details for a suggestion.
## Properties
### `createdBy`

```typescript
createdBy: string | null
```
### `createdOn`

```typescript
createdOn: number
```
### `rejectionReason`

```typescript
rejectionReason: SuggestionResolutionRejectionReason | null
```
### `resolution`

```typescript
resolution: SuggestionResolutionStatus
```

---

# index.SDK.TileLayerOptions

---
title: SDK.TileLayerOptions interface
source: interfaces/index.SDK.TileLayerOptions.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TileLayerOptions

```typescript
interface TileLayerOptions {
  tileHeight: number ;
  tileWidth: number ;
  url: {
  fileName: string ;
  params ?: Record < string , unknown > ;
  servers: string [] ;
} ;
}
```
#### Members
| Name | Type/Value | Tags |
|------|------------|------|
| fileName | string |  |
| params | Record | Optional |
| servers | string |  |
## Properties
### `tileHeight`

```typescript
tileHeight: number
```
### `tileWidth`

```typescript
tileWidth: number
```
### `url`

```typescript
url: { fileName: string ; params ?: Record < string , unknown > ; servers: string [] }
```

---

# index.SDK.TimeFrame

---
title: SDK.TimeFrame interface
source: interfaces/index.SDK.TimeFrame.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TimeFrame

```typescript
interface TimeFrame {
  dayAlternation: DayAlternation | null ;
  daysOfMonth: DayAlternation | null ;
  endDate: string | null ;
  fromTime: string | null ;
  repeatYearly: boolean | null ;
  startDate: string | null ;
  timeZone: string | null ;
  toTime: string | null ;
  weekdays: WeekDay [] | null ;
}
```
Represents a time frame indicating when a restriction is active.
## Properties
### `dayAlternation`

```typescript
dayAlternation: DayAlternation | null
```
### `daysOfMonth`

```typescript
daysOfMonth: DayAlternation | null
```
### `endDate`

```typescript
endDate: string | null
```
### `fromTime`

```typescript
fromTime: string | null
```
### `repeatYearly`

```typescript
repeatYearly: boolean | null
```
### `startDate`

```typescript
startDate: string | null
```
### `timeZone`

```typescript
timeZone: string | null
```
### `toTime`

```typescript
toTime: string | null
```
### `weekdays`

```typescript
weekdays: WeekDay [] | null
```

---

# index.SDK.TrackedDataModel

---
title: SDK.TrackedDataModel interface
source: interfaces/index.SDK.TrackedDataModel.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TrackedDataModel

```typescript
interface TrackedDataModel {
  events: {
  "objects-state-deleted": (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectsadded: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectschanged: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  "objectschanged-id": ( changedIds: ChangedIDsInfo ) = > void ;
  objectsremoved: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectssynced: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
} ;
}
```
## Properties
### `events`

```typescript
events: {
  "objects-state-deleted": (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectsadded: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectschanged: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  "objectschanged-id": ( changedIds: ChangedIDsInfo ) = > void ;
  objectsremoved: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectssynced: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
}
```

---

# index.SDK.TrackedLayer

---
title: SDK.TrackedLayer interface
source: interfaces/index.SDK.TrackedLayer.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TrackedLayer

```typescript
interface TrackedLayer {
  events: {
  visibilitychanged: () = > void ;
  "waze-feature-clicked": ( e: { feature: WMEFeature } ) = > void ;
  "waze-feature-in": ( e: { feature: WMEFeature } ) = > void ;
  "waze-feature-out": ( e: { feature: WMEFeature } ) = > void ;
} ;
}
```
## Properties
### `events`

```typescript
events: {
  visibilitychanged: () = > void ;
  "waze-feature-clicked": ( e: { feature: WMEFeature } ) = > void ;
  "waze-feature-in": ( e: { feature: WMEFeature } ) = > void ;
  "waze-feature-out": ( e: { feature: WMEFeature } ) = > void ;
}
```

---

# index.SDK.Turn

---
title: SDK.Turn interface
source: interfaces/index.SDK.Turn.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Turn

```typescript
interface Turn {
  fromSegmentFwd: boolean ;
  fromSegmentId: number ;
  hasCustomTTS: boolean ;
  hasShieldsPopulated: boolean ;
  hasTowardsGuidance: boolean ;
  hasTurnGuidance: boolean ;
  hasVisualInstruction: boolean ;
  id: string ;
  instructionOpCode: InstructionOpCode | null ;
  isAllowed: boolean ;
  isJunctionBoxTurn: boolean ;
  isPathTurn: boolean ;
  isUTurn: boolean ;
  lanes: TurnLanes | null ;
  restrictions: BaseRestriction [] ;
  segmentPath: number [] ;
  toSegmentFwd: boolean ;
  toSegmentId: number ;
  turnGuidance: TurnGuidance | null ;
}
```
## Properties
### `fromSegmentFwd`

```typescript
fromSegmentFwd: boolean
```
### `fromSegmentId`

```typescript
fromSegmentId: number
```
### `hasCustomTTS`

```typescript
hasCustomTTS: boolean
```
### `hasShieldsPopulated`

```typescript
hasShieldsPopulated: boolean
```
### `hasTowardsGuidance`

```typescript
hasTowardsGuidance: boolean
```
### `hasTurnGuidance`

```typescript
hasTurnGuidance: boolean
```
### `hasVisualInstruction`

```typescript
hasVisualInstruction: boolean
```
### `id`

```typescript
id: string
```
### `instructionOpCode`

```typescript
instructionOpCode: InstructionOpCode | null
```
### `isAllowed`

```typescript
isAllowed: boolean
```
### `isJunctionBoxTurn`

```typescript
isJunctionBoxTurn: boolean
```
### `isPathTurn`

```typescript
isPathTurn: boolean
```
### `isUTurn`

```typescript
isUTurn: boolean
```
### `lanes`

```typescript
lanes: TurnLanes | null
```
### `restrictions`

```typescript
restrictions: BaseRestriction []
```
### `segmentPath`

```typescript
segmentPath: number []
```
### `toSegmentFwd`

```typescript
toSegmentFwd: boolean
```
### `toSegmentId`

```typescript
toSegmentId: number
```
### `turnGuidance`

```typescript
turnGuidance: TurnGuidance | null
```

---

# index.SDK.TurnClosure

---
title: SDK.TurnClosure interface
source: interfaces/index.SDK.TurnClosure.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnClosure

```typescript
interface TurnClosure {
  description: string | null ;
  endDate: string | null ;
  fromSegmentId: number ;
  id: string ;
  isPermanent: boolean ;
  majorTrafficEventId: string | null ;
  modificationData: ModificationMetadata ;
  startDate: string | null ;
  status: ClosureStatus ;
  toSegmentId: number ;
}
```
## Properties
### `description`

```typescript
description: string | null
```
### `endDate`

```typescript
endDate: string | null
```
### `fromSegmentId`

```typescript
fromSegmentId: number
```
### `id`

```typescript
id: string
```
### `isPermanent`

```typescript
isPermanent: boolean
```
### `majorTrafficEventId`

```typescript
majorTrafficEventId: string | null
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `startDate`

```typescript
startDate: string | null
```
### `status`

```typescript
status: ClosureStatus
```
### `toSegmentId`

```typescript
toSegmentId: number
```

---

# index.SDK.TurnGuidance

---
title: SDK.TurnGuidance interface
source: interfaces/index.SDK.TurnGuidance.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnGuidance

```typescript
interface TurnGuidance {
  exitSigns: ExitSign [] ;
  towards: ( string | RoadShield ) [] ;
  tts: string | null ;
  visualInstruction: ( string | RoadShield ) [] ;
}
```
## Properties
### `exitSigns`

```typescript
exitSigns: ExitSign []
```
### `towards`

```typescript
towards: ( string | RoadShield ) []
```
### `tts`

```typescript
tts: string | null
```
### `visualInstruction`

```typescript
visualInstruction: ( string | RoadShield ) []
```

---

# index.SDK.TurnLanes

---
title: SDK.TurnLanes interface
source: interfaces/index.SDK.TurnLanes.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnLanes

```typescript
interface TurnLanes {
  angleOverride: number | null ;
  arrowAngle: number | null ;
  fromLaneIndex: number ;
  guidanceMode: LaneGuidanceMode ;
  instructionStrategy: LaneInstructionStrategy ;
  toLaneIndex: number ;
}
```
## Properties
### `angleOverride`

```typescript
angleOverride: number | null
```
### `arrowAngle`

```typescript
arrowAngle: number | null
```
### `fromLaneIndex`

```typescript
fromLaneIndex: number
```
### `guidanceMode`

```typescript
guidanceMode: LaneGuidanceMode
```
### `instructionStrategy`

```typescript
instructionStrategy: LaneInstructionStrategy
```
### `toLaneIndex`

```typescript
toLaneIndex: number
```

---

# index.SDK.UpdateRequestDetails

---
title: SDK.UpdateRequestDetails interface
source: interfaces/index.SDK.UpdateRequestDetails.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UpdateRequestDetails

```typescript
interface UpdateRequestDetails {
  comments: ConversationElement [] ;
  driveGeometry: MultiLineString | null ;
  id: number ;
}
```
## Properties
### `comments`

```typescript
comments: ConversationElement []
```
### `driveGeometry`

```typescript
driveGeometry: MultiLineString | null
```
### `id`

```typescript
id: number
```

---

# index.SDK.UpdateRequestUserPreferences

---
title: SDK.UpdateRequestUserPreferences interface
source: interfaces/index.SDK.UpdateRequestUserPreferences.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UpdateRequestUserPreferences

```typescript
interface UpdateRequestUserPreferences {
  activeHovSubscriptions: string [] ;
  avoidDangerousTurns: boolean | null ;
  avoidFerries: boolean | null ;
  avoidPrimaryRoads: boolean | null ;
  avoidTollRoads: boolean | null ;
  hasEv: boolean | null ;
  isEmailVerified: boolean | null ;
  language: string | null ;
  licensePlateSuffix: string | null ;
  os: string | null ;
  unpavedRoads: UnpavedRoadsSetting | null ;
  vehicleType: VehicleType | null ;
}
```
## Properties
### `activeHovSubscriptions`

```typescript
activeHovSubscriptions: string []
```
### `avoidDangerousTurns`

```typescript
avoidDangerousTurns: boolean | null
```
### `avoidFerries`

```typescript
avoidFerries: boolean | null
```
### `avoidPrimaryRoads`

```typescript
avoidPrimaryRoads: boolean | null
```
### `avoidTollRoads`

```typescript
avoidTollRoads: boolean | null
```
### `hasEv`

```typescript
hasEv: boolean | null
```
### `isEmailVerified`

```typescript
isEmailVerified: boolean | null
```
### `language`

```typescript
language: string | null
```
### `licensePlateSuffix`

```typescript
licensePlateSuffix: string | null
```
### `os`

```typescript
os: string | null
```
### `unpavedRoads`

```typescript
unpavedRoads: UnpavedRoadsSetting | null
```
### `vehicleType`

```typescript
vehicleType: VehicleType | null
```

---

# index.SDK.UpdateRequestsFilterState

---
title: SDK.UpdateRequestsFilterState interface
source: interfaces/index.SDK.UpdateRequestsFilterState.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UpdateRequestsFilterState

```typescript
interface UpdateRequestsFilterState {
  status: "OPEN" | "CLOSED" ;
}
```
## Properties
### `status`

```typescript
status: "OPEN" | "CLOSED"
```

---

# index.SDK.User

---
title: SDK.User interface
source: interfaces/index.SDK.User.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface User

```typescript
interface User {
  rank: UserRank ;
  userName: string ;
}
```
## Properties
### `rank`

```typescript
rank: UserRank
```
### `userName`

```typescript
userName: string
```

---

# index.SDK.UserEditableArea

---
title: SDK.UserEditableArea interface
source: interfaces/index.SDK.UserEditableArea.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UserEditableArea

```typescript
interface UserEditableArea {
  geometry: Polygon ;
  type: UserEditableAreaType ;
}
```
A geographical area where the user has permission to edit map features.
## Properties
### `geometry`

```typescript
geometry: Polygon
```
### `type`

```typescript
type: UserEditableAreaType
```

---

# index.SDK.UserProfile

---
title: SDK.UserProfile interface
source: interfaces/index.SDK.UserProfile.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UserProfile

```typescript
interface UserProfile {
  dailyEditCount: number [] ;
  editCountByType: {
  mapProblems: number ;
  placeUpdateRequests: number ;
  segmentHouseNumbers: number ;
  segments: number ;
  updateRequests: number ;
  venues: number ;
} ;
  totalEditCount: number ;
}
```
## Properties
### `dailyEditCount`

```typescript
dailyEditCount: number []
```
### `editCountByType`

```typescript
editCountByType: {
  mapProblems: number ;
  placeUpdateRequests: number ;
  segmentHouseNumbers: number ;
  segments: number ;
  updateRequests: number ;
  venues: number ;
}
```
### `totalEditCount`

```typescript
totalEditCount: number
```

---

# index.SDK.UserSession

---
title: SDK.UserSession interface
source: interfaces/index.SDK.UserSession.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UserSession

```typescript
interface UserSession {
  editableAreas: UserEditableArea [] ;
  isAreaManager: boolean ;
  isCountryManager: boolean ;
  managedAreas: ManagedAreaShort [] ;
  rank: UserRank ;
  userName: string ;
}
```
## Properties
### `editableAreas`

```typescript
editableAreas: UserEditableArea []
```
### `isAreaManager`

```typescript
isAreaManager: boolean
```
### `isCountryManager`

```typescript
isCountryManager: boolean
```
### `managedAreas`

```typescript
managedAreas: ManagedAreaShort []
```
### `rank`

```typescript
rank: UserRank
```
### `userName`

```typescript
userName: string
```

---

# index.SDK.UserSettings

---
title: SDK.UserSettings interface
source: interfaces/index.SDK.UserSettings.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UserSettings

```typescript
interface UserSettings {
  isCompactMode: boolean ;
  isCreateRoadsAsTwoWay: boolean ;
  isCreateRoadsWithAllTurnsAllowed: boolean ;
  isDisplayTransparentTurnArrows: boolean ;
  isImperial ?: boolean ;
  isSelectOnlyOnEmptySelection: boolean ;
  isSpreadOverlappingTurnArrows: boolean ;
}
```
User settings set in the settings tab of the WME UI
## Properties
### `isCompactMode`

```typescript
isCompactMode: boolean
```
### `isCreateRoadsAsTwoWay`

```typescript
isCreateRoadsAsTwoWay: boolean
```
### `isCreateRoadsWithAllTurnsAllowed`

```typescript
isCreateRoadsWithAllTurnsAllowed: boolean
```
### `isDisplayTransparentTurnArrows`

```typescript
isDisplayTransparentTurnArrows: boolean
```
### **Optional** `isImperial`

```typescript
isImperial ?: boolean
```
### `isSelectOnlyOnEmptySelection`

```typescript
isSelectOnlyOnEmptySelection: boolean
```
### `isSpreadOverlappingTurnArrows`

```typescript
isSpreadOverlappingTurnArrows: boolean
```

---

# index.SDK.VehicleRule

---
title: SDK.VehicleRule interface
source: interfaces/index.SDK.VehicleRule.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VehicleRule

```typescript
interface VehicleRule {
  licensePlateNumber: LicensePlateRule | null ;
  licensePlateRule: LicensePlateRule | null ;
  minPassengers: number ;
  numPassengers: number ;
  subscriptions: string [] ;
  vehicleTypes: VehicleType [] ;
}
```
Represents a vehicle rule for specific vehicle exemptions or restrictions.
## Properties
### `licensePlateNumber`

```typescript
licensePlateNumber: LicensePlateRule | null
```
### `minPassengers`

```typescript
minPassengers: number
```
### `numPassengers`

```typescript
numPassengers: number
```
### `vehicleTypes`

```typescript
vehicleTypes: VehicleType []
```

---

# index.SDK.Venue

---
title: SDK.Venue interface
source: interfaces/index.SDK.Venue.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Venue

```typescript
interface Venue {
  aliases: string [] ;
  approved: boolean ;
  brand: string | null ;
  categories: VenueCategoryId [] ;
  description: string ;
  externalProviderIds: string [] ;
  geometry: Point | Polygon ;
  id: string ;
  images: VenueImage [] ;
  isAdLocked: boolean ;
  isResidential: boolean ;
  lockRank: number ;
  modificationData: ModificationMetadata ;
  name: string ;
  navigationPoints: NavigationPoint [] ;
  openingHours: OpeningHour [] ;
  phone: string ;
  services: ServiceType [] ;
  url: string ;
  venueUpdateRequests: VenueUpdateRequest [] ;
}
```
## Properties
### `aliases`

```typescript
aliases: string []
```
### `approved`

```typescript
approved: boolean
```
### `brand`

```typescript
brand: string | null
```
### `categories`

```typescript
categories: VenueCategoryId []
```
### `description`

```typescript
description: string
```
### `externalProviderIds`

```typescript
externalProviderIds: string []
```
### `geometry`

```typescript
geometry: Point | Polygon
```
### `id`

```typescript
id: string
```
### `images`

```typescript
images: VenueImage []
```
### `isAdLocked`

```typescript
isAdLocked: boolean
```
### `isResidential`

```typescript
isResidential: boolean
```
### `lockRank`

```typescript
lockRank: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```
### `navigationPoints`

```typescript
navigationPoints: NavigationPoint []
```
### `openingHours`

```typescript
openingHours: OpeningHour []
```
### `phone`

```typescript
phone: string
```
### `services`

```typescript
services: ServiceType []
```
### `url`

```typescript
url: string
```
### `venueUpdateRequests`

```typescript
venueUpdateRequests: VenueUpdateRequest []
```

---

# index.SDK.VenueAddress

---
title: SDK.VenueAddress interface
source: interfaces/index.SDK.VenueAddress.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueAddress

```typescript
interface VenueAddress {
  city: City | null ;
  country: Country | null ;
  houseNumber: string | null ;
  isEmpty: boolean ;
  state: State | null ;
  street: Street | null ;
}
```
## Properties
### `houseNumber`

```typescript
houseNumber: string | null
```

---

# index.SDK.VenueCategory

---
title: SDK.VenueCategory interface
source: interfaces/index.SDK.VenueCategory.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueCategory

```typescript
interface VenueCategory {
  id: VenueCategoryId ;
  localizedName: string ;
}
```
## Properties
### `id`

```typescript
id: VenueCategoryId
```
### `localizedName`

```typescript
localizedName: string
```

---

# index.SDK.VenueImage

---
title: SDK.VenueImage interface
source: interfaces/index.SDK.VenueImage.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueImage

```typescript
interface VenueImage {
  creationDate: number ;
  id: string ;
  isApproved: boolean ;
  url: string ;
}
```
## Properties
### `creationDate`

```typescript
creationDate: number
```
### `id`

```typescript
id: string
```
### `isApproved`

```typescript
isApproved: boolean
```
### `url`

```typescript
url: string
```

---

# index.SDK.VenueSubCategory

---
title: SDK.VenueSubCategory interface
source: interfaces/index.SDK.VenueSubCategory.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueSubCategory

```typescript
interface VenueSubCategory {
  categoryId: VenueCategoryId ;
  localizedName: string ;
  subCategoryId: VenueCategoryId ;
}
```
## Properties
### `categoryId`

```typescript
categoryId: VenueCategoryId
```
### `localizedName`

```typescript
localizedName: string
```
### `subCategoryId`

```typescript
subCategoryId: VenueCategoryId
```

---

# index.SDK.VenueUpdateRequest

---
title: SDK.VenueUpdateRequest interface
source: interfaces/index.SDK.VenueUpdateRequest.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueUpdateRequest

```typescript
interface VenueUpdateRequest {
  changedFields ?: ChangedField [] ;
  createdBy: string | null ;
  dateAdded: number ;
  id: string | number | null ;
  subject: PLACE_UPDATE_SUBJECT ;
  updateType: PlaceUpdateType ;
}
```
## Properties
### **Optional** `changedFields`

```typescript
changedFields ?: ChangedField []
```
### `createdBy`

```typescript
createdBy: string | null
```
### `dateAdded`

```typescript
dateAdded: number
```
### `id`

```typescript
id: string | number | null
```
### `subject`

```typescript
subject: PLACE_UPDATE_SUBJECT
```
### `updateType`

```typescript
updateType: PlaceUpdateType
```

---

