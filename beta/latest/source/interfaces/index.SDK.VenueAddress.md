---
title: SDK.VenueAddress interface
source: interfaces/index.SDK.VenueAddress.html
created: 2026-09-30
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
