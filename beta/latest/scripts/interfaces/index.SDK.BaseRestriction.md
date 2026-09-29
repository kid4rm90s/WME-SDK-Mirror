---
title: SDK.BaseRestriction interface
source: interfaces/index.SDK.BaseRestriction.html
created: 2026-09-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface BaseRestriction

```typescript
interface BaseRestriction {
  defaultType: RESTRICTION_TYPE | null ;
  description: string | null ;
  driveProfiles: VehicleRules ;
  editable: boolean ;
  isExpired: boolean ;
  timeFrames: TimeFrame [] ;
  vehicleRules: VehicleRules ;
}
```
Base restriction contract shared by turn and segment restrictions.
## Properties
### `defaultType`

```typescript
defaultType: RESTRICTION_TYPE | null
```
### `description`

```typescript
description: string | null
```
### `driveProfiles`

```typescript
driveProfiles: VehicleRules
```
### `editable`

```typescript
editable: boolean
```
### `isExpired`

```typescript
isExpired: boolean
```
### `timeFrames`

```typescript
timeFrames: TimeFrame []
```
### `vehicleRules`

```typescript
vehicleRules: VehicleRules
```
