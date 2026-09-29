---
title: SDK.MapUpdateRequest interface
source: interfaces/index.SDK.MapUpdateRequest.html
created: 2026-09-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface MapUpdateRequest

```typescript
interface MapUpdateRequest {
  description: string | null ;
  geometry: Point ;
  id: number ;
  isEditable: boolean ;
  isOpen: boolean ;
  isRead: boolean ;
  isStarred: boolean ;
  reportedOn: number ;
  resolutionState: string | null ;
  resolvedBy: string | null ;
  resolvedOn: number | null ;
  severity: IssueSeverity ;
  source: UpdateRequestSource ;
  updateRequestType: UpdateRequestType ;
  userPreferences: UpdateRequestUserPreferences ;
}
```
## Properties
### `description`

```typescript
description: string | null
```
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
resolutionState: string | null
```
### `resolvedBy`

```typescript
resolvedBy: string | null
```
### `resolvedOn`

```typescript
resolvedOn: number | null
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
