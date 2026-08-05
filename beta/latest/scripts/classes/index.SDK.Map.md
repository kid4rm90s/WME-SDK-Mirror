---
title: SDK.Map class
source: classes/index.SDK.Map.html
created: 2026-08-05
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
