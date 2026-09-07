---
title: SDK.MajorTrafficEvent interface
source: interfaces/index.SDK.MajorTrafficEvent.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MajorTrafficEvent

```typescript
interface MajorTrafficEvent {
  category: null | MajorTrafficEventCategory ;
  cityId: null | number ;
  endDate: null | string ;
  id: string ;
  isPublished: boolean ;
  isReady: boolean ;
  lockRank: null | UserRank ;
  modificationData: ModificationMetadata ;
  names: LocalizedString [] ;
  startDate: null | string ;
}
```
## Properties
### `category`

```typescript
category: null | MajorTrafficEventCategory
```
### `cityId`

```typescript
cityId: null | number
```
### `endDate`

```typescript
endDate: null | string
```
### `id`

```typescript
id: string
```
### `isPublished`

```typescript
isPublished: boolean
```
### `isReady`

```typescript
isReady: boolean
```
### `lockRank`

```typescript
lockRank: null | UserRank
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `names`

```typescript
names: LocalizedString []
```
### `startDate`

```typescript
startDate: null | string
```
