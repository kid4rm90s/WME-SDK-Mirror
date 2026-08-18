---
title: SDK.Shortcuts class
source: classes/index.SDK.Shortcuts.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Shortcuts

```typescript
areShortcutKeysInUse ( args: { shortcutKeys: string } ) : boolean
```
Methods for defining shortcuts.
## Methods
### `areShortcutKeysInUse`

```typescript
areShortcutKeysInUse ( args: { shortcutKeys: string } ) : boolean
```
true if a shortcut key combination is already in use, otherwise false
### `createShortcut`

```typescript
createShortcut ( args: KeyboardShortcut ) : void
```

### `deleteShortcut`

```typescript
deleteShortcut ( args: { shortcutId: string } ) : void
```

### `getAllShortcuts`

```typescript
getAllShortcuts () : KeyboardShortcut []
```
all registered shortcuts of the userscript.
### `isShortcutRegistered`

```typescript
isShortcutRegistered ( args: { shortcutId: string } ) : boolean
```
true if a shortcut with specified id is already registered.
