---
title: SDK.MapUpdateRequests class
source: classes/index.SDK.MapUpdateRequests.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class MapUpdateRequests

```typescript
addComment (
  args: { mapUpdateRequestId: number ; text: string } ,
  ) : Promise < ConversationElement >
```
Methods for dealing with MapUpdateRequests.
## Methods
### `addComment`

```typescript
addComment (
  args: { mapUpdateRequestId: number ; text: string } ,
  ) : Promise < ConversationElement >
```
A promise that resolves to a created conversation element representing the comment.
### `getAll`

```typescript
getAll () : MapUpdateRequest []
```
an array of all the map update requests in the WME data model
### `getById`

```typescript
getById ( args: { mapUpdateRequestId: number } ) : null | MapUpdateRequest
```
map update request with id, or null if not found in the WME data model
### `getUpdateRequestDetails`

```typescript
getUpdateRequestDetails (
  args: { mapUpdateRequestId: number } ,
  ) : Promise < null | UpdateRequestDetails >
```
map update request details. If details are not present in the WME data model, they will be fetched.
Returns null if not found in the WME data model.
### `updateResolutionState`

```typescript
updateResolutionState (
  args: {
  mapUpdateRequestId: number ;
  resolutionState: UpdateableMapProblemState ;
} ,
  ) : void
```
