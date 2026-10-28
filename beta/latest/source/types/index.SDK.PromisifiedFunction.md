---
title: SDK.PromisifiedFunction type
source: types/index.SDK.PromisifiedFunction.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PromisifiedFunction<T>

```typescript
PromisifiedFunction: ReturnType < T > extends Promise < unknown >
  ? T
  : ( ... args: Parameters < T > ) = > Promise < Awaited < ReturnType < T > > >
```
