---
title: SDK.SegmentSuggestion interface
source: interfaces/index.SDK.SegmentSuggestion.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SegmentSuggestion

```typescript
interface SegmentSuggestion {
  geometry: LineString ;
  id: number ;
  segmentId: number | null ;
  source: SegmentSuggestionSource ;
  status: SegmentSuggestionStatus ;
  streetName: string | null ;
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
segmentId: number | null
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
streetName: string | null
```
