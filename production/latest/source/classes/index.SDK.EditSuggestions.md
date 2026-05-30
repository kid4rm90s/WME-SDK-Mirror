---
title: SDK.EditSuggestions class
source: classes/index.SDK.EditSuggestions.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class EditSuggestions

```typescript
getAll () : EditSuggestion []
```
Methods for dealing with EditSuggestions.
## Methods
### `getAll`

```typescript
getAll () : EditSuggestion []
```
an array of all the edit suggestions in the WME data model
### `getById`

```typescript
getById ( args: { editSuggestionId: string } ) : null | EditSuggestion
```
edit suggestion with id, or null if not found in the WME data model
### `getEditSuggestionChanges`

```typescript
getEditSuggestionChanges (
  args: { editSuggestionId: string } ,
  ) : EditSuggestionChange []
```
an array of edit suggestion changes
