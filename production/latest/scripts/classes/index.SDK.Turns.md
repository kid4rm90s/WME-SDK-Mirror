---
title: SDK.Turns class
source: classes/index.SDK.Turns.html
created: 2026-04-23
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Turns

```typescript
canEditTurnsThroughNode ( args: { nodeId: number } ) : boolean
```
Methods for dealing with Turns.
## Methods
### `canEditTurnsThroughNode`

```typescript
canEditTurnsThroughNode ( args: { nodeId: number } ) : boolean
```
true if all the segments going through the node allow connections to be edited.
### `createPathTurn`

```typescript
createPathTurn (
  args: { fromSegmentId: number ; isForward: boolean ; toSegmentId: number } ,
  ) : Turn
```
created path turn from the source segment to the target segment.
### `getAll`

```typescript
getAll () : Turn []
```
an array of all the turns in the WME data model
### `getById`

```typescript
getById ( args: { turnId: string } ) : null | Turn
```
turn with id, or null if not found in the WME data model
### `getTurnsFromSegment`

```typescript
getTurnsFromSegment ( args: { segmentId: number } ) : Turn []
```
all turns from the segment
### `getTurnsThroughNode`

```typescript
getTurnsThroughNode ( args: { nodeId: number } ) : Turn []
```
an array of all known turns through the node
### `getTurnsToSegment`

```typescript
getTurnsToSegment ( args: { segmentId: number } ) : Turn []
```
all turns to the segment
### `isTurnAllowed`

```typescript
isTurnAllowed (
  args: { fromSegmentId: number ; nodeId: number ; toSegmentId: number } ,
  ) : boolean
```
true if a turn is allowed
### `isTurnAllowedBySegmentDirections`

```typescript
isTurnAllowedBySegmentDirections (
  args: { fromSegmentId: number ; nodeId: number ; toSegmentId: number } ,
  ) : boolean
```
true if a turn is allowed
### `setSegmentTurnsLaneCount`

```typescript
setSegmentTurnsLaneCount (
  args: {
  laneCount: number ;
  laneDirection: SegmentLaneGuidanceDirection ;
  segmentId: number ;
} ,
  ) : void
```

### `setTurnLaneGuidance`

```typescript
setTurnLaneGuidance ( args: { laneIndexes: number [] ; turnId: string } ) : void
```

### `updateTurn`

```typescript
updateTurn ( args: { isAllowed ?: boolean ; turnId: string } ) : void
```
