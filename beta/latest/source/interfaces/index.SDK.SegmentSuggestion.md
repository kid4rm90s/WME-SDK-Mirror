---
title: SDK.SegmentSuggestion interface
source: interfaces/index.SDK.SegmentSuggestion.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentSuggestion

```typescript
interface SegmentSuggestion {
  geometry: LineString ;
  id: number ;
  segmentId: null | number ;
  source: SegmentSuggestionSource ;
  status: SegmentSuggestionStatus ;
  streetName: null | string ;
}
```
## Properties
### `geometry`

```typescript
geometry: LineString
```
### `id`

```typescript
id: number
```
### `segmentId`

```typescript
segmentId: null | number
```
### `source`

```typescript
source: SegmentSuggestionSource
```
### `status`

```typescript
status: SegmentSuggestionStatus
```
### `streetName`

```typescript
streetName: null | string
```
