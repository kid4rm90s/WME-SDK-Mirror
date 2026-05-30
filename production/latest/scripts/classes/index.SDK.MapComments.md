---
title: SDK.MapComments class
source: classes/index.SDK.MapComments.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class MapComments

```typescript
addComment (
  args: {
  body: string ;
  endDate: number ;
  geometry: Point | Polygon ;
  subject: string ;
} ,
  ) : MapComment
```
Methods for dealing with MapComments.
## Methods
### `addComment`

```typescript
addComment (
  args: {
  body: string ;
  endDate: number ;
  geometry: Point | Polygon ;
  subject: string ;
} ,
  ) : MapComment
```
the created map comment.
### `deleteComment`

```typescript
deleteComment ( args: { mapCommentId: string } ) : null
```
null.
### `getAll`

```typescript
getAll () : MapComment []
```
an array of all the map comments in the WME data model
### `getById`

```typescript
getById ( args: { mapCommentId: string } ) : null | MapComment
```
map comment with id, or null if not found in the WME data model
### `updateComment`

```typescript
updateComment (
  args: {
  body ?: string ;
  endDate ?: null | number ;
  geometry ?: Point | Polygon ;
  mapCommentId: string ;
  subject ?: string ;
} ,
  ) : MapComment
```
the updated map comment.
