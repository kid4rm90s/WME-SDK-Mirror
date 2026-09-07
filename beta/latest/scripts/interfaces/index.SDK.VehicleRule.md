---
title: SDK.VehicleRule interface
source: interfaces/index.SDK.VehicleRule.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VehicleRule

```typescript
interface VehicleRule {
  licensePlateNumber: null | LicensePlateRule ;
  licensePlateRule: null | LicensePlateRule ;
  minPassengers: number ;
  numPassengers: number ;
  subscriptions: string [] ;
  vehicleTypes: VehicleType [] ;
}
```
Represents a vehicle rule for specific vehicle exemptions or restrictions.
## Properties
### `licensePlateNumber`

```typescript
licensePlateNumber: null | LicensePlateRule
```
### `minPassengers`

```typescript
minPassengers: number
```
### `numPassengers`

```typescript
numPassengers: number
```
### `vehicleTypes`

```typescript
vehicleTypes: VehicleType []
```
