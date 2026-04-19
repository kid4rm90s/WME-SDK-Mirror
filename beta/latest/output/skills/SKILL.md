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
| **Script Examples** | `../../output/docs/script-example-1.md` through `script-example-8.md` |

> **Beta SDK:** The `beta/latest/output/skills/SKILL.md` mirrors this structure but references `beta/latest/output/docs/` locally.

### Fallback — GitHub Pages (Online, when local docs unavailable)

| Document | URL |
|----------|-----|
| **Index & Overview** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/index.md |
| **Classes** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/classes.md |
| **Interfaces** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/interfaces.md |
| **Types** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/types.md |
| **Functions** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/functions.md |
| **Variables** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/variables.md |
| **Modules** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/modules.md |
| **WME SDK Typings** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/wmeSDK_typedefs.d.md |
| **GeoJSON Typings** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/geojson_typeddefs.d.md |
| **Getting Started** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/how-to-get-started-with-the-wmeSDK.md |
| **Migration Guide** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/migration-guide.md |
| **Changelog** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/changelog.md |
| **Turf.js Docs** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/Turf-Docs.md |
| **GeoJSON RFC 7946** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/GeoJSON-Format-RFC-7946.md |
| **Script Example 1** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/script-example-1.md |
| **Script Example 2** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/script-example-2.md |
| **Script Example 3** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/script-example-3.md |
| **Script Example 4** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/script-example-4.md |
| **Script Example 5** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/script-example-5.md |
| **Script Example 6** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/script-example-6.md |
| **Script Example 7** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/script-example-7.md |
| **Script Example 8** | https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/script-example-8.md |

> **Production fallback:** Replace `beta/latest` with `production/latest` in any URL above.

---

## SDK Version

Current stable: **v2.343** (April 2026) | Live: https://www.waze.com/editor/sdk/ | Beta: https://beta.waze.com/editor/sdk/

---

## Script Initialization Template

### How SDK initialization actually works

WME injects `window.SDK_INITIALIZED` (a Promise) when the page loads. Your script must
wait for that Promise before calling `getWmeSdk()`. The `@include` regex pattern is the
correct way to match both www and beta WME.

**`getWmeSdk()` is synchronous** — it does not return a Promise. The async part is waiting
for `SDK_INITIALIZED` first.

**`wmeSDK.State.isReady`** is a **boolean property**, not a function. Do not call it as
`isReady()`.

### Simple pattern (no UI bootstrap polling needed)

```javascript
// ==UserScript==
// @name         My WME Script
// @namespace    https://greasyfork.org/users/YOUR_ID
// @version      1.0.0
// @description  Description here
// @author       Your Name
// @include      /^https:\/\/(www|beta)\.waze\.com\/(?!user\/)(.{2,6}\/)?editor.*$/
// @grant        GM_info
// @grant        unsafeWindow
// @require      https://greasyfork.org/scripts/560385/code/WazeToastr.js
// ==/UserScript==

/* global getWmeSdk, WazeToastr */
(function main() {
  'use strict';

  const scriptName = GM_info.script.name;
  let wmeSDK;

  // SDK_INITIALIZED is a Promise injected by WME. Wait for it before calling getWmeSdk().
  (unsafeWindow || window).SDK_INITIALIZED.then(async () => {
    wmeSDK = getWmeSdk({ scriptId: 'my-script', scriptName: 'My WME Script' });

    // Option A: listen for the ready event
    wmeSDK.Events.on({
      eventName: 'wme-ready',
      eventHandler: () => initialize()
    });

    // Also call immediately if SDK is already ready (e.g. script injected late)
    if (wmeSDK.State.isReady) initialize();
  });

  function initialize() {
    console.log(`${scriptName}: ready`);
    // Your script logic here
  }
})();
```

### Bootstrap polling pattern (for scripts that need the edit panel / country to be ready)

Some scripts require additional WME state before initializing (e.g. `#edit-panel` in the
DOM, `getTopCountry()` returning a value). Use a polling bootstrap for this:

