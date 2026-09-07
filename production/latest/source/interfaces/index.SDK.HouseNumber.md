---
title: SDK.HouseNumber interface
source: interfaces/index.SDK.HouseNumber.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface HouseNumber

```typescript
interface HouseNumber {
  fractionPoint: null | Point ;
  geometry: Point ;
  id: string ;
  isForced: boolean ;
  number: string ;
  segmentId: number ;
  updatedBy: null | string ;
}
```
Represents a house number associated with a segment.
It provides information about the house number itself, its location, and its relation to the segment.
## Properties
### `fractionPoint`

```typescript
fractionPoint: null | Point
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: string
```
### `isForced`

```typescript
isForced: boolean
```
### `number`

```typescript
number: string
```
### `segmentId`

```typescript
segmentId: number
```
### `updatedBy`

```typescript
updatedBy: null | string
```
