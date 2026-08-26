---
title: SDK.VenueAddressData type
source: types/index.SDK.VenueAddressData.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias VenueAddressData

```typescript
VenueAddressData: 
  | AddressRawComponents & { houseNumber ?: string ; streetId ?: never }
  | ExcludeRawFields & { houseNumber ?: string ; streetId ?: number }
```
