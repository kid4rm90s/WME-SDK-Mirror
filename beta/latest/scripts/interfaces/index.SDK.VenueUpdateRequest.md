---
title: SDK.VenueUpdateRequest interface
source: interfaces/index.SDK.VenueUpdateRequest.html
created: 2026-08-05
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueUpdateRequest

```typescript
interface VenueUpdateRequest {
  changedFields ?: ChangedField [] ;
  createdBy: null | string ;
  dateAdded: number ;
  id: null | string | number ;
  subject: PLACE_UPDATE_SUBJECT ;
  updateType: PlaceUpdateType ;
}
```
## Properties
### **Optional** `changedFields`

```typescript
changedFields ?: ChangedField []
```
### `createdBy`

```typescript
createdBy: null | string
```
### `dateAdded`

```typescript
dateAdded: number
```
### `id`

```typescript
id: null | string | number
```
### `subject`

```typescript
subject: PLACE_UPDATE_SUBJECT
```
### `updateType`

```typescript
updateType: PlaceUpdateType
```
