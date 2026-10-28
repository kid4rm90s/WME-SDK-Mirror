---
title: SDK.PromisifiedModule type
source: types/index.SDK.PromisifiedModule.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Type Alias PromisifiedModule<T>

```typescript
PromisifiedModule: {
  [ K in keyof T ] : T [ K ] extends SdkEventBus
  ? T [ K ]
  : T [ K ] extends AnyFunction
  ? PromisifiedFunction < T [ K ] >
  : T [ K ] extends SdkModule ? PromisifiedModule < T [ K ] > : T [ K ]
  }
```
