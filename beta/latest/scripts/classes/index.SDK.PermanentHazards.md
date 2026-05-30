---
title: SDK.PermanentHazards class
source: classes/index.SDK.PermanentHazards.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class PermanentHazards

```typescript
getAllCameras () : Camera []
```
Methods for dealing with PermanentHazards.
## Methods
### `getAllCameras`

```typescript
getAllCameras () : Camera []
```
an array of all the cameras in the WME data model
### `getCameraById`

```typescript
getCameraById ( args: { cameraId: number } ) : null | Camera
```
camera with id, or null if not found in the WME data model
