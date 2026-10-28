---
title: SDK.City interface
source: interfaces/index.SDK.City.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface City

```typescript
interface City {
  countryId: number | null ;
  geometry: Point ;
  id: number ;
  isEmpty: boolean ;
  modificationData: ModificationMetadata ;
  name: string | null ;
  stateId: number | null ;
}
```
## Properties
### `countryId`

```typescript
countryId: number | null
```
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
```
### `isEmpty`

```typescript
isEmpty: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string | null
```
### `stateId`

```typescript
stateId: number | null
```
