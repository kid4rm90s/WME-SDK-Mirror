---
title: SDK.TurnClosure interface
source: interfaces/index.SDK.TurnClosure.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnClosure

```typescript
interface TurnClosure {
  description: null | string ;
  endDate: null | string ;
  fromSegmentId: number ;
  id: string ;
  isPermanent: boolean ;
  majorTrafficEventId: null | string ;
  modificationData: ModificationMetadata ;
  startDate: null | string ;
  status: ClosureStatus ;
  toSegmentId: number ;
}
```
## Properties
### `description`

```typescript
description: null | string
```
### `endDate`

```typescript
endDate: null | string
```
### `fromSegmentId`

```typescript
fromSegmentId: number
```
### `id`

```typescript
id: string
```
### `isPermanent`

```typescript
isPermanent: boolean
```
### `majorTrafficEventId`

```typescript
majorTrafficEventId: null | string
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `startDate`

```typescript
startDate: null | string
```
### `status`

```typescript
status: ClosureStatus
```
### `toSegmentId`

```typescript
toSegmentId: number
```
