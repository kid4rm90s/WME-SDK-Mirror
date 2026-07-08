---
title: SDK.Countries class
source: classes/index.SDK.Countries.html
created: 2026-07-08
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Countries

```typescript
getAll () : Country []
```
Methods for dealing with Countries.
## Methods
### `getAll`

```typescript
getAll () : Country []
```
an array of all the countries in the WME data model
### `getById`

```typescript
getById ( args: { countryId: number } ) : null | Country
```
country with id, or null if not found in the WME data model
### `getTopCountry`

```typescript
getTopCountry () : null | Country
```
the Country set to be the top country in the WME data model, or null
if none set
