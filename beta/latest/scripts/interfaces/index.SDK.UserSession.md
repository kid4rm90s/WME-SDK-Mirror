---
title: SDK.UserSession interface
source: interfaces/index.SDK.UserSession.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UserSession

```typescript
interface UserSession {
  editableAreas: UserEditableArea [] ;
  isAreaManager: boolean ;
  isCountryManager: boolean ;
  managedAreas: ManagedAreaShort [] ;
  rank: UserRank ;
  userName: string ;
}
```
## Properties
### `editableAreas`

```typescript
editableAreas: UserEditableArea []
```
### `isAreaManager`

```typescript
isAreaManager: boolean
```
### `isCountryManager`

```typescript
isCountryManager: boolean
```
### `managedAreas`

```typescript
managedAreas: ManagedAreaShort []
```
### `rank`

```typescript
rank: UserRank
```
### `userName`

```typescript
userName: string
```
