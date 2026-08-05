---
title: SDK.FeatureStyle interface
source: interfaces/index.SDK.FeatureStyle.html
created: 2026-08-05
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
  externalGraphic ?: null | string ;
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
  | "solid"
  | "dot"
  | "dash"
  | "dashdot"
  | "longdash"
  | "longdashdot" ;
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
