---
title: SDK.SuggestionAttributeChange interface
source: interfaces/index.SDK.SuggestionAttributeChange.html
created: 2026-06-10
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SuggestionAttributeChange<T>

```typescript
interface SuggestionAttributeChange < T = unknown > {
  id: string ;
  name: string ;
  newValue: T ;
  objectType: ObjectType ;
  oldValue: T ;
  timestamp: null | number ;
}
```
Represents a single attribute change in an edit suggestion change.
## Properties
### `id`

```typescript
id: string
```
### `name`

```typescript
name: string
```
### `newValue`

```typescript
newValue: T
```
### `objectType`

```typescript
objectType: ObjectType
```
### `oldValue`

```typescript
oldValue: T
```
### `timestamp`

```typescript
timestamp: null | number
```