```javascript
(unsafeWindow || window).SDK_INITIALIZED.then(() => {
  wmeSDK = getWmeSdk({ scriptId: 'my-script', scriptName: 'My WME Script' });
  bootstrap();
});

function bootstrap() {
  // Poll until the edit panel exists AND the top country is available
  if (!document.getElementById('edit-panel') || !wmeSDK.DataModel.Countries.getTopCountry()) {
    setTimeout(bootstrap, 250);
    return;
  }
  // Now safe to initialize fully
  if (wmeSDK.State.isReady) init();
  else wmeSDK.Events.once({ eventName: 'wme-ready' }).then(init);
}

function init() {
  // Full initialization: shortcuts, sidebar, event listeners, etc.
}
```

### Common `@grant` directives

```javascript
// @grant  GM_info          // Access script metadata (name, version, etc.)
// @grant  GM_getValue      // Persistent key/value storage
// @grant  GM_setValue      // Persistent key/value storage
// @grant  GM_xmlhttpRequest // Cross-origin HTTP requests
// @grant  unsafeWindow     // Access the page's real window object (needed for SDK_INITIALIZED)
```

> **Note:** If you only need `unsafeWindow` access, use `(unsafeWindow || window)` as a
> safe fallback when the grant is absent.

---

## Core SDK Classes Reference

> All APIs live under the `wmeSDK` object returned by `getWmeSdk()`. The top-level
> namespaces are `DataModel`, `Editing`, `Events`, `Map`, `Shortcuts`, `Sidebar`,
> `State`, `LayerSwitcher`. There is no direct `wmeSDK.Segments.*` shortcut —
> always use the full path `wmeSDK.DataModel.Segments.*`.

### `wmeSDK.DataModel.Segments` — Road Segments

```javascript
wmeSDK.DataModel.Segments.getAll()                              // Segment[]
wmeSDK.DataModel.Segments.getById({ segmentId })               // Segment | null
wmeSDK.DataModel.Segments.getAddress({ segmentId })            // Address object
wmeSDK.DataModel.Segments.getConnectedSegments({ segmentId, reverseDirection }) // Segment[]
wmeSDK.DataModel.Segments.addSegment({ geometry, roadType })   // new segment ID
wmeSDK.DataModel.Segments.deleteSegment({ segmentId })
wmeSDK.DataModel.Segments.updateSegment({ segmentId, roadType?, lockRank?, fwdSpeedLimit?,
  revSpeedLimit?, geometry?, flagAttributes?, elevationLevel?, direction? })
wmeSDK.DataModel.Segments.updateAddress({ segmentId, primaryStreetId, alternateStreetIds? })
wmeSDK.DataModel.Segments.splitSegment({ segmentId, geometry })
wmeSDK.DataModel.Segments.hasPermissions({ segmentId, permission? })  // boolean
```

### `wmeSDK.DataModel.Streets`

```javascript
wmeSDK.DataModel.Streets.getAll()                              // Street[]
wmeSDK.DataModel.Streets.getById({ streetId })                 // Street | null
wmeSDK.DataModel.Streets.getStreet({ cityId, streetName })     // Street | null
wmeSDK.DataModel.Streets.addStreet({ streetName, cityId })     // Street
```

### `wmeSDK.DataModel.Cities`

```javascript
wmeSDK.DataModel.Cities.getAll()                               // City[]
wmeSDK.DataModel.Cities.getById({ cityId })                    // City | null
wmeSDK.DataModel.Cities.getTopCity()                           // City — default city for current viewport
wmeSDK.DataModel.Cities.getCity({ cityName, countryId })       // City | null
wmeSDK.DataModel.Cities.addCity({ cityName, countryId? })      // City
```

### `wmeSDK.DataModel.Countries` / `States`

```javascript
wmeSDK.DataModel.Countries.getTopCountry()   // Country — top country for current viewport
wmeSDK.DataModel.States.getTopState()        // State | null
```

### `wmeSDK.DataModel.Turns`

```javascript
wmeSDK.DataModel.Turns.canEditTurnsThroughNode({ nodeId })     // boolean
wmeSDK.DataModel.Turns.getTurnsThroughNode({ nodeId })         // Turn[]
wmeSDK.DataModel.Turns.updateTurn({ turnId, isAllowed })
```

