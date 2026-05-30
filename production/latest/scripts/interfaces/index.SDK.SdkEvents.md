---
title: SDK.SdkEvents interface
source: interfaces/index.SDK.SdkEvents.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkEvents

```typescript
interface SdkEvents {
  "wme-after-edit": { affectedObjects: AffectedObject [] } ;
  "wme-after-redo-clear": undefined ;
  "wme-after-undo": undefined ;
  "wme-data-model-object-changed-id": {
  dataModelName: DataModelName ;
  objectIds: ChangedIDsInfo ;
} ;
  "wme-data-model-object-state-deleted": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
} ;
  "wme-data-model-objects-added": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
} ;
  "wme-data-model-objects-changed": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
} ;
  "wme-data-model-objects-removed": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
} ;
  "wme-data-model-objects-saved": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
} ;
  "wme-editing-house-numbers": { isEditingHouseNumbers: false } ;
  "wme-feature-editor-opened": {
  featureType: 
  | "bigJunction"
  | "city"
  | "googlePlace"
  | "mapComment"
  | "node"
  | "permanentHazard"
  | "restrictedDrivingArea"
  | "segment"
  | "segmentSuggestion"
  | "venue" ;
} ;
  "wme-house-number-added": { houseNumberId: string } ;
  "wme-house-number-deleted": { houseNumberId: string } ;
  "wme-house-number-moved": { houseNumberId: string } ;
  "wme-house-number-updated": { houseNumberId: string } ;
  "wme-initialized": undefined ;
  "wme-layer-checkbox-toggled": { checked: boolean ; name: string } ;
  "wme-layer-feature-clicked": {
  featureId: string | number ;
  layerName: string ;
} ;
  "wme-layer-feature-mouse-enter": {
  featureId: string
  | number ;
  layerName: string ;
} ;
  "wme-layer-feature-mouse-leave": {
  featureId: string
  | number ;
  layerName: string ;
} ;
  "wme-layer-visibility-changed": { layerName: string } ;
  "wme-logged-in": undefined ;
  "wme-logged-out": undefined ;
  "wme-map-data-loaded": undefined ;
  "wme-map-house-number-marker-added": undefined ;
  "wme-map-initial-data-loaded": undefined ;
  "wme-map-layer-added": { layerName: string } ;
  "wme-map-layer-changed": { layerName: string } ;
  "wme-map-layer-removed": { layerName: string } ;
  "wme-map-mouse-click": SdkMouseEvent ;
  "wme-map-mouse-down": SdkMouseEvent ;
  "wme-map-mouse-move": SdkMouseEvent ;
  "wme-map-mouse-out": SdkMouseEvent ;
  "wme-map-mouse-up": SdkMouseEvent ;
  "wme-map-move": undefined ;
  "wme-map-move-end": undefined ;
  "wme-map-zoom-changed": undefined ;
  "wme-no-edits": undefined ;
  "wme-ready": undefined ;
  "wme-save-finished": { success: boolean } ;
  "wme-save-mode-changed": { saveMode: SaveMode } ;
  "wme-selection-changed": undefined ;
  "wme-sidebar-tab-opened": { domId: string ; tabName: SidebarTabName } ;
  "wme-street-view-button-activated": undefined ;
  "wme-street-view-button-deactivated": undefined ;
  "wme-street-view-panel-visibility-changed": { isVisible: boolean } ;
  "wme-update-request-panel-opened": { updateRequestId: number } ;
  "wme-user-settings-changed": undefined ;
}
```
SDK events and their payload (if any).
## Properties
### `wme-after-edit`

```typescript
"wme-after-edit": { affectedObjects: AffectedObject [] }
```
### `wme-after-redo-clear`

```typescript
"wme-after-redo-clear": undefined
```
### `wme-after-undo`

```typescript
"wme-after-undo": undefined
```
### `wme-data-model-object-changed-id`

```typescript
"wme-data-model-object-changed-id": {
  dataModelName: DataModelName ;
  objectIds: ChangedIDsInfo ;
}
```
### `wme-data-model-object-state-deleted`

```typescript
"wme-data-model-object-state-deleted": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-added`

```typescript
"wme-data-model-objects-added": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-changed`

```typescript
"wme-data-model-objects-changed": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-removed`

```typescript
"wme-data-model-objects-removed": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
}
```
### `wme-data-model-objects-saved`

```typescript
"wme-data-model-objects-saved": {
  dataModelName: DataModelName ;
  objectIds: ( string | number ) [] ;
}
```
### `wme-editing-house-numbers`

