---
title: SDK.Segment interface
source: interfaces/index.SDK.Segment.html
created: 2026-04-22
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Segment

```typescript
interface Segment {
  allowNoDirection: boolean ;
  alternateStreetIds: number [] ;
  areFwdTurnsVerified: boolean ;
  areRevTurnsVerified: boolean ;
  elevationLevel: null | number ;
  flagAttributes: SegmentFlagAttributes ;
  fromLanesInfo: null | SegmentLanesInfo ;
  fromNodeId: null | number ;
  fromNodeLanesCount: number ;
  fwdSpeedLimit: null | number ;
  geometry: LineString ;
  hasClosures: boolean ;
  hasHouseNumbers: boolean ;
  hasRestrictions: boolean ;
  hasSeparator: boolean ;
  id: number ;
  isAtoB: boolean ;
  isBtoA: boolean ;
  isFwdSpeedLimitVerified: boolean ;
  isRevSpeedLimitVerified: boolean ;
  isTwoWay: boolean ;
  junctionId: null | number ;
  length: number ;
  lockRank: UserRank ;
  modificationData: ModificationMetadata ;
  primaryStreetId: null | number ;
  rank: UserRank ;
  restrictions: BaseRestriction [] ;
  revSpeedLimit: null | number ;
  roadType: RoadTypeId ;
  routingRoadType: null | 1 | 2 | 3 | 6 | 7 ;
  toLanesInfo: null | SegmentLanesInfo ;
  toNodeId: null | number ;
  toNodeLanesCount: number ;
}
```
## Properties
### `allowNoDirection`

```typescript
allowNoDirection: boolean
```
### `alternateStreetIds`

```typescript
alternateStreetIds: number []
```
### `areFwdTurnsVerified`

```typescript
areFwdTurnsVerified: boolean
```
### `areRevTurnsVerified`

```typescript
areRevTurnsVerified: boolean
```
### `elevationLevel`

```typescript
elevationLevel: null | number
```
### `flagAttributes`

```typescript
flagAttributes: SegmentFlagAttributes
```
### `fromLanesInfo`

```typescript
fromLanesInfo: null | SegmentLanesInfo
```
### `fromNodeId`

```typescript
fromNodeId: null | number
```
### `fromNodeLanesCount`

```typescript
fromNodeLanesCount: number
```
### `fwdSpeedLimit`

```typescript
fwdSpeedLimit: null | number
```
### `geometry`

```typescript
geometry: LineString
```
### `hasClosures`

```typescript
hasClosures: boolean
```
### `hasHouseNumbers`

```typescript
hasHouseNumbers: boolean
```
### `hasRestrictions`

```typescript
hasRestrictions: boolean
```
### `hasSeparator`

```typescript
hasSeparator: boolean
```
### `id`

```typescript
id: number
```
### `isAtoB`

```typescript
isAtoB: boolean
```
### `isBtoA`

```typescript
isBtoA: boolean
```
### `isFwdSpeedLimitVerified`

```typescript
isFwdSpeedLimitVerified: boolean
```
### `isRevSpeedLimitVerified`

```typescript
isRevSpeedLimitVerified: boolean
```
### `isTwoWay`

```typescript
isTwoWay: boolean
```
### `junctionId`

```typescript
junctionId: null | number
```
### `length`

```typescript
length: number
```
### `lockRank`

```typescript
lockRank: UserRank
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `primaryStreetId`

```typescript
primaryStreetId: null | number
```
### `rank`

```typescript
rank: UserRank
```
### `restrictions`

```typescript
restrictions: BaseRestriction []
```
### `revSpeedLimit`

```typescript
revSpeedLimit: null | number
```
### `roadType`

```typescript
roadType: RoadTypeId
```
### `routingRoadType`

```typescript
routingRoadType: null | 1 | 2 | 3 | 6 | 7
```
### `toLanesInfo`

```typescript
toLanesInfo: null | SegmentLanesInfo
```
### `toNodeId`

```typescript
toNodeId: null | number
```
### `toNodeLanesCount`

```typescript
toNodeLanesCount: number
```
