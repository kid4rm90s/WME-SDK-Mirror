---
title: SDK.MultiPolygon interface
source: interfaces/index.SDK.MultiPolygon.html
created: 2026-07-08
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
