# index.SDK.BigJunctions

---
title: SDK.BigJunctions class
source: classes/index.SDK.BigJunctions.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class BigJunctions

```typescript
getAll () : BigJunction []
```
Methods for dealing with BigJunctions.
## Methods
### `getAll`

```typescript
getAll () : BigJunction []
```
an array of all the bigJunctions in the WME data model
### `getAllPossibleTurns`

```typescript
getAllPossibleTurns ( args: { bigJunctionId: number } ) : Turn []
```
all possible turns for the bigJunction
### `getById`

```typescript
getById ( args: { bigJunctionId: number } ) : null | BigJunction
```
bigJunction with id, or null if not found in the WME data model

---

# index.SDK.ChargingStation

---
title: SDK.ChargingStation class
source: classes/index.SDK.ChargingStation.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class ChargingStation

```typescript
getBrands () : string []
```
Methods for dealing with ChargingStations.
## Methods
### `getBrands`

```typescript
getBrands () : string []
```
a list of charging station brands
### `getChargersAccessType`

```typescript
getChargersAccessType ( args: { venueId: string } ) : null | ChargersAccessType
```
chargers access type of the venue in case the venue is a charging station, null otherwise.
### `getCostType`

```typescript
getCostType ( args: { venueId: string } ) : null | ChargingStationCostType
```
cost type of the venue in case the venue is a charging station, null otherwise.
### `getNetwork`

```typescript
getNetwork ( args: { venueId: string } ) : null | string
```
network of the venue in case the venue is a charging station, null otherwise.
### `getPaymentMethods`

```typescript
getPaymentMethods ( args: { venueId: string } ) : null | PaymentMethod []
```
payment methods of the venue in case the venue is a charging station, null otherwise.

---

# index.SDK.Chat

---
title: SDK.Chat class
source: classes/index.SDK.Chat.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Chat

```typescript
startChat ( args: { userName: string } ) : void
```
Methods for dealing with Chat/Communication.
## Methods
### `startChat`

```typescript
startChat ( args: { userName: string } ) : void
```

---

# index.SDK.Cities

---
title: SDK.Cities class
source: classes/index.SDK.Cities.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Cities

```typescript
addCity (
  options: { cityName: string ; countryId ?: number ; stateId ?: number } ,
  ) : City
```
Methods for dealing with Cities.
## Methods
### `addCity`

```typescript
addCity (
  options: { cityName: string ; countryId ?: number ; stateId ?: number } ,
  ) : City
```
a new city object
### `getAll`

```typescript
getAll () : City []
```
an array of all the cities in the WME data model
### `getById`

```typescript
getById ( args: { cityId: number } ) : null | City
```
city with id, or null if not found in the WME data model
### `getCity`

```typescript
getCity (
  options: { cityName: string ; countryId ?: number ; stateId ?: number } ,
  ) : null | City
```
a city object or null if not found
### `getTopCity`

```typescript
getTopCity () : null | City
```
top city or null

---

# index.SDK.Countries

---
title: SDK.Countries class
source: classes/index.SDK.Countries.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Countries

```typescript
getAll () : Country []
```
Methods for dealing with Countries.
## Methods
### `getAll`

```typescript
getAll () : Country []
```
an array of all the countries in the WME data model
### `getById`

```typescript
getById ( args: { countryId: number } ) : null | Country
```
country with id, or null if not found in the WME data model
### `getTopCountry`

```typescript
getTopCountry () : null | Country
```
the Country set to be the top country in the WME data model, or null
if none set

---

# index.SDK.DataModel

---
title: SDK.DataModel class
source: classes/index.SDK.DataModel.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class DataModel

```typescript
BigJunctions: BigJunctions = ...
```
Methods for dealing with the WME data model objects.
## Properties
### **Readonly** `BigJunctions`

```typescript
BigJunctions: BigJunctions = ...
```
### **Readonly** `Cities`

```typescript
Cities: Cities = ...
```
### **Readonly** `Countries`

```typescript
Countries: Countries = ...
```
### **Readonly** `EditSuggestions`

```typescript
EditSuggestions: EditSuggestions = ...
```
### **Readonly** `HouseNumbers`

```typescript
HouseNumbers: HouseNumbers = ...
```
### **Readonly** `Junctions`

```typescript
Junctions: Junctions = ...
```
### **Readonly** `MajorTrafficEvents`

```typescript
MajorTrafficEvents: MajorTrafficEvents = ...
```
### **Readonly** `ManagedAreas`

```typescript
ManagedAreas: ManagedAreas = ...
```
### **Readonly** `MapComments`

```typescript
MapComments: MapComments = ...
```
### **Readonly** `MapProblems`

```typescript
MapProblems: MapProblems = ...
```
### **Readonly** `MapUpdateRequests`

```typescript
MapUpdateRequests: MapUpdateRequests = ...
```
### **Readonly** `Nodes`

```typescript
Nodes: Nodes = ...
```
### **Readonly** `PermanentHazards`

```typescript
PermanentHazards: PermanentHazards = ...
```
### **Readonly** `RestrictedDrivingAreas`

```typescript
RestrictedDrivingAreas: RestrictedDrivingAreas = ...
```
### **Readonly** `RoadClosures`

```typescript
RoadClosures: RoadClosures = ...
```
### **Readonly** `Segments`

```typescript
Segments: Segments = ...
```
### **Readonly** `SegmentSuggestions`

```typescript
SegmentSuggestions: SegmentSuggestions = ...
```
### **Readonly** `Signs`

```typescript
Signs: Signs = ...
```
### **Readonly** `States`

```typescript
States: States = ...
```
### **Readonly** `Streets`

```typescript
Streets: Streets = ...
```
### **Readonly** `TurnClosures`

```typescript
TurnClosures: TurnClosures = ...
```
### **Readonly** `Turns`

```typescript
Turns: Turns = ...
```
### **Readonly** `Users`

```typescript
Users: Users = ...
```
### **Readonly** `Venues`

```typescript
Venues: Venues = ...
```
## Methods
### `isDeletable`

```typescript
isDeletable (
  args: { dataModelName: DataModelName ; objectId: string | number } ,
  ) : boolean
```
true if the object is deletable, false otherwise.
### `isDeleted`

```typescript
isDeleted (
  args: { dataModelName: DataModelName ; objectId: string | number } ,
  ) : boolean
```
true if the object is deleted, false otherwise.
### `isNew`

```typescript
isNew (
  args: { dataModelName: DataModelName ; objectId: string | number } ,
  ) : boolean
```
true if the object is new, false otherwise.
### `refreshData`

```typescript
refreshData () : Promise < void >
```
promise that resolves once the data refresh completed.

---

# index.SDK.DataModelNotFoundError

---
title: SDK.DataModelNotFoundError class
source: classes/index.SDK.DataModelNotFoundError.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class DataModelNotFoundError

```typescript
cause ?: unknown
```
This error indicates that the entity that was referenced in the SDK method call not found.
## Properties
### **Readonly** `modelId`

```typescript
modelId: string | number
```
### **Readonly** `modelType`

```typescript
modelType: string
```
### **Readonly** `name`

```typescript
name: "DataModelNotFoundError"
```
## Methods

---

# index.SDK.EditSuggestions

---
title: SDK.EditSuggestions class
source: classes/index.SDK.EditSuggestions.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class EditSuggestions

```typescript
getAll () : EditSuggestion []
```
Methods for dealing with EditSuggestions.
## Methods
### `getAll`

