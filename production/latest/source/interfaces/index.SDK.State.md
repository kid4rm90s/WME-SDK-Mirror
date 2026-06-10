---
title: SDK.State interface
source: interfaces/index.SDK.State.html
created: 2026-06-10
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface State

```typescript
interface State {
  geometry: null | Polygon | MultiPolygon ;
  id: number ;
  modificationData: ModificationMetadata ;
  name: string ;
}
```
## Properties
### `geometry`

```typescript
geometry: null | Polygon | MultiPolygon
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
