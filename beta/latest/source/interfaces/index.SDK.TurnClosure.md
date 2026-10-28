---
title: SDK.TurnClosure interface
source: interfaces/index.SDK.TurnClosure.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnClosure

```typescript
interface TurnClosure {
  description: string | null ;
  endDate: string | null ;
  fromSegmentId: number ;
  id: string ;
  isPermanent: boolean ;
  majorTrafficEventId: string | null ;
  modificationData: ModificationMetadata ;
  startDate: string | null ;
  status: ClosureStatus ;
  toSegmentId: number ;
}
```
## Properties
### `description`

```typescript
description: string | null
```
### `endDate`

```typescript
endDate: string | null
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
majorTrafficEventId: string | null
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `startDate`

```typescript
startDate: string | null
```
### `status`

```typescript
status: ClosureStatus
```
### `toSegmentId`

```typescript
toSegmentId: number
```
