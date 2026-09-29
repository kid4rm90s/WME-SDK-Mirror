---
title: SDK.MajorTrafficEvent interface
source: interfaces/index.SDK.MajorTrafficEvent.html
created: 2026-09-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MajorTrafficEvent

```typescript
interface MajorTrafficEvent {
  category: MajorTrafficEventCategory | null ;
  cityId: number | null ;
  endDate: string | null ;
  id: string ;
  isPublished: boolean ;
  isReady: boolean ;
  lockRank: UserRank | null ;
  modificationData: ModificationMetadata ;
  names: LocalizedString [] ;
  startDate: string | null ;
}
```
## Properties
### `category`

```typescript
category: MajorTrafficEventCategory | null
```
### `cityId`

```typescript
cityId: number | null
```
### `endDate`

```typescript
endDate: string | null
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
lockRank: UserRank | null
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
startDate: string | null
```
