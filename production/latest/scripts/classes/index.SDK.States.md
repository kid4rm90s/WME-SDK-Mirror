---
title: SDK.States class
source: classes/index.SDK.States.html
created: 2026-04-23
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class States

```typescript
getAll () : State []
```
Methods for dealing with State.
## Methods
### `getAll`

```typescript
getAll () : State []
```
an array of all the states in the WME data model
### `getAllWithoutDefault`

```typescript
getAllWithoutDefault () : State []
```
an array of all the states apart from default in the WME data model
### `getById`

```typescript
getById ( args: { stateId: number } ) : null | State
```
state with id, or null if not found in the WME data model
### `getTopState`

```typescript
getTopState () : null | State
```
the State set to be the top state in the WME data model, or null
if none set
### `hasNonDefaultStates`

```typescript
hasNonDefaultStates () : boolean
```
true if there are any states apart from the default state in the WME data model.
