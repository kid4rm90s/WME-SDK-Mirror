---
title: SDK.MapProblem interface
source: interfaces/index.SDK.MapProblem.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapProblem

```typescript
interface MapProblem {
  geometry: Point ;
  id: string ;
  isEditable: boolean ;
  isOpen: boolean ;
  isRead: boolean ;
  isStarred: boolean ;
  problemType: MapProblemType ;
  resolvedOn: null | number ;
  severity: IssueSeverity ;
}
```
## Properties
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: string
```
### `isEditable`

```typescript
isEditable: boolean
```
### `isOpen`

```typescript
isOpen: boolean
```
### `isRead`

```typescript
isRead: boolean
```
### `isStarred`

```typescript
isStarred: boolean
```
### `problemType`

```typescript
problemType: MapProblemType
```
### `resolvedOn`

```typescript
resolvedOn: null | number
```
### `severity`

```typescript
severity: IssueSeverity
```
