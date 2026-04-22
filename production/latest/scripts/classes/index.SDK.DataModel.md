---
title: SDK.DataModel class
source: classes/index.SDK.DataModel.html
created: 2026-04-22
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class DataModel

```typescript
BigJunctions: BigJunctions = ...
```
Methods for dealing with the WME data model objects.
## Properties
### **Readonly** `BigJunctions`

```typescript
BigJunctions: BigJunctions = ...
```
### **Readonly** `Cities`

```typescript
Cities: Cities = ...
```
### **Readonly** `Countries`

```typescript
Countries: Countries = ...
```
### **Readonly** `EditSuggestions`

```typescript
EditSuggestions: EditSuggestions = ...
```
### **Readonly** `HouseNumbers`

```typescript
HouseNumbers: HouseNumbers = ...
```
### **Readonly** `Junctions`

```typescript
Junctions: Junctions = ...
```
### **Readonly** `MajorTrafficEvents`

```typescript
MajorTrafficEvents: MajorTrafficEvents = ...
```
### **Readonly** `ManagedAreas`

```typescript
ManagedAreas: ManagedAreas = ...
```
### **Readonly** `MapComments`

```typescript
MapComments: MapComments = ...
```
### **Readonly** `MapProblems`

```typescript
MapProblems: MapProblems = ...
```
### **Readonly** `MapUpdateRequests`

```typescript
MapUpdateRequests: MapUpdateRequests = ...
```
### **Readonly** `Nodes`

```typescript
Nodes: Nodes = ...
```
### **Readonly** `PermanentHazards`

```typescript
PermanentHazards: PermanentHazards = ...
```
### **Readonly** `RestrictedDrivingAreas`

```typescript
RestrictedDrivingAreas: RestrictedDrivingAreas = ...
```
### **Readonly** `RoadClosures`

```typescript
RoadClosures: RoadClosures = ...
```
### **Readonly** `Segments`

```typescript
Segments: Segments = ...
```
### **Readonly** `States`

```typescript
States: States = ...
```
### **Readonly** `Streets`

```typescript
Streets: Streets = ...
```
### **Readonly** `TurnClosures`

```typescript
TurnClosures: TurnClosures = ...
```
### **Readonly** `Turns`

```typescript
Turns: Turns = ...
```
### **Readonly** `Users`

```typescript
Users: Users = ...
```
### **Readonly** `Venues`

```typescript
Venues: Venues = ...
```
## Methods
### `isDeletable`

```typescript
isDeletable (
  args: { dataModelName: DataModelName ; objectId: string | number } ,
  ) : boolean
```
true if the object is deletable, false otherwise.
### `isDeleted`

```typescript
isDeleted (
  args: { dataModelName: DataModelName ; objectId: string | number } ,
  ) : boolean
```
true if the object is deleted, false otherwise.
### `isNew`

```typescript
isNew (
  args: { dataModelName: DataModelName ; objectId: string | number } ,
  ) : boolean
```
true if the object is new, false otherwise.
### `refreshData`

```typescript
refreshData () : Promise < void >
```
promise that resolves once the data refresh completed.
