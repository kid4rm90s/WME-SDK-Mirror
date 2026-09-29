---
title: SDK.VenueUpdateRequest interface
source: interfaces/index.SDK.VenueUpdateRequest.html
created: 2026-09-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VenueUpdateRequest

```typescript
interface VenueUpdateRequest {
  changedFields ?: ChangedField [] ;
  createdBy: string | null ;
  dateAdded: number ;
  id: string | number | null ;
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
createdBy: string | null
```
### `dateAdded`

```typescript
dateAdded: number
```
### `id`

```typescript
id: string | number | null
```
### `subject`

```typescript
subject: PLACE_UPDATE_SUBJECT
```
### `updateType`

```typescript
updateType: PlaceUpdateType
```
