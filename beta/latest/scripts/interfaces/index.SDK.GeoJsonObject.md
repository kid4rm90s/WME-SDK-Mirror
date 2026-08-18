---
title: SDK.GeoJsonObject interface
source: interfaces/index.SDK.GeoJsonObject.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface GeoJsonObject

```typescript
interface GeoJsonObject {
  bbox ?: BBox ;
  type: 
  | "Point"
  | "Polygon"
  | "MultiPolygon"
  | "LineString"
  | "MultiPoint"
  | "MultiLineString"
  | "GeometryCollection"
  | "FeatureCollection"
  | "Feature" ;
}
```
The base GeoJSON object.https://tools.ietf.org/html/rfc7946#section-3The GeoJSON specification also allows foreign members
(https://tools.ietf.org/html/rfc7946#section-6.1)
Developers should use "&" type in TypeScript or extend the interface
to add these foreign members.
## Properties