### `wmeSDK.DataModel.Venues` — Points of Interest

```javascript
wmeSDK.DataModel.Venues.getAll()
wmeSDK.DataModel.Venues.getById({ venueId })
wmeSDK.DataModel.Venues.getAddress({ venueId })
wmeSDK.DataModel.Venues.addVenue({ category, geometry })
wmeSDK.DataModel.Venues.deleteVenue({ venueId })
wmeSDK.DataModel.Venues.updateAddress({ venueId, ... })
wmeSDK.DataModel.Venues.getAllVenueCategories()
wmeSDK.DataModel.Venues.getVenueMainCategories()
wmeSDK.DataModel.Venues.getVenueSubCategories()
```

### `wmeSDK.DataModel.HouseNumbers`

```javascript
wmeSDK.DataModel.HouseNumbers.addHouseNumber({ segmentId, number, lon, lat })
```

### `wmeSDK.DataModel.MapUpdateRequests`

```javascript
wmeSDK.DataModel.MapUpdateRequests.getUpdateRequestDetails({ requestId })
wmeSDK.DataModel.MapUpdateRequests.addComment({ requestId, text })
```

### `wmeSDK.Map` — Map Control

```javascript
wmeSDK.Map.getZoomLevel()                                // number
wmeSDK.Map.getMapExtent()                                // [west, south, east, north]
wmeSDK.Map.getMapCenter()                                // { lon, lat }
wmeSDK.Map.setMapCenter({ lon, lat })
wmeSDK.Map.getMapViewportElement()                       // HTMLElement — overlay container
wmeSDK.Map.getMapPixelFromLonLat({ lonLat: { lon, lat } })  // { x, y } — geo → screen px
wmeSDK.Map.getLonLatFromMapPixel({ x, y })               // { lon, lat }
wmeSDK.Map.addLayer({ layerName })
wmeSDK.Map.removeLayer({ layerName })
wmeSDK.Map.addFeaturesToLayer({ layerName, features })
wmeSDK.Map.removeAllFeaturesFromLayer({ layerName })     // also: clearLayerFeatures
wmeSDK.Map.redrawLayer({ layerName })
wmeSDK.Map.setLayerVisibility({ layerName, visible })
wmeSDK.Map.isLayerVisible({ layerName })                 // boolean
```

### `wmeSDK.Editing` — Selection & Editing State

```javascript
wmeSDK.Editing.getSelection()                      // { objectType, ids } | null
wmeSDK.Editing.setSelection({ selection: { objectType, ids } })
wmeSDK.Editing.clearSelection()
wmeSDK.Editing.save()                              // Save to server (no beginAction needed for simple saves)
```

### `wmeSDK.State`

```javascript
wmeSDK.State.isReady            // boolean PROPERTY (not a function — do NOT call as isReady())
wmeSDK.State.getUserInfo()      // { rank, ... } — current user's profile and rank (0-based: rank 2 = L3)
```

### `wmeSDK.Events` — Event System

```javascript
wmeSDK.Events.on({ eventName, eventHandler })           // Subscribe; returns unsubscribe fn
wmeSDK.Events.once({ eventName })                       // Returns a Promise that resolves once
wmeSDK.Events.trackLayerEvents({ layerName })           // Activate layer-click events for a layer
wmeSDK.Events.stopLayerEventsTracking({ layerName })
wmeSDK.Events.trackDataModelEvents({ dataModelName })   // Activate datamodel change events
wmeSDK.Events.stopDataModelEventsTracking({ dataModelName })

// Key event names:
'wme-ready'                          // SDK fully initialized (use Events.once for one-shot)
'wme-selection-changed'              // User changed selection
'wme-map-move'                       // Map panning (continuous, fires frequently)
'wme-map-move-end'                   // Map panning finished
'wme-map-zoom-changed'               // Map zoom level changed
'wme-map-layer-added'
'wme-map-layer-removed'
'wme-map-mouse-click'                // { lat, lon, x, y }
'wme-map-data-loaded'                // New map tiles loaded
'wme-layer-visibility-changed'       // { layerName, visible }
'wme-layer-feature-clicked'          // Feature on a tracked layer was clicked
'wme-data-model-objects-added'
'wme-data-model-objects-removed'
'wme-data-model-objects-saved'
'wme-after-undo'
'wme-after-redo-clear'
```