```typescript
getAll () : EditSuggestion []
```
an array of all the edit suggestions in the WME data model
### `getById`

```typescript
getById ( args: { editSuggestionId: string } ) : null | EditSuggestion
```
edit suggestion with id, or null if not found in the WME data model
### `getEditSuggestionChanges`

```typescript
getEditSuggestionChanges (
  args: { editSuggestionId: string } ,
  ) : EditSuggestionChange []
```
an array of edit suggestion changes

---

# index.SDK.Editing

---
title: SDK.Editing class
source: classes/index.SDK.Editing.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Editing

```typescript
clearSelection () : void
```
Methods for dealing with selection and undoing/redoing actions.
## Methods
### `clearSelection`

```typescript
clearSelection () : void
```

### `getCurrentSaveMode`

```typescript
getCurrentSaveMode () : SaveMode
```
current SaveMode .
### `getRedoChangesCount`

```typescript
getRedoChangesCount () : number
```
the number of changes that can be redone.
### `getSelection`

```typescript
getSelection () : null | SelectionWithLocalizedTypeName
```
ids of currently selected objects or null if nothing selected. The selection
only includes objects of a single type.
### `getUnsavedChangesCount`

```typescript
getUnsavedChangesCount () : number
```
the number of unsaved edits.
### `isDrawingInProgress`

```typescript
isDrawingInProgress () : boolean
```
true if drawing is in progress.
### `isEditingAllowed`

```typescript
isEditingAllowed () : boolean
```
true if editing is allowed.
### `isEditingHouseNumbers`

```typescript
isEditingHouseNumbers () : boolean
```
false.
### `isPracticeModeOn`

```typescript
isPracticeModeOn () : boolean
```
true if user is editing as a guest in "practice mode"
### `isSnapshotModeOn`

```typescript
isSnapshotModeOn () : boolean
```
true if user is in "snapshot mode", viewing what’s currently live
in the Waze app.
### `lockEditing`

```typescript
lockEditing () : string
```
unique id to be used for unlocking editing.
### `redo`

```typescript
redo () : void
```

### `releaseEditingLock`

```typescript
releaseEditingLock ( args: { lockId: string } ) : void
```

### `save`

```typescript
save () : Promise < void >
```
promise that resolves once save completed successfully or failed.
### `setSelection`

```typescript
setSelection ( options: { selection: Selection } ) : void
```

### `undo`

```typescript
undo () : void
```

### `undoAll`

```typescript
undoAll () : void
```

---

# index.SDK.HouseNumbers

---
title: SDK.HouseNumbers class
source: classes/index.SDK.HouseNumbers.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class HouseNumbers

```typescript
addHouseNumber ( args: { number: string ; point: Point ; segmentId ?: number } ) : void
```
Methods for dealing with HouseNumbers
## Methods
### `addHouseNumber`

```typescript
addHouseNumber ( args: { number: string ; point: Point ; segmentId ?: number } ) : void
```

### `clearHouseNumbers`

```typescript
clearHouseNumbers () : void
```

### `deleteHouseNumber`

```typescript
deleteHouseNumber ( args: { houseNumberId: string } ) : void
```

### `fetchHouseNumbers`

```typescript
fetchHouseNumbers ( options: { segmentIds: number [] } ) : Promise < HouseNumber [] >
```
A Promise that resolves to an array of HouseNumber objects.
### `moveHouseNumber`

```typescript
moveHouseNumber (
  args: { houseNumberId: string ; point: Point ; segmentId ?: number } ,
  ) : void
```

### `moveHouseNumberFractionPoint`

```typescript
moveHouseNumberFractionPoint (
  args: { fractionPoint: Point ; houseNumberId: string } ,
  ) : void
```

### `updateHouseNumber`

```typescript
updateHouseNumber (
  args: {
  fractionPoint ?: Point ;
  houseNumberId: string ;
  number ?: string ;
  point ?: Point ;
  segmentId ?: number ;
} ,
  ) : void
```

---

# index.SDK.InvalidStateError

---
title: SDK.InvalidStateError class
source: classes/index.SDK.InvalidStateError.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class InvalidStateError

```typescript
new InvalidStateError ( message ?: string ) : InvalidStateError
```
This error indicates that the SDK method call cannot be completed in current state of the WME.
## Constructors
## Properties
### **Readonly** `name`

```typescript
name: "InvalidStateError"
```
## Methods

---

# index.SDK.IssueTracker

---
title: SDK.IssueTracker class
source: classes/index.SDK.IssueTracker.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class IssueTracker

```typescript
closePanel () : void
```
Methods for managing the WME Issue Tracker panels.
## Methods
### `closePanel`

```typescript
closePanel () : void
```

### `getActiveFilters`

```typescript
getActiveFilters () : IssueTrackerFilters
```
Active filters configured in the WME Issue Tracker panel.
### `showPanel`

```typescript
showPanel ( args: { issueTrackerId: number ; type: IssueTrackerType } ) : void
```

---

# index.SDK.Junctions

---
title: SDK.Junctions class
source: classes/index.SDK.Junctions.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Junctions

```typescript
getAll () : Junction []
```
Methods for dealing with Junctions.
## Methods
### `getAll`

```typescript
getAll () : Junction []
```
an array of all the junctions in the WME data model
### `getById`

```typescript
getById ( args: { junctionId: number } ) : null | Junction
```
junctions with id, or null if not found in the WME data model

---

# index.SDK.LayerSwitcher

---
title: SDK.LayerSwitcher class
source: classes/index.SDK.LayerSwitcher.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class LayerSwitcher

```typescript
addLayerCheckbox ( __namedParameters: { isChecked ?: boolean ; name: string } ) : void
```
Methods for interacting with LayerSwitcher.
## Methods
### `addLayerCheckbox`

```typescript
addLayerCheckbox ( __namedParameters: { isChecked ?: boolean ; name: string } ) : void
```

### `getWMELayerVisibility`

```typescript
getWMELayerVisibility ( args: { layerName: WmeLayerName } ) : boolean
```
true if the layer is visible, or false otherwise.
### `isLayerCheckboxChecked`

```typescript
isLayerCheckboxChecked ( args: { name: string } ) : boolean
```
value of the checkbox
### `removeLayerCheckbox`

```typescript
removeLayerCheckbox ( args: { name: string } ) : void
```

### `setClosuresLayerCheckboxChecked`

```typescript
setClosuresLayerCheckboxChecked ( args: { isChecked: boolean } ) : void
```

### `setHazardsLayerCheckboxChecked`

```typescript
setHazardsLayerCheckboxChecked ( args: { isChecked: boolean } ) : void
```

### `setJunctionBoxesLayerCheckboxChecked`

```typescript
setJunctionBoxesLayerCheckboxChecked ( args: { isChecked: boolean } ) : void
```

### `setLayerCheckboxChecked`

```typescript
setLayerCheckboxChecked ( args: { isChecked: boolean ; name: string } ) : void
```

### `setPathsLayerCheckboxChecked`

```typescript
setPathsLayerCheckboxChecked ( args: { isChecked: boolean } ) : void
```

### `setPlacesLayerCheckboxChecked`

```typescript
setPlacesLayerCheckboxChecked ( args: { isChecked: boolean } ) : void
```

### `setRoadsLayerCheckboxChecked`

```typescript
setRoadsLayerCheckboxChecked ( args: { isChecked: boolean } ) : void
```

