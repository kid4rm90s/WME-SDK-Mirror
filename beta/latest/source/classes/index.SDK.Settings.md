---
title: SDK.Settings class
source: classes/index.SDK.Settings.html
created: 2026-07-08
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Settings

```typescript
getLocale () : { localeCode: string ; localeName: string }
```
Methods for managing user settings.
## Methods
### `getLocale`

```typescript
getLocale () : { localeCode: string ; localeName: string }
```
and object with the current locale code and locale name
### `getRegionCode`

```typescript
getRegionCode () : null | RegionCode
```
the current region code, or null if not available
### `getUserSettings`

```typescript
getUserSettings () : UserSettings
```
the current user settings or default settings if user isn't logged in yet.
### `setRegionCode`

```typescript
setRegionCode ( args: { regionCode: RegionCode } ) : void
```

### `setUserSettings`

```typescript
setUserSettings ( options: Partial < UserSettings > ) : void
```
