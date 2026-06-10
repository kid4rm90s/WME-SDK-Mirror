---
title: SDK.Venues class
source: classes/index.SDK.Venues.html
created: 2026-06-10
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class Venues

```typescript
ChargingStation: ChargingStation = ...
```
Methods for dealing with Venues.
## Properties
### **Readonly** `ChargingStation`

```typescript
ChargingStation: ChargingStation = ...
```
### **Readonly** `ParkingLot`

```typescript
ParkingLot: ParkingLot = ...
```
## Methods
### `addVenue`

```typescript
addVenue ( args: { category: VenueCategoryId ; geometry: Point | Polygon } ) : number
```
id of the new venue
### `deleteImage`

```typescript
deleteImage ( args: { imageId: string ; venueId: string } ) : void
```

### `deleteVenue`

```typescript
deleteVenue ( args: { venueId: string } ) : void
```

### `getAddress`

```typescript
getAddress ( args: { venueId: string } ) : VenueAddress
```
an address of the venue with the provided id.
### `getAll`

```typescript
getAll () : Venue []
```
an array of all the venues in the WME data model
### `getAllVenueCategories`

```typescript
getAllVenueCategories () : VenueCategory []
```
all possible venue categories and their localised names.
### `getById`

```typescript
getById ( args: { venueId: string } ) : null | Venue
```
venue with id, or null if not found in the WME data model
### `getChargingStationBrands`

```typescript
getChargingStationBrands () : string []
```
a list of charging station brands
### `getGasStationBrands`

```typescript
getGasStationBrands () : string []
```
a list of gas stations brands
### `getParkingLotBrands`

```typescript
getParkingLotBrands () : string []
```
a list of parking lot brands
### `getParkingLotType`

```typescript
getParkingLotType ( args: { venueId: string } ) : ParkingType
```
parking lot type of the venue in case the venue is a parking lot, null othervise.
### `getVenueMainCategories`

```typescript
getVenueMainCategories () : VenueCategory []
```
a list of the venue main categories and their localised names.
### `getVenueSubCategories`

```typescript
getVenueSubCategories () : VenueSubCategory []
```
a list of the venue sub-categories, their main category id
and their localised names.
### `hasPermissions`

```typescript
hasPermissions ( args: { permission ?: VenuePermission ; venueId: string } ) : boolean
```
whether the current user has a permission for this venue or not.
### `replaceNavigationPoints`

```typescript
replaceNavigationPoints (
  args: { navigationPoints: Partial < NavigationPoint > [] ; venueId: string } ,
  ) : void
```

### `showVenueUpdateRequestDialog`

```typescript
showVenueUpdateRequestDialog ( args: { venueId: string } ) : void
```

### `updateAddress`

```typescript
updateAddress (
  args: { houseNumber ?: string ; streetId ?: number ; venueId: string } ,
  ) : void
```

### `updateVenue`

```typescript
updateVenue (
  args: {
  aliases ?: string [] ;
  brand ?: string ;
  categories ?: VenueCategoryId [] ;
  description ?: string ;
  geometry ?: Point | Polygon ;
  lockRank ?: number ;
  name ?: string ;
  openingHours ?: OpeningHour [] ;
  phone ?: string ;
  services ?: ServiceType [] ;
  url ?: string ;
  venueId: string ;
} ,
  ) : void
```

### `updateVenueIsResidential`

```typescript
updateVenueIsResidential (
  args: { isResidential: boolean ; venueId: string } ,
  ) : void
```

### `updateVenueUpdateRequest`

```typescript
updateVenueUpdateRequest (
  args: {
  isApproved: boolean ;
  venueId: string ;
  venueUpdateRequestId: string ;
} ,
  ) : void
```