### `setWMELayerVisibility`

```typescript
setWMELayerVisibility (
  args: { isVisible: boolean ; layerName: WmeLayerName } ,
  ) : void
```

---

# index.SDK.MajorTrafficEvents

---
title: SDK.MajorTrafficEvents class
source: classes/index.SDK.MajorTrafficEvents.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class MajorTrafficEvents

```typescript
getAll () : MajorTrafficEvent []
```
Methods for dealing with MajorTrafficEvents.
## Methods
### `getAll`

```typescript
getAll () : MajorTrafficEvent []
```
an array of all the major traffic event in the WME data model
### `getById`

```typescript
getById ( args: { majorTrafficEventId: string } ) : null | MajorTrafficEvent
```
major traffic event with id, or null if not found in the WME data model

---

# index.SDK.ManagedAreas

---
title: SDK.ManagedAreas class
source: classes/index.SDK.ManagedAreas.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class ManagedAreas

```typescript
getAll () : ManagedArea []
```
Methods for dealing with ManagedAreas.
## Methods
### `getAll`

```typescript
getAll () : ManagedArea []
```
an array of all the managed areas in the WME data model
### `getById`

```typescript
getById ( args: { managedAreaId: string } ) : null | ManagedArea
```
managed area with id, or null if not found in the WME data model

---

# index.SDK.Map

---
title: SDK.Map class
source: classes/index.SDK.Map.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Map

```typescript
MAX_ZOOM_LEVEL: ZoomLevel = MAX_ZOOM_LEVEL
```
Methods for dealing with the map.
## Properties
### **Readonly** `MAX_ZOOM_LEVEL`

```typescript
MAX_ZOOM_LEVEL: ZoomLevel = MAX_ZOOM_LEVEL
```
### **Readonly** `MIN_ZOOM_LEVEL`

```typescript
MIN_ZOOM_LEVEL: ZoomLevel = MIN_ZOOM_LEVEL
```
## Methods
### `addFeaturesToLayer`

```typescript
addFeaturesToLayer (
  args: { features: SdkFeature < SdkFeatureGeometry > [] ; layerName: string } ,
  ) : void
```

### `addFeatureToLayer`

```typescript
addFeatureToLayer ( args: { feature: SdkFeature ; layerName: string } ) : void
```

### `addLayer`

```typescript
addLayer (
  args: {
  layerName: string ;
  styleContext ?: SdkFeatureStyleContext ;
  styleRules ?: SdkFeatureStyleRule [] ;
  zIndexing ?: boolean ;
} ,
  ) : void
```
**Example: Basic layer with no styling**
```typescript
sdk.Map.addLayer({ layerName: "basic_layer" });
```
**Example: Layer with predicate-based styling and default style**
```typescript
sdk.Map.addLayer({
  layerName: "predicate_style_layer",
  styleRules: [
    {
      style: { // Default style
        strokeColor: "lightgray",
        strokeWidth: 5,
      },
    },
    {
      predicate: (featureProperties, zoomLevel) => featureProperties.isHighlighted && zoomLevel === 12,
      style: {
        strokeColor: "yellow",
        strokeWidth: 10,
      },
    },
  ]
});
```
**Example: Layer with style context**
```typescript
sdk.Map.addLayer({
  layerName: "context_style_layer",
  styleContext: {
    getStrokeColor: ({ feature, zoomLevel }) => feature?.properties.color ?? "#FF007F",
    getStrokeWidth: () => 10,
  },
  styleRules: [
    {
      style: {
        strokeColor: "${getStrokeColor}",
        strokeWidth: "${getStrokeWidth}",
      },
    },
  ]
});
```
**Example: Layer with external graphic (for example, a marker layer)**
```typescript
const redCircleImage = 'data:image/svg+xml;base64,Cjxzdmcgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxlbGxpcHNlIHN0eWxlPSJmaWxsOnJlZDsgc3Ryb2tlOm5vbmUiIGN4PSIxMCIgY3k9IjEwIiByeD0iMTAiIHJ5PSIxMCI+PC9lbGxpcHNlPjwvc3ZnPgo='
const blueSquareImage = 'data:image/svg+xml;base64,Cjxzdmcgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCIgc3R5bGU9ImZpbGw6Ymx1ZTtzdHJva2U6bm9uZSIgLz48L3N2Zz4K'
sdk.Map.addLayer({
  layerName: "marker_layer",
  styleRules: [
    {
      predicate: (featureProperties) => featureProperties.redCircle,
      style: {
        externalGraphic: redCircleImage,
        fillOpacity: 1,
      },
    },
    {
      predicate: (featureProperties) => featureProperties.blueSquare,
      style: {
        externalGraphic: blueSquareImage,
        fillOpacity: 1,
      },
    },
  ],
});
sdk.Map.addFeatureToLayer({
   layerName: "marker_layer",
   feature: {
     id: "marker_1",
     type: "Feature",
     geometry: {
       type: "Point",
       coordinates: [-36.44069, 39.42386],
     },
     properties: {
       redCircle: true,
     },
   },
})
```
### `addStyleRuleToLayer`

```typescript
addStyleRuleToLayer (
  args: { layerName: WME_LAYER_NAMES ; styleRules: SdkFeatureStyleRule [] } ,
  ) : void
```

### `addTileLayer`

```typescript
addTileLayer ( args: { layerName: string ; layerOptions: TileLayerOptions } ) : void
```

### `centerMapOnGeometry`

```typescript
centerMapOnGeometry ( args: { geometry: Point | Polygon | LineString } ) : void
```

### `dangerouslyAddFeaturesToLayerWithoutValidation`

```typescript
dangerouslyAddFeaturesToLayerWithoutValidation (
  args: { features: object [] ; layerName: string } ,
  ) : void
```

### `disablePolygonResize`

```typescript
disablePolygonResize () : void
```

### `disablePolygonRotation`

```typescript
disablePolygonRotation () : void
```

### `disableSelectionToggling`

```typescript
disableSelectionToggling () : void
```

### `drawLine`

```typescript
drawLine () : Promise < LineString >
```
a new LineString geometry
### `drawPoint`

```typescript
drawPoint ( __namedParameters ?: { snapTo ?: SnapTo } ) : Promise < Point >
```
**Example**
```typescript
// Draw a point without snapping.
const point = await sdk.Map.drawPoint();
console.log(point.coordinates); // Output: [longitude, latitude]
// Draw a point and snap it to the nearest segment.
const snappedPoint = await sdk.Map.drawPoint({ snapTo: "segment" });
console.log(snappedPoint.coordinates); // Output: [longitude, latitude] (projected onto the segment)
```
a new point geometry that was drawn on the map.
### `drawPolygon`

```typescript
drawPolygon () : Promise < null | Polygon >
```
a new polygon geometry or null if an invalid polygon was drawn.
### `enablePolygonResize`

```typescript
enablePolygonResize () : void
```

### `enablePolygonRotation`

```typescript
enablePolygonRotation () : void
```

### `enableSelectionToggling`

```typescript
enableSelectionToggling () : void
```

### `getFeatureDomElement`

```typescript
getFeatureDomElement (
  args: { featureId: string | number ; layerName: string } ,
  ) : null | HTMLElement | SVGElement
```
a DOM element of a feature on the map within the given layer.
The return value is HTMLElement in case it's a marker, and SVGElement otherwise. null if a feature with provided featureId does not exist within the layer.
### `getLayerOpacity`

