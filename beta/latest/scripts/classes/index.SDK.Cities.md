---
title: SDK.Cities class
source: classes/index.SDK.Cities.html
created: 2026-04-17
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Cities

```typescript
addCity (
  options: { cityName: string ; countryId ?: number ; stateId ?: number } ,
  ) : City
```
Methods for dealing with Cities.
## Methods
### `addCity`

```typescript
addCity (
  options: { cityName: string ; countryId ?: number ; stateId ?: number } ,
  ) : City
```
a new city object
### `getAll`

```typescript
getAll () : City []
```
an array of all the cities in the WME data model
### `getById`

```typescript
getById ( args: { cityId: number } ) : null | City
```
city with id, or null if not found in the WME data model
### `getCity`

```typescript
getCity (
  options: { cityName: string ; countryId ?: number ; stateId ?: number } ,
  ) : null | City
```
a city object or null if not found
### `getTopCity`

```typescript
getTopCity () : null | City
```
top city or null
