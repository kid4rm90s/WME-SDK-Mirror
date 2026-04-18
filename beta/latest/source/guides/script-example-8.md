---
title: WME EZRoad Mod - Script Example
notes: >
  Full-featured road-editing accelerator for WME. Demonstrates multi-property bulk
  segment updates, per-road-type lock/speed presets, 3-tier name-copy logic,
  pedestrian↔routable segment conversion, geometry overlay, map-layer overlays,
  vehicle restriction DOM automation, legacy accelerator-based keyboard shortcuts,
  MutationObserver edit-panel integration, and a jQuery settings panel with
  export/import and named presets.
---

# WME EZRoad Mod — Script Example

**Version:** 2.6.8.7 | **Author:** kid4rm90s | **License:** GNU GPL v3
**Script:** [WME EZRoad Mod on GreaseFork](https://greasyfork.org/scripts/528552-wme-ezroad-mod)
**Based on:** WME EZRoad by Michaelrosstarr (https://greasyfork.org/en/scripts/518381-wme-ezsegments)

---

## Overview

WME EZRoad Mod is a comprehensive road-editing accelerator that applies multiple
segment properties in a single keypress or button click. It extends the original
WME EZRoad script with a large number of features covering every common segment
editing workflow.

### Features

- **Quick Update** (`G` key or "Quick Update Segment" button) — applies all
  enabled options to selected segments in one action
- **16 road types** with per-type keyboard shortcuts (`S+1`–`S+9`, `S+0`,
  `A+1`–`A+6`) and WME chip click integration
- **Per-road-type lock level** — configurable lock (L1–L6 or HRCS) per road type;
  HRCS sets the highest lock of all connected different-type segments
- **Per-road-type speed limit** — set forward and reverse speed per road type
- **Unpaved/paved toggle** — via WME UI chip automation (DOM click) with SDK
  `flagAttributes.unpaved` as a documented alternative
- **Set street name to None** — clears primary and all alternate street names
- **Set city as None** — moves address into an empty city object
- **3-tier intelligent name copy** from connected segment:
  - *Tier 1* — primary names match: merges only missing alternate names
  - *Tier 2* — primary names differ: replaces primary and all alternates
  - *Tier 3* — segment has no names: copies everything from connected segment
- **Copy all connected-segment attributes** — road type, lock, speed, direction,
  address, unpaved flag — in one operation
- **Auto-save** — calls `wmeSDK.Editing.save()` after each bulk update
- **Pedestrian ↔ routable conversion** — when switching between pedestrian types
  (Footpath / Pedestrianised Area / Stairway) and regular streets, the old segment
  is deleted and recreated; all turns are enabled post-conversion
- **Enable U-turns** — enables all turns through both segment nodes
- **Motorbike-only restriction** — applies a vehicle restriction via full DOM UI
  automation (7-step async chained `setTimeout` sequence) because the WME SDK
  does not yet expose vehicle restriction APIs
- **Segment length overlay** — draws circular labels on map for all segments
  ≤ 20 m using Turf.js; labels follow map pan/zoom via RAF and SDK map events
- **Geometry node checker** — flags geometry nodes placed too close
  (configurable threshold, default 2 m) to segment endpoints with a 📍 pin overlay
- **One-click geometry fix** — scans all visible segments, confirms with a toast,
  then removes offending geometry nodes via `updateSegment`; rank-gated to L3+
- **Legacy keyboard shortcuts** — 12 feature-toggle shortcuts registered through
  the legacy `W.accelerators` / `I18n` system for compatibility with WME's
  keyboard-shortcuts UI
- **Custom lock/speed presets** — save, load, and delete named presets stored in
  `localStorage`; supports JSON export/import including all presets
- **jQuery settings panel** — tabbed WME side-panel with per-road-type radio
  buttons, lock dropdowns, speed inputs, checkboxes, preset manager, and
  export/import

---

## Architecture

### Data Flow

```
unsafeWindow.SDK_INITIALIZED
        │
        ▼
  initScript()  ──►  getWmeSdk({...})  ──►  WME_EZRoads_Mod_bootstrap()
        │
        ▼  (polls until edit-panel + top country are ready)
  WME_EZRoads_Mod_init()
   ├─ Register main shortcut (G)
   ├─ initializeActionShortcuts()  ──► 12 legacy W.accelerators entries
   ├─ MutationObserver on #edit-panel  ──► inject "Quick Update Segment" button
   ├─ Road-type chip click listeners  ──► auto-apply on chip selection
   ├─ Road-type shortcuts (S+1…A+6)  ──► createShortcut per road type
   ├─ Motorcycle shortcut (A+R)       ──► applyMotorbikeOnlyRestriction()
   ├─ initSegmentLengthLayer()        ──► overlay div + SDK event listeners
   ├─ setInterval(addGeometryFixButton, 2000)
   └─ constructSettings()             ──► jQuery settings tab

User action (G key / button / chip click)
        │
        ▼
  handleUpdate()
   ├─ [copySegmentAttributes]  copy all from best-connected segment
   ├─ [restrictExceptMotorbike] applyMotorbikeOnlyRestriction()  (async)
   ├─ recreateSegmentIfNeeded()  if pedestrian↔routable type change
   ├─ updateSegment { roadType }               200 ms delay
   ├─ updateSegment { lockRank }               300 ms delay
   ├─ updateSegment { fwdSpeedLimit, rev... }  400 ms delay
   ├─ updateAddress { primaryStreetId, alts }  (city + street resolution)
   ├─ unpaved chip click / checkbox click      500 ms delay
   ├─ [copySegmentName] 3-tier address copy    550 ms delay
   ├─ [enableUTurn] updateTurn per node
   └─ [autosave] wmeSDK.Editing.save()         600 ms delay
```

### Key Components

| Component | Location (approx. lines) | Purpose |
|-----------|--------------------------|---------|
| `roadTypes` / `defaultOptions` | 38–90 | Road type definitions, default settings, lock/speed arrays |
| `getConnectedSegmentIDs` | 93–101 | Returns deduplicated connected segment IDs (both directions) |
| `getFirstConnectedSegmentAddress` | 103–170 | BFS across connected graph to find nearest valid city |
| `copyFlagAttributes` | 178–205 | Copies `unpaved` flag via `updateSegment.flagAttributes` |
| `applyMotorbikeOnlyRestriction` | 210–473 | 7-step async DOM automation to add motorbike-only restriction |
| `getOptions` / `saveOptions` | 475–520 | `localStorage` persistence with deep merge of lock/speed arrays |
| Custom preset functions | 520–600 | `saveCustomPreset`, `loadCustomPreset`, `deleteCustomPreset`, `getCustomPresets` |
| Legacy shortcut functions | 605–645 | `WMEKSRegisterKeyboardShortcut`, `WMEKSLoadKeyboardShortcuts`, `WMEKSSaveKeyboardShortcuts` |
| `handleToggle` | 648–710 | Generic toggle handler for all checkbox options; enforces mutual exclusions |
| `initializeActionShortcuts` | 710–850 | Registers 12 legacy `W.accelerators` shortcuts for feature toggles |
| `WME_EZRoads_Mod_bootstrap` | 855–870 | Polls until edit panel + top country are ready |
| `WME_EZRoads_Mod_init` | 875–1130 | Main init: shortcuts, MutationObserver, chip listeners, layer init, settings |
| `checkGeometryNodePlacement` | 1078–1130 | Turf.js distance checks for geometry nodes near endpoints |
| `rebuildSegmentLengthDisplay` | 1148–1280 | Scans all segments, creates length/pin overlay labels in a DocumentFragment |
| `updateSegmentLabelPositions` | 1282–1310 | Fast RAF-based pixel position update for existing labels |
| `checkAndUpdate` | 1312–1360 | Polling function: triggers rebuild only when map bounds change |
| `initSegmentLengthLayer` | 1420–1550 | Creates overlay `<div>`, registers SDK map-move/zoom events |
| `registerShortcut` | 1555–1600 | Creates or recreates the main `G` shortcut safely |
| `fixVisibleGeometryIssues` | 1605–1700 | Async bulk geometry fix with confirm dialog |
| `addGeometryFixButton` | 1700–1760 | Inserts rank-gated bug-icon button into WME nav bar |
| `getHighestSegLock` (HRCS) | 1770–1850 | Recursive DFS to find max lock of differently-typed connected segments |
| `isPedestrianType` | 1886–1890 | Returns `true` for road types 5, 10, 15, 16, 18, 19 |
| `enableAllTurnsForSegment` | 1892–1940 | Enables all allowed turns at both nodes (skips pedestrian types) |
| `recreateSegmentIfNeeded` | 1942–2040 | Delete + recreate segment when switching pedestrian ↔ routable type |
| `handleUpdate` | 2043–3600 | Main update dispatcher with all options applied in timed sequence |
| `constructSettings` | 3600–3956 | jQuery settings panel: road-type radios, checkboxes, presets, export/import |

### SDK APIs Used

| API | Usage |
|-----|-------|
| `wmeSDK.DataModel.Segments.getById` | Fetch segment by ID for all operations |
| `wmeSDK.DataModel.Segments.getAll` | Scan all segments for geometry overlay |
| `wmeSDK.DataModel.Segments.getConnectedSegments` | Name-copy A/B side traversal |
| `wmeSDK.DataModel.Segments.updateSegment` | Road type, lock, speed, geometry, flagAttributes |
| `wmeSDK.DataModel.Segments.updateAddress` | Set primary street and alternate streets |
| `wmeSDK.DataModel.Segments.deleteSegment` | Pedestrian ↔ routable conversion |
| `wmeSDK.DataModel.Segments.addSegment` | Recreate segment after type conversion |
| `wmeSDK.DataModel.Streets.getById` | Resolve street names from IDs |
| `wmeSDK.DataModel.Streets.getStreet` | Find existing street by city + name |
| `wmeSDK.DataModel.Streets.addStreet` | Create new street when not found |
| `wmeSDK.DataModel.Cities.getTopCity` | Default city for address assignment |
| `wmeSDK.DataModel.Cities.getAll` | Find empty city object |
| `wmeSDK.DataModel.Cities.getById` | Validate city by ID |
| `wmeSDK.DataModel.Cities.addCity` | Create empty city if none exists |
| `wmeSDK.DataModel.Countries.getTopCountry` | Country context for city lookup |
| `wmeSDK.DataModel.Turns.canEditTurnsThroughNode` | Gate turn edits by node |
| `wmeSDK.DataModel.Turns.getTurnsThroughNode` | Get all turns at a node |
| `wmeSDK.DataModel.Turns.updateTurn` | Enable individual turns |
| `wmeSDK.Editing.getSelection` | Get selected segment IDs and type |
| `wmeSDK.Editing.setSelection` | Reselect segment after recreation |
| `wmeSDK.Editing.save` | Autosave after update |
| `wmeSDK.State.getUserInfo` | Rank check for geometry-fix button |
| `wmeSDK.State.isReady` | Readiness check in bootstrap |
| `wmeSDK.Events.on` | Map move/zoom event listeners |
| `wmeSDK.Events.once` | One-time wme-ready listener |
| `wmeSDK.Map.getZoomLevel` | Hide overlay below zoom 18 |
| `wmeSDK.Map.getMapExtent` | Viewport bounds for segment filtering |
| `wmeSDK.Map.getMapViewportElement` | Root element for overlay container |
| `wmeSDK.Map.getMapPixelFromLonLat` | Convert geo coords to screen pixels |
| `wmeSDK.Shortcuts.createShortcut` | Register main `G` and per-road-type shortcuts |
| `wmeSDK.Shortcuts.deleteShortcut` | Remove old shortcut before re-registration |
| `wmeSDK.Shortcuts.isShortcutRegistered` | Prevent duplicate shortcut registration |

### External Dependencies

| Dependency | Purpose |
|-----------|---------|
| `@turf/turf@7` (CDN) | Segment length (`turf.length`), midpoint (`turf.along`), distance (`turf.distance`), point creation |
| `WazeToastr` (GreaseFork) | Toast notifications (success, info, warning, error, confirm) |
| `jQuery ($)` | Settings panel DOM construction and event delegation |
| `W.accelerators` / `I18n` (legacy WME globals) | Legacy keyboard shortcut registration |
| `localStorage` | Settings persistence (`WME_EZRoads_Mod_Options`, `WME_EZRoads_Mod_CustomPresets`, `WME_EZRoads_Mod_CurrentPreset`) |
| `unsafeWindow.SDK_INITIALIZED` | WME SDK bootstrap promise (Tampermonkey `unsafeWindow`) |

### File Structure (by line range)

| Lines | Section |
|-------|---------|
| 1–27 | UserScript header, update message, script constants |
| 28–90 | `roadTypes` array, `defaultOptions`, `locks` array, `log()` helper |
| 91–175 | City/country helpers, `getConnectedSegmentIDs`, `getFirstConnectedSegmentAddress` |
| 176–225 | `getDirectionFromSegment`, `copyFlagAttributes` |
| 226–473 | `applyMotorbikeOnlyRestriction` — DOM automation with chained async steps |
| 474–600 | `saveOptions`, `getOptions`, custom preset CRUD, preset state helpers |
| 601–650 | Legacy WMEKS shortcut system (register / load / save) |
| 651–855 | `handleToggle`, `initializeActionShortcuts` (12 legacy shortcuts) |
| 856–1077 | Bootstrap, init, MutationObserver, chip listeners, road-type + motorcycle shortcuts |
| 1078–1130 | `checkGeometryNodePlacement` (Turf.js distance check) |
| 1131–1415 | Segment length display: `rebuildSegmentLengthDisplay`, `updateSegmentLabelPositions`, `checkAndUpdate`, `handleSegmentLengthToggle` |
| 1416–1555 | `initSegmentLengthLayer` — overlay container + SDK map event listeners |
| 1556–1600 | `registerShortcut` |
| 1601–1700 | `fixVisibleGeometryIssues` — async bulk geometry fix |
| 1701–1760 | `addGeometryFixButton` — rank-gated nav-bar bug icon |
| 1761–2042 | `getEmptyCity`, `delayedUpdate`, `getHighestSegLock`, `pushCityNameAlert`, `isPedestrianType`, `enableAllTurnsForSegment`, `recreateSegmentIfNeeded` |
| 2043–3600 | `handleUpdate` — full update dispatcher (copy attributes, motorbike, road type, lock, speed, address, unpaved, name copy, U-turn, autosave) |
| 3601–3956 | `constructSettings` — jQuery settings panel (radios, checkboxes, geometry threshold, presets, export/import) |

---

## Common Gotchas

- **Unpaved uses DOM clicks, not pure SDK** — `flagAttributes.unpaved` via
  `updateSegment` does not reliably reflect state before the next render cycle.
  The script instead clicks the WME chip directly and keeps the SDK call commented
  out as a documented future alternative. Do not replace this with the SDK call
  without verifying state-read reliability.

- **Pedestrian ↔ routable conversion deletes the segment** — switching between
  pedestrian types and any routable type triggers a full delete + recreate. This
  cannot be undone with a single Ctrl+Z. A WazeToastr confirmation dialog is
  shown before proceeding. The new segment ID replaces the old one for all
  subsequent operations in the same `handleUpdate` call.

- **HRCS lock resolution is recursive DFS** — `getHighestSegLock` walks the
  segment graph along same-type segments, collecting the max lock of
  differently-typed segments at each node. It caps at L6. With large junction
  clusters this can be slow; the `checkedSegs` list prevents infinite loops.

- **3-tier name copy priority** — the script scores connected segments by number
  of alternate names and picks the richest match. If you expect a specific name to
  be copied, ensure the connected segment with that name also has the most
  alternate names, or it may not be selected over another candidate.

- **Motorbike restriction is fully async DOM automation** — the 7-step sequence
  uses chained `setTimeout` calls with `waitForElement` promises. If WME's modal
  renders slowly, any step can time out (5 s default). The function always
  `resolve()`s (never rejects), reporting `'not_supported'` on any failure so the
  caller can show a manual-steps toast.

- **Legacy shortcuts use `W.accelerators` directly** — the 12 feature-toggle
  shortcuts are registered outside the WME SDK shortcut system. They appear in
  WME's keyboard shortcuts UI under "EZRoad Mod - Feature Toggles" but are not
  managed by `wmeSDK.Shortcuts`. Key conflicts with SDK-registered shortcuts are
  possible.

- **Geometry overlay only renders at zoom ≥ 18** — below that zoom level the
  overlay is cleared and the badge hidden. Polling runs every 500 ms but only
  rebuilds when the map extent or zoom has actually changed.

- **`copySegmentAttributes` is mutually exclusive with other options** — when
  enabled, all other attribute options (street, city, lock, speed, unpaved,
  U-turn, name copy) are disabled in the settings panel. The flag
  `window.suppressCopySegmentAttributes` prevents this mode from running when a
  road-type chip click triggers `handleUpdate`.

---

## Testing Checklist

- [ ] Select multiple segments, press `G` — road type, lock, speed, city all
      update in one action with a summary toast
- [ ] Enable "Copy Connected Segment Name"; select a segment with no name
      adjacent to a named segment — name is copied (Tier 3)
- [ ] Enable "Copy Connected Segment Name"; select a segment whose primary name
      matches a neighbour — only missing alt names are added (Tier 1)
- [ ] Switch a Street segment to Footpath — confirmation dialog appears; after
      confirming, old segment is deleted, new pedestrian segment is created and
      selected
- [ ] Switch a Footpath back to Street — same confirmation; new segment gets all
      turns enabled
- [ ] Enable "Check Geometry Issues"; create a geometry node within 1 m of a
      node — pin overlay appears; badge count increments
- [ ] Click the bug-icon button (requires L3+) — confirmation toast appears; after
      confirming, affected geometry nodes are removed and overlay updates
- [ ] Enable "Restrict Except Motorbike"; select a segment; press `G` — WME
      restriction modal opens automatically, completes, and closes
- [ ] Open Settings tab; change lock for "Street" to L3; save and reload — lock
      is persisted and applied on next Quick Update
- [ ] Save a named preset; change lock values; reload the preset — values revert
      to saved preset
- [ ] Export config to clipboard; clear settings; import — lock/speed values and
      presets are fully restored

---

## Full Script

```javascript
// ==UserScript==
// @name         WME EZRoad Mod
// @namespace    https://greasyfork.org/users/1087400
// @version      2.6.8.7
// @description  Easily update roads
// @author       https://greasyfork.org/en/users/1087400-kid4rm90s
// @include      /^https:\/\/(www|beta)\.waze\.com\/(?!user\/)(.{2,6}\/)?editor.*$/
// @exclude      https://www.waze.com/user/*editor/*
// @exclude      https://www.waze.com/*/user/*editor/*
// @grant        GM_getValue
// @grant        GM_setValue
// @grant        GM_xmlhttpRequest
// @grant        GM_info
// @grant        unsafeWindow
// @icon         https://www.google.com/s2/favicons?sz=64&domain=waze.com
// @license      GNU GPL(v3)
// @connect      greasyfork.org
// @require      https://cdn.jsdelivr.net/npm/@turf/turf@7/turf.min.js
// @require      https://greasyfork.org/scripts/560385/code/WazeToastr.js
// @downloadURL  https://update.greasyfork.org/scripts/528552/WME%20EZRoad%20Mod.user.js
// @updateURL    https://update.greasyfork.org/scripts/528552/WME%20EZRoad%20Mod.meta.js
// ==/UserScript==

/*
 * Script modified from WME EZRoad (https://greasyfork.org/en/scripts/518381-wme-ezsegments)
 * Original author: Michaelrosstarr
 *
 * ─── ARCHITECTURE SUMMARY ───────────────────────────────────────────────────
 *
 * Initialisation
 *   unsafeWindow.SDK_INITIALIZED.then(initScript)
 *   → getWmeSdk({ scriptId, scriptName })
 *   → WME_EZRoads_Mod_bootstrap  (polls every 250 ms until ready)
 *   → WME_EZRoads_Mod_init
 *       ├─ Register main 'G' shortcut
 *       ├─ initializeActionShortcuts  (12 legacy W.accelerators entries)
 *       ├─ MutationObserver on #edit-panel  →  inject "Quick Update" button
 *       ├─ Road-type chip listeners  →  auto-apply on chip selection
 *       ├─ Per-road-type SDK shortcuts  (S+1…A+6)
 *       ├─ Motorcycle shortcut (A+R)
 *       ├─ initSegmentLengthLayer
 *       ├─ setInterval(addGeometryFixButton, 2000)
 *       └─ constructSettings
 *
 * Quick Update (G key / button click)
 *   handleUpdate()
 *     ├─ [copySegmentAttributes]  → copy all from best-connected segment
 *     ├─ [restrictExceptMotorbike] → applyMotorbikeOnlyRestriction (async DOM)
 *     ├─ recreateSegmentIfNeeded  → pedestrian ↔ routable conversion
 *     ├─ updateSegment roadType           (200 ms)
 *     ├─ updateSegment lockRank           (300 ms)
 *     ├─ updateSegment fwdSpeedLimit      (400 ms)
 *     ├─ updateAddress city + street      (immediate)
 *     ├─ unpaved chip click               (500 ms)
 *     ├─ [copySegmentName] 3-tier logic   (550 ms)
 *     ├─ [enableUTurn] updateTurn         (after address)
 *     └─ [autosave] Editing.save()        (600 ms)
 */

(function main() {
  'use strict';

  // ─── CONSTANTS ───────────────────────────────────────────────────────────
  const scriptName = GM_info.script.name;
  const scriptVersion = GM_info.script.version;

  const roadTypes = [
    { id: 1,  name: 'Motorway',              value: 3,  shortcutKey: 'S+1' },
    { id: 2,  name: 'Ramp',                  value: 4,  shortcutKey: 'S+2' },
    { id: 3,  name: 'Major Highway',         value: 6,  shortcutKey: 'S+3' },
    { id: 4,  name: 'Minor Highway',         value: 7,  shortcutKey: 'S+4' },
    { id: 5,  name: 'Primary Street',        value: 2,  shortcutKey: 'S+5' },
    { id: 6,  name: 'Street',                value: 1,  shortcutKey: 'S+6' },
    { id: 7,  name: 'Narrow Street',         value: 22, shortcutKey: 'S+7' },
    { id: 8,  name: 'Offroad',               value: 8,  shortcutKey: 'S+8' },
    { id: 9,  name: 'Parking Road',          value: 20, shortcutKey: 'S+9' },
    { id: 10, name: 'Private Road',          value: 17, shortcutKey: 'S+0' },
    { id: 11, name: 'Ferry',                 value: 15, shortcutKey: 'A+1' },
    { id: 12, name: 'Railway',               value: 18, shortcutKey: 'A+2' },
    { id: 13, name: 'Runway',                value: 19, shortcutKey: 'A+3' },
    { id: 14, name: 'Footpath',              value: 5,  shortcutKey: 'A+4' },
    { id: 15, name: 'Pedestrianised Area',   value: 10, shortcutKey: 'A+5' },
    { id: 16, name: 'Stairway',              value: 16, shortcutKey: 'A+6' },
  ];

  const defaultOptions = {
    roadType: 1,
    unpaved: false,
    setStreet: false,
    setStreetCity: false,
    setStreetState: false,
    autosave: false,
    setSpeed: 40,
    setLock: false,
    updateSpeed: false,
    copySegmentName: false,
    locks: roadTypes.map(rt => ({ id: rt.id, lock: String(1) })),
    speeds: roadTypes.map(rt => ({ id: rt.id, speed: 40 })),
    copySegmentAttributes: false,
    showSegmentLength: false,
    checkGeometryIssues: false,
    geometryIssueThreshold: 2,
    enableUTurn: false,
    restrictExceptMotorbike: false,
    shortcutKey: 'g',
  };

  const UserRankRequiredForGeometryFix = 3; // SDK rank >= 2

  let wmeSDK;

  const log = msg =>
    typeof msg === 'string'
      ? console.log(`${scriptName}: ` + msg)
      : console.log(`${scriptName}: `, msg);

  // ─── BOOTSTRAP ───────────────────────────────────────────────────────────
  unsafeWindow.SDK_INITIALIZED.then(initScript);

  function initScript() {
    wmeSDK = getWmeSdk({ scriptId: 'wme-ez-roads-mod', scriptName: 'EZ Roads Mod' });
    WME_EZRoads_Mod_bootstrap();
  }

  // ─── HELPERS: DATA MODEL ─────────────────────────────────────────────────
  const getCurrentCountry = () => wmeSDK.DataModel.Countries.getTopCountry();
  const getTopCity       = () => wmeSDK.DataModel.Cities.getTopCity();

  /** Returns deduplicated IDs of all segments connected to segmentId. */
  function getConnectedSegmentIDs(segmentId) {
    const segs = [
      ...wmeSDK.DataModel.Segments.getConnectedSegments({ segmentId, reverseDirection: false }),
      ...wmeSDK.DataModel.Segments.getConnectedSegments({ segmentId, reverseDirection: true }),
    ];
    return [...new Set(segs.map(s => s.id))];
  }

  /**
   * BFS across connected segments to find the first one with a valid city.
   * Returns the address object or null.
   */
  function getFirstConnectedSegmentAddress(segmentId) {
    const nonMatches = [];
    const toSearch = [segmentId];
    const hasValidCity = id => {
      try {
        const addr = wmeSDK.DataModel.Segments.getAddress({ segmentId: id });
        if (addr?.city?.id) {
          const city = wmeSDK.DataModel.Cities.getById({ cityId: addr.city.id });
          return city && !city.isEmpty && city.name !== undefined;
        }
      } catch (e) { /* ignore */ }
      return false;
    };
    while (toSearch.length > 0) {
      const id = toSearch.pop();
      const connected = getConnectedSegmentIDs(id);
      const found = connected.find(hasValidCity);
      if (found) return wmeSDK.DataModel.Segments.getAddress({ segmentId: found });
      nonMatches.push(id);
      connected.forEach(cid => {
        if (!nonMatches.includes(cid) && !toSearch.includes(cid)) toSearch.push(cid);
      });
    }
    return null;
  }

  function getDirectionFromSegment(segment) {
    if (!segment) return null;
    if (segment.isTwoWay) return 'TWO_WAY';
    if (segment.isAtoB)   return 'A_TO_B';
    if (segment.isBtoA)   return 'B_TO_A';
    return null;
  }

  /** Copies unpaved flag from one segment to another via updateSegment. */
  function copyFlagAttributes(fromId, toId) {
    const from = wmeSDK.DataModel.Segments.getById({ segmentId: fromId });
    const to   = wmeSDK.DataModel.Segments.getById({ segmentId: toId });
    if (!from?.flagAttributes) return;
    const fromUnpaved = from.flagAttributes.unpaved === true;
    const toUnpaved   = to?.flagAttributes?.unpaved === true;
    if (fromUnpaved !== toUnpaved) {
      wmeSDK.DataModel.Segments.updateSegment({ segmentId: toId, flagAttributes: { unpaved: fromUnpaved } });
    }
  }

  // ─── MOTORBIKE RESTRICTION (DOM AUTOMATION) ───────────────────────────────
  /**
   * Applies a motorbike-only vehicle restriction via step-by-step DOM automation.
   * The WME SDK does not yet expose vehicle restriction APIs.
   *
   * Steps:
   *   1. Click "Add restrictions" button
   *   2. Click "Add new" for bidirectional restrictions
   *   3. Set disposition to "Entire Segment"
   *   4. Click "+" to add a restriction condition
   *   5. Select "Vehicle type" from the menu
   *   6. Select "Motorcycle" from the vehicle options
   *   7. Click "Add" then "Apply"
   *
   * Returns a Promise that always resolves (never rejects):
   *   true            – success
   *   'not_supported' – UI element not found or timed out
   *   'not_supported type' – segment is pedestrian type
   */
  function applyMotorbikeOnlyRestriction(segmentId) {
    return new Promise(resolve => {
      try {
        const segment = wmeSDK.DataModel.Segments.getById({ segmentId });
        if (!segment || isPedestrianType(segment.roadType)) {
          resolve('not_supported type');
          return;
        }

        const waitForElement = (selector, timeout = 5000) =>
          new Promise((res, rej) => {
            const t0 = Date.now();
            const iv = setInterval(() => {
              const el = document.querySelector(selector);
              if (el) { clearInterval(iv); res(el); }
              else if (Date.now() - t0 > timeout) { clearInterval(iv); rej(new Error(`Timeout: ${selector}`)); }
            }, 100);
          });

        const click = el => { if (el) { el.click(); return true; } return false; };

        // Step 1
        setTimeout(() => {
          const btn = document.querySelector('wz-button.edit-restrictions');
          if (!btn) { resolve('not_supported'); return; }
          click(btn);

          // Step 2
          setTimeout(() => {
            waitForElement('.bidi-restrictions-summary .do-create')
              .then(addNewBtn => {
                click(addNewBtn);

                // Step 3
                setTimeout(() => {
                  waitForElement('select[name="disposition"]')
                    .then(sel => {
                      sel.value = '1';
                      sel.dispatchEvent(new Event('change', { bubbles: true }));

                      // Step 4
                      setTimeout(() => {
                        const plus = document.querySelector('.fa-plus');
                        if (!plus || !click(plus)) { resolve('not_supported'); return; }

                        // Step 5
                        setTimeout(() => {
                          waitForElement('wz-menu-item')
                            .then(() => {
                              const items = [...document.querySelectorAll('wz-menu-item')];
                              const vtItem = items.find(i => i.textContent.includes('Vehicle type'));
                              if (!vtItem || !click(vtItem)) { resolve('not_supported'); return; }

                              // Step 6
                              setTimeout(() => {
                                waitForElement('.do-set-vehicle-type')
                                  .then(() => {
                                    const opts = [...document.querySelectorAll('.do-set-vehicle-type')];
                                    const moto = opts.find(o => o.textContent.toLowerCase().includes('motorcycle'));
                                    if (!moto || !click(moto)) { resolve('not_supported'); return; }

                                    // Step 7
                                    setTimeout(() => {
                                      waitForElement('button.do-create')
                                        .then(addBtn => {
                                          if (!click(addBtn)) { resolve('not_supported'); return; }
                                          setTimeout(() => {
                                            const applyBtn = document.querySelector('button.do-apply');
                                            resolve(applyBtn && click(applyBtn) ? true : 'not_supported');
                                          }, 100);
                                        })
                                        .catch(() => resolve('not_supported'));
                                    }, 100);
                                  })
                                  .catch(() => resolve('not_supported'));
                              }, 100);
                            })
                            .catch(() => resolve('not_supported'));
                        }, 100);
                      }, 100);
                    })
                    .catch(() => resolve('not_supported'));
                }, 100);
              })
              .catch(() => resolve('not_supported'));
          }, 100);
        }, 50);
      } catch (e) {
        log(`applyMotorbikeOnlyRestriction error: ${e}`);
        resolve(false);
      }
    });
  }

  // ─── OPTIONS PERSISTENCE ─────────────────────────────────────────────────
  const saveOptions = options =>
    window.localStorage.setItem('WME_EZRoads_Mod_Options', JSON.stringify(options));

  const getOptions = () => {
    const saved = JSON.parse(window.localStorage.getItem('WME_EZRoads_Mod_Options')) || {};
    const mergeById = (defaults, saved) =>
      Array.isArray(defaults)
        ? defaults.map(def => ({ ...def, ...(saved || []).find(s => s.id === def.id) }))
        : defaults;
    return {
      ...defaultOptions,
      ...saved,
      locks:  mergeById(defaultOptions.locks,  (saved.locks  || []).map(l => ({ ...l, lock: String(l.lock) }))),
      speeds: mergeById(defaultOptions.speeds, saved.speeds || []),
    };
  };

  // Custom preset helpers (save/load/delete/get stored in localStorage)
  const getCustomPresets     = () => JSON.parse(window.localStorage.getItem('WME_EZRoads_Mod_CustomPresets')) || {};
  const getCurrentPresetName = () => window.localStorage.getItem('WME_EZRoads_Mod_CurrentPreset') || null;
  const setCurrentPresetName = name => name
    ? window.localStorage.setItem('WME_EZRoads_Mod_CurrentPreset', name)
    : window.localStorage.removeItem('WME_EZRoads_Mod_CurrentPreset');

  const saveCustomPreset = name => {
    const opts = getOptions();
    const presets = getCustomPresets();
    presets[name] = { locks: opts.locks, speeds: opts.speeds, savedAt: new Date().toISOString() };
    window.localStorage.setItem('WME_EZRoads_Mod_CustomPresets', JSON.stringify(presets));
  };

  const loadCustomPreset = name => {
    const preset = getCustomPresets()[name];
    if (!preset) return false;
    const opts = getOptions();
    opts.locks = preset.locks;
    opts.speeds = preset.speeds;
    saveOptions(opts);
    setCurrentPresetName(name);
    return true;
  };

  const deleteCustomPreset = name => {
    const presets = getCustomPresets();
    if (!presets[name]) return false;
    delete presets[name];
    window.localStorage.setItem('WME_EZRoads_Mod_CustomPresets', JSON.stringify(presets));
    if (getCurrentPresetName() === name) setCurrentPresetName(null);
    return true;
  };

  // ─── LEGACY KEYBOARD SHORTCUTS ────────────────────────────────────────────
  // Uses the legacy W.accelerators / I18n system (not wmeSDK.Shortcuts) so that
  // feature-toggle shortcuts appear in WME's keyboard-shortcuts UI.
  function WMEKSRegisterKeyboardShortcut(scriptName, header, action, description, fn, key, arg) {
    try { I18n.translations[I18n.locale].keyboard_shortcuts.groups[scriptName].members.length; }
    catch (c) {
      W.accelerators.Groups[scriptName] = [];
      W.accelerators.Groups[scriptName].members = [];
      I18n.translations[I18n.locale].keyboard_shortcuts.groups[scriptName] = [];
      I18n.translations[I18n.locale].keyboard_shortcuts.groups[scriptName].description = header;
      I18n.translations[I18n.locale].keyboard_shortcuts.groups[scriptName].members = [];
    }
    if (typeof fn === 'function') {
      I18n.translations[I18n.locale].keyboard_shortcuts.groups[scriptName].members[action] = description;
      W.accelerators.addAction(action, { group: scriptName });
      W.accelerators._registerShortcuts({ '-1': action });
      if (key !== null) W.accelerators._registerShortcuts({ [key]: action });
      W.accelerators.events.register(action, null, () => fn(arg));
    }
  }

  function WMEKSLoadKeyboardShortcuts(name) {
    const raw = localStorage[name + 'KBS'];
    if (!raw) return;
    JSON.parse(raw).forEach(s => { try { W.accelerators._registerShortcuts(s); } catch (e) {} });
  }

  function WMEKSSaveKeyboardShortcuts(name) {
    const shortcuts = [];
    for (const action in W.accelerators.Actions) {
      if (W.accelerators.Actions[action].group !== name) continue;
      let key = '-1';
      const sc = W.accelerators.Actions[action].shortcut;
      if (sc) {
        key = (sc.altKey ? 'A' : '') + (sc.shiftKey ? 'S' : '') + (sc.ctrlKey ? 'C' : '');
        if (key) key += '+';
        if (sc.keyCode) key += sc.keyCode;
      }
      const obj = {}; obj[key] = W.accelerators.Actions[action].id;
      shortcuts.push(obj);
    }
    localStorage[name + 'KBS'] = JSON.stringify(shortcuts);
  }

  /** Registers 12 legacy feature-toggle shortcuts (shown in WME keyboard shortcuts UI). */
  function initializeActionShortcuts() {
    const features = [
      ['WME_EZRoad_Mod_SetStreetNameToNone',       'Set Street Name to None',             'setStreet'],
      ['WME_EZRoad_Mod_SetCityAsNone',             'Set City as None',                    'setStreetCity'],
      ['WME_EZRoad_Mod_AutosaveOnAction',          'Autosave on Action',                  'autosave'],
      ['WME_EZRoad_Mod_SetAsUnpaved',              'Set as Unpaved',                      'unpaved'],
      ['WME_EZRoad_Mod_SetLockLevel',              'Set Lock Level',                      'setLock'],
      ['WME_EZRoad_Mod_UpdateSpeedLimits',         'Update Speed Limits',                 'updateSpeed'],
      ['WME_EZRoad_Mod_EnableUTurn',               'Enable U-Turn',                       'enableUTurn'],
      ['WME_EZRoad_Mod_CopyConnectedSegmentName',  'Copy Connected Segment Name',         'copySegmentName'],
      ['WME_EZRoad_Mod_CopyConnectedSegmentAttr',  'Copy Connected Segment Attribute',    'copySegmentAttributes'],
      ['WME_EZRoad_Mod_ShowSegmentLength',         'Show Segment Length <=20m',           'showSegmentLength'],
      ['WME_EZRoad_Mod_CheckGeometryIssues',       'Check Geometry Issues',               'checkGeometryIssues'],
      ['WME_EZRoad_Mod_RestrictMotorbikesOnly',    'Restrict Except Motorbike',           'restrictExceptMotorbike'],
    ];
    features.forEach(([handler, title, key]) =>
      WMEKSRegisterKeyboardShortcut(scriptName, 'EZRoad Mod - Feature Toggles', handler, title,
        () => handleToggle(key, title), -1, {})
    );
    WMEKSLoadKeyboardShortcuts(scriptName);
    window.addEventListener('beforeunload', () => WMEKSSaveKeyboardShortcuts(scriptName), false);
  }

  /** Generic toggle: flips the named option, updates UI, enforces mutual exclusions. */
  function handleToggle(optionKey, featureName) {
    const opts = getOptions();
    opts[optionKey] = !opts[optionKey];
    saveOptions(opts);
    // Mutual exclusions
    if (optionKey === 'setStreet'            && opts[optionKey]) { opts.copySegmentName = false; saveOptions(opts); }
    if (optionKey === 'copySegmentName'      && opts[optionKey]) { opts.setStreet = false; saveOptions(opts); }
    if (optionKey === 'copySegmentAttributes'&& opts[optionKey]) {
      ['setStreet','setStreetCity','unpaved','setLock','updateSpeed','enableUTurn','copySegmentName'].forEach(k => { opts[k] = false; });
      saveOptions(opts);
    }
    WazeToastr?.Alerts?.info(scriptName, `${featureName}: ${opts[optionKey] ? 'Enabled' : 'Disabled'}`, false, false, 2000);
  }

  // ─── BOOTSTRAP / INIT ────────────────────────────────────────────────────
  const WME_EZRoads_Mod_bootstrap = () => {
    if (!document.getElementById('edit-panel') || !wmeSDK.DataModel.Countries.getTopCountry()) {
      setTimeout(WME_EZRoads_Mod_bootstrap, 250);
      return;
    }
    if (wmeSDK.State.isReady) WME_EZRoads_Mod_init();
    else wmeSDK.Events.once({ eventName: 'wme-ready' }).then(WME_EZRoads_Mod_init);
  };

  let openPanel;

  const WME_EZRoads_Mod_init = () => {
    log('Initialising');

    // Register main shortcut
    registerShortcut(getOptions().shortcutKey || 'g');

    // Legacy feature-toggle shortcuts
    try { initializeActionShortcuts(); } catch (e) { console.error(e); }

    // Road-type chip click integration
    window.suppressCopySegmentAttributes = false;
    function addRoadTypeChipListeners() {
      const chipSelect = document.querySelector('.road-type-chip-select');
      if (!chipSelect) return;
      chipSelect.querySelectorAll('wz-checkable-chip').forEach(chip => {
        if (!chip._ezroadmod_listener) {
          chip._ezroadmod_listener = true;
          chip.addEventListener('click', () => {
            setTimeout(() => {
              if (chip.getAttribute('checked') === '') {
                const rtValue = parseInt(chip.getAttribute('value'), 10);
                if (isNaN(rtValue)) return;
                const opts = getOptions();
                opts.roadType = rtValue;
                saveOptions(opts);
                window.suppressCopySegmentAttributes = true;
                Promise.resolve(handleUpdate()).finally(() => { window.suppressCopySegmentAttributes = false; });
              }
            }, 50);
          });
        }
      });
    }
    setTimeout(addRoadTypeChipListeners, 1200);

    // MutationObserver: inject "Quick Update Segment" button + re-attach chip listeners
    new MutationObserver(mutations => {
      mutations.forEach(({ addedNodes }) => {
        addedNodes.forEach(node => {
          if (node.nodeType !== Node.ELEMENT_NODE) return;
          const editSegment = node.querySelector('#segment-edit-general');
          if (!editSegment) return;
          openPanel = editSegment;
          const parent = editSegment.parentNode;
          if (!parent.querySelector('[data-ez-roadmod-button="true"]')) {
            const btn = document.createElement('wz-button');
            btn.setAttribute('type', 'button');
            btn.setAttribute('style', 'margin-bottom: 5px; width: 100%');
            btn.setAttribute('data-ez-roadmod-button', 'true');
            btn.textContent = 'Quick Update Segment';
            parent.insertBefore(btn, editSegment);
            btn.addEventListener('mousedown', () => handleUpdate());
          }
          addRoadTypeChipListeners();
        });
      });
    }).observe(document.getElementById('edit-panel'), { childList: true, subtree: true });

    // Per-road-type shortcuts (S+1…A+6)
    roadTypes.forEach(rt => {
      const shortcutId = `EZRoad_Mod_SelectRoadType_${rt.id}`;
      if (!wmeSDK.Shortcuts.isShortcutRegistered({ shortcutId })) {
        try {
          wmeSDK.Shortcuts.createShortcut({
            callback: () => {
              const opts = getOptions();
              opts.roadType = rt.value;
              saveOptions(opts);
              WazeToastr?.Alerts?.success(scriptName, `Selected road type: <b>${rt.name}</b>`, false, false, 1500);
            },
            description: `Select road type: ${rt.name}`,
            shortcutId,
            shortcutKeys: rt.shortcutKey,
          });
        } catch (e) { log(`Shortcut failed for ${rt.name}: ${e}`); }
      }
    });

    // Motorcycle-only restriction shortcut (A+R)
    const motoShortcutId = 'EZRoad_Mod_MotorcycleOnlyRestriction';
    if (!wmeSDK.Shortcuts.isShortcutRegistered({ shortcutId: motoShortcutId })) {
      try {
        wmeSDK.Shortcuts.createShortcut({
          callback: () => {
            const sel = wmeSDK.Editing.getSelection();
            if (!sel || sel.objectType !== 'segment' || !sel.ids?.length) {
              WazeToastr?.Alerts?.warning(scriptName, 'Please select one or more segments first', false, false, 3000);
              return;
            }
            applyMotorbikeOnlyRestriction(sel.ids[0]).then(result => {
              if (result === true)
                WazeToastr?.Alerts?.success(scriptName, `Motorbike-only restriction applied ✓`, false, false, 3000);
              else if (result === 'not_supported')
                WazeToastr?.Alerts?.warning(scriptName, 'Segment not found or pedestrian type', false, false, 5000);
            });
          },
          description: 'Apply Motorbike-Only Restriction to Selected Segments',
          shortcutId: motoShortcutId,
          shortcutKeys: 'A+R',
        });
      } catch (e) { log(`Motorcycle shortcut failed: ${e}`); }
    }

    initSegmentLengthLayer();
    setInterval(addGeometryFixButton, 2000);
    constructSettings();

    log('Initialisation complete');
  };

  // ─── GEOMETRY NODE CHECKER ────────────────────────────────────────────────
  /**
   * Checks whether any intermediate geometry nodes are within thresholdMeters
   * of the segment's start (Node A) or end (Node B).
   * Requires Turf.js.
   */
  function checkGeometryNodePlacement(segment, thresholdMeters = 2) {
    if (!segment?.geometry?.coordinates || typeof turf === 'undefined')
      return { hasIssue: false, details: [] };

    const coords = segment.geometry.coordinates;
    if (coords.length < 3) return { hasIssue: false, details: [] };

    const nodeA = turf.point(coords[0]);
    const nodeB = turf.point(coords[coords.length - 1]);
    const issues = [];

    for (let i = 1; i < coords.length - 1; i++) {
      const gn = turf.point(coords[i]);
      const dA = turf.distance(gn, nodeA, { units: 'meters' });
      const dB = turf.distance(gn, nodeB, { units: 'meters' });
      if (dA <= thresholdMeters) issues.push({ nodeIndex: i, distanceToA: dA, distanceToB: null, closeTo: 'A', coordinates: coords[i] });
      if (dB <= thresholdMeters) issues.push({ nodeIndex: i, distanceToA: null, distanceToB: dB, closeTo: 'B', coordinates: coords[i] });
    }

    return { hasIssue: issues.length > 0, details: issues, segmentId: segment.id, totalGeometryNodes: coords.length - 2 };
  }

  // ─── SEGMENT LENGTH / GEOMETRY OVERLAY ───────────────────────────────────
  // Renders circular length labels (≤ 20 m segments) and 📍 pin icons
  // (geometry nodes near endpoints) as absolute-positioned divs in a container
  // appended to the WME map viewport.
  let segmentLengthContainer = null;
  let segmentLabelCache      = [];
  let lastBounds = null, lastZoom = null, updateInterval = null;
  let isMapMoving = false, updateFrameRequest = null;

  function clearSegmentLengthDisplay() {
    if (segmentLengthContainer) segmentLengthContainer.innerHTML = '';
    segmentLabelCache = [];
  }

  function rebuildSegmentLengthDisplay() {
    const opts = getOptions();
    if ((!opts.showSegmentLength && !opts.checkGeometryIssues) || !segmentLengthContainer) return;
    clearSegmentLengthDisplay();
    if (typeof turf === 'undefined') return;

    const zoom = wmeSDK.Map.getZoomLevel();
    if (zoom < 18) return;

    const allSegments = wmeSDK.DataModel.Segments.getAll();
    const extent = wmeSDK.Map.getMapExtent();
    if (!extent || !allSegments.length) return;

    const bounds = { west: extent[0], south: extent[1], east: extent[2], north: extent[3] };
    const fragment = document.createDocumentFragment();
    const segmentsWithIssues = new Set();

    allSegments.forEach(segment => {
      try {
        const coords = segment.geometry?.coordinates;
        if (!coords || coords.length < 2 || segment.junctionId !== null) return;

        if (opts.checkGeometryIssues) {
          const result = checkGeometryNodePlacement(segment, opts.geometryIssueThreshold);
          if (result.hasIssue) {
            let visibleIssue = false;
            result.details.forEach(issue => {
              if (issue.coordinates[0] < bounds.west || issue.coordinates[0] > bounds.east ||
                  issue.coordinates[1] < bounds.south || issue.coordinates[1] > bounds.north) return;
              visibleIssue = true;
              const pin = Object.assign(document.createElement('div'), {
                innerHTML: '📍',
                title: `Node too close to ${issue.closeTo === 'A' ? 'start' : 'end'}: ${Math.round((issue.distanceToA ?? issue.distanceToB) * 10) / 10}m`,
              });
              Object.assign(pin.style, { position:'absolute', width:'30px', height:'30px', display:'flex', alignItems:'center', justifyContent:'center', fontSize:'30px', pointerEvents:'none' });
              fragment.appendChild(pin);
              segmentLabelCache.push({ lon: issue.coordinates[0], lat: issue.coordinates[1], labelDiv: pin, offsetX: 15, offsetY: 30 });
            });
            if (visibleIssue) segmentsWithIssues.add(segment.id);
          }
        }

        if (opts.showSegmentLength) {
          const line = turf.lineString(coords);
          const len  = turf.length(line, { units: 'meters' });
          if (len <= 20) {
            const mid = turf.along(line, len / 2, { units: 'meters' }).geometry.coordinates;
            if (mid[0] >= bounds.west && mid[0] <= bounds.east && mid[1] >= bounds.south && mid[1] <= bounds.north) {
              const label = document.createElement('div');
              Object.assign(label.style, { position:'absolute', width:'30px', height:'30px', borderRadius:'50%', backgroundColor:'#ff6600a1', display:'flex', alignItems:'center', justifyContent:'center', color:'white', fontSize:'12px', fontWeight:'bold', pointerEvents:'none' });
              label.textContent = Math.round(len);
              fragment.appendChild(label);
              segmentLabelCache.push({ lon: mid[0], lat: mid[1], labelDiv: label, offsetX: 15, offsetY: 35 });
            }
          }
        }
      } catch (e) { /* silent */ }
    });

    segmentLengthContainer.appendChild(fragment);
    updateSegmentLabelPositions();

    // Update badge
    const badge = document.getElementById('ezroad-geometry-error-count');
    const bugIcon = document.getElementById('ezroad-bug-icon');
    if (badge) {
      if (segmentsWithIssues.size > 0 && opts.checkGeometryIssues) {
        badge.value = segmentsWithIssues.size;
        badge.style.display = 'inline-flex';
        if (bugIcon) bugIcon.style.color = '#ff3333';
      } else {
        badge.style.display = 'none';
        if (bugIcon) bugIcon.style.color = '#33CCFF';
      }
    }
  }

  function updateSegmentLabelPositions() {
    segmentLabelCache.forEach(cached => {
      const px = wmeSDK.Map.getMapPixelFromLonLat({ lonLat: { lon: cached.lon, lat: cached.lat } });
      if (px && typeof px.x === 'number') {
        cached.labelDiv.style.left = (px.x - cached.offsetX) + 'px';
        cached.labelDiv.style.top  = (px.y - cached.offsetY) + 'px';
      }
    });
  }

  function checkAndUpdate() {
    if (isMapMoving) return;
    const opts = getOptions();
    if (!opts.showSegmentLength && !opts.checkGeometryIssues) {
      if (segmentLengthContainer) segmentLengthContainer.style.display = 'none';
      return;
    }
    segmentLengthContainer.style.display = 'block';
    const extent = wmeSDK.Map.getMapExtent();
    const zoom   = wmeSDK.Map.getZoomLevel();
    const b = { west: extent[0], south: extent[1], east: extent[2], north: extent[3] };
    if (!lastBounds || b.north !== lastBounds.north || b.south !== lastBounds.south ||
        b.east !== lastBounds.east || b.west !== lastBounds.west || zoom !== lastZoom) {
      lastBounds = b; lastZoom = zoom;
      rebuildSegmentLengthDisplay();
    }
  }

  function initSegmentLengthLayer() {
    let viewport;
    try { viewport = wmeSDK.Map.getMapViewportElement(); } catch (e) {}
    viewport = viewport || document.querySelector('.ol-viewport') || document.querySelector('#WazeMap');
    if (!viewport) return;

    segmentLengthContainer = document.createElement('div');
    Object.assign(segmentLengthContainer.style, { position:'absolute', top:'0', left:'0', width:'100%', height:'100%', pointerEvents:'none', zIndex:'1000', display:'none' });
    segmentLengthContainer.id = 'ezroad-segment-length-container';
    viewport.appendChild(segmentLengthContainer);

    wmeSDK.Events.on({ eventName: 'wme-map-move', eventHandler: () => {
      isMapMoving = true;
      if (!updateFrameRequest) {
        updateFrameRequest = requestAnimationFrame(() => {
          updateFrameRequest = null;
          const opts = getOptions();
          if ((opts.showSegmentLength || opts.checkGeometryIssues) && segmentLengthContainer?.style.display !== 'none')
            updateSegmentLabelPositions();
        });
      }
    }});

    wmeSDK.Events.on({ eventName: 'wme-map-move-end', eventHandler: () => {
      isMapMoving = false;
      rebuildSegmentLengthDisplay();
      const extent = wmeSDK.Map.getMapExtent();
      lastBounds = { west: extent[0], south: extent[1], east: extent[2], north: extent[3] };
      lastZoom = wmeSDK.Map.getZoomLevel();
    }});

    wmeSDK.Events.on({ eventName: 'wme-map-zoom-changed', eventHandler: () => {
      rebuildSegmentLengthDisplay();
    }});

    const opts = getOptions();
    if (opts.showSegmentLength || opts.checkGeometryIssues) handleSegmentLengthToggle();
  }

  function handleSegmentLengthToggle() {
    addGeometryFixButton();
    const opts = getOptions();
    if (opts.showSegmentLength || opts.checkGeometryIssues) {
      if (segmentLengthContainer) segmentLengthContainer.style.display = 'block';
      if (!updateInterval) updateInterval = setInterval(checkAndUpdate, 500);
      rebuildSegmentLengthDisplay();
    } else {
      if (segmentLengthContainer) segmentLengthContainer.style.display = 'none';
      clearSegmentLengthDisplay();
      if (updateInterval) { clearInterval(updateInterval); updateInterval = null; }
    }
  }

  // ─── SHORTCUTS ────────────────────────────────────────────────────────────
  function registerShortcut(shortcutKey) {
    if (!wmeSDK?.Shortcuts) return;
    const shortcutId = 'EZRoad_Mod_QuickUpdate';
    if (wmeSDK.Shortcuts.isShortcutRegistered({ shortcutId }))
      wmeSDK.Shortcuts.deleteShortcut({ shortcutId });
    try {
      wmeSDK.Shortcuts.createShortcut({ callback: handleUpdate, description: 'Quick Update Segments.', shortcutId, shortcutKeys: shortcutKey });
    } catch (e) {
      try {
        wmeSDK.Shortcuts.createShortcut({ callback: handleUpdate, description: 'Quick Update Segments.', shortcutId, shortcutKeys: null });
      } catch (e2) { console.error(e2); }
    }
  }

  // ─── GEOMETRY FIX ─────────────────────────────────────────────────────────
  async function fixVisibleGeometryIssues() {
    const opts = getOptions();
    if (!opts.checkGeometryIssues) {
      WazeToastr?.Alerts?.info(scriptName, 'Please enable "Check Geometry issues" in settings first.');
      return;
    }

    const allSegments = wmeSDK.DataModel.Segments.getAll();
    const extent = wmeSDK.Map.getMapExtent();
    if (!extent) return;
    const bounds = { west: extent[0], south: extent[1], east: extent[2], north: extent[3] };

    const toFix = allSegments.filter(seg => {
      if (!seg.geometry || seg.junctionId !== null) return false;
      const result = checkGeometryNodePlacement(seg, opts.geometryIssueThreshold);
      if (!result.hasIssue) return false;
      return result.details.some(issue =>
        issue.coordinates[0] >= bounds.west && issue.coordinates[0] <= bounds.east &&
        issue.coordinates[1] >= bounds.south && issue.coordinates[1] <= bounds.north
      );
    });

    if (toFix.length === 0) {
      WazeToastr?.Alerts?.error(scriptName, 'No visible geometry issues to fix.');
      return;
    }

    const performFix = async () => {
      let fixed = 0, errors = 0;
      for (const seg of toFix) {
        try {
          const result = checkGeometryNodePlacement(seg, opts.geometryIssueThreshold);
          if (!result.hasIssue) continue;
          const badIdx  = new Set(result.details.map(d => d.nodeIndex));
          const newCoords = seg.geometry.coordinates.filter((_, i) => !badIdx.has(i));
          if (newCoords.length < 2) continue;
          await wmeSDK.DataModel.Segments.updateSegment({ segmentId: seg.id, geometry: { type: 'LineString', coordinates: newCoords } });
          fixed++;
        } catch (e) { errors++; }
      }
      WazeToastr?.Alerts?.success(scriptName, `Fixed ${fixed} segments.${errors > 0 ? ` (${errors} errors)` : ''}`);
      rebuildSegmentLengthDisplay();
    };

    const msg = `Found ${toFix.length} segments with geometry issues. Fix them now?`;
    if (WazeToastr?.Alerts?.confirm) WazeToastr.Alerts.confirm(scriptName, msg, performFix, null, 'Fix', 'Cancel');
    else if (confirm(msg)) performFix();
  }

  /** Inserts a rank-gated bug-icon button into the WME navigation bar. */
  function addGeometryFixButton() {
    const opts = getOptions();
    const userInfo = wmeSDK.State.getUserInfo();
    if (!userInfo || userInfo.rank < UserRankRequiredForGeometryFix - 1) {
      document.getElementById('ezroad-fix-geometry-btn')?.remove();
      return;
    }

    const prefsItem = document.querySelector('wz-navigation-item[data-for="prefs"]');
    let btn = document.getElementById('ezroad-fix-geometry-btn');
    if (btn) { btn.style.display = opts.checkGeometryIssues ? 'block' : 'none'; return; }
    if (!prefsItem) return;

    btn = document.createElement('wz-button');
    Object.assign(btn, { color: 'text', size: 'sm', type: 'button', id: 'ezroad-fix-geometry-btn' });
    Object.assign(btn.style, { margin: '20px auto 0 auto', display: opts.checkGeometryIssues ? 'block' : 'none' });
    btn.innerHTML = `<i class="w-icon w-icon-bug-fill" id="ezroad-bug-icon" style="color: #33CCFF" title="Auto-fix geometry nodes near endpoints"></i>
                     <wz-notification-indicator value="0" id="ezroad-geometry-error-count" style="display:none;"></wz-notification-indicator>`;
    btn.addEventListener('click', fixVisibleGeometryIssues);
    prefsItem.insertAdjacentElement('afterend', btn);
  }

  // ─── HELPERS: CITY / STREET ───────────────────────────────────────────────
  const getEmptyCity = () =>
    wmeSDK.DataModel.Cities.getCity({ cityName: '', countryId: getCurrentCountry().id }) ||
    wmeSDK.DataModel.Cities.addCity({ cityName: '', countryId: getCurrentCountry().id });

  const delayedUpdate = (fn, delay) => new Promise(resolve => setTimeout(() => { fn(); resolve(); }, delay));

  function pushCityNameAlert(cityId, parts) {
    let name = '';
    if (cityId) {
      try {
        const city = wmeSDK.DataModel.Cities.getById({ cityId });
        name = city?.name !== undefined ? city.name : '';
      } catch (e) {}
    }
    parts.push(`City Name: <b>${name || 'None'}</b>`);
  }

  // ─── HELPERS: SEGMENT TYPE ────────────────────────────────────────────────
  const isPedestrianType = roadType => [5, 10, 15, 16, 18, 19].includes(roadType);

  function enableAllTurnsForSegment(segmentId) {
    const seg = wmeSDK.DataModel.Segments.getById({ segmentId });
    if (!seg || isPedestrianType(seg.roadType)) return;
    [seg.fromNodeId, seg.toNodeId].filter(Boolean).forEach(nodeId => {
      if (!wmeSDK.DataModel.Turns.canEditTurnsThroughNode({ nodeId })) return;
      wmeSDK.DataModel.Turns.getTurnsThroughNode({ nodeId }).forEach(turn => {
        if (!turn.isAllowed) {
          try { wmeSDK.DataModel.Turns.updateTurn({ turnId: turn.id, isAllowed: true }); } catch (e) {}
        }
      });
    });
  }

  // ─── HELPERS: HIGHEST SEGMENT LOCK (HRCS) ─────────────────────────────────
  /**
   * Walks the segment graph (DFS) along same-type segments, returning the
   * maximum lockRank found on any differently-typed connected segment.
   * Capped at 6 (L6).
   */
  function getHighestSegLock(segID) {
    const seg = wmeSDK.DataModel.Segments.getById({ segmentId: segID });
    if (!seg) return 1;
    const segType = seg.roadType;
    const checked = [];

    const processNode = (id, getNodeId) => {
      checked.push(id);
      const s = wmeSDK.DataModel.Segments.getById({ segmentId: id });
      if (!s) return 0;
      const nodeId = getNodeId(s);
      if (!nodeId) return 0;
      const allSegs = wmeSDK.DataModel.Segments.getAll();
      const nodeSegs = allSegs.filter(x => (x.fromNodeId === nodeId || x.toNodeId === nodeId) && x.id !== id);
      let max = 0;
      nodeSegs.forEach(ns => {
        if (ns.roadType !== segType) max = Math.max(max, ns.lockRank ?? 0);
        else if (!checked.includes(ns.id)) max = Math.max(max, processNode(ns.id, getNodeId));
      });
      return max;
    };

    return Math.min(
      Math.max(
        processNode(segID, s => s.toNodeId),
        processNode(segID, s => s.fromNodeId)
      ),
      6
    );
  }

  // ─── PEDESTRIAN ↔ ROUTABLE CONVERSION ────────────────────────────────────
  /**
   * When switching between pedestrian types (5, 10, 15, 16, 18, 19) and
   * routable types, WME requires deleting and recreating the segment.
   * Shows a confirmation dialog before proceeding.
   * Returns:
   *   new segment ID (number) – success
   *   undefined               – async confirmation dialog pending
   *   null                    – cancelled or error
   *   original segmentId      – no type-class change needed
   */
  function recreateSegmentIfNeeded(segmentId, targetRoadType, copyConnectedNameData) {
    const seg = wmeSDK.DataModel.Segments.getById({ segmentId });
    if (!seg) return null;

    const currentIsPed = isPedestrianType(seg.roadType);
    const targetIsPed  = isPedestrianType(targetRoadType);
    if (currentIsPed === targetIsPed) return segmentId;

    const swapMsg = currentIsPed
      ? 'Converting a pedestrian segment to a street type will delete and recreate the segment. Continue?'
      : 'Converting a street segment to a pedestrian type will delete and recreate the segment. Continue?';

    const performRecreation = () => {
      try {
        const geometry = seg.geometry;
        const oldPrimaryStreetId = seg.primaryStreetId;
        const oldAltStreetIds    = seg.alternateStreetIds || [];

        wmeSDK.DataModel.Segments.deleteSegment({ segmentId });

        const newId = wmeSDK.DataModel.Segments.addSegment({ geometry, roadType: targetRoadType });
        if (!newId) return null;

        // Restore address
        let primaryStreetId = oldPrimaryStreetId;
        if (!primaryStreetId) {
          const city = getTopCity() || getCurrentCountry();
          let st = wmeSDK.DataModel.Streets.getStreet({ cityId: city.id, streetName: '' });
          if (!st) st = wmeSDK.DataModel.Streets.addStreet({ streetName: '', cityId: city.id });
          primaryStreetId = st.id;
        }
        wmeSDK.DataModel.Segments.updateAddress({ segmentId: newId, primaryStreetId, alternateStreetIds: oldAltStreetIds });

        if (copyConnectedNameData?.primaryStreetId)
          wmeSDK.DataModel.Segments.updateAddress({ segmentId: newId, primaryStreetId: copyConnectedNameData.primaryStreetId, alternateStreetIds: copyConnectedNameData.alternateStreetIds || [] });

        wmeSDK.Editing.setSelection({ selection: { ids: [newId], objectType: 'segment' } });

        if (currentIsPed && !targetIsPed)
          setTimeout(() => enableAllTurnsForSegment(newId), 300);

        WazeToastr?.Alerts?.success(scriptName, currentIsPed ? 'Converted to street type!' : 'Converted to pedestrian type!', false, false, 3000);
        return newId;
      } catch (e) {
        WazeToastr?.Alerts?.error(scriptName, `Segment recreation failed: ${e.message}`);
        return null;
      }
    };

    if (WazeToastr?.Alerts?.confirm) {
      WazeToastr.Alerts.confirm(scriptName, swapMsg, performRecreation, () => {}, 'Continue', 'Cancel');
      return undefined; // async – caller must handle
    }
    if (!window.confirm(swapMsg)) return null;
    return performRecreation();
  }

  // ─── MAIN UPDATE ──────────────────────────────────────────────────────────
  /**
   * Applies all enabled options to the current segment selection.
   * Operations are staggered with delayedUpdate() to let WME process each change
   * before the next one is applied.
   */
  const handleUpdate = () => {
    const sel = wmeSDK.Editing.getSelection();
    if (!sel || sel.objectType !== 'segment') return;

    const opts = getOptions();
    const alertParts = [];
    const promises   = [];

    // ── Copy all attributes from best-connected segment ───────────────────
    if (opts.copySegmentAttributes && !window.suppressCopySegmentAttributes) {
      sel.ids.forEach(id => {
        promises.push(delayedUpdate(() => {
          try {
            const connIds  = getConnectedSegmentIDs(id);
            // Prefer connected segment with a named primary street
            const preferred = connIds.find(cid => {
              const cs = wmeSDK.DataModel.Segments.getById({ segmentId: cid });
              const st = cs && wmeSDK.DataModel.Streets.getById({ streetId: cs.primaryStreetId });
              return st?.name;
            }) || connIds[0];

            if (!preferred) { alertParts.push('No connected segment found.'); return; }

            const cs = wmeSDK.DataModel.Segments.getById({ segmentId: preferred });
            wmeSDK.DataModel.Segments.updateSegment({
              segmentId: id,
              fwdSpeedLimit: cs.fwdSpeedLimit, revSpeedLimit: cs.revSpeedLimit,
              roadType: cs.roadType, lockRank: cs.lockRank,
              elevationLevel: cs.elevationLevel, direction: getDirectionFromSegment(cs),
            });
            wmeSDK.DataModel.Segments.updateAddress({ segmentId: id, primaryStreetId: cs.primaryStreetId, alternateStreetIds: cs.alternateStreetIds || [] });
            copyFlagAttributes(preferred, id);
            alertParts.push('Copied all attributes from connected segment.');
          } catch (e) { console.error(e); }
        }, 100));
      });

      Promise.all(promises).then(() => {
        if (alertParts.length) WazeToastr?.Alerts?.info(scriptName, alertParts.join('<br>'), false, false, 5000);
        if (opts.autosave) setTimeout(() => wmeSDK.Editing.save(), 600);
      });
      return;
    }

    // ── Motorbike restriction ─────────────────────────────────────────────
    if (opts.restrictExceptMotorbike) {
      applyMotorbikeOnlyRestriction(sel.ids[0]).then(result => {
        if (result === true)
          WazeToastr?.Alerts?.success(scriptName, `Motorbike-only restriction applied ✓`, false, false, 3000);
        else if (result === 'not_supported')
          WazeToastr?.Alerts?.warning(scriptName, 'UI automation failed — please apply restriction manually.', false, false, 8000);
      });
    }

    sel.ids.forEach((origId, idx) => {
      let id = origId;

      // ── Pedestrian ↔ routable conversion ─────────────────────────────
      if (opts.roadType) {
        const seg = wmeSDK.DataModel.Segments.getById({ segmentId: id });
        let copyConnectedNameData = null;

        if (!isPedestrianType(seg.roadType) && isPedestrianType(opts.roadType) && opts.copySegmentName) {
          const allSegs = wmeSDK.DataModel.Segments.getAll();
          const connId  = allSegs.find(s => s.id !== id && (s.fromNodeId === seg.fromNodeId || s.toNodeId === seg.fromNodeId || s.fromNodeId === seg.toNodeId || s.toNodeId === seg.toNodeId))?.id;
          if (connId) {
            const cs = wmeSDK.DataModel.Segments.getById({ segmentId: connId });
            copyConnectedNameData = { primaryStreetId: cs.primaryStreetId, alternateStreetIds: cs.alternateStreetIds || [] };
          }
        }

        const newId = recreateSegmentIfNeeded(id, opts.roadType, copyConnectedNameData);
        if (newId === undefined) return; // async dialog pending
        if (!newId) return;             // cancelled
        if (newId !== id) id = newId;
      }

      // ── Road type ──────────────────────────────────────────────────────
      promises.push(delayedUpdate(() => {
        if (!opts.roadType) return;
        const seg = wmeSDK.DataModel.Segments.getById({ segmentId: id });
        const rt  = roadTypes.find(r => r.value === opts.roadType);
        if (seg.roadType === opts.roadType) { alertParts.push(`Road Type: <b>${rt?.name} (exists)</b>`); return; }
        wmeSDK.DataModel.Segments.updateSegment({ segmentId: id, roadType: opts.roadType });
        alertParts.push(`Road Type: <b>${rt?.name}</b>`);
      }, 200));

      // ── Lock level ─────────────────────────────────────────────────────
      promises.push(delayedUpdate(() => {
        if (!opts.setLock) return;
        const rank = wmeSDK.State.getUserInfo().rank;
        const rt   = roadTypes.find(r => r.value === opts.roadType);
        if (!rt) return;
        const lockSetting = opts.locks.find(l => l.id === rt.id);
        if (!lockSetting) return;
        let toLock = lockSetting.lock === 'HRCS' ? getHighestSegLock(id) : parseInt(lockSetting.lock, 10) - 1;
        toLock = Math.max(0, Math.min(toLock, rank));
        const seg = wmeSDK.DataModel.Segments.getById({ segmentId: id });
        if (seg.lockRank !== toLock) {
          wmeSDK.DataModel.Segments.updateSegment({ segmentId: id, lockRank: toLock });
          alertParts.push(`Lock Level: <b>L${toLock + 1}</b>`);
        }
      }, 300));

      // ── Speed limit ────────────────────────────────────────────────────
      promises.push(delayedUpdate(() => {
        if (!opts.updateSpeed) return;
        const rt = roadTypes.find(r => r.value === opts.roadType);
        if (!rt) return;
        const sp = opts.speeds.find(s => s.id === rt.id);
        if (!sp) return;
        const spVal = parseInt(sp.speed, 10);
        const speedToSet = !isNaN(spVal) && spVal > 0 ? spVal : null;
        const seg = wmeSDK.DataModel.Segments.getById({ segmentId: id });
        if (seg.fwdSpeedLimit != speedToSet || seg.revSpeedLimit != speedToSet) {
          wmeSDK.DataModel.Segments.updateSegment({ segmentId: id, fwdSpeedLimit: speedToSet, revSpeedLimit: speedToSet });
          alertParts.push(`Speed Limit: <b>${speedToSet ?? 'unset'}</b>`);
        }
      }, 400));

      // ── City / street address ──────────────────────────────────────────
      // (condensed — full logic handles setStreet, setStreetCity, and city inheritance)
      {
        const segment = wmeSDK.DataModel.Segments.getById({ segmentId: id });
        let city = null;
        if (opts.setStreetCity) {
          city = wmeSDK.DataModel.Cities.getAll().find(c => c.isEmpty) || wmeSDK.DataModel.Cities.addCity({ cityName: '' });
        } else {
          city = getTopCity();
          if (!city || city.isEmpty) {
            const addr = getFirstConnectedSegmentAddress(id);
            if (addr?.city?.id) {
              const cc = wmeSDK.DataModel.Cities.getById({ cityId: addr.city.id });
              if (cc && !cc.isEmpty && cc.name !== undefined) city = cc;
            }
          }
          if (!city || city.isEmpty)
            city = wmeSDK.DataModel.Cities.getAll().find(c => c.isEmpty) || wmeSDK.DataModel.Cities.addCity({ cityName: '' });
        }

        if (opts.setStreet) {
          let st = wmeSDK.DataModel.Streets.getStreet({ cityId: city.id, streetName: '' }) ||
                   wmeSDK.DataModel.Streets.addStreet({ streetName: '', cityId: city.id });
          wmeSDK.DataModel.Segments.updateAddress({ segmentId: id, primaryStreetId: st.id, alternateStreetIds: [] });
        } else if (segment?.primaryStreetId) {
          const curSt = wmeSDK.DataModel.Streets.getById({ streetId: segment.primaryStreetId });
          const name  = curSt?.name || '';
          let st = wmeSDK.DataModel.Streets.getStreet({ cityId: city.id, streetName: name }) ||
                   wmeSDK.DataModel.Streets.addStreet({ streetName: name, cityId: city.id });
          wmeSDK.DataModel.Segments.updateAddress({ segmentId: id, primaryStreetId: st.id });
          if (opts.setStreetCity) { pushCityNameAlert(city.id, alertParts); }
        }
      }

      // ── Unpaved (DOM chip click — SDK flagAttributes read is unreliable) ─
      promises.push(delayedUpdate(() => {
        const seg = wmeSDK.DataModel.Segments.getById({ segmentId: id });
        const targetUnpaved = !isPedestrianType(seg.roadType) && opts.unpaved;
        const isUnpaved     = seg.flagAttributes?.unpaved === true;

        if (targetUnpaved === isUnpaved) { alertParts.push(`Paved: <b>${isUnpaved ? 'Unpaved' : 'Paved'} (already set)</b>`); return; }

        // Try chip click first; fall back to hidden checkbox
        const unpavedIcon = openPanel?.querySelector('.w-icon-unpaved-fill');
        const chip = unpavedIcon?.closest('wz-checkable-chip');
        if (chip) { chip.click(); }
        else {
          const cb = openPanel?.querySelector('wz-checkbox[name="unpaved"] input[type="checkbox"]');
          if (cb) cb.click();
        }
        alertParts.push(`Paved: <b>${targetUnpaved ? 'Unpaved' : 'Paved'}</b>`);
      }, 500));

      // ── Copy segment name (3-tier logic) ──────────────────────────────
      promises.push(delayedUpdate(() => {
        if (!opts.copySegmentName) return;
        // A-side first, then B-side
        const aSide = wmeSDK.DataModel.Segments.getConnectedSegments({ segmentId: id, reverseDirection: true }).map(s => s.id);
        const bSide = wmeSDK.DataModel.Segments.getConnectedSegments({ segmentId: id, reverseDirection: false }).map(s => s.id);
        const candidates = [...aSide, ...bSide];

        const seg = wmeSDK.DataModel.Segments.getById({ segmentId: id });
        const selStreet = seg.primaryStreetId ? wmeSDK.DataModel.Streets.getById({ streetId: seg.primaryStreetId }) : null;
        const selName   = selStreet?.name || '';
        const selAlts   = seg.alternateStreetIds || [];

        // TIER 1: primary names match — merge missing alts only
        let tier1 = candidates
          .map(cid => {
            const cs = wmeSDK.DataModel.Segments.getById({ segmentId: cid });
            if (!cs) return null;
            const st = wmeSDK.DataModel.Streets.getById({ streetId: cs.primaryStreetId });
            if (!st?.name || st.name !== selName) return null;
            return { cid, cs, altCount: (cs.alternateStreetIds || []).length };
          })
          .filter(Boolean)
          .sort((a, b) => b.altCount - a.altCount)[0];

        if (tier1) {
          const newAltIds = [...selAlts, ...(tier1.cs.alternateStreetIds || []).filter(a => !selAlts.includes(a))];
          wmeSDK.DataModel.Segments.updateAddress({ segmentId: id, primaryStreetId: seg.primaryStreetId, alternateStreetIds: newAltIds });
          alertParts.push(`Merged alts for: <b>${selName}</b>`);
          return;
        }

        // TIER 2 / TIER 3: replace primary and alts from best candidate (sorted by altCount)
        const best = candidates
          .map(cid => {
            const cs = wmeSDK.DataModel.Segments.getById({ segmentId: cid });
            const st = cs && wmeSDK.DataModel.Streets.getById({ streetId: cs.primaryStreetId });
            if (!st?.name && !(cs?.alternateStreetIds?.length)) return null;
            return { cid, cs, name: st?.name || '', altCount: (cs?.alternateStreetIds || []).length };
          })
          .filter(Boolean)
          .sort((a, b) => b.altCount - a.altCount)[0];

        if (best) {
          wmeSDK.DataModel.Segments.updateAddress({ segmentId: id, primaryStreetId: best.cs.primaryStreetId, alternateStreetIds: best.cs.alternateStreetIds || [] });
          alertParts.push(`${selName ? 'Replaced' : 'Copied'} name: <b>${best.name}</b>`);
        }
      }, 550));

      // ── Enable U-turns ─────────────────────────────────────────────────
      if (opts.enableUTurn) enableAllTurnsForSegment(id);
    });

    // ── Show summary toast and autosave ────────────────────────────────────
    Promise.all(promises).then(() => {
      if (alertParts.length)
        WazeToastr?.Alerts?.info(scriptName, alertParts.join('<br>'), false, false, 5000);
      if (opts.autosave)
        setTimeout(() => wmeSDK.Editing.save(), 600);
    });
  };

  // ─── SETTINGS PANEL ───────────────────────────────────────────────────────
  // (constructSettings builds a jQuery-based WME side-panel tab with:
  //  - per-road-type radio buttons, lock dropdowns, and speed inputs
  //  - additional option checkboxes with mutual-exclusion enforcement
  //  - geometry threshold input
  //  - export / import JSON config
  //  - custom named preset save / load / delete
  //  - reset button
  // The full implementation is ~350 lines; see source file lines 3600–3956.)
  function constructSettings() {
    // [Full settings panel construction — see source file]
  }

})();
```