```typescript
getLayerOpacity ( args: { layerName: string } ) : number
```
layer's opacity level - a float number between 0.0 and 1.0.
### `getLayerZIndex`

```typescript
getLayerZIndex ( args: { layerName: string } ) : number
```
map layer's z-index value.
### `getLiveMapLink`

```typescript
getLiveMapLink () : string
```
a link to the LiveMap with the current map state
### `getLonLatFromMapPixel`

```typescript
getLonLatFromMapPixel ( args: { x: number ; y: number } ) : LonLat
```
the coordinates in WGS84 format, corresponding to the given pixel.
### `getLonLatFromPixel`

```typescript
getLonLatFromPixel ( args: { x: number ; y: number } ) : LonLat
```
the coordinates in WGS84 format, corresponding to the given pixel.
### `getMapCenter`

```typescript
getMapCenter () : LonLat
```
the map's current center coordinates in WGS84 format
### `getMapExtent`

```typescript
getMapExtent () : BBox
```
the map's currently visible area as a GeoJSON BBox
which is an array of coordinates in WGS84 format in the following order:
[left, bottom, right, top]
### `getMapPixelFromLonLat`

```typescript
getMapPixelFromLonLat ( args: { lonLat: LonLat } ) : Pixel
```
the map pixel coordinates corresponding to the given geographic coordinates in WGS84 format.
### `getMapResolution`

```typescript
getMapResolution () : number
```
The current resolution of the map.
Map resolution defines the number of map units per pixel at the current zoom level.
### `getMapViewportElement`

```typescript
getMapViewportElement () : HTMLElement
```
the map's viewport element.
### `getPermalink`

```typescript
getPermalink ( options ?: { includeLayers ?: boolean } ) : string
```
the current WME permalink
### `getPixelFromLonLat`

```typescript
getPixelFromLonLat ( args: { lonLat: LonLat } ) : Pixel
```
the screen pixel coordinates corresponding to the given geographic coordinates in WGS84 format.
### `getZoomLevel`

```typescript
getZoomLevel () : ZoomLevel
```
the map's current zoom level
### `isLayerVisible`

```typescript
isLayerVisible ( args: { layerName: string } ) : boolean
```
true if layer is visible, false otherwise
### `isStreetViewActive`

```typescript
isStreetViewActive () : boolean
```
true if the street view pane is active
### `redrawLayer`

```typescript
redrawLayer ( args: { layerName: string } ) : void
```

### `removeAllFeaturesFromLayer`

```typescript
removeAllFeaturesFromLayer ( args: { layerName: string } ) : void
```

### `removeFeatureFromLayer`

```typescript
removeFeatureFromLayer (
  args: { featureId: string | number ; layerName: string } ,
  ) : void
```

### `removeFeaturesFromLayer`

```typescript
removeFeaturesFromLayer (
  args: { featureIds: ( string | number ) [] ; layerName: string } ,
  ) : void
```

### `removeLayer`

```typescript
removeLayer ( args: { layerName: string } ) : void
```

### `setLayerOpacity`

```typescript
setLayerOpacity ( args: { layerName: string ; opacity: number } ) : void
```

### `setLayerVisibility`

```typescript
setLayerVisibility ( args: { layerName: string ; visibility: boolean } ) : void
```

### `setLayerZIndex`

```typescript
setLayerZIndex ( args: { layerName: string ; zIndex: number } ) : void
```

### `setMapCenter`

```typescript
setMapCenter ( args: { lonLat: LonLat ; zoomLevel ?: ZoomLevel } ) : void
```

### `setZoomLevel`

```typescript
setZoomLevel ( args: { zoomLevel: ZoomLevel } ) : void
```

### `zoomIn`

```typescript
zoomIn () : void
```

### `zoomOut`

```typescript
zoomOut () : void
```

### `zoomToExtent`

```typescript
zoomToExtent ( args: { bbox: BBox } ) : void
```

---

# index.SDK.MapComments

---
title: SDK.MapComments class
source: classes/index.SDK.MapComments.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class MapComments

```typescript
addComment (
  args: {
  body: string ;
  endDate: number ;
  geometry: Point | Polygon ;
  subject: string ;
} ,
  ) : MapComment
```
Methods for dealing with MapComments.
## Methods
### `addComment`

```typescript
addComment (
  args: {
  body: string ;
  endDate: number ;
  geometry: Point | Polygon ;
  subject: string ;
} ,
  ) : MapComment
```
the created map comment.
### `deleteComment`

```typescript
deleteComment ( args: { mapCommentId: string } ) : null
```
null.
### `getAll`

```typescript
getAll () : MapComment []
```
an array of all the map comments in the WME data model
### `getById`

```typescript
getById ( args: { mapCommentId: string } ) : null | MapComment
```
map comment with id, or null if not found in the WME data model
### `updateComment`

```typescript
updateComment (
  args: {
  body ?: string ;
  endDate ?: null | number ;
  geometry ?: Point | Polygon ;
  mapCommentId: string ;
  subject ?: string ;
} ,
  ) : MapComment
```
the updated map comment.

---

# index.SDK.MapProblems

---
title: SDK.MapProblems class
source: classes/index.SDK.MapProblems.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class MapProblems

```typescript
getAll () : MapProblem []
```
Methods for dealing with MapProblems.
## Methods
### `getAll`

```typescript
getAll () : MapProblem []
```
an array of all the map problems in the WME data model
### `getById`

```typescript
getById ( args: { mapProblemId: string } ) : null | MapProblem
```
map problem with id, or null if not found in the WME data model

---

# index.SDK.MapUpdateRequests

---
title: SDK.MapUpdateRequests class
source: classes/index.SDK.MapUpdateRequests.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class MapUpdateRequests

```typescript
addComment (
  args: { mapUpdateRequestId: number ; text: string } ,
  ) : Promise < ConversationElement >
```
Methods for dealing with MapUpdateRequests.
## Methods
### `addComment`

```typescript
addComment (
  args: { mapUpdateRequestId: number ; text: string } ,
  ) : Promise < ConversationElement >
```
A promise that resolves to a created conversation element representing the comment.
### `getAll`

```typescript
getAll () : MapUpdateRequest []
```
an array of all the map update requests in the WME data model
### `getById`

```typescript
getById ( args: { mapUpdateRequestId: number } ) : null | MapUpdateRequest
```
map update request with id, or null if not found in the WME data model
### `getUpdateRequestDetails`

```typescript
getUpdateRequestDetails (
  args: { mapUpdateRequestId: number } ,
  ) : Promise < null | UpdateRequestDetails >
```
map update request details. If details are not present in the WME data model, they will be fetched.
Returns null if not found in the WME data model.
### `updateResolutionState`

```typescript
updateResolutionState (
  args: {
  mapUpdateRequestId: number ;
  resolutionState: UpdateableMapProblemState ;
} ,
  ) : void
```

---

# index.SDK.Nodes

---
title: SDK.Nodes class
source: classes/index.SDK.Nodes.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Nodes

```typescript
allowNodeTurns ( args: { allow: boolean ; nodeId: number } ) : boolean
```
Methods for dealing with Nodes.
## Methods
### `allowNodeTurns`

```typescript
allowNodeTurns ( args: { allow: boolean ; nodeId: number } ) : boolean
```
false if there's nothing to change(all turns are already allowed/disallowed or there are no turns), true if the change is successful.
### `canEdit`

