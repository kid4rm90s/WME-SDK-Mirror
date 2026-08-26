---
title: SDK.Streets class
source: classes/index.SDK.Streets.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Streets

```typescript
addStreet ( args: { cityId ?: number ; streetName: string } ) : Street
```
Methods for dealing with Streets.
## Methods
### `addStreet`

```typescript
addStreet ( args: { cityId ?: number ; streetName: string } ) : Street
```
a new street object
### `getAll`

```typescript
getAll () : Street []
```
an array of all the streets in the WME data model
### `getById`

```typescript
getById ( args: { streetId: number } ) : null | Street
```
street with id, or null if not found in the WME data model
### `getStreet`

```typescript
getStreet ( args: { cityId ?: number ; streetName: string } ) : null | Street
```
a street object or null if not found
### `updateStreet`

```typescript
updateStreet ( args: { direction ?: string ; streetId: number } ) : void
```
