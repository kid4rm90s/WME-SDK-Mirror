---
title: getWmeSdk function
source: functions/index.getWmeSdk.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Function getWmeSdk

```typescript
getWmeSdk (
  options: {
  mode: "as ync" ;
  scriptId: string ;
  scriptName: string ;
  version ?: string ;
} ,
  ) : AsyncWmeSDK
```
Get a reference to the WME SDK. If preferred version not specified, returns the latest SDK.
Subsequent calls to this function with the same scriptId would return the same SDK instance.
Returnsa reference to the WME SDK (returnsAsyncWmeSDKif initialized withmode: 'async')ThrowsInvalidStateError if another instance of the SDK had been requested with a different version