```typescript
canEdit ( args: { nodeId: number } ) : boolean
```
true if node properties are editable.
### `canEditTurns`

```typescript
canEditTurns ( args: { nodeId: number } ) : boolean
```
true if all segments connected to the node are allowed to edit connections.
### `getAll`

```typescript
getAll () : Node []
```
an array of all the nodes in the WME data model
### `getById`

```typescript
getById ( args: { nodeId: number } ) : null | Node
```
node with id, or null if not found in the WME data model
### `isVirtual`

```typescript
isVirtual ( args: { nodeId: number } ) : boolean
```
boolean indicating whether the node is virtually connected to any segment.
### `moveNode`

```typescript
moveNode ( args: { geometry: Point ; id: number } ) : void
```

---

# index.SDK.ParkingLot

---
title: SDK.ParkingLot class
source: classes/index.SDK.ParkingLot.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class ParkingLot

```typescript
canExitWhileClosed ( args: { venueId: string } ) : null | boolean
```
Methods for dealing with Parking Lots.
## Methods
### `canExitWhileClosed`

```typescript
canExitWhileClosed ( args: { venueId: string } ) : null | boolean
```
whether the current venue can be exited while closed in case the venue is a parking lot, null otherwise.
### `getBrands`

```typescript
getBrands () : string []
```
a list of parking lot brands
### `getCostType`

```typescript
getCostType ( args: { venueId: string } ) : null | ParkingLotCostType
```
cost type of the venue in case the venue is a parking lot, null otherwise.
### `getEstimatedNumberOfSpots`

```typescript
getEstimatedNumberOfSpots ( args: { venueId: string } ) : null | SpotsEstimate
```
SpotsEstimate | null - the estimated number of spots the venue in case the venue is a parking lot, null otherwise.
### `getLotTypes`

```typescript
getLotTypes ( args: { venueId: string } ) : null | LotType []
```
parking lot types of the venue in case the venue is a parking lot, null otherwise.
### `getParkingLotType`

```typescript
getParkingLotType ( args: { venueId: string } ) : ParkingType
```
parking type of the venue in case the venue is a parking lot, null otherwise.
### `getPaymentMethods`

```typescript
getPaymentMethods ( args: { venueId: string } ) : null | PaymentType []
```
payment types of the venue in case the venue is a parking lot, null otherwise.
### `isLotTypeDependentOnDayTime`

```typescript
isLotTypeDependentOnDayTime ( args: { venueId: string } ) : null | boolean
```
whether lot type of the current venue varies depending on time/day in case the venue is a parking lot, null otherwise.
### `setEstimatedNumberOfSpots`

```typescript
setEstimatedNumberOfSpots (
  args: { estimatedNumberOfSpots: SpotsEstimate ; venueId: string } ,
  ) : void
```

---

# index.SDK.PermanentHazards

---
title: SDK.PermanentHazards class
source: classes/index.SDK.PermanentHazards.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class PermanentHazards

```typescript
getAll () : PermanentHazard []
```
Methods for dealing with PermanentHazards.
## Methods
### `getAll`

```typescript
getAll () : PermanentHazard []
```
an array of all the permanent hazards in the WME data model
### `getAllCameras`

```typescript
getAllCameras () : Camera []
```
an array of all the cameras in the WME data model
### `getById`

```typescript
getById ( args: { hazardId: number } ) : null | PermanentHazard
```
permanent hazard with id, or null if not found in the WME data model
### `getCameraById`

```typescript
getCameraById ( args: { cameraId: number } ) : null | Camera
```
camera with id, or null if not found in the WME data model

---

# index.SDK.RestrictedDrivingAreas

---
title: SDK.RestrictedDrivingAreas class
source: classes/index.SDK.RestrictedDrivingAreas.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class RestrictedDrivingAreas

```typescript
getAll () : RestrictedDrivingArea []
```
Methods for dealing with RestrictedDrivingAreas.
## Methods
### `getAll`

```typescript
getAll () : RestrictedDrivingArea []
```
an array of all the restricted driving areas in the WME data model
### `getById`

```typescript
getById ( args: { restrictedDrivingAreaId: number } ) : null | RestrictedDrivingArea
```
restricted driving area with id, or null if not found in the WME data model

---

# index.SDK.RoadClosures

---
title: SDK.RoadClosures class
source: classes/index.SDK.RoadClosures.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class RoadClosures

```typescript
addClosure (
  args: {
  description: string ;
  endDate: number ;
  fromNodeClosed: boolean ;
  isForward: boolean ;
  isPermanent: boolean ;
  segmentId: number ;
  startDate: number ;
  trafficEventId: null | string ;
} ,
  ) : RoadClosure
```
Methods for dealing with RoadClosures.
## Methods
### `addClosure`

```typescript
addClosure (
  args: {
  description: string ;
  endDate: number ;
  fromNodeClosed: boolean ;
  isForward: boolean ;
  isPermanent: boolean ;
  segmentId: number ;
  startDate: number ;
  trafficEventId: null | string ;
} ,
  ) : RoadClosure
```
the created road closure.
### `getAll`

```typescript
getAll () : RoadClosure []
```
an array of all the road closures in the WME data model
### `getById`

```typescript
getById ( args: { roadClosureId: string } ) : null | RoadClosure
```
road closure with id, or null if not found in the WME data model

---

# index.SDK.SdkEventBus

---
title: SDK.SdkEventBus class
source: classes/index.SDK.SdkEventBus.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class SdkEventBus

```typescript
clear () : void
```
Event bus for SDK events. For the list of events and their payload checkSdkEvents.
## Methods
### `clear`

```typescript
clear () : void
```

### `off`

```typescript
off < EventName extends keyof SdkEvents > (
  args: {
  eventHandler: EventHandler < SdkEvents [ EventName ] > ;
  eventName: EventName ;
} ,
  ) : void
```

### `on`

```typescript
on < EventName extends keyof SdkEvents > (
  args: {
  eventHandler: EventHandler < SdkEvents [ EventName ] > ;
  eventName: EventName ;
} ,
  ) : () = > void
```
a cleanup function that will unregister the handler from the event.
### `once`

```typescript
once < EventName extends keyof SdkEvents > (
  args: { eventName: EventName } ,
  ) : Promise < SdkEvents [ EventName ] >
```
a promise that gets resolved once the event happens.
### `stopDataModelEventsTracking`

```typescript
stopDataModelEventsTracking ( args: { dataModelName: DataModelName } ) : void
```

### `stopLayerEventsTracking`

```typescript
stopLayerEventsTracking ( args: { layerName: string } ) : void
```

### `trackDataModelEvents`

```typescript
trackDataModelEvents ( args: { dataModelName: DataModelName } ) : void
```

### `trackLayerEvents`

```typescript
trackLayerEvents ( args: { layerName: string } ) : void
```

---

# index.SDK.SegmentSuggestions

---
title: SDK.SegmentSuggestions class
source: classes/index.SDK.SegmentSuggestions.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class SegmentSuggestions

```typescript
getAll () : SegmentSuggestion []
```
Methods for dealing with SegmentSuggestions.
## Methods
### `getAll`

```typescript
getAll () : SegmentSuggestion []
```
an array of all the segment suggestions in the WME data model
### `getById`

```typescript
getById ( args: { segmentSuggestionId: number } ) : null | SegmentSuggestion
```
segment suggestion with id, or null if not found in the WME data model
### `reject`