### `wmeSDK.Sidebar` — UI Panel

```javascript
// Register a sidebar tab (returns a Promise)
const { tabLabel, tabPane } = await wmeSDK.Sidebar.registerScriptTab();
tabLabel.innerHTML = 'My Script';   // Tab button text
tabPane.innerHTML = '<div>...</div>'; // Tab content area
```

### `wmeSDK.Shortcuts` — Keyboard Shortcuts

```javascript
wmeSDK.Shortcuts.createShortcut({
  callback: () => doSomething(),
  description: 'My shortcut description',
  shortcutId: 'myScript.action',      // unique ID
  shortcutKeys: 'G',                  // key or combo: 'G', 'S+1', 'A+R', 'C+S'
});
wmeSDK.Shortcuts.deleteShortcut({ shortcutId })
wmeSDK.Shortcuts.isShortcutRegistered({ shortcutId })   // boolean — check before creating
```

### `wmeSDK.LayerSwitcher` — Layer Toggle UI

```javascript
wmeSDK.LayerSwitcher.addLayerCheckbox({
  layerName,
  label: 'My Layer',
  defaultChecked: true
});
```

### `SDK.Settings` — User Preferences



---

## WazeToastr — Toast Notifications

WazeToastr is a community library commonly used in WME scripts for user feedback.
Add it as a `@require` and declare it in the `/* global */` comment.

```javascript
// @require  https://greasyfork.org/scripts/560385/code/WazeToastr.js
/* global WazeToastr */
```

```javascript
WazeToastr.Alerts.success(scriptName, 'Saved successfully!', false, false, 3000);
WazeToastr.Alerts.info(scriptName, 'Summary line 1<br>Summary line 2', false, false, 5000);
WazeToastr.Alerts.warning(scriptName, 'Something looks off', false, false, 4000);
WazeToastr.Alerts.error(scriptName, 'Operation failed');

// Confirmation dialog (callback-based)
WazeToastr.Alerts.confirm(scriptName, 'Are you sure?', onConfirm, onCancel, 'Yes', 'Cancel');

// Text prompt
WazeToastr.Alerts.prompt(scriptName, 'Enter a value:', onSubmit, onCancel, 'OK', 'Cancel');
```

Parameters for `success / info / warning / error`:
`(scriptName, message, sticky?, clickThrough?, durationMs?)`

---

## Common Patterns

### Query and Filter Segments

```javascript
// All segments on screen
const allSegments = wmeSDK.DataModel.Segments.getAll();

// Filter by road type
const freeways = allSegments.filter(s => s.roadType === 3);

// Filter by lock rank
const highLocked = allSegments.filter(s => s.lockRank >= 4);

// Get selected segments
const selected = wmeSDK.Editing.getSelection();
if (selected?.objectType === 'segment') {
  const segments = selected.ids.map(id =>
    wmeSDK.DataModel.Segments.getById({ segmentId: id })
  ).filter(Boolean);
}
```

### Event-Driven Logic

```javascript
// Always prefer events over polling
wmeSDK.Events.on({
  eventName: 'wme-selection-changed',
  eventHandler: () => {
    const sel = wmeSDK.Editing.getSelection();
    if (!sel) return;
    console.log('Selected:', sel.objectType, sel.ids);
  }
});

// One-shot event (returns Promise)
wmeSDK.Events.once({ eventName: 'wme-ready' }).then(() => init());
```

### Map Click Handler

```javascript
wmeSDK.Events.on({
  eventName: 'wme-map-mouse-click',
  eventHandler: ({ lat, lon }) => {
    console.log(`Clicked at ${lat}, ${lon}`);
  }
});
```

### Segment Address Update (city + street resolution)

