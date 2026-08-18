---
title: SDK.BaseRestriction interface
source: interfaces/index.SDK.BaseRestriction.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface BaseRestriction

```typescript
interface BaseRestriction {
  defaultType: null | RESTRICTION_TYPE ;
  description: null | string ;
  driveProfiles: DriveProfiles ;
  editable: boolean ;
  isExpired: boolean ;
  timeFrames: TimeFrame [] ;
}
```
Base restriction contract shared by turn and segment restrictions.
## Properties
### `defaultType`

```typescript
defaultType: null | RESTRICTION_TYPE
```
### `description`

```typescript
description: null | string
```
### `driveProfiles`

```typescript
driveProfiles: DriveProfiles
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
