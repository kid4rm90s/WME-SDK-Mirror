---
title: SDK.Editing class
source: classes/index.SDK.Editing.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Editing

```typescript
clearSelection () : void
```
Methods for dealing with selection and undoing/redoing actions.
## Methods
### `clearSelection`

```typescript
clearSelection () : void
```

### `getCurrentSaveMode`

```typescript
getCurrentSaveMode () : SaveMode
```
current SaveMode .
### `getRedoChangesCount`

```typescript
getRedoChangesCount () : number
```
the number of changes that can be redone.
### `getSelection`

```typescript
getSelection () : null | SelectionWithLocalizedTypeName
```
ids of currently selected objects or null if nothing selected. The selection
only includes objects of a single type.
### `getUnsavedChangesCount`

```typescript
getUnsavedChangesCount () : number
```
the number of unsaved edits.
### `isDrawingInProgress`

```typescript
isDrawingInProgress () : boolean
```
true if drawing is in progress.
### `isEditingAllowed`

```typescript
isEditingAllowed () : boolean
```
true if editing is allowed.
### `isEditingHouseNumbers`

```typescript
isEditingHouseNumbers () : boolean
```
false.
### `isPracticeModeOn`

```typescript
isPracticeModeOn () : boolean
```
true if user is editing as a guest in "practice mode"
### `isSnapshotModeOn`

```typescript
isSnapshotModeOn () : boolean
```
true if user is in "snapshot mode", viewing what’s currently live
in the Waze app.
### `lockEditing`

```typescript
lockEditing () : string
```
unique id to be used for unlocking editing.
### `redo`

```typescript
redo () : void
```

### `releaseEditingLock`

```typescript
releaseEditingLock ( args: { lockId: string } ) : void
```

### `save`

```typescript
save () : Promise < void >
```
promise that resolves once save completed successfully or failed.
### `setSelection`

```typescript
setSelection ( options: { selection: Selection } ) : void
```

### `undo`

```typescript
undo () : void
```

### `undoAll`

```typescript
undoAll () : void
```
