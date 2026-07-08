---
title: SDK.Segments class
source: classes/index.SDK.Segments.html
created: 2026-07-08
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Segments

```typescript
addAlternateStreet ( args: { segmentIds: number [] ; streetId: number } ) : void
```
Methods for dealing with Segments.
## Methods
### `addAlternateStreet`

```typescript
addAlternateStreet ( args: { segmentIds: number [] ; streetId: number } ) : void
```

### `addIntersection`

```typescript
addIntersection (
  args: { segmentIds: [ number , number ] } ,
  ) : { sourceSplits: [ number , number ] ; targetSplits: [ number , number ] }
```
the ids of the four newly created segments.
### `addSegment`

```typescript
addSegment ( args: { geometry: LineString ; roadType: RoadTypeId } ) : number
```
segment id of the new segment
### `connectsToBigJunction`

```typescript
connectsToBigJunction ( args: { segmentId: number } ) : boolean
```
true if the segment is completely within, goes inside or goes outside of a big junction.
### `createRoundabout`

```typescript
createRoundabout ( args: { center: LonLat ; rx: number ; ry: number } ) : number []
```
ids of roundabout segments
### `deleteSegment`

```typescript
deleteSegment ( args: { segmentId: number } ) : void
```

### `findSegment`

```typescript
findSegment ( args: { segmentId: number } ) : Promise < Segment >
```
A promise that resolves to the found segment.
### `getAddress`

```typescript
getAddress ( args: { segmentId: number } ) : SegmentAddress
```
an address of the segment with provided id.
### `getAll`

```typescript
getAll () : Segment []
```
an array of all the segments in the WME data model
### `getById`

```typescript
getById ( args: { segmentId: number } ) : null | Segment
```
segment with id, or null if not found in the WME data model
### `getConnectedSegments`

```typescript
getConnectedSegments (
  args: { reverseDirection ?: boolean ; segmentId: number } ,
  ) : Segment []
```
connected segments in specified direction
### `getReversedSegments`

```typescript
getReversedSegments ( args: { segmentIds: number [] } ) : Segment []
```
An array of segments that are considered reversed within the provided list.
### `getRoadTypes`

```typescript
getRoadTypes () : RoadType []
```
all possible road types and their localised names.
### `getVirtualNodes`

```typescript
getVirtualNodes ( args: { segmentId: number } ) : Node []
```
array of nodes virtually connected to the specified segment.
### `getWKTGeometry`

```typescript
getWKTGeometry ( args: { segmentId: number } ) : string
```
the WKT string representation of the segment's geometry
### `hasPermissions`

```typescript
hasPermissions (
  args: { permission ?: SegmentPermission ; segmentId: number } ,
  ) : boolean
```
whether the current user has a permission for this segment or not.
### `isContainedInBigJunction`

```typescript
isContainedInBigJunction ( args: { segmentId: number } ) : boolean
```
true if the segment is completely within a big junction
### `isFromNodeInBigJunction`

```typescript
isFromNodeInBigJunction (
  args: { bigJunctionId ?: number ; segmentId: number } ,
  ) : boolean
```
true if the segment's "from" node is part of a big junction, indicating the segment leads away from it.
### `isRoadTypeDrivable`

```typescript
isRoadTypeDrivable ( args: { roadType: RoadTypeId } ) : boolean
```
boolean indicating whether the specified road type is drivable by vehicles.
A road type is considered non-drivable if it is a walking trail, pedestrian boardwalk, stairway, railroad, or runway/taxiway.
### `isTollSegment`

```typescript
isTollSegment ( args: { segmentId: number } ) : boolean
```
true if the segment is a toll road or has a toll-free restriction
### `isToNodeInBigJunction`

```typescript
isToNodeInBigJunction (
  args: { bigJunctionId ?: number ; segmentId: number } ,
  ) : boolean
```
true if the segment's "to" node is part of a big junction, indicating the segment leads into it.
### `mergeSegments`

```typescript
mergeSegments ( args: { segmentIds: number [] } ) : void
```

### `splitSegment`

```typescript
splitSegment ( args: { segmentId: number ; splitPoint: Point } ) : [ number , number ]
```
two segments the original segment was split into.
### `updateAddress`

```typescript
updateAddress (
  args: { addressData ?: SegmentAddressData ; segmentId: number } ,
  ) : void
```

### `updateSegment`

```typescript
updateSegment (
  args: {
  direction ?: SegmentDirection ;
  elevationLevel ?: number ;
  flagAttributes ?: Partial <
  Pick <
  SegmentFlagAttributes ,
  "headlights"
  | "nearbyHOV"
  | "tunnel"
  | "unpaved" ,
  > ,
  > ;
  fromLanesInfo ?: null | SegmentLanesInfo ;
  fwdSpeedLimit ?: null | number ;
  geometry ?: LineString ;
  hasToll ?: boolean ;
  lockRank ?: UserRank ;
  revSpeedLimit ?: null | number ;
  roadType ?: RoadTypeId ;
  routingRoadType ?: 1 | 2 | 3 | 6 | 7 ;
  segmentId: number ;
  toLanesInfo ?: null | SegmentLanesInfo ;
} ,
  ) : void
```

### `verifyTurns`

```typescript
verifyTurns ( args: { isForward: boolean ; segmentId: number } ) : void
```