```javascript
// Always resolve or create the Street object before calling updateAddress.
// Never pass raw strings — updateAddress takes IDs.
function setSegmentAddress(segmentId, streetName) {
  const city = wmeSDK.DataModel.Cities.getTopCity();
  let street = wmeSDK.DataModel.Streets.getStreet({ cityId: city.id, streetName })
             || wmeSDK.DataModel.Streets.addStreet({ streetName, cityId: city.id });
  wmeSDK.DataModel.Segments.updateAddress({
    segmentId,
    primaryStreetId: street.id,
    alternateStreetIds: []
  });
}

// Clear street name (set to "None")
function clearSegmentStreet(segmentId) {
  const city = wmeSDK.DataModel.Cities.getAll().find(c => c.isEmpty)
             || wmeSDK.DataModel.Cities.addCity({ cityName: '' });
  let st = wmeSDK.DataModel.Streets.getStreet({ cityId: city.id, streetName: '' })
         || wmeSDK.DataModel.Streets.addStreet({ streetName: '', cityId: city.id });
  wmeSDK.DataModel.Segments.updateAddress({ segmentId, primaryStreetId: st.id, alternateStreetIds: [] });
}
```

### Update Segment Properties

```javascript
// Road type, lock, speed — pass only the properties you want to change
wmeSDK.DataModel.Segments.updateSegment({
  segmentId: id,
  roadType: 1,       // street
  lockRank: 2,       // L3 (0-based: lockRank 0 = L1, lockRank 5 = L6)
  fwdSpeedLimit: 50,
  revSpeedLimit: 50,
});

// Flag attributes (note: some flags like 'unpaved' may not reliably read back
// immediately after writing — use DOM chip clicks as a fallback when needed)
wmeSDK.DataModel.Segments.updateSegment({
  segmentId: id,
  flagAttributes: { unpaved: true }
});
```

### Enable All Turns Through a Node

```javascript
function enableAllTurnsForSegment(segmentId) {
  const seg = wmeSDK.DataModel.Segments.getById({ segmentId });
  [seg.fromNodeId, seg.toNodeId].filter(Boolean).forEach(nodeId => {
    if (!wmeSDK.DataModel.Turns.canEditTurnsThroughNode({ nodeId })) return;
    wmeSDK.DataModel.Turns.getTurnsThroughNode({ nodeId }).forEach(turn => {
      if (!turn.isAllowed) wmeSDK.DataModel.Turns.updateTurn({ turnId: turn.id, isAllowed: true });
    });
  });
}
```

### Staggered Multi-Property Updates

When applying several properties to a segment, stagger them with small delays so WME
can process each change before the next is applied:

```javascript
const delayedUpdate = (fn, delay) =>
  new Promise(resolve => setTimeout(() => { fn(); resolve(); }, delay));

async function applyAllOptions(segmentId) {
  const ops = [];
  ops.push(delayedUpdate(() =>
    wmeSDK.DataModel.Segments.updateSegment({ segmentId, roadType: 1 }), 200));
  ops.push(delayedUpdate(() =>
    wmeSDK.DataModel.Segments.updateSegment({ segmentId, lockRank: 2 }), 300));
  ops.push(delayedUpdate(() =>
    wmeSDK.DataModel.Segments.updateSegment({ segmentId, fwdSpeedLimit: 50, revSpeedLimit: 50 }), 400));
  await Promise.all(ops);
  wmeSDK.Editing.save();
}
```

### Add a Custom Map Overlay (DOM-based, for fast RAF tracking)

For overlays that need smooth pan-following (e.g. length labels), use a DOM `<div>`
container appended to the map viewport and reposition with RAF:

