---
title: SDK.CallSite interface
source: interfaces/index.SDK.CallSite.html
created: 2026-07-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface CallSite

```typescript
interface CallSite {
  getColumnNumber () : null | number ;
  getEnclosingColumnNumber () : null | number ;
  getEnclosingLineNumber () : null | number ;
  getEvalOrigin () : undefined | string ;
  getFileName () : null | string ;
  getFunction () : undefined | Function ;
  getFunctionName () : null | string ;
  getLineNumber () : null | number ;
  getMethodName () : null | string ;
  getPosition () : number ;
  getPromiseIndex () : null | number ;
  getScriptHash () : string ;
  getScriptNameOrSourceURL () : null | string ;
  getThis () : unknown ;
  getTypeName () : null | string ;
  isAsync () : boolean ;
  isConstructor () : boolean ;
  isEval () : boolean ;
  isNative () : boolean ;
  isPromiseAll () : boolean ;
  isToplevel () : boolean ;
}
```
## Methods
