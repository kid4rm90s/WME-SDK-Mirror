---
title: SDK.WmeState class
source: classes/index.SDK.WmeState.html
created: 2026-08-05
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class WmeState

```typescript
getManagedCountries () : Country []
```
Contains information about current state of the WME.
## Methods
### `getManagedCountries`

```typescript
getManagedCountries () : Country []
```
the list of the countries in the WME data model that are managed by the current user.
### `getUserInfo`

```typescript
getUserInfo () : null | UserSession
```
information about currently logged in user or null if user isn't logged in yet.
### `isInitialized`

```typescript
isInitialized () : boolean
```
true if WME initialized successfully.
### `isInitialMapDataLoaded`

```typescript
isInitialMapDataLoaded () : boolean
```
true if WME already fetched map data from the server.
### `isLoggedIn`

```typescript
isLoggedIn () : boolean
```
true if user logged in
### `isMapLoading`

```typescript
isMapLoading () : boolean
```
true if WME map is loading.
### `isReady`

```typescript
isReady () : boolean
```
true if WME already fetched map data and user logged in.
