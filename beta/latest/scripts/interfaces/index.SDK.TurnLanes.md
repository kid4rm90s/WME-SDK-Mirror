---
title: SDK.TurnLanes interface
source: interfaces/index.SDK.TurnLanes.html
created: 2026-09-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnLanes

```typescript
interface TurnLanes {
  angleOverride: number | null ;
  arrowAngle: number | null ;
  fromLaneIndex: number ;
  guidanceMode: LaneGuidanceMode ;
  instructionStrategy: LaneInstructionStrategy ;
  toLaneIndex: number ;
}
```
## Properties
### `angleOverride`

```typescript
angleOverride: number | null
```
### `arrowAngle`

```typescript
arrowAngle: number | null
```
### `fromLaneIndex`

```typescript
fromLaneIndex: number
```
### `guidanceMode`

```typescript
guidanceMode: LaneGuidanceMode
```
### `instructionStrategy`

```typescript
instructionStrategy: LaneInstructionStrategy
```
### `toLaneIndex`

```typescript
toLaneIndex: number
```
