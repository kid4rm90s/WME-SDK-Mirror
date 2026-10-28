---
title: SDK.RoadClosure interface
source: interfaces/index.SDK.RoadClosure.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface RoadClosure

```typescript
interface RoadClosure {
  attributions: RoadClosureAttribution [] ;
  description: string | null ;
  endDate: string | null ;
  id: string ;
  isForward: boolean ;
  isPermanent: boolean ;
  modificationData: ModificationMetadata ;
  segmentId: number ;
  startDate: string | null ;
  status: ClosureStatus ;
  trafficEventId: string | null ;
}
```
## Properties
### `attributions`

```typescript
attributions: RoadClosureAttribution []
```
### `description`

```typescript
description: string | null
```
### `endDate`

```typescript
endDate: string | null
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
startDate: string | null
```
### `status`

```typescript
status: ClosureStatus
```
### `trafficEventId`

```typescript
trafficEventId: string | null
```
