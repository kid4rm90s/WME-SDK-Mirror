---
title: SDK.SegmentAddressData type
source: types/index.SDK.SegmentAddressData.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias SegmentAddressData

```typescript
SegmentAddressData: 
  | AddressRawComponents & {
  alternateStreetIds ?: number [] ;
  primaryStreetId ?: never ;
}
  | ExcludeRawFields & {
  alternateStreetIds ?: number [] ;
  primaryStreetId ?: number ;
}
```
