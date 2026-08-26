---
title: SDK.TileLayerOptions interface
source: interfaces/index.SDK.TileLayerOptions.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TileLayerOptions

```typescript
interface TileLayerOptions {
  tileHeight: number ;
  tileWidth: number ;
  url: {
  fileName: string ;
  params ?: Record < string , unknown > ;
  servers: string [] ;
} ;
}
```
#### Members
| Name | Type/Value | Tags |
|------|------------|------|
| fileName | string |  |
| params | string | Optional |
| servers | string |  |
## Properties
### `tileHeight`

```typescript
tileHeight: number
```
### `tileWidth`

```typescript
tileWidth: number
```
### `url`

```typescript
url: { fileName: string ; params ?: Record < string , unknown > ; servers: string [] }
```