```typescript
reject (
  args: {
  reason: SegmentSuggestionRejectionReason ;
  segmentSuggestionIds: number [] ;
} ,
  ) : void
```

---

# index.SDK.Segments

---
title: SDK.Segments class
source: classes/index.SDK.Segments.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Segments

```typescript
addAlternateStreet ( args: { segmentIds: number [] ; streetId: number } ) : void
```
Methods for dealing with Segments.
## Methods
### `addAlternateStreet`

```typescript
addAlternateStreet ( args: { segmentIds: number [] ; streetId: number } ) : void
```

### `addIntersection`

```typescript
addIntersection (
  args: { segmentIds: [ number , number ] } ,
  ) : { sourceSplits: [ number , number ] ; targetSplits: [ number , number ] }
```
the ids of the four newly created segments.
### `addSegment`

```typescript
addSegment ( args: { geometry: LineString ; roadType: RoadTypeId } ) : number
```
segment id of the new segment
### `connectsToBigJunction`

```typescript
connectsToBigJunction ( args: { segmentId: number } ) : boolean
```
true if the segment is completely within, goes inside or goes outside of a big junction.
### `createRoundabout`

```typescript
createRoundabout ( args: { center: LonLat ; rx: number ; ry: number } ) : number []
```
ids of roundabout segments
### `deleteSegment`

```typescript
deleteSegment ( args: { segmentId: number } ) : void
```

### `findSegment`

```typescript
findSegment ( args: { segmentId: number } ) : Promise < Segment >
```
A promise that resolves to the found segment.
### `getAddress`

```typescript
getAddress ( args: { segmentId: number } ) : SegmentAddress
```
an address of the segment with provided id.
### `getAll`

```typescript
getAll () : Segment []
```
an array of all the segments in the WME data model
### `getById`

```typescript
getById ( args: { segmentId: number } ) : null | Segment
```
segment with id, or null if not found in the WME data model
### `getConnectedSegments`

```typescript
getConnectedSegments (
  args: { reverseDirection ?: boolean ; segmentId: number } ,
  ) : Segment []
```
connected segments in specified direction
### `getReversedSegments`

```typescript
getReversedSegments ( args: { segmentIds: number [] } ) : Segment []
```
An array of segments that are considered reversed within the provided list.
### `getRoadTypes`

```typescript
getRoadTypes () : RoadType []
```
all possible road types and their localised names.
### `getVirtualNodes`

```typescript
getVirtualNodes ( args: { segmentId: number } ) : Node []
```
array of nodes virtually connected to the specified segment.
### `getWKTGeometry`

```typescript
getWKTGeometry ( args: { segmentId: number } ) : string
```
the WKT string representation of the segment's geometry
### `hasPermissions`

```typescript
hasPermissions (
  args: { permission ?: SegmentPermission ; segmentId: number } ,
  ) : boolean
```
whether the current user has a permission for this segment or not.
### `isContainedInBigJunction`

```typescript
isContainedInBigJunction ( args: { segmentId: number } ) : boolean
```
true if the segment is completely within a big junction
### `isFromNodeInBigJunction`

```typescript
isFromNodeInBigJunction (
  args: { bigJunctionId ?: number ; segmentId: number } ,
  ) : boolean
```
true if the segment's "from" node is part of a big junction, indicating the segment leads away from it.
### `isRoadTypeDrivable`

```typescript
isRoadTypeDrivable ( args: { roadType: RoadTypeId } ) : boolean
```
boolean indicating whether the specified road type is drivable by vehicles.
A road type is considered non-drivable if it is a walking trail, pedestrian boardwalk, stairway, railroad, or runway/taxiway.
### `isTollSegment`

```typescript
isTollSegment ( args: { segmentId: number } ) : boolean
```
true if the segment is a toll road or has a toll-free restriction
### `isToNodeInBigJunction`

```typescript
isToNodeInBigJunction (
  args: { bigJunctionId ?: number ; segmentId: number } ,
  ) : boolean
```
true if the segment's "to" node is part of a big junction, indicating the segment leads into it.
### `mergeSegments`

```typescript
mergeSegments ( args: { segmentIds: number [] } ) : void
```

### `splitSegment`

```typescript
splitSegment ( args: { segmentId: number ; splitPoint: Point } ) : [ number , number ]
```
two segments the original segment was split into.
### `updateAddress`

```typescript
updateAddress (
  args: { addressData ?: SegmentAddressData ; segmentId: number } ,
  ) : void
```

### `updateSegment`

```typescript
updateSegment (
  args: {
  direction ?: SegmentDirection ;
  elevationLevel ?: number ;
  flagAttributes ?: Partial <
  Pick <
  SegmentFlagAttributes ,
  "headlights"
  | "nearbyHOV"
  | "tunnel"
  | "unpaved" ,
  > ,
  > ;
  fromLanesInfo ?: null | SegmentLanesInfo ;
  fwdSpeedLimit ?: null | number ;
  geometry ?: LineString ;
  hasToll ?: boolean ;
  lockRank ?: UserRank ;
  restrictions ?: SegmentRestrictionData [] ;
  revSpeedLimit ?: null | number ;
  roadType ?: RoadTypeId ;
  routingRoadType ?: 1 | 2 | 3 | 6 | 7 ;
  segmentId: number ;
  toLanesInfo ?: null | SegmentLanesInfo ;
} ,
  ) : void
```

### `verifyTurns`

```typescript
verifyTurns ( args: { isForward: boolean ; segmentId: number } ) : void
```

---

# index.SDK.Settings

---
title: SDK.Settings class
source: classes/index.SDK.Settings.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Settings

```typescript
getLocale () : { localeCode: string ; localeName: string }
```
Methods for managing user settings.
## Methods
### `getLocale`

```typescript
getLocale () : { localeCode: string ; localeName: string }
```
and object with the current locale code and locale name
### `getRegionCode`

```typescript
getRegionCode () : null | RegionCode
```
the current region code, or null if not available
### `getUserSettings`

```typescript
getUserSettings () : UserSettings
```
the current user settings or default settings if user isn't logged in yet.
### `setRegionCode`

```typescript
setRegionCode ( args: { regionCode: RegionCode } ) : void
```

### `setUserSettings`

```typescript
setUserSettings ( options: Partial < UserSettings > ) : void
```

---

# index.SDK.Shortcuts

---
title: SDK.Shortcuts class
source: classes/index.SDK.Shortcuts.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Shortcuts

```typescript
areShortcutKeysInUse ( args: { shortcutKeys: string } ) : boolean
```
Methods for defining shortcuts.
## Methods
### `areShortcutKeysInUse`

```typescript
areShortcutKeysInUse ( args: { shortcutKeys: string } ) : boolean
```
true if a shortcut key combination is already in use, otherwise false
### `createShortcut`

```typescript
createShortcut ( args: KeyboardShortcut ) : void
```

### `deleteShortcut`

```typescript
deleteShortcut ( args: { shortcutId: string } ) : void
```

### `getAllShortcuts`

```typescript
getAllShortcuts () : KeyboardShortcut []
```
all registered shortcuts of the userscript.
### `isShortcutRegistered`

```typescript
isShortcutRegistered ( args: { shortcutId: string } ) : boolean
```
true if a shortcut with specified id is already registered.

---

# index.SDK.Sidebar

---
title: SDK.Sidebar class
source: classes/index.SDK.Sidebar.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Sidebar

