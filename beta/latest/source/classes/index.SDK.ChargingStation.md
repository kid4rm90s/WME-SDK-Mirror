---
title: SDK.ChargingStation class
source: classes/index.SDK.ChargingStation.html
created: 2026-08-05
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class ChargingStation

```typescript
getBrands () : string []
```
Methods for dealing with ChargingStations.
## Methods
### `getBrands`

```typescript
getBrands () : string []
```
a list of charging station brands
### `getChargersAccessType`

```typescript
getChargersAccessType ( args: { venueId: string } ) : null | ChargersAccessType
```
chargers access type of the venue in case the venue is a charging station, null otherwise.
### `getCostType`

```typescript
getCostType ( args: { venueId: string } ) : null | ChargingStationCostType
```
cost type of the venue in case the venue is a charging station, null otherwise.
### `getNetwork`

```typescript
getNetwork ( args: { venueId: string } ) : null | string
```
network of the venue in case the venue is a charging station, null otherwise.
### `getPaymentMethods`

```typescript
getPaymentMethods ( args: { venueId: string } ) : null | PaymentMethod []
```
payment methods of the venue in case the venue is a charging station, null otherwise.