```javascript
let myLabels = []; // [{ lon, lat, el }]
let container;

function initOverlay() {
  container = document.createElement('div');
  Object.assign(container.style, {
    position: 'absolute', top: '0', left: '0',
    width: '100%', height: '100%', pointerEvents: 'none', zIndex: '1000'
  });
  wmeSDK.Map.getMapViewportElement().appendChild(container);

  wmeSDK.Events.on({ eventName: 'wme-map-move', eventHandler: () =>
    requestAnimationFrame(updateLabelPositions) });
  wmeSDK.Events.on({ eventName: 'wme-map-move-end', eventHandler: rebuildLabels });
  wmeSDK.Events.on({ eventName: 'wme-map-zoom-changed', eventHandler: rebuildLabels });
}

function updateLabelPositions() {
  myLabels.forEach(({ lon, lat, el }) => {
    const px = wmeSDK.Map.getMapPixelFromLonLat({ lonLat: { lon, lat } });
    el.style.left = px.x + 'px';
    el.style.top  = px.y + 'px';
  });
}
```

### Add a Custom SDK Layer (GeoJSON features + click events)

```javascript
wmeSDK.Map.addLayer({ layerName: 'myScript.overlay' });
wmeSDK.Events.trackLayerEvents({ layerName: 'myScript.overlay' });

wmeSDK.Map.addFeaturesToLayer({
  layerName: 'myScript.overlay',
  features: [{
    type: 'Feature',
    geometry: { type: 'Point', coordinates: [lon, lat] },
    properties: { id: '123' },
    style: { fillColor: '#ff0000', strokeColor: '#000000', pointRadius: 8 }
  }]
});

wmeSDK.Events.on({
  eventName: 'wme-layer-feature-clicked',
  eventHandler: ({ feature }) => console.log('Clicked:', feature.properties.id)
});

// Cleanup
wmeSDK.Events.stopLayerEventsTracking({ layerName: 'myScript.overlay' });
wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: 'myScript.overlay' });
```

### Register Sidebar Tab

```javascript
async function setupUI() {
  const { tabLabel, tabPane } = await wmeSDK.Sidebar.registerScriptTab();
  tabLabel.innerHTML = 'My Script';
  tabPane.innerHTML = `<div style="padding:10px"><h3>My Script</h3></div>`;
}
```

### MutationObserver on Edit Panel

Inject a button into WME's segment edit panel when it opens:

```javascript
new MutationObserver(mutations => {
  mutations.forEach(({ addedNodes }) => {
    addedNodes.forEach(node => {
      if (node.nodeType !== Node.ELEMENT_NODE) return;
      const editPanel = node.querySelector('#segment-edit-general');
      if (!editPanel || editPanel.parentNode.querySelector('[data-myscript-btn]')) return;
      const btn = document.createElement('wz-button');
      btn.setAttribute('data-myscript-btn', 'true');
      btn.textContent = 'My Action';
      btn.addEventListener('mousedown', () => doAction());
      editPanel.parentNode.insertBefore(btn, editPanel);
    });
  });
}).observe(document.getElementById('edit-panel'), { childList: true, subtree: true });
```

### Legacy Keyboard Shortcuts (W.accelerators)

When you need feature-toggle shortcuts to appear in WME's built-in keyboard shortcuts UI,
use the legacy `W.accelerators` / `I18n` system. The SDK `Shortcuts` API does not yet
expose the group/toggle UI:

```javascript
function registerLegacyShortcut(groupName, groupLabel, actionId, description, callback) {
  try { I18n.translations[I18n.locale].keyboard_shortcuts.groups[groupName].members.length; }
  catch (e) {
    W.accelerators.Groups[groupName] = [];
    W.accelerators.Groups[groupName].members = [];
    I18n.translations[I18n.locale].keyboard_shortcuts.groups[groupName] = {
      description: groupLabel, members: {}
    };
  }
  I18n.translations[I18n.locale].keyboard_shortcuts.groups[groupName].members[actionId] = description;
  W.accelerators.addAction(actionId, { group: groupName });
  W.accelerators._registerShortcuts({ '-1': actionId });
  W.accelerators.events.register(actionId, null, callback);
}
```

> This is one of the few cases where direct `W.*` / `I18n` usage is acceptable because
> the WME SDK does not yet provide an equivalent group/toggle shortcut registration API.

### Rank Check

