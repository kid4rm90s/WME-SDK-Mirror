---
title: SDK.Users class
source: classes/index.SDK.Users.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Users

```typescript
getByUserName ( options: { userName: string } ) : null | User
```
Methods for dealing with Users.
## Methods
### `getByUserName`

```typescript
getByUserName ( options: { userName: string } ) : null | User
```
user with userName, or null if not found
### `getCurrentUser`

```typescript
getCurrentUser () : null | User
```
the currently logged in user or null if not logged in
### `getLocalizedUserProfileLink`

```typescript
getLocalizedUserProfileLink ( options: { userName: string } ) : string
```
a formatted link which includes the current locale for a users editor profile page
### `getUserProfile`

```typescript
getUserProfile ( options: { userName: string } ) : Promise < UserProfile >
```
a fetched user profile
### `getUserProfileLink`

```typescript
getUserProfileLink ( options: { userName: string } ) : string
```
a formatted link for a users editor profile page
