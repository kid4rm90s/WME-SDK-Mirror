---
title: SDK.StreetView class
source: classes/index.SDK.StreetView.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class StreetView

```typescript
close () : void
```
Methods for dealing with Street View.
## Methods
### `close`

```typescript
close () : void
```

### `isActive`

```typescript
isActive () : boolean
```
true if the street view pane is active
### `open`

```typescript
open ( args: { lonLat: LonLat ; radius ?: number } ) : Promise < void >
```
