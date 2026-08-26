---
title: SDK.Turn interface
source: interfaces/index.SDK.Turn.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Turn

```typescript
interface Turn {
  fromSegmentFwd: boolean ;
  fromSegmentId: number ;
  hasCustomTTS: boolean ;
  hasShieldsPopulated: boolean ;
  hasTowardsGuidance: boolean ;
  hasTurnGuidance: boolean ;
  hasVisualInstruction: boolean ;
  id: string ;
  instructionOpCode: null | InstructionOpCode ;
  isAllowed: boolean ;
  isJunctionBoxTurn: boolean ;
  isPathTurn: boolean ;
  isUTurn: boolean ;
  lanes: null | TurnLanes ;
  restrictions: BaseRestriction [] ;
  segmentPath: number [] ;
  toSegmentFwd: boolean ;
  toSegmentId: number ;
  turnGuidance: null | TurnGuidance ;
}
```
## Properties
### `fromSegmentFwd`

```typescript
fromSegmentFwd: boolean
```
### `fromSegmentId`

```typescript
fromSegmentId: number
```
### `hasCustomTTS`

```typescript
hasCustomTTS: boolean
```
### `hasShieldsPopulated`

```typescript
hasShieldsPopulated: boolean
```
### `hasTowardsGuidance`

```typescript
hasTowardsGuidance: boolean
```
### `hasTurnGuidance`

```typescript
hasTurnGuidance: boolean
```
### `hasVisualInstruction`

```typescript
hasVisualInstruction: boolean
```
### `id`

```typescript
id: string
```
### `instructionOpCode`

```typescript
instructionOpCode: null | InstructionOpCode
```
### `isAllowed`

```typescript
isAllowed: boolean
```
### `isJunctionBoxTurn`

```typescript
isJunctionBoxTurn: boolean
```
### `isPathTurn`

```typescript
isPathTurn: boolean
```
### `isUTurn`

```typescript
isUTurn: boolean
```
### `lanes`

```typescript
lanes: null | TurnLanes
```
### `restrictions`

```typescript
restrictions: BaseRestriction []
```
### `segmentPath`

```typescript
segmentPath: number []
```
### `toSegmentFwd`

```typescript
toSegmentFwd: boolean
```
### `toSegmentId`

```typescript
toSegmentId: number
```
### `turnGuidance`

```typescript
turnGuidance: null | TurnGuidance
```
