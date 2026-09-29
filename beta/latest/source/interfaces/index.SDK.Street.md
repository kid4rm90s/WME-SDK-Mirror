---
title: SDK.Street interface
source: interfaces/index.SDK.Street.html
created: 2026-09-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Street

```typescript
interface Street {
  cityId: number | null ;
  direction: string | null ;
  englishName: string | null ;
  id: number ;
  isEmpty: boolean ;
  modificationData: ModificationMetadata ;
  name: string | null ;
  signText: string | null ;
  signType: number | null ;
}
```
## Properties
### `cityId`

```typescript
cityId: number | null
```
### `direction`

```typescript
direction: string | null
```
### `englishName`

```typescript
englishName: string | null
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
### `signText`

```typescript
signText: string | null
```
### `signType`

```typescript
signType: number | null
```