```typescript
"wme-editing-house-numbers": { isEditingHouseNumbers: false }
```
### `wme-feature-editor-opened`

```typescript
"wme-feature-editor-opened": {
  featureType: 
  | "bigJunction"
  | "city"
  | "googlePlace"
  | "mapComment"
  | "node"
  | "permanentHazard"
  | "restrictedDrivingArea"
  | "segment"
  | "segmentSuggestion"
  | "venue" ;
}
```
### `wme-house-number-added`

```typescript
"wme-house-number-added": { houseNumberId: string }
```
### `wme-house-number-deleted`

```typescript
"wme-house-number-deleted": { houseNumberId: string }
```
### `wme-house-number-moved`

```typescript
"wme-house-number-moved": { houseNumberId: string }
```
### `wme-house-number-updated`

```typescript
"wme-house-number-updated": { houseNumberId: string }
```
### `wme-initialized`

```typescript
"wme-initialized": undefined
```
### `wme-layer-checkbox-toggled`

```typescript
"wme-layer-checkbox-toggled": { checked: boolean ; name: string }
```
### `wme-layer-feature-clicked`

```typescript
"wme-layer-feature-clicked": { featureId: string | number ; layerName: string }
```
### `wme-layer-feature-mouse-enter`

```typescript
"wme-layer-feature-mouse-enter": {
  featureId: string | number ;
  layerName: string ;
}
```
### `wme-layer-feature-mouse-leave`

```typescript
"wme-layer-feature-mouse-leave": {
  featureId: string | number ;
  layerName: string ;
}
```
### `wme-layer-visibility-changed`

```typescript
"wme-layer-visibility-changed": { layerName: string }
```
### `wme-logged-in`

```typescript
"wme-logged-in": undefined
```
### `wme-logged-out`

```typescript
"wme-logged-out": undefined
```
### `wme-map-data-loaded`

```typescript
"wme-map-data-loaded": undefined
```
### `wme-map-house-number-marker-added`

```typescript
"wme-map-house-number-marker-added": undefined
```
### `wme-map-initial-data-loaded`

```typescript
"wme-map-initial-data-loaded": undefined
```
### `wme-map-layer-added`

```typescript
"wme-map-layer-added": { layerName: string }
```
### `wme-map-layer-changed`

```typescript
"wme-map-layer-changed": { layerName: string }
```
### `wme-map-layer-removed`

```typescript
"wme-map-layer-removed": { layerName: string }
```
### `wme-map-mouse-click`

```typescript
"wme-map-mouse-click": SdkMouseEvent
```
### `wme-map-mouse-down`

```typescript
"wme-map-mouse-down": SdkMouseEvent
```
### `wme-map-mouse-move`

```typescript
"wme-map-mouse-move": SdkMouseEvent
```
### `wme-map-mouse-out`

```typescript
"wme-map-mouse-out": SdkMouseEvent
```
### `wme-map-mouse-up`

```typescript
"wme-map-mouse-up": SdkMouseEvent
```
### `wme-map-move`

```typescript
"wme-map-move": undefined
```
### `wme-map-move-end`

```typescript
"wme-map-move-end": undefined
```
### `wme-map-zoom-changed`

```typescript
"wme-map-zoom-changed": undefined
```
### `wme-no-edits`

```typescript
"wme-no-edits": undefined
```
### `wme-ready`

```typescript
"wme-ready": undefined
```
### `wme-save-finished`

```typescript
"wme-save-finished": { success: boolean }
```
### `wme-save-mode-changed`

```typescript
"wme-save-mode-changed": { saveMode: SaveMode }
```
### `wme-selection-changed`

```typescript
"wme-selection-changed": undefined
```
### `wme-sidebar-tab-opened`

```typescript
"wme-sidebar-tab-opened": { domId: string ; tabName: SidebarTabName }
```
### `wme-street-view-button-activated`

```typescript
"wme-street-view-button-activated": undefined
```
### `wme-street-view-button-deactivated`

```typescript
"wme-street-view-button-deactivated": undefined
```
### `wme-street-view-panel-visibility-changed`

```typescript
"wme-street-view-panel-visibility-changed": { isVisible: boolean }
```
### `wme-update-request-panel-opened`

```typescript
"wme-update-request-panel-opened": { updateRequestId: number }
```
### `wme-user-settings-changed`

```typescript
"wme-user-settings-changed": undefined
```
