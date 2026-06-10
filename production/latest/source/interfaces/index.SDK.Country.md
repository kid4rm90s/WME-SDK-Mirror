---
title: SDK.Country interface
source: interfaces/index.SDK.Country.html
created: 2026-06-10
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Country

```typescript
interface Country {
  abbr: string ;
  defaultLaneWidthPerRoadType: 
  | null
  | Partial <
  {
  "1": number ;
  "10": number ;
  "15": number ;
  "16": number ;
  "17": number ;
  "18": number ;
  "19": number ;
  "2": number ;
  "20": number ;
  "22": number ;
  "3": number ;
  "4": number ;
  "5": number ;
  "6": number ;
  "7": number ;
  "8": number ;
  "9": number ;
} ,
  > ;
  id: number ;
  isLeftHandTraffic: boolean ;
  modificationData: ModificationMetadata ;
  name: string ;
  regionCode: null
  | RegionCode ;
  restrictionSubscriptions: Subscription [] ;
}
```
## Properties
### `abbr`

```typescript
abbr: string
```
### `defaultLaneWidthPerRoadType`

```typescript
defaultLaneWidthPerRoadType: 
  | null
  | Partial <
  {
  "1": number ;
  "10": number ;
  "15": number ;
  "16": number ;
  "17": number ;
  "18": number ;
  "19": number ;
  "2": number ;
  "20": number ;
  "22": number ;
  "3": number ;
  "4": number ;
  "5": number ;
  "6": number ;
  "7": number ;
  "8": number ;
  "9": number ;
} ,
  >
```
### `id`

```typescript
id: number
```
### `isLeftHandTraffic`

```typescript
isLeftHandTraffic: boolean
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```
### `regionCode`

```typescript
regionCode: null | RegionCode
```
### `restrictionSubscriptions`

```typescript
restrictionSubscriptions: Subscription []
```
