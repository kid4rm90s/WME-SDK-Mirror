---
title: SDK.Turn interface
source: interfaces/index.SDK.Turn.html
created: 2026-09-30
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
  instructionOpCode: InstructionOpCode | null ;
  isAllowed: boolean ;
  isJunctionBoxTurn: boolean ;
  isPathTurn: boolean ;
  isUTurn: boolean ;
  lanes: TurnLanes | null ;
  restrictions: BaseRestriction [] ;
  segmentPath: number [] ;
  toSegmentFwd: boolean ;
  toSegmentId: number ;
  turnGuidance: TurnGuidance | null ;
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
instructionOpCode: InstructionOpCode | null
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
lanes: TurnLanes | null
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
turnGuidance: TurnGuidance | null
```
