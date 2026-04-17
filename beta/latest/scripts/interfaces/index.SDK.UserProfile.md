---
title: SDK.UserProfile interface
source: interfaces/index.SDK.UserProfile.html
created: 2026-04-17
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UserProfile

```typescript
interface UserProfile {
  dailyEditCount: number [] ;
  editCountByType: {
  mapProblems: number ;
  placeUpdateRequests: number ;
  segmentHouseNumbers: number ;
  segments: number ;
  updateRequests: number ;
  venues: number ;
} ;
  totalEditCount: number ;
}
```
## Properties
### `dailyEditCount`

```typescript
dailyEditCount: number []
```
### `editCountByType`

```typescript
editCountByType: {
  mapProblems: number ;
  placeUpdateRequests: number ;
  segmentHouseNumbers: number ;
  segments: number ;
  updateRequests: number ;
  venues: number ;
}
```
### `totalEditCount`

```typescript
totalEditCount: number
```
