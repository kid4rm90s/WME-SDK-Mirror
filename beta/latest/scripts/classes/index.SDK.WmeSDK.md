---
title: SDK.WmeSDK class
source: classes/index.SDK.WmeSDK.html
created: 2026-08-05
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class WmeSDK

```typescript
DataModel: DataModel = ...
```
WME SDK container.
## Properties
### **Readonly** `DataModel`

```typescript
DataModel: DataModel = ...
```
### **Readonly** `Editing`

```typescript
Editing: Editing = ...
```
### **Readonly** `Errors`

```typescript
Errors: {
  DataModelNotFoundError: typeof DataModelNotFoundError ;
  InvalidStateError: typeof InvalidStateError ;
  ValidationError: typeof ValidationError ;
  WMEError: typeof WMEError ;
}
```
### **Readonly** `Events`

```typescript
Events: SdkEventBus = ...
```
### **Readonly** `LayerSwitcher`

```typescript
LayerSwitcher: LayerSwitcher = ...
```
### **Readonly** `Map`

```typescript
Map: Map = ...
```
### **Readonly** `Settings`

```typescript
Settings: Settings = ...
```
### **Readonly** `Shortcuts`

```typescript
Shortcuts: Shortcuts = ...
```
### **Readonly** `Sidebar`

```typescript
Sidebar: Sidebar = ...
```
### **Readonly** `State`

```typescript
State: WmeState = ...
```
## Methods
### `getScriptId`

```typescript
getScriptId () : string
```
the script id this sdk instance was initialized with
### `getScriptName`

```typescript
getScriptName () : string
```
the script name this sdk instance was initialized with
### `getSDKVersion`

```typescript
getSDKVersion () : string
```
the current version of this SDK
### `getWMEBackEndVersion`

```typescript
getWMEBackEndVersion () : Promise < string >
```
the current version of the WME backend
### `getWMEVersion`

```typescript
getWMEVersion () : string
```
the current version of the WME frontend
### `isBetaEnvironment`

```typescript
isBetaEnvironment () : boolean
```
true if running in the WME beta environment
