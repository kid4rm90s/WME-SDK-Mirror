---
title: SDK.TurnGuidance interface
source: interfaces/index.SDK.TurnGuidance.html
created: 2026-09-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnGuidance

```typescript
interface TurnGuidance {
  exitSigns: ExitSign [] ;
  towards: ( string | RoadShield ) [] ;
  tts: string | null ;
  visualInstruction: ( string | RoadShield ) [] ;
}
```
## Properties
### `exitSigns`

```typescript
exitSigns: ExitSign []
```
### `towards`

```typescript
towards: ( string | RoadShield ) []
```
### `tts`

```typescript
tts: string | null
```
### `visualInstruction`

```typescript
visualInstruction: ( string | RoadShield ) []
```
