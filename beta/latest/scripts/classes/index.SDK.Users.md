---
title: SDK.Users class
source: classes/index.SDK.Users.html
created: 2026-05-15
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Users

```typescript
getLocalizedUserProfileLink ( options: { userName: string } ) : string
```
Methods for dealing with Users.
## Methods
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
