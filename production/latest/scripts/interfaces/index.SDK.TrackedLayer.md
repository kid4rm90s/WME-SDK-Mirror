---
title: SDK.TrackedLayer interface
source: interfaces/index.SDK.TrackedLayer.html
created: 2026-04-22
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
