---
title: SDK.SdkEventBus class
source: classes/index.SDK.SdkEventBus.html
created: 2026-04-23
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Class SdkEventBus

```typescript
clear () : void
```
Event bus for SDK events. For the list of events and their payload checkSdkEvents.
## Methods
### `clear`

```typescript
clear () : void
```

### `off`

```typescript
off < EventName extends keyof SdkEvents > (
  args: {
  eventHandler: EventHandler < SdkEvents [ EventName ] > ;
  eventName: EventName ;
} ,
  ) : void
```

### `on`

```typescript
on < EventName extends keyof SdkEvents > (
  args: {
  eventHandler: EventHandler < SdkEvents [ EventName ] > ;
  eventName: EventName ;
} ,
  ) : () = > void
```
a cleanup function that will unregister the handler from the event.
### `once`

```typescript
once < EventName extends keyof SdkEvents > (
  args: { eventName: EventName } ,
  ) : Promise < SdkEvents [ EventName ] >
```
a promise that gets resolved once the event happens.
### `stopDataModelEventsTracking`

```typescript
stopDataModelEventsTracking ( args: { dataModelName: DataModelName } ) : void
```

### `stopLayerEventsTracking`

```typescript
stopLayerEventsTracking ( args: { layerName: string } ) : void
```

### `trackDataModelEvents`

```typescript
trackDataModelEvents ( args: { dataModelName: DataModelName } ) : void
```

### `trackLayerEvents`

```typescript
trackLayerEvents ( args: { layerName: string } ) : void
```
