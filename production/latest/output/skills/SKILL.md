# WME SDK Skill

You are an expert in the Waze Map Editor (WME) SDK. Use your deep knowledge to help developers build WME Tampermonkey scripts and extensions. Always use modern WME SDK APIs — never legacy `W`, `Waze`, or `OL`/`OpenLayers` objects unless no SDK alternative exists. Provide clear, concise code examples and best practices for working with the WME SDK. When referencing documentation, link to the latest stable version on the official WME site or the GitHub Pages mirror if local docs are unavailable.

---

## SDK Documentation

### Primary — Local (Offline, if repo is cloned)

Docs are at `../../output/docs/` relative to `output/skills/SKILL.md`:

| Document | Local Path |
|----------|------------|
| **Index & Overview** | `../../output/docs/index.md` |
| **Classes** | `../../output/docs/classes.md` |
| **Interfaces** | `../../output/docs/interfaces.md` |
| **Types** | `../../output/docs/types.md` |
| **Functions** | `../../output/docs/functions.md` |
| **Variables** | `../../output/docs/variables.md` |
| **Modules** | `../../output/docs/modules.md` |
| **WME SDK Typings** | `../../output/docs/wmeSDK_typedefs.d.md` |
| **GeoJSON Typings** | `../../output/docs/geojson_typeddefs.d.md` |
| **Getting Started** | `../../output/docs/how-to-get-started-with-the-wmeSDK.md` |
| **Migration Guide** | `../../output/docs/migration-guide.md` |
| **Changelog** | `../../output/docs/changelog.md` |
| **Turf.js Docs** | `../../output/docs/Turf-Docs.md` |
| **GeoJSON RFC 7946** | `../../output/docs/GeoJSON-Format-RFC-7946.md` |
| **Script Examples** | `../../output/docs/script-example-1.md` through `script-example-6.md` |

> **Beta SDK:** The `beta/latest/output/skills/SKILL.md` mirrors this structure but references `beta/latest/output/docs/` locally.

### Fallback — GitHub Pages (Online, when local docs unavailable)

| Document | URL |
|----------|-----|
| **Index & Overview** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/index.md |
| **Classes** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/classes.md |
| **Interfaces** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/interfaces.md |
| **Types** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/types.md |
| **Functions** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/functions.md |
| **Variables** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/variables.md |
| **Modules** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/modules.md |
| **WME SDK Typings** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/wmeSDK_typedefs.d.md |
| **GeoJSON Typings** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/geojson_typeddefs.d.md |
| **Getting Started** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/how-to-get-started-with-the-wmeSDK.md |
| **Migration Guide** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/migration-guide.md |
| **Changelog** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/changelog.md |
| **Turf.js Docs** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/Turf-Docs.md |
| **GeoJSON RFC 7946** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/GeoJSON-Format-RFC-7946.md |
| **Script Example 1** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/script-example-1.md |
| **Script Example 2** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/script-example-2.md |
| **Script Example 3** | https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/script-example-3.md |

> **Beta fallback:** Replace `production/latest` with `beta/latest` in any URL above.

---

## SDK Version

Current stable: **v2.343** (April 2026) | Live: https://www.waze.com/editor/sdk/ | Beta: https://beta.waze.com/editor/sdk/

---

## Script Initialization Template

Every WME Tampermonkey script starts the same way:

```javascript
// ==UserScript==
// @name         My WME Script
// @namespace    https://greasyfork.org/users/YOUR_ID
// @version      1.0.0
// @description  Description here
// @author       Your Name
// @match        https://www.waze.com/*/editor/*
// @match        https://www.waze.com/editor/*
// @match        https://beta.waze.com/*/editor/*
// @grant        none
// @require      https://greasyfork.org/scripts/YOUR_BOOTSTRAP_ID/code/bootstrap.js
// ==/UserScript==

(async () => {
  // Wait for WME SDK to be available
  const SDK = await window.getWmeSdk({ scriptId: 'my-script', scriptName: 'My WME Script' });

  SDK.Events.on({
    eventName: 'wme-ready',
    eventHandler: () => initialize(SDK)
  });

  if (SDK.State.isReady()) initialize(SDK);
})();

async function initialize(SDK) {
  console.log('WME SDK ready. Version:', SDK.getVersion());
  // Your script logic here
}
```

