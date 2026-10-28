---
title: SDK.State interface
source: interfaces/index.SDK.State.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface State

```typescript
interface State {
  geometry: Polygon | MultiPolygon | null ;
  id: number ;
  modificationData: ModificationMetadata ;
  name: string ;
}
```
## Properties
### `geometry`

```typescript
geometry: Polygon | MultiPolygon | null
```
### `id`

```typescript
id: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```
