---
title: SDK.TrackedDataModel interface
source: interfaces/index.SDK.TrackedDataModel.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TrackedDataModel

```typescript
interface TrackedDataModel {
  events: {
  "objects-state-deleted": (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectsadded: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectschanged: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  "objectschanged-id": ( changedIds: ChangedIDsInfo ) = > void ;
  objectsremoved: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectssynced: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
} ;
}
```
## Properties
### `events`

```typescript
events: {
  "objects-state-deleted": (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectsadded: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectschanged: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  "objectschanged-id": ( changedIds: ChangedIDsInfo ) = > void ;
  objectsremoved: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
  objectssynced: (
  objects: DataModelObject < ObjectId , FeatureVectorAttributes < ObjectId > > [] ,
  ) = > void ;
}
```