---

## Core SDK Classes Reference

### `SDK.Segments` — Road Segments

```javascript
SDK.Segments.getAll()                           // Segment[] — all loaded segments
SDK.Segments.getById({ segmentId: '123' })      // Segment | null
SDK.Segments.getSelected()                      // Segment[] — currently selected
SDK.Segments.addSegment({ geometry, ... })      // Add new segment
SDK.Segments.deleteSegment({ segmentId })       // Delete segment
SDK.Segments.updateSegment({ segmentId, ... })  // Update geometry/attributes
SDK.Segments.updateAddress({ segmentId, ... })  // Update street/city/country
SDK.Segments.addAlternateStreet({ segmentId, streetId })
SDK.Segments.splitSegment({ segmentId, geometry })
SDK.Segments.mergeSegments({ segmentIds })
SDK.Segments.hasPermissions({ segmentId, permission? })  // boolean
SDK.Segments.getVirtualNodes({ segmentId })
```

### `SDK.Nodes` — Junctions / Intersections

```javascript
SDK.Nodes.getAll()                              // Node[]
SDK.Nodes.getById({ nodeId: '123' })            // Node | null
SDK.Nodes.moveNode({ nodeId, geometry })
SDK.Nodes.allowNodeTurns({ nodeId })
SDK.Nodes.canEditTurns({ nodeId })              // boolean
```

### `SDK.Venues` — Points of Interest

```javascript
SDK.Venues.getAll()                             // Venue[]
SDK.Venues.getById({ venueId: '123' })          // Venue | null
SDK.Venues.getAddress({ venueId })              // VenueAddress
SDK.Venues.addVenue({ category, geometry })     // number (new ID)
SDK.Venues.deleteVenue({ venueId })
SDK.Venues.updateAddress({ venueId, ... })
SDK.Venues.getAllVenueCategories()              // VenueCategory[]
SDK.Venues.getVenueMainCategories()            // VenueCategory[]
SDK.Venues.getVenueSubCategories()             // VenueSubCategory[]
SDK.Venues.hasPermissions({ venueId, permission? })  // boolean
SDK.Venues.ChargingStation                      // ChargingStation sub-class
SDK.Venues.ParkingLot                          // ParkingLot sub-class
```

### `SDK.Map` — Map Control

```javascript
SDK.Map.getZoomLevel()                          // number
SDK.Map.getExtent()                             // BBox
SDK.Map.getLonLatFromPixel({ x, y })           // LonLat
SDK.Map.getMapPixelFromLonLat({ lon, lat })    // Pixel
SDK.Map.getMapViewportElement()                 // HTMLElement
SDK.Map.addLayer({ layerName, ... })           // Add custom layer
SDK.Map.removeLayer({ layerName })
SDK.Map.addFeaturesToLayer({ layerName, features })
SDK.Map.clearLayerFeatures({ layerName })
SDK.Map.setLayerVisibility({ layerName, visible })
```

### `SDK.Editing` — Selection & Editing State

```javascript
SDK.Editing.getSelection()                      // Selection | null
SDK.Editing.setSelection({ objectType, ids })   // Select features
SDK.Editing.clearSelection()                    // Deselect all
SDK.Editing.beginAction({ actionName })         // Start edit action
SDK.Editing.commitAction()                      // Commit changes
SDK.Editing.rollbackAction()                    // Cancel changes
SDK.Editing.save({ saveMode? })                 // Save to server
```

### `SDK.DataModel` — Generic Data Access

```javascript
SDK.DataModel.Segments.getAll()
SDK.DataModel.Segments.getById({ segmentId })
SDK.DataModel.Nodes.getAll()
SDK.DataModel.Junctions.getById({ junctionId })
SDK.DataModel.Cities.getAll()
SDK.DataModel.Cities.getById({ cityId })
SDK.DataModel.Cities.addCity({ name, stateId })
SDK.DataModel.Streets.addStreet({ cityId, name })
SDK.DataModel.Streets.getById({ streetId })
SDK.DataModel.Countries.getTopCountry()
SDK.DataModel.States.getTopState()
SDK.DataModel.Users.getUserProfileLink({ userId })
SDK.DataModel.MapUpdateRequests.getUpdateRequestDetails({ requestId })
SDK.DataModel.MapUpdateRequests.addComment({ requestId, text })
```

