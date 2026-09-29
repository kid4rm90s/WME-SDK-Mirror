---
title: SDK.Segment interface
source: interfaces/index.SDK.Segment.html
created: 2026-09-30
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
  elevationLevel: number | null ;
  flagAttributes: SegmentFlagAttributes ;
  fromLanesInfo: SegmentLanesInfo | null ;
  fromNodeId: number | null ;
  fromNodeLanesCount: number ;
  fwdSpeedLimit: number | null ;
  geometry: LineString ;
  hasClosures: boolean ;
  hasHouseNumbers: boolean ;
  hasRestrictions: boolean ;
  hasSeparator: boolean ;
  id: number ;
  isAtoB: boolean ;
  isBtoA: boolean ;
  isDrivable: boolean ;
  isFwdSpeedLimitVerified: boolean ;
  isRevSpeedLimitVerified: boolean ;
  isTwoWay: boolean ;
  junctionId: number | null ;
  length: number ;
  lockRank: UserRank ;
  modificationData: ModificationMetadata ;
  primaryStreetId: number | null ;
  rank: UserRank ;
  restrictions: SegmentRestriction [] ;
  revSpeedLimit: number | null ;
  roadType: RoadTypeId ;
  routingRoadType: 6 | 7 | 1 | 2 | 3 | null ;
  toLanesInfo: SegmentLanesInfo | null ;
  toNodeId: number | null ;
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
elevationLevel: number | null
```
### `flagAttributes`

```typescript
flagAttributes: SegmentFlagAttributes
```
### `fromLanesInfo`

```typescript
fromLanesInfo: SegmentLanesInfo | null
```
### `fromNodeId`

```typescript
fromNodeId: number | null
```
### `fromNodeLanesCount`

```typescript
fromNodeLanesCount: number
```
### `fwdSpeedLimit`

```typescript
fwdSpeedLimit: number | null
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
### `isDrivable`

```typescript
isDrivable: boolean
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
junctionId: number | null
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
primaryStreetId: number | null
```
### `rank`

```typescript
rank: UserRank
```
### `restrictions`

```typescript
restrictions: SegmentRestriction []
```
### `revSpeedLimit`

```typescript
revSpeedLimit: number | null
```
### `roadType`

```typescript
roadType: RoadTypeId
```
### `routingRoadType`

```typescript
routingRoadType: 6 | 7 | 1 | 2 | 3 | null
```
### `toLanesInfo`

```typescript
toLanesInfo: SegmentLanesInfo | null
```
### `toNodeId`

```typescript
toNodeId: number | null
```
### `toNodeLanesCount`

```typescript
toNodeLanesCount: number
```
