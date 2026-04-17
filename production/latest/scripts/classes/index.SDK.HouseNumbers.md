---
title: SDK.HouseNumbers class
source: classes/index.SDK.HouseNumbers.html
created: 2026-04-17
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class HouseNumbers

```typescript
addHouseNumber ( args: { number: string ; point: Point ; segmentId ?: number } ) : void
```
Methods for dealing with HouseNumbers
## Methods
### `addHouseNumber`

```typescript
addHouseNumber ( args: { number: string ; point: Point ; segmentId ?: number } ) : void
```

### `clearHouseNumbers`

```typescript
clearHouseNumbers () : void
```

### `deleteHouseNumber`

```typescript
deleteHouseNumber ( args: { houseNumberId: string } ) : void
```

### `fetchHouseNumbers`

```typescript
fetchHouseNumbers ( options: { segmentIds: number [] } ) : Promise < HouseNumber [] >
```
A Promise that resolves to an array of HouseNumber objects.
### `moveHouseNumber`

```typescript
moveHouseNumber (
  args: { houseNumberId: string ; point: Point ; segmentId ?: number } ,
  ) : void
```

### `moveHouseNumberFractionPoint`

```typescript
moveHouseNumberFractionPoint (
  args: { fractionPoint: Point ; houseNumberId: string } ,
  ) : void
```

### `updateHouseNumber`

```typescript
updateHouseNumber (
  args: {
  fractionPoint ?: Point ;
  houseNumberId: string ;
  number ?: string ;
  point ?: Point ;
  segmentId ?: number ;
} ,
  ) : void
```