```javascript
const userInfo = wmeSDK.State.getUserInfo();
// userInfo.rank is 0-based (0 = L1, 1 = L2, 2 = L3 ... 5 = L6)
if (userInfo.rank < 2) { // require L3+
  WazeToastr.Alerts.warning(scriptName, 'Requires rank L3 or higher.');
  return;
}
```

---

## Error Types

```javascript
wmeSDK.DataModelNotFoundError  // getById returned nothing — check before using
```

---

## Key Deprecated API → SDK Replacements

| Old (Legacy) | New (SDK) |
|---|---|
| `W.model.segments.get(id)` | `wmeSDK.DataModel.Segments.getById({ segmentId: id })` |
| `W.model.segments.getByAttributes({...})` | `wmeSDK.DataModel.Segments.getAll().filter(...)` |
| `W.selectionManager.getSelectedFeatures()` | `wmeSDK.Editing.getSelection()` |
| `W.selectionManager.selectFeatures(features)` | `wmeSDK.Editing.setSelection({ selection: { objectType, ids } })` |
| `W.selectionManager.unselectFeatures()` | `wmeSDK.Editing.clearSelection()` |
| `W.map.getZoom()` | `wmeSDK.Map.getZoomLevel()` |
| `W.map.addUniqueLayer(layer)` | `wmeSDK.Map.addLayer({ layerName })` |
| `W.map.getLonLatFromPixel(px)` | `wmeSDK.Map.getLonLatFromMapPixel({ x, y })` |
| `W.map.getExtent()` | `wmeSDK.Map.getMapExtent()` |
| `W.map.events.register('moveend', ...)` | `wmeSDK.Events.on({ eventName: 'wme-map-move-end', ... })` |
| `W.map.events.register('click', ...)` | `wmeSDK.Events.on({ eventName: 'wme-map-mouse-click', ... })` |
| `W.userscripts.registerSidebarTab(...)` | `await wmeSDK.Sidebar.registerScriptTab()` |
| `W.loginManager` | `wmeSDK.State.getUserInfo()` |
| `W.model.cities.getTopCity()` | `wmeSDK.DataModel.Cities.getTopCity()` |
| `W.model.countries.getTopCountry()` | `wmeSDK.DataModel.Countries.getTopCountry()` |

---

## Rules to Always Follow

1. **Prefer SDK APIs** over legacy `W`, `Waze`, `OL`, or `OpenLayers` objects. Use legacy
   `W.accelerators` / `I18n` only when no SDK equivalent exists (e.g. group-based keyboard
   shortcut registration in WME's shortcuts UI).
2. **Never `await getWmeSdk()`** — it is synchronous. Wait for `SDK_INITIALIZED` instead.
3. **`wmeSDK.State.isReady` is a boolean property**, not a function. Do not call it as `isReady()`.
4. **Always check `wmeSDK.State.isReady`** (or listen for `wme-ready`) before running init logic.
5. **Declare `/* global getWmeSdk, WazeToastr */`** so linters don't flag injected globals.
6. **Prefer event-driven logic** over polling or `setInterval`. Use `once()` for one-shot events.
7. **Unsubscribe from events and disconnect observers** when a feature is disabled or torn down.
8. **Use `@include` with regex** to match both www and beta WME: `/^https:\/\/(www|beta)\.waze\.com\/(?!user\/)(.{2,6}\/)?editor.*$/`
9. Scripts run in **Tampermonkey** — declare all required `@grant` directives; `@grant unsafeWindow` is needed to access `SDK_INITIALIZED`.

---

## Resources

- **WME SDK Docs (Stable):** https://www.waze.com/editor/sdk/
- **WME SDK Docs (Beta):** https://beta.waze.com/editor/sdk/
- **WME-SDK-Mirror (GitHub):** https://github.com/JS55CT/WME-SDK-Mirror
- **Mirror Docs (Production):** https://kid4rm90s.github.io/WME-SDK-Mirror/production/latest/output/docs/
- **Mirror Docs (Beta):** https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/
- **Waze Map Editor:** https://www.waze.com/editor/

---

**SDK Version:** v2.343 (April 2026)
**Repository:** WME-SDK-Mirror (JS55CT)
**Last Updated:** April 2026
