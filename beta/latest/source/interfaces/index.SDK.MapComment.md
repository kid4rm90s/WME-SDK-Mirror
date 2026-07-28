---
title: SDK.MapComment interface
source: interfaces/index.SDK.MapComment.html
created: 2026-07-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapComment

```typescript
interface MapComment {
  body: string ;
  conversation: ConversationElement [] ;
  endDate: null | string ;
  geometry: Point | Polygon ;
  id: string ;
  isFollowing: boolean ;
  isPoint: boolean ;
  lockRank: UserRank ;
  modificationData: ModificationMetadata ;
  subject: string ;
}
```
## Properties
### `body`

```typescript
body: string
```
### `conversation`

```typescript
conversation: ConversationElement []
```
### `endDate`

```typescript
endDate: null | string
```
### `geometry`

```typescript
geometry: Point | Polygon
```
### `id`

```typescript
id: string
```
### `isFollowing`

```typescript
isFollowing: boolean
```
### `isPoint`

```typescript
isPoint: boolean
```
### `lockRank`

```typescript
lockRank: UserRank
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `subject`

```typescript
subject: string
```