```typescript
registerScriptTab () : Promise < RegisterSidebarTabResult >
```
Methods for interacting with Sidebar.
## Methods
### `registerScriptTab`

```typescript
registerScriptTab () : Promise < RegisterSidebarTabResult >
```
a sidebar tab label element and a tab pane element
### `removeScriptTab`

```typescript
removeScriptTab () : void
```

---

# index.SDK.Signs

---
title: SDK.Signs class
source: classes/index.SDK.Signs.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Signs

```typescript
getAll ( args ?: { type ?: SignType } ) : Sign []
```
Methods for dealing with Signs.
## Methods
### `getAll`

```typescript
getAll ( args ?: { type ?: SignType } ) : Sign []
```
an array of all the signs in the WME data model
### `getById`

```typescript
getById ( args: { signId: number } ) : null | Sign
```
sign with id, or null if not found in the WME data model

---

# index.SDK.States

---
title: SDK.States class
source: classes/index.SDK.States.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class States

```typescript
getAll () : State []
```
Methods for dealing with State.
## Methods
### `getAll`

```typescript
getAll () : State []
```
an array of all the states in the WME data model
### `getAllWithoutDefault`

```typescript
getAllWithoutDefault () : State []
```
an array of all the states apart from default in the WME data model
### `getById`

```typescript
getById ( args: { stateId: number } ) : null | State
```
state with id, or null if not found in the WME data model
### `getTopState`

```typescript
getTopState () : null | State
```
the State set to be the top state in the WME data model, or null
if none set
### `hasNonDefaultStates`

```typescript
hasNonDefaultStates () : boolean
```
true if there are any states apart from the default state in the WME data model.

---

# index.SDK.StreetView

---
title: SDK.StreetView class
source: classes/index.SDK.StreetView.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class StreetView

```typescript
close () : void
```
Methods for dealing with Street View.
## Methods
### `close`

```typescript
close () : void
```

### `isActive`

```typescript
isActive () : boolean
```
true if the street view pane is active
### `open`

```typescript
open ( args: { lonLat: LonLat ; radius ?: number } ) : Promise < void >
```

---

# index.SDK.Streets

---
title: SDK.Streets class
source: classes/index.SDK.Streets.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Streets

```typescript
addStreet ( args: { cityId ?: number ; streetName: string } ) : Street
```
Methods for dealing with Streets.
## Methods
### `addStreet`

```typescript
addStreet ( args: { cityId ?: number ; streetName: string } ) : Street
```
a new street object
### `getAll`

```typescript
getAll () : Street []
```
an array of all the streets in the WME data model
### `getById`

```typescript
getById ( args: { streetId: number } ) : null | Street
```
street with id, or null if not found in the WME data model
### `getStreet`

```typescript
getStreet ( args: { cityId ?: number ; streetName: string } ) : null | Street
```
a street object or null if not found
### `updateStreet`

```typescript
updateStreet ( args: { direction ?: string ; streetId: number } ) : void
```

---

# index.SDK.TurnClosures

---
title: SDK.TurnClosures class
source: classes/index.SDK.TurnClosures.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class TurnClosures

```typescript
addClosure (
  args: {
  description: string ;
  endDate: number ;
  isPermanent ?: boolean ;
  majorTrafficEventId ?: string ;
  startDate: number ;
  turnId: string ;
} ,
  ) : TurnClosure
```
Methods for dealing with TurnClosures.
## Methods
### `addClosure`

```typescript
addClosure (
  args: {
  description: string ;
  endDate: number ;
  isPermanent ?: boolean ;
  majorTrafficEventId ?: string ;
  startDate: number ;
  turnId: string ;
} ,
  ) : TurnClosure
```
The newly created turn closure object.
### `getAll`

```typescript
getAll () : TurnClosure []
```
an array of all the turn closures in the WME data model
### `getById`

```typescript
getById ( args: { turnClosureId: string } ) : null | TurnClosure
```
turn closure with id, or null if not found in the WME data model

---

# index.SDK.Turns

---
title: SDK.Turns class
source: classes/index.SDK.Turns.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Turns

```typescript
canEditTurnsThroughNode ( args: { nodeId: number } ) : boolean
```
Methods for dealing with Turns.
## Methods
### `canEditTurnsThroughNode`

```typescript
canEditTurnsThroughNode ( args: { nodeId: number } ) : boolean
```
true if all the segments going through the node allow connections to be edited.
### `createPathTurn`

```typescript
createPathTurn (
  args: { fromSegmentId: number ; isForward: boolean ; toSegmentId: number } ,
  ) : Turn
```
created path turn from the source segment to the target segment.
### `getAll`

```typescript
getAll () : Turn []
```
an array of all the turns in the WME data model
### `getById`

```typescript
getById ( args: { turnId: string } ) : null | Turn
```
turn with id, or null if not found in the WME data model
### `getTurnsFromSegment`

```typescript
getTurnsFromSegment ( args: { segmentId: number } ) : Turn []
```
all turns from the segment
### `getTurnsThroughNode`

```typescript
getTurnsThroughNode ( args: { nodeId: number } ) : Turn []
```
an array of all known turns through the node
### `getTurnsToSegment`

```typescript
getTurnsToSegment ( args: { segmentId: number } ) : Turn []
```
all turns to the segment
### `isTurnAllowed`

```typescript
isTurnAllowed (
  args: { fromSegmentId: number ; nodeId: number ; toSegmentId: number } ,
  ) : boolean
```
true if a turn is allowed
### `isTurnAllowedBySegmentDirections`

```typescript
isTurnAllowedBySegmentDirections (
  args: { fromSegmentId: number ; nodeId: number ; toSegmentId: number } ,
  ) : boolean
```
true if a turn is allowed
### `setSegmentTurnsLaneCount`

```typescript
setSegmentTurnsLaneCount (
  args: {
  laneCount: number ;
  laneDirection: SegmentLaneGuidanceDirection ;
  segmentId: number ;
} ,
  ) : void
```

### `setTurnLaneGuidance`

```typescript
setTurnLaneGuidance ( args: { laneIndexes: number [] ; turnId: string } ) : void
```

### `updateTurn`

```typescript
updateTurn (
  args: {
  isAllowed ?: boolean ;
  restrictions ?: TurnRestrictionData [] ;
  turnGuidance ?: null | TurnGuidance ;
  turnId: string ;
} ,
  ) : void
```

---

# index.SDK.Users

---
title: SDK.Users class
source: classes/index.SDK.Users.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Users

```typescript
getByUserName ( options: { userName: string } ) : null | User
```
Methods for dealing with Users.
## Methods
### `getByUserName`

```typescript
getByUserName ( options: { userName: string } ) : null | User
```
user with userName, or null if not found
### `getCurrentUser`

```typescript
getCurrentUser () : null | User
```
the currently logged in user or null if not logged in
### `getLocalizedUserProfileLink`

```typescript
getLocalizedUserProfileLink ( options: { userName: string } ) : string
```
a formatted link which includes the current locale for a users editor profile page
### `getUserProfile`

```typescript
getUserProfile ( options: { userName: string } ) : Promise < UserProfile >
```
a fetched user profile
### `getUserProfileLink`

```typescript
getUserProfileLink ( options: { userName: string } ) : string
```
a formatted link for a users editor profile page

---

# index.SDK.ValidationError

---
title: SDK.ValidationError class
source: classes/index.SDK.ValidationError.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class ValidationError

