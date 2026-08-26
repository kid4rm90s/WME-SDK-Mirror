---
title: SDK.AddableVehicleRule interface
source: interfaces/index.SDK.AddableVehicleRule.html
created: 2026-08-26
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface AddableVehicleRule

```typescript
interface AddableVehicleRule {
  licensePlateRule: null | LicensePlateRule ;
  minPassengers: 0 | 2 | 3 | 4 ;
  subscriptions: string [] ;
  vehicleTypes: AddableVehicleType [] ;
}
```
Represents a vehicle rule when updating restrictions.
## Properties
### `minPassengers`

```typescript
minPassengers: 0 | 2 | 3 | 4
```
### `vehicleTypes`

```typescript
vehicleTypes: AddableVehicleType []
```
