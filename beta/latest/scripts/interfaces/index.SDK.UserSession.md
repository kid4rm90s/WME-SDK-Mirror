---
title: SDK.UserSession interface
source: interfaces/index.SDK.UserSession.html
created: 2026-07-08
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface UserSession

```typescript
interface UserSession {
  isAreaManager: boolean ;
  isCountryManager: boolean ;
  managedAreas: ManagedAreaShort [] ;
  rank: UserRank ;
  userName: string ;
}
```
## Properties
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
