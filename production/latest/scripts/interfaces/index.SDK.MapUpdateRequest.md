---
title: SDK.MapUpdateRequest interface
source: interfaces/index.SDK.MapUpdateRequest.html
created: 2026-06-10
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapUpdateRequest

```typescript
interface MapUpdateRequest {
  geometry: Point ;
  id: number ;
  isEditable: boolean ;
  isOpen: boolean ;
  isRead: boolean ;
  isStarred: boolean ;
  reportedOn: number ;
  resolutionState: null | string ;
  resolvedOn: null | number ;
  severity: IssueSeverity ;
  source: UpdateRequestSource ;
  updateRequestType: UpdateRequestType ;
  userPreferences: UpdateRequestUserPreferences ;
}
```
## Properties
### `geometry`

```typescript
geometry: Point
```
### `id`

```typescript
id: number
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
### `reportedOn`

```typescript
reportedOn: number
```
### `resolutionState`

```typescript
resolutionState: null | string
```
### `resolvedOn`

```typescript
resolvedOn: null | number
```
### `severity`

```typescript
severity: IssueSeverity
```
### `source`

```typescript
source: UpdateRequestSource
```
### `updateRequestType`

```typescript
updateRequestType: UpdateRequestType
```
### `userPreferences`

```typescript
userPreferences: UpdateRequestUserPreferences
```
