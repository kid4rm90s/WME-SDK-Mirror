---
title: SDK.PermanentHazards class
source: classes/index.SDK.PermanentHazards.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class PermanentHazards

```typescript
getAll () : PermanentHazard []
```
Methods for dealing with PermanentHazards.
## Methods
### `getAll`

```typescript
getAll () : PermanentHazard []
```
an array of all the permanent hazards in the WME data model
### `getAllCameras`

```typescript
getAllCameras () : Camera []
```
an array of all the cameras in the WME data model
### `getById`

```typescript
getById ( args: { hazardId: number } ) : null | PermanentHazard
```
permanent hazard with id, or null if not found in the WME data model
### `getCameraById`

```typescript
getCameraById ( args: { cameraId: number } ) : null | Camera
```
camera with id, or null if not found in the WME data model
