---
title: SDK.RoadClosure interface
source: interfaces/index.SDK.RoadClosure.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RoadClosure

```typescript
interface RoadClosure {
  description: null | string ;
  endDate: null | string ;
  id: string ;
  isForward: boolean ;
  isPermanent: boolean ;
  modificationData: ModificationMetadata ;
  segmentId: number ;
  startDate: null | string ;
  status: ClosureStatus ;
  trafficEventId: null | string ;
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
### `id`

```typescript
id: string
```
### `isForward`

```typescript
isForward: boolean
```
### `isPermanent`

```typescript
isPermanent: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `segmentId`

```typescript
segmentId: number
```
### `startDate`

```typescript
startDate: null | string
```
### `status`

```typescript
status: ClosureStatus
```
### `trafficEventId`

```typescript
trafficEventId: null | string
```
