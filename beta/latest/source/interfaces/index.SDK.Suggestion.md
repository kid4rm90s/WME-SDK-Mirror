---
title: SDK.Suggestion interface
source: interfaces/index.SDK.Suggestion.html
created: 2026-08-05
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Suggestion

```typescript
interface Suggestion {
  createdOn: null | number ;
  edits: SuggestionEntityEdit [] ;
  id: string ;
  resolutionData: SuggestionResolution [] ;
}
```
Represents a suggestion for an edit.
## Properties
### `createdOn`

```typescript
createdOn: null | number
```
### `edits`

```typescript
edits: SuggestionEntityEdit []
```
### `id`

```typescript
id: string
```
### `resolutionData`

```typescript
resolutionData: SuggestionResolution []
```
