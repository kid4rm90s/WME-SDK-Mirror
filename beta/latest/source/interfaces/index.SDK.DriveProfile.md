---
title: SDK.DriveProfile interface
source: interfaces/index.SDK.DriveProfile.html
created: 2026-08-18
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface DriveProfile

```typescript
interface DriveProfile {
  licensePlateNumber: null | LicensePlate ;
  numPassengers: number ;
  subscriptions: string [] ;
  vehicleTypes: VehicleType [] ;
}
```
Represents a driving profile rule for specific vehicle exemptions or restrictions.
## Properties
### `licensePlateNumber`

```typescript
licensePlateNumber: null | LicensePlate
```
### `numPassengers`

```typescript
numPassengers: number
```
### `subscriptions`

```typescript
subscriptions: string []
```
### `vehicleTypes`

```typescript
vehicleTypes: VehicleType []
```
