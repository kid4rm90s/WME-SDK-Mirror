---
title: SDK.SegmentSuggestions class
source: classes/index.SDK.SegmentSuggestions.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class SegmentSuggestions

```typescript
getAll () : SegmentSuggestion []
```
Methods for dealing with SegmentSuggestions.
## Methods
### `getAll`

```typescript
getAll () : SegmentSuggestion []
```
an array of all the segment suggestions in the WME data model
### `getById`

```typescript
getById ( args: { segmentSuggestionId: number } ) : null | SegmentSuggestion
```
segment suggestion with id, or null if not found in the WME data model