```typescript
new ValidationError ( message ?: string ) : ValidationError
```
This error indicates that invalid arguments were passed into SDK method.
## Constructors
## Properties
### **Readonly** `name`

```typescript
name: "ValidationError"
```
## Methods

---

# index.SDK.Venues

---
title: SDK.Venues class
source: classes/index.SDK.Venues.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Venues

```typescript
ChargingStation: ChargingStation = ...
```
Methods for dealing with Venues.
## Properties
### **Readonly** `ChargingStation`

```typescript
ChargingStation: ChargingStation = ...
```
### **Readonly** `ParkingLot`

```typescript
ParkingLot: ParkingLot = ...
```
## Methods
### `addVenue`

```typescript
addVenue ( args: { category: VenueCategoryId ; geometry: Point | Polygon } ) : number
```
id of the new venue
### `deleteImage`

```typescript
deleteImage ( args: { imageId: string ; venueId: string } ) : void
```

### `deleteVenue`

```typescript
deleteVenue ( args: { venueId: string } ) : void
```

### `getAddress`

```typescript
getAddress ( args: { venueId: string } ) : VenueAddress
```
an address of the venue with the provided id.
### `getAll`

```typescript
getAll () : Venue []
```
an array of all the venues in the WME data model
### `getAllVenueCategories`

```typescript
getAllVenueCategories () : VenueCategory []
```
all possible venue categories and their localised names.
### `getById`

```typescript
getById ( args: { venueId: string } ) : null | Venue
```
venue with id, or null if not found in the WME data model
### `getChargingStationBrands`

```typescript
getChargingStationBrands () : string []
```
a list of charging station brands
### `getGasStationBrands`

```typescript
getGasStationBrands () : string []
```
a list of gas stations brands
### `getParkingLotBrands`

```typescript
getParkingLotBrands () : string []
```
a list of parking lot brands
### `getParkingLotType`

```typescript
getParkingLotType ( args: { venueId: string } ) : ParkingType
```
parking lot type of the venue in case the venue is a parking lot, null othervise.
### `getVenueMainCategories`

```typescript
getVenueMainCategories () : VenueCategory []
```
a list of the venue main categories and their localised names.
### `getVenueSubCategories`

```typescript
getVenueSubCategories () : VenueSubCategory []
```
a list of the venue sub-categories, their main category id
and their localised names.
### `hasPermissions`

```typescript
hasPermissions ( args: { permission ?: VenuePermission ; venueId: string } ) : boolean
```
whether the current user has a permission for this venue or not.
### `replaceNavigationPoints`

```typescript
replaceNavigationPoints (
  args: { navigationPoints: Partial < NavigationPoint > [] ; venueId: string } ,
  ) : void
```

### `showVenueUpdateRequestDialog`

```typescript
showVenueUpdateRequestDialog ( args: { venueId: string } ) : void
```

### `updateAddress`

```typescript
updateAddress ( args: { addressData ?: VenueAddressData ; venueId: string } ) : void
```

### `updateVenue`

```typescript
updateVenue (
  args: {
  aliases ?: string [] ;
  brand ?: string ;
  categories ?: VenueCategoryId [] ;
  description ?: string ;
  geometry ?: Point | Polygon ;
  lockRank ?: number ;
  name ?: string ;
  openingHours ?: OpeningHour [] ;
  phone ?: string ;
  services ?: ServiceType [] ;
  url ?: string ;
  venueId: string ;
} ,
  ) : void
```

### `updateVenueIsResidential`

```typescript
updateVenueIsResidential (
  args: { isResidential: boolean ; venueId: string } ,
  ) : void
```

### `updateVenueUpdateRequest`

```typescript
updateVenueUpdateRequest (
  args: {
  isApproved: boolean ;
  venueId: string ;
  venueUpdateRequestId: string ;
} ,
  ) : void
```

---

# index.SDK.WMEError

---
title: SDK.WMEError class
source: classes/index.SDK.WMEError.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class WMEError

```typescript
new WMEError ( message ?: string ) : WMEError
```
This error indicates that the WME encountered an unexpected condition that
prevented it from fulfilling the request.
## Constructors
## Properties
### **Readonly** `name`

```typescript
name: "WMEError"
```
## Methods

---

# index.SDK.WmeSDK

---
title: SDK.WmeSDK class
source: classes/index.SDK.WmeSDK.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class WmeSDK

```typescript
Chat: Chat = ...
```
WME SDK container.
## Properties
### **Readonly** `Chat`

```typescript
Chat: Chat = ...
```
### **Readonly** `DataModel`

```typescript
DataModel: DataModel = ...
```
### **Readonly** `Editing`

```typescript
Editing: Editing = ...
```
### **Readonly** `Errors`

```typescript
Errors: {
  DataModelNotFoundError: typeof DataModelNotFoundError ;
  InvalidStateError: typeof InvalidStateError ;
  ValidationError: typeof ValidationError ;
  WMEError: typeof WMEError ;
}
```
### **Readonly** `Events`

```typescript
Events: SdkEventBus = ...
```
### **Readonly** `IssueTracker`

```typescript
IssueTracker: IssueTracker = ...
```
### **Readonly** `LayerSwitcher`

```typescript
LayerSwitcher: LayerSwitcher = ...
```
### **Readonly** `Map`

```typescript
Map: Map = ...
```
### **Readonly** `Settings`

```typescript
Settings: Settings = ...
```
### **Readonly** `Shortcuts`

```typescript
Shortcuts: Shortcuts = ...
```
### **Readonly** `Sidebar`

```typescript
Sidebar: Sidebar = ...
```
### **Readonly** `State`

```typescript
State: WmeState = ...
```
### **Readonly** `StreetView`

```typescript
StreetView: StreetView = ...
```
## Methods
### `getScriptId`

```typescript
getScriptId () : string
```
the script id this sdk instance was initialized with
### `getScriptName`

```typescript
getScriptName () : string
```
the script name this sdk instance was initialized with
### `getSDKVersion`

```typescript
getSDKVersion () : string
```
the current version of this SDK
### `getWMEBackEndVersion`

```typescript
getWMEBackEndVersion () : Promise < string >
```
the current version of the WME backend
### `getWMEVersion`

```typescript
getWMEVersion () : string
```
the current version of the WME frontend
### `isBetaEnvironment`

```typescript
isBetaEnvironment () : boolean
```
true if running in the WME beta environment

---

# index.SDK.WmeState

---
title: SDK.WmeState class
source: classes/index.SDK.WmeState.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class WmeState

```typescript
getManagedCountries () : Country []
```
Contains information about current state of the WME.
## Methods
### `getManagedCountries`

```typescript
getManagedCountries () : Country []
```
the list of the countries in the WME data model that are managed by the current user.
### `getUserInfo`

```typescript
getUserInfo () : null | UserSession
```
information about currently logged in user or null if user isn't logged in yet.
### `isInitialized`

```typescript
isInitialized () : boolean
```
true if WME initialized successfully.
### `isInitialMapDataLoaded`

```typescript
isInitialMapDataLoaded () : boolean
```
true if WME already fetched map data from the server.
### `isLoggedIn`

```typescript
isLoggedIn () : boolean
```
true if user logged in
### `isMapLoading`

```typescript
isMapLoading () : boolean
```
true if WME map is loading.
### `isReady`

```typescript
isReady () : boolean
```
true if WME already fetched map data and user logged in.

---

