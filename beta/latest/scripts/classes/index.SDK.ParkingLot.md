---
title: SDK.ParkingLot class
source: classes/index.SDK.ParkingLot.html
created: 2026-07-08
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class ParkingLot

```typescript
canExitWhileClosed ( args: { venueId: string } ) : null | boolean
```
Methods for dealing with Parking Lots.
## Methods
### `canExitWhileClosed`

```typescript
canExitWhileClosed ( args: { venueId: string } ) : null | boolean
```
whether the current venue can be exited while closed in case the venue is a parking lot, null otherwise.
### `getBrands`

```typescript
getBrands () : string []
```
a list of parking lot brands
### `getCostType`

```typescript
getCostType ( args: { venueId: string } ) : null | ParkingLotCostType
```
cost type of the venue in case the venue is a parking lot, null otherwise.
### `getEstimatedNumberOfSpots`

```typescript
getEstimatedNumberOfSpots ( args: { venueId: string } ) : null | SpotsEstimate
```
SpotsEstimate | null - the estimated number of spots the venue in case the venue is a parking lot, null otherwise.
### `getLotTypes`

```typescript
getLotTypes ( args: { venueId: string } ) : null | LotType []
```
parking lot types of the venue in case the venue is a parking lot, null otherwise.
### `getParkingLotType`

```typescript
getParkingLotType ( args: { venueId: string } ) : ParkingType
```
parking type of the venue in case the venue is a parking lot, null otherwise.
### `getPaymentMethods`

```typescript
getPaymentMethods ( args: { venueId: string } ) : null | PaymentType []
```
payment types of the venue in case the venue is a parking lot, null otherwise.
### `isLotTypeDependentOnDayTime`

```typescript
isLotTypeDependentOnDayTime ( args: { venueId: string } ) : null | boolean
```
whether lot type of the current venue varies depending on time/day in case the venue is a parking lot, null otherwise.
### `setEstimatedNumberOfSpots`

```typescript
setEstimatedNumberOfSpots (
  args: { estimatedNumberOfSpots: SpotsEstimate ; venueId: string } ,
  ) : void
```
