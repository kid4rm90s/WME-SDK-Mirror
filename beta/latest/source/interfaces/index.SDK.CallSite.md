---
title: SDK.CallSite interface
source: interfaces/index.SDK.CallSite.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface CallSite

```typescript
interface CallSite {
  getColumnNumber () : number | null ;
  getEnclosingColumnNumber () : number | null ;
  getEnclosingLineNumber () : number | null ;
  getEvalOrigin () : string | undefined ;
  getFileName () : string | null ;
  getFunction () : Function | undefined ;
  getFunctionName () : string | null ;
  getLineNumber () : number | null ;
  getMethodName () : string | null ;
  getPosition () : number ;
  getPromiseIndex () : number | null ;
  getScriptHash () : string ;
  getScriptNameOrSourceURL () : string | null ;
  getThis () : unknown ;
  getTypeName () : string | null ;
  isAsync () : boolean ;
  isConstructor () : boolean ;
  isEval () : boolean ;
  isNative () : boolean ;
  isPromiseAll () : boolean ;
  isToplevel () : boolean ;
}
```
## Methods
