---
title: SDK.Nodes class
source: classes/index.SDK.Nodes.html
created: 2026-06-29
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Nodes

```typescript
allowNodeTurns ( args: { allow: boolean ; nodeId: number } ) : boolean
```
Methods for dealing with Nodes.
## Methods
### `allowNodeTurns`

```typescript
allowNodeTurns ( args: { allow: boolean ; nodeId: number } ) : boolean
```
false if there's nothing to change(all turns are already allowed/disallowed or there are no turns), true if the change is successful.
### `canEdit`

```typescript
canEdit ( args: { nodeId: number } ) : boolean
```
true if node properties are editable.
### `canEditTurns`

```typescript
canEditTurns ( args: { nodeId: number } ) : boolean
```
true if all segments connected to the node are allowed to edit connections.
### `getAll`

```typescript
getAll () : Node []
```
an array of all the nodes in the WME data model
### `getById`

```typescript
getById ( args: { nodeId: number } ) : null | Node
```
node with id, or null if not found in the WME data model
### `isVirtual`

```typescript
isVirtual ( args: { nodeId: number } ) : boolean
```
boolean indicating whether the node is virtually connected to any segment.
### `moveNode`

```typescript
moveNode ( args: { geometry: Point ; id: number } ) : void
```
