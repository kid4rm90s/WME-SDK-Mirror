---
title: SDK.TurnGuidance interface
source: interfaces/index.SDK.TurnGuidance.html
created: 2026-07-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TurnGuidance

```typescript
interface TurnGuidance {
  exitSigns: ExitSign [] ;
  towards: ( string | RoadShield ) [] ;
  tts: null | string ;
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
tts: null | string
```
### `visualInstruction`

```typescript
visualInstruction: ( string | RoadShield ) []
```