### `SDK.Events` — Event System

```javascript
SDK.Events.on({ eventName, eventHandler })      // Returns Subscription
SDK.Events.off(subscription)                    // Unsubscribe

// Key event names:
'wme-ready'                    // SDK fully initialized
'wme-selection-changed'        // User changed selection
'wme-map-move-end'             // Map panning finished
'wme-map-move'                 // Map panning (continuous)
'wme-map-layer-added'          // Layer added to map
'wme-map-layer-removed'        // Layer removed
'wme-map-mouse-click'          // Map clicked — { lat, lon, x, y }
'wme-map-data-loaded'          // New map tiles loaded
'wme-segment-changed'          // Segment modified
'wme-node-changed'             // Node modified
```

### `SDK.Sidebar` — UI Panel

```javascript
// Register a sidebar tab
const { tabLabel, tabPane } = await SDK.Sidebar.registerScriptTab();
// tabPane is the HTMLElement to fill with your UI
// tabLabel is the tab button element (set its innerHTML)
tabLabel.innerHTML = 'My Script';
tabPane.innerHTML = '<div>My UI</div>';
```

### `SDK.Shortcuts` — Keyboard Shortcuts

```javascript
SDK.Shortcuts.createShortcut({
  callback: () => doSomething(),
  description: 'My shortcut',
  shortcutKey: 'S',     // key letter
  shortcutId: 'myScript.doSomething'
});
```

### `SDK.LayerSwitcher` — Layer Toggle UI

```javascript
SDK.LayerSwitcher.addLayerCheckbox({
  layerName,
  label: 'My Layer',
  defaultChecked: true
});
```

### `SDK.Settings` — User Preferences

```javascript
SDK.Settings.getUserInfo()     // UserProfile
SDK.Settings.getUserRank()     // UserRank
```

### `SDK.States` — WME State

```javascript
SDK.State.isReady()            // boolean — safe to use SDK
SDK.State.isInEditMode()       // boolean
SDK.State.getSelectedCity()    // City | null
```

---

## Common Patterns

### Query and Filter

```javascript
// All segments on screen
const allSegments = SDK.Segments.getAll();

// Filter by road type
const freeways = allSegments.filter(s => s.roadTypeId === 3);

// Filter by lock rank
const highLocked = allSegments.filter(s => s.lockRank >= 4);

// Get selected segments
const selected = SDK.Editing.getSelection();
if (selected?.objectType === 'segment') {
  const segments = selected.ids.map(id =>
    SDK.Segments.getById({ segmentId: id })
  ).filter(Boolean);
}
```

### Event-Driven Logic

```javascript
// Always prefer events over polling
const sub = SDK.Events.on({
  eventName: 'wme-selection-changed',
  eventHandler: () => {
    const sel = SDK.Editing.getSelection();
    if (!sel) return;
    console.log('Selected:', sel.objectType, sel.ids);
  }
});

// Clean up when done
// SDK.Events.off(sub);
```

### Map Click Handler

```javascript
SDK.Events.on({
  eventName: 'wme-map-mouse-click',
  eventHandler: ({ lat, lon }) => {
    console.log(`Clicked at ${lat}, ${lon}`);
  }
});
```

### Edit with Error Handling

```javascript
async function updateSegmentAddress(segmentId, cityName) {
  try {
    SDK.Editing.beginAction({ actionName: 'Update Address' });
    SDK.DataModel.Segments.updateAddress({
      segmentId,
      attributes: { primaryStreetCityName: cityName }
    });
    await SDK.Editing.save();
    console.log('Saved successfully');
  } catch (err) {
    SDK.Editing.rollbackAction();
    if (err instanceof SDK.WMEError) {
      console.error('WME SDK error:', err.message);
    } else {
      throw err;
    }
  }
}
```

### Add a Custom Map Layer

