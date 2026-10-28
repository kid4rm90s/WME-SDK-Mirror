---
title: SDK.SuggestionResolution interface
source: interfaces/index.SDK.SuggestionResolution.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SuggestionResolution

```typescript
interface SuggestionResolution {
  createdBy: string | null ;
  createdOn: number ;
  rejectionReason: SuggestionResolutionRejectionReason | null ;
  resolution: SuggestionResolutionStatus ;
}
```
Represents the resolution details for a suggestion.
## Properties
### `createdBy`

```typescript
createdBy: string | null
```
### `createdOn`

```typescript
createdOn: number
```
### `rejectionReason`

```typescript
rejectionReason: SuggestionResolutionRejectionReason | null
```
### `resolution`

```typescript
resolution: SuggestionResolutionStatus
```
