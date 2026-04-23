---
title: SDK.Selection type
source: types/index.SDK.Selection.html
created: 2026-04-23
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias Selection

```typescript
Selection: 
  | { ids: number [] ; objectType: typeof SEGMENT }
  | { ids: string [] ; objectType: typeof VENUE }
  | { ids: number [] ; objectType: typeof BIG_JUNCTION }
  | { ids: number [] ; objectType: typeof CITY }
  | { ids: string [] ; objectType: typeof MAP_COMMENT }
  | { ids: number [] ; objectType: typeof NODE }
  | { ids: number [] ; objectType: typeof PERMANENT_HAZARD }
  | { ids: number [] ; objectType: typeof RESTRICTED_DRIVING_AREA }
  | { ids: number [] ; objectType: typeof SEGMENT_SUGGESTION }
```