```javascript
SDK.Map.addLayer({ layerName: 'myScript.overlay' });

// Add GeoJSON features to it
SDK.Map.addFeaturesToLayer({
  layerName: 'myScript.overlay',
  features: [
    {
      type: 'Feature',
      geometry: { type: 'Point', coordinates: [lon, lat] },
      properties: { label: 'My Point' },
      style: { fillColor: '#ff0000', strokeColor: '#000000', pointRadius: 8 }
    }
  ]
});
```

### Register Sidebar Tab

```javascript
async function setupUI(SDK) {
  const { tabLabel, tabPane } = await SDK.Sidebar.registerScriptTab();
  tabLabel.innerHTML = 'My Script';
  tabPane.innerHTML = `
    <div style="padding:10px">
      <h3>My Script</h3>
      <button id="myBtn">Do Something</button>
    </div>
  `;
  document.getElementById('myBtn').addEventListener('click', () => {
    // action here
  });
}
```

---

## Error Types

```javascript
SDK.WMEError            // Base error — all SDK errors extend this
SDK.ValidationError     // Input validation failed
SDK.DataModelNotFoundError  // getById returned nothing
SDK.InvalidStateError   // Operation not valid in current WME state
```

---

## Key Deprecated API → SDK Replacements

| Old (Legacy) | New (SDK) |
|---|---|
| `W.model.segments.get(id)` | `SDK.DataModel.Segments.getById({ segmentId: id })` |
| `W.model.segments.getByAttributes({...})` | `SDK.DataModel.Segments.getAll().filter(...)` |
| `W.selectionManager.getSelectedFeatures()` | `SDK.Editing.getSelection()` |
| `W.selectionManager.selectFeatures(features)` | `SDK.Editing.setSelection({ objectType, ids })` |
| `W.selectionManager.unselectFeatures()` | `SDK.Editing.clearSelection()` |
| `W.map.getZoom()` | `SDK.Map.getZoomLevel()` |
| `W.map.addUniqueLayer(layer)` | `SDK.Map.addLayer({ layerName, ... })` |
| `W.map.getLonLatFromPixel(px)` | `SDK.Map.getLonLatFromPixel({ x, y })` |
| `W.map.getExtent()` | `SDK.Map.getExtent()` |
| `W.map.events.register('moveend', ...)` | `SDK.Events.on({ eventName: 'wme-map-move-end', ... })` |
| `W.map.events.register('click', ...)` | `SDK.Events.on({ eventName: 'wme-map-mouse-click', ... })` |
| `W.userscripts.registerSidebarTab(...)` | `await SDK.Sidebar.registerScriptTab()` |
| `W.Config.venues` | `SDK.DataModel.Venues.getAllVenueCategories()` |
| `W.loginManager` | `SDK.Settings.getUserInfo()` |

---

## Rules to Always Follow

1. **Never** use `W`, `Waze`, `OL`, `OpenLayers`, or `I18n` objects directly.
2. **Always** await `getWmeSdk()` before accessing any SDK APIs.
3. **Always** check `SDK.State.isReady()` before running initialization logic.
4. **Always** use `SDK.Editing.beginAction` / `commitAction` / `rollbackAction` for edits.
5. **Always** unsubscribe from events when a feature is disabled or torn down.
6. **Prefer** event-driven logic over polling or timeouts.
7. **Only** act on visible/selected features — avoid bulk operations on all map data.
8. Scripts run in **Tampermonkey** — use `@match` patterns and `@grant none` unless grants are needed.

---

## Resources

- **WME SDK Docs (Stable):** https://www.waze.com/editor/sdk/
- **WME SDK Docs (Beta):** https://beta.waze.com/editor/sdk/
- **WME-SDK-Mirror (GitHub):** https://github.com/JS55CT/WME-SDK-Mirror
- **Mirror Docs (Production):** https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/
- **Mirror Docs (Beta):** https://js55ct.github.io/WME-SDK-Mirror/beta/latest/output/docs/
- **Waze Map Editor:** https://www.waze.com/editor/

---

**SDK Version:** v2.343 (April 2026)
**Repository:** WME-SDK-Mirror (JS55CT)
**Last Updated:** April 2026
