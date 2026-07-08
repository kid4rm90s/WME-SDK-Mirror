---
title: SDK.EditSuggestion interface
source: interfaces/index.SDK.EditSuggestion.html
created: 2026-07-08
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface EditSuggestion

```typescript
interface EditSuggestion {
  bbox: BBox ;
  id: string ;
  isRead: boolean ;
  isStarred: boolean ;
  modificationData: ModificationMetadata ;
  source: EditSuggestionSource ;
  status: EditSuggestionStatus ;
  suggestions: Suggestion [] ;
}
```
Represents an edit suggestion, potentially containing multiple individual suggestions.
## Properties
### `bbox`

```typescript
bbox: BBox
```
### `id`

```typescript
id: string
```
### `isRead`

```typescript
isRead: boolean
```
### `isStarred`

```typescript
isStarred: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `source`

```typescript
source: EditSuggestionSource
```
### `status`

```typescript
status: EditSuggestionStatus
```
### `suggestions`

```typescript
suggestions: Suggestion []
```
