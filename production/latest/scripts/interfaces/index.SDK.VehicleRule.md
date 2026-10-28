---
title: SDK.VehicleRule interface
source: interfaces/index.SDK.VehicleRule.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface VehicleRule

```typescript
interface VehicleRule {
  licensePlateNumber: LicensePlateRule | null ;
  licensePlateRule: LicensePlateRule | null ;
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
licensePlateNumber: LicensePlateRule | null
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
