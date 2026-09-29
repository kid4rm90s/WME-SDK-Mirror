---
title: SDK.SegmentAddress interface
source: interfaces/index.SDK.SegmentAddress.html
created: 2026-09-30
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
