# WME Quick HN Importer for NP - Script Example

WME Quick HN Importer for NP is a house number import tool for the Waze Map Editor, designed specifically for Nepal (and adaptable for any region). It supports loading house number data from local geometry files and remote URL-based open data sources, and then lets editors click each point to quickly assign the house number to the nearest road segment.

## Overview

This script enhances WME's house number editing workflow by:

- **Loading open data** from GeoJSON, KML, KMZ, GML, GPX, WKT, and ZIP (Shapefile) files.
- **Fetching live data** from the Lalitpur Metropolitan City (LMC) Metric House API (ward-by-ward).
- **Persisting data** across page reloads using IndexedDB so uploads are not lost on refresh.
- **Matching house numbers** to the nearest named road segment, with fuzzy Nepal street-name normalization.
- **Visualizing import points** on an SDK-managed overlay layer with color-coded status (matched, unmatched, already added).
- **Allowing layer offset** adjustment (X/Y shift in meters) via a draggable dialog.
- **Autocomplete shortcut** (Ctrl+Space) to bulk-assign all visible matching house numbers in one keypress.

## Architecture

### Data Flow

1. **File import** (`handleFileImport`) → parse with format-specific library → CRS transform to WGS84 → user picks `street`, `number`, and optional `nepali` attributes → features stored in `uploadedFileFeatures` array and persisted to IndexedDB.
2. **URL import** (`fetchMetricHouseData`) → boundary check (Lalitpur polygon) → parallel ward API requests → build `urlFeatures` array → persist to IndexedDB.
3. `Repository.getExtentData()` combines both sources, deduplicates, and returns features in the current map extent.
4. `updateLayer()` clears and redraws the SDK layer with offset-adjusted coordinates.
5. Clicking a feature → `layerFeatureClickHandler` → street-name matching → `addHouseNumber` via `wmeSDK.DataModel.HouseNumbers.addHouseNumber`.

### Key Components

| Component | Purpose |
|-----------|---------|
| `Repository` | In-memory spatial grid + directory of all features; merges file + URL sources |
| `Shortcut` | Registers/removes the Ctrl+Space autocomplete shortcut via `wmeSDK.Shortcuts` |
| `Messages` | Floating overlay messages on the map viewport (loading spinner, autocomplete hint) |
| `cleanup` | Tracks all event listeners and observers for safe re-initialization |
| `initDatabase` | Opens IndexedDB `QHNI_Database` v3 with `uploadedFeatures` + `urlFeatures` stores |
| `normalizeNepalStreetName` | Applies suffix normalization (Marg→Marga, Road→Rd, Street→St, Saraswoti→Saraswati) |
| `isHouseNumberAlreadyAdded` | Checks `streetNumbers` Map to dim already-added points |
| `applyHNLayerOffset` | Shifts feature geometries by configured X/Y offset using `turf.transformTranslate` |
| `createFileUploadUI` | Builds the sidebar tab with file picker, URL toggle, offset button, and status |
| `rebuildStreetNumbers` | Rebuilds street↔number tracking from the `W.model` (source of truth for undo/redo) |

### SDK APIs Used

- `wmeSDK.Sidebar.registerScriptTab()` — register the sidebar tab
- `wmeSDK.Map.addLayer()` / `removeAllFeaturesFromLayer()` / `addFeaturesToLayer()` / `redrawLayer()` — layer management
- `wmeSDK.Map.setLayerVisibility()` / `isLayerVisible()` — visibility control
- `wmeSDK.Map.getMapExtent()` / `getMapCenter()` / `getZoomLevel()` / `setMapCenter()` — map navigation
- `wmeSDK.Map.getMapViewportElement()` — for injecting the loading messages overlay
- `wmeSDK.Events.on()` / `once()` — event subscriptions (map-move-end, layer-visibility-changed, layer-feature-clicked, selection-changed, data-model-objects-added/removed/saved, after-undo, after-redo-clear, wme-ready)
- `wmeSDK.Events.trackLayerEvents()` / `trackDataModelEvents()` — activate SDK event tracking
- `wmeSDK.DataModel.HouseNumbers.addHouseNumber()` — add a house number to a segment
- `wmeSDK.DataModel.Streets.getAll()` / `getById()` — street name lookup
- `wmeSDK.DataModel.Segments.getAll()` / `getById()` — segment geometry for proximity search
- `wmeSDK.Editing.getSelection()` / `setSelection()` — segment selection management
- `wmeSDK.Shortcuts.createShortcut()` / `deleteShortcut()` — keyboard shortcut management

### Dependencies

- **Turf.js v7** — spatial operations (distance, point-in-polygon, bboxPolygon, transformTranslate, center)
- **proj4js v2.19** — coordinate reference system transformations
- **GeoKMLer / GeoKMZer / GeoWKTer / GeoGPXer / GeoGMLer / GeoSHPer** — format parsers
- **WazeToastr** — toast notification system (success, warning, error, info, prompt)
- **Preeti to Unicode Converter** — optional Nepali script conversion for tooltip display
- **IndexedDB** — client-side persistence for uploaded and URL features

### File Structure (line ranges)

- Metadata & constants (lines 1–60): UserScript header, globals, cleanup manager, street cache
- Database layer (lines 100–450): `initDatabase`, `loadUploadedFeatures`, `storeUploadedFeatures`, `clearUploadedFeatures`, `loadURLFeatures`, `storeURLFeatures`, `clearURLFeatures`
- Lalitpur API fetch (lines 450–730): `fetchMetricHouseData`, `toggleParsingMessage`
- Geometry processing (lines 730–1200): `setupProjectionsAndTransforms`, `stripZ`, `transformGeoJSON`, `applyHNLayerOffset`, `showHNLayerOffsetDialog`, `convertCoordinates`
- File parsing & import (lines 1200–1600): `parseFileFormat`, `handleFileImport`, `presentFeaturesAttributesSDK`
- Repository & Shortcut (lines 1600–1900): `Messages`, `Shortcut`, `Repository`
- Sidebar UI (lines 1900–2200): `createFileUploadUI`, `clearUploadedData`
- Initialization & event wiring (lines 2200–2650): `init`, `updateLayer`, `findNearestSegment`, `isHouseNumberAlreadyAdded`, `rebuildStreetNumbers`, `refreshLayerFeatures`
- Utilities (lines 2650–2824): `simplifyNumber`, `cleanupName`, `normalizeNepalStreetName`

## Common Gotchas

- **Zoom requirement** — Layer only shows at zoom level 19+ with the WME house_numbers layer visible.
- **Boundary check** — The LMC Metric House API only loads data when the map center is inside the Lalitpur Municipality polygon. Outside this area the checkbox is auto-unchecked.
- **IndexedDB v3** — If the database is corrupt or missing stores, `initDatabase` deletes and recreates the entire database.
- **Street name normalization** — Street matching uses `normalizeNepalStreetName` on both the feature and WME streets, so mismatches from suffix differences (Marg/Marga, Road/Rd) are handled automatically.
- **Undo/redo sync** — `wme-after-undo` and `wme-after-redo-clear` events call `rebuildStreetNumbers` from the `W.model` (legacy layer) to keep the already-added tracking accurate.
- **Offset double-apply** — `Repository.clearAll()` does NOT clear `uploadedFileFeatures` or `urlFeatures`; offsets are applied at render time in `updateLayer`, not stored back into source arrays.

## Maintenance Notes

### Testing Checklist

- [ ] Zoom in/out across level 19 boundary — layer should appear/disappear correctly
- [ ] Import GeoJSON, KML, KMZ, GPX, GML, WKT, ZIP files — each should parse and display
- [ ] Lalitpur boundary check — Metric House checkbox outside boundary should revert to unchecked
- [ ] Page reload with data — features should restore from IndexedDB automatically
- [ ] Undo after adding HN — layer opacity should revert (already-added marking cleared)
- [ ] Offset dialog — directional shifts should move points and show toast notifications
- [ ] Street mismatch prompt — WazeToastr.Alerts.prompt should appear with duration input
- [ ] Ctrl+Space autocomplete — should bulk-add all matching visible HNs

```javascript
// ==UserScript==
// @name         WME Quick HN Importer for NP
// @namespace    https://greasyfork.org/users/1087400
// @version      1.2.7.8
// @description  Quickly add house numbers based on open data sources of house numbers. Supports loading from URLs and file formats: GeoJSON, KML, KMZ, GML, GPX, WKT, ZIP (Shapefile)
// @author       kid4rm90s
// @include      /^https:\/\/(www|beta)\.waze\.com\/(?!user\/)(.{2,6}\/)?editor.*$/
// @grant        GM_xmlhttpRequest
// @grant        unsafeWindow
// @license      MIT
// @connect      greasyfork.org
// @connect      geonep.com.np
// @require      https://cdn.jsdelivr.net/npm/@turf/turf@7.2.0/turf.min.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.19.10/proj4.min.js
// @require      https://update.greasyfork.org/scripts/524747/GeoKMLer.js
// @require      https://update.greasyfork.org/scripts/527113/GeoKMZer.js
// @require      https://update.greasyfork.org/scripts/523986/GeoWKTer.js
// @require      https://update.greasyfork.org/scripts/523870/GeoGPXer.js
// @require      https://update.greasyfork.org/scripts/526229/GeoGMLer.js
// @require      https://update.greasyfork.org/scripts/526996/GeoSHPer.js
// @require      https://update.greasyfork.org/scripts/560385/WazeToastr.js
// @require https://update.greasyfork.org/scripts/565546/Preeti%20to%20Unicode%20Converter.js
// @downloadURL https://update.greasyfork.org/scripts/566190/WME%20Quick%20HN%20Importer%20for%20NP.user.js
// @updateURL https://update.greasyfork.org/scripts/566190/WME%20Quick%20HN%20Importer%20for%20NP.meta.js
// ==/UserScript==

/* global getWmeSdk, turf, proj4, WazeToastr */
// Original Author: Glodenox (https://greasyfork.org/en/scripts/421430-wme-quick-hn-importer) and JS55CT for WME GEOFILE (https://greasyfork.org/en/scripts/540764-wme-geofile) script. Modified by kid4rm90s for Quick HN Importer for Nepal with additional features.
(function main() {
  ('use strict');

  const scriptName = GM_info.script.name;
  const scriptVersion = GM_info.script.version;
  const downloadUrl = 'https://update.greasyfork.org/scripts/566190/WME%20Quick%20HN%20Importer%20for%20NP.user.js';
  const forumURL = 'https://greasyfork.org/en/scripts/566190-wme-quick-hn-importer-for-np/feedback';

  let wmeSDK;
  const LAYER_NAME = 'Quick HN importer for NP';
  const SHORTCUT_ID = 'quickhnimporterfornp';
  let db; // IndexedDB database instance
  let debug = false;

  // Cleanup manager to prevent memory leaks
  let cleanup = {
    eventCleanups: [],
    observers: [],

    addEvent: (cleanupFn) => {
      if (cleanupFn && typeof cleanupFn === 'function') {
        cleanup.eventCleanups.push(cleanupFn);
      }
    },

    addObserver: (observer) => {
      if (observer) {
        cleanup.observers.push(observer);
      }
    },

    all: () => {
      cleanup.eventCleanups.forEach(fn => { try { fn(); } catch (e) {} });
      cleanup.eventCleanups = [];
      cleanup.observers.forEach(obs => { try { obs.disconnect(); } catch (e) {} });
      cleanup.observers = [];
      if (wmeSDK) {
        try { wmeSDK.Events.stopLayerEventsTracking({ layerName: LAYER_NAME }); } catch (e) {}
        try { wmeSDK.Events.stopLayerEventsTracking({ layerName: "house_numbers" }); } catch (e) {}
        try { wmeSDK.Events.stopDataModelEventsTracking({ dataModelName: "segmentHouseNumbers" }); } catch (e) {}
        try { wmeSDK.Events.stopDataModelEventsTracking({ dataModelName: "streets" }); } catch (e) {}
      }
      Repository.clearAll();
      Shortcut.deactivate();
    }
  };

  // Cache for remembered street name pairs with expiration
  let streetNameCache = {};

  const createCacheKey = (originalStreet, targetStreet) => `${originalStreet}|||${targetStreet}`;

  const isCachedStreetPair = (originalStreet, targetStreet) => {
    const key = createCacheKey(originalStreet, targetStreet);
    if (streetNameCache[key]) {
      if (Date.now() < streetNameCache[key].expiresAt) return true;
      delete streetNameCache[key];
    }
    return false;
  };

  const addToCacheStreetPair = (originalStreet, targetStreet, durationMinutes) => {
    const key = createCacheKey(originalStreet, targetStreet);
    streetNameCache[key] = { expiresAt: Date.now() + durationMinutes * 60 * 1000 };
  };

  (unsafeWindow || window).SDK_INITIALIZED.then(async () => {
    wmeSDK = getWmeSdk({ scriptId: "quick-hn-importer-for-np", scriptName: "Quick HN Importer for NP" });
    let loadResult = { loaded: false, count: 0 };
    let urlLoadResult = { loaded: false, count: 0 };

    try {
      await initDatabase();
      loadResult = await loadUploadedFeatures();
      const urlSourceEnabled = localStorage.getItem('qhni-enable-url-source') === 'true';
      if (urlSourceEnabled) urlLoadResult = await loadURLFeatures();
    } catch (error) {
      log('Error initializing database: ' + error);
    }

    wmeSDK.Events.once({ eventName: "wme-ready" }).then(() => {
      init();
      const totalCount = loadResult.count + urlLoadResult.count;
      if (totalCount > 0) {
        setTimeout(() => {
          const zoomLevel = wmeSDK.Map.getZoomLevel();
          const houseNumbersVisible = wmeSDK.Map.isLayerVisible({ layerName: "house_numbers" });
          let message = '';
          if (loadResult.count > 0 && urlLoadResult.count > 0) {
            message = `Loaded ${loadResult.count} features from ${loadResult.filename} and ${urlLoadResult.count} Metric House features`;
          } else if (loadResult.count > 0) {
            message = `Loaded ${loadResult.count} features from ${loadResult.filename}`;
          } else if (urlLoadResult.count > 0) {
            message = `Loaded ${urlLoadResult.count} Metric House features`;
          }
          if (typeof WazeToastr !== 'undefined' && WazeToastr.Alerts) {
            if (zoomLevel < 19 || !houseNumbersVisible) {
              WazeToastr.Alerts.warning('Data Restored', `${message}. Zoom to level 19+ and enable House Numbers layer to view.`);
            } else {
              WazeToastr.Alerts.success('Data Restored', message);
            }
          }
          updateLayer();
        }, 1500);
      }
    });
  });

  let previousCenterLocation = null;
  let selectedStreetNames = [];
  let autocompleteFeatures = [];
  let streetNumbers = new Map();
  let streetNames = new Set();
  let hnLayerOffset = { x: 0, y: 0 };
  let selectedNepaliAttribute = null;

  // ─── Logging ────────────────────────────────────────────────────────────────
  function log(message) { console.log(`[${scriptName}]`, message); }

  // ─── IndexedDB ──────────────────────────────────────────────────────────────
  function initDatabase() {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open('QHNI_Database', 3);
      request.onerror = () => reject(request.error);
      request.onsuccess = () => {
        db = request.result;
        const hasUploaded = db.objectStoreNames.contains('uploadedFeatures');
        const hasUrl = db.objectStoreNames.contains('urlFeatures');
        if (!hasUploaded || !hasUrl) {
          db.close();
          const del = indexedDB.deleteDatabase('QHNI_Database');
          del.onsuccess = () => initDatabase().then(resolve).catch(reject);
          del.onerror = () => reject(new Error('Database validation failed'));
        } else {
          resolve();
        }
      };
      request.onupgradeneeded = (event) => {
        db = event.target.result;
        if (!db.objectStoreNames.contains('uploadedFeatures'))
          db.createObjectStore('uploadedFeatures', { keyPath: 'id' });
        if (!db.objectStoreNames.contains('urlFeatures'))
          db.createObjectStore('urlFeatures', { keyPath: 'id' });
      };
    });
  }

  async function loadUploadedFeatures() {
    if (!db || !db.objectStoreNames.contains('uploadedFeatures'))
      return { loaded: false, count: 0 };
    return new Promise((resolve) => {
      const req = db.transaction(['uploadedFeatures'], 'readonly').objectStore('uploadedFeatures').get('current');
      req.onerror = () => resolve({ loaded: false, count: 0 });
      req.onsuccess = () => {
        if (req.result?.features) {
          uploadedFileFeatures = req.result.features;
          resolve({ loaded: true, count: uploadedFileFeatures.length, filename: req.result.filename || 'Unknown' });
        } else {
          resolve({ loaded: false, count: 0 });
        }
      };
    });
  }

  async function storeUploadedFeatures(filename) {
    if (!db || !db.objectStoreNames.contains('uploadedFeatures')) return;
    return new Promise((resolve, reject) => {
      const req = db.transaction(['uploadedFeatures'], 'readwrite').objectStore('uploadedFeatures').put({
        id: 'current', features: uploadedFileFeatures, filename, timestamp: new Date().toISOString(), count: uploadedFileFeatures.length
      });
      req.onerror = () => reject(req.error);
      req.onsuccess = () => resolve();
    });
  }

  async function clearUploadedFeatures() {
    if (!db || !db.objectStoreNames.contains('uploadedFeatures')) return;
    return new Promise((resolve, reject) => {
      const req = db.transaction(['uploadedFeatures'], 'readwrite').objectStore('uploadedFeatures').delete('current');
      req.onerror = () => reject(req.error);
      req.onsuccess = () => resolve();
    });
  }

  async function loadURLFeatures() {
    if (!db || !db.objectStoreNames.contains('urlFeatures'))
      return { loaded: false, count: 0 };
    return new Promise((resolve) => {
      const req = db.transaction(['urlFeatures'], 'readonly').objectStore('urlFeatures').get('current');
      req.onerror = () => resolve({ loaded: false, count: 0 });
      req.onsuccess = () => {
        if (req.result?.features) {
          urlFeatures = req.result.features;
          resolve({ loaded: true, count: urlFeatures.length });
        } else {
          resolve({ loaded: false, count: 0 });
        }
      };
    });
  }

  async function storeURLFeatures() {
    if (!db || !db.objectStoreNames.contains('urlFeatures')) return;
    return new Promise((resolve, reject) => {
      const req = db.transaction(['urlFeatures'], 'readwrite').objectStore('urlFeatures').put({
        id: 'current', features: urlFeatures, timestamp: new Date().toISOString(), count: urlFeatures.length
      });
      req.onerror = () => reject(req.error);
      req.onsuccess = () => resolve();
    });
  }

  async function clearURLFeatures() {
    if (!db || !db.objectStoreNames.contains('urlFeatures')) {
      urlFeatures = [];
      return;
    }
    return new Promise((resolve, reject) => {
      const req = db.transaction(['urlFeatures'], 'readwrite').objectStore('urlFeatures').delete('current');
      req.onerror = () => reject(req.error);
      req.onsuccess = () => {
        const directory = Repository.getDirectory?.();
        if (directory) {
          Array.from(directory.keys()).filter(id => id.startsWith('url-') || id.startsWith('np-')).forEach(id => directory.delete(id));
        }
        urlFeatures = [];
        resolve();
      };
    });
  }

  // ─── Lalitpur Metropolitan City API ─────────────────────────────────────────
  async function fetchMetricHouseData() {
    const laliturBoundary = turf.polygon([[
      [85.29377337876386, 27.603309874523035], [85.28907174008309, 27.610757759711703],
      [85.28112722544194, 27.644637619503936], [85.2911097667452,  27.673688570775262],
      [85.301321831427,   27.692360556657775], [85.30740589291473, 27.694362605619077],
      [85.32757155676471, 27.68690327105091],  [85.34449915180973, 27.672768378131995],
      [85.35597653295329, 27.63372772622652],  [85.33227244070862, 27.616131609219202],
      [85.29377337876386, 27.603309874523035]
    ]]);

    const mapCenter = wmeSDK.Map.getMapCenter();
    if (!turf.booleanPointInPolygon(turf.point([mapCenter.lon, mapCenter.lat]), laliturBoundary)) {
      WazeToastr.Alerts.info('Location Notice', 'Metric House data is only available within Lalitpur Municipality.');
      return [];
    }

    toggleParsingMessage(true);
    const wardNumbers = Array.from({ length: 29 }, (_, i) => i + 1);
    let allFeatures = [];

    try {
      const results = await Promise.allSettled(wardNumbers.map(wardNo =>
        httpRequest({ url: `https://geonep.com.np/LMC/ajax/x_building.php?ward_no=${wardNo}` }, (response) => {
          const features = [];
          response.response.features?.forEach((feature) => {
            const props = feature.properties || {};
            const number = props.metric_num;
            const street = props.rd_naeng;
            if (!number || !street) return;
            const center = turf.center(feature);
            features.push({
              type: "Feature",
              id: `url-np-${props.gid}`,
              geometry: center.geometry,
              properties: {
                street: normalizeNepalStreetName(street),
                streetOriginal: street,
                number,
                municipality: props.tole_ne_en || `Ward ${wardNo}`,
                rd_nanep: props.rd_nanep || '',
                type: 'active'
              }
            });
          });
          return features;
        })
      ));

      results.forEach(result => {
        if (result.status === 'fulfilled' && result.value) allFeatures = allFeatures.concat(result.value);
      });
    } finally {
      toggleParsingMessage(false);
    }
    return allFeatures;
  }

  function toggleParsingMessage(show) {
    const existing = document.getElementById('QHNIParsingMessage');
    if (show && !existing) {
      const msg = document.createElement('div');
      msg.id = 'QHNIParsingMessage';
      msg.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);padding:16px 32px;background:rgba(0,0,0,0.7);border-radius:12px;z-index:2000;color:#ffffff;border:2px solid #33ff57;font-family:Arial,sans-serif;font-size:1.1rem;text-align:center;';
      msg.innerHTML = '<i class="fa fa-pulse fa-spinner"></i> Loading Metric House data from LMC, please wait...';
      document.body.appendChild(msg);
    } else if (!show && existing) {
      existing.remove();
    }
  }

  // ─── Projection / CRS setup ──────────────────────────────────────────────────
  proj4.defs("EPSG:3794", "+proj=tmerc +lat_0=0 +lon_0=15 +k=0.9999 +x_0=500000 +y_0=-5000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs +type=crs");

  let projectionMap = {};
  let uploadedFileFeatures = [];
  let urlFeatures = [];

  function setupProjectionsAndTransforms() {
    const projDefs = {
      'EPSG:4326': '+proj=longlat +ellps=WGS84 +datum=WGS84 +units=degrees',
      'EPSG:3857': '+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs',
      'EPSG:4269': '+proj=longlat +a=6378137.0 +b=6356752.31414036 +ellps=GRS80 +datum=NAD83 +units=degrees',
    };
    for (let z = 1; z <= 60; z++) {
      projDefs[`EPSG:326${String(z).padStart(2,'0')}`] = `+proj=utm +zone=${z} +datum=WGS84 +units=m +no_defs`;
      projDefs[`EPSG:327${String(z).padStart(2,'0')}`] = `+proj=utm +zone=${z} +south +datum=WGS84 +units=m +no_defs`;
    }
    for (const [epsg, def] of Object.entries(projDefs)) proj4.defs(epsg, def);
    projectionMap = {
      CRS84: 'EPSG:4326', 'urn:ogc:def:crs:OGC:1.3:CRS84': 'EPSG:4326', WGS84: 'EPSG:4326',
      NAD83: 'EPSG:4269',
    };
    const codes = Object.keys(projDefs).map(k => k.split(':')[1]);
    codes.forEach(code => {
      [`EPSG:${code}`, `urn:ogc:def:crs:EPSG:${code}`, `CRS:${code}`].forEach(k => projectionMap[k] = `EPSG:${code}`);
    });
  }

  function stripZ(coords) {
    return Array.isArray(coords[0]) ? coords.map(stripZ) : coords.slice(0, 2);
  }

  function stripZFromGeoJSON(geoJSON) {
    if (!geoJSON) return geoJSON;
    const stripGeometry = g => g?.coordinates ? { ...g, coordinates: stripZ(g.coordinates) } : g;
    if (geoJSON.type === 'FeatureCollection')
      return { ...geoJSON, features: geoJSON.features.map(f => ({ ...f, geometry: stripGeometry(f.geometry) })) };
    if (geoJSON.type === 'Feature') return { ...geoJSON, geometry: stripGeometry(geoJSON.geometry) };
    return geoJSON.coordinates ? stripGeometry(geoJSON) : geoJSON;
  }

  function applyHNLayerOffset(features) {
    if (!features?.length || (!hnLayerOffset.x && !hnLayerOffset.y)) return features;
    return features.map(feature => {
      try {
        if (feature.geometry?.type === 'Point') {
          let f = feature;
          if (hnLayerOffset.x) f = turf.transformTranslate(f, Math.abs(hnLayerOffset.x), hnLayerOffset.x > 0 ? 90 : 270, { units: 'meters' });
          if (hnLayerOffset.y) f = turf.transformTranslate(f, Math.abs(hnLayerOffset.y), hnLayerOffset.y > 0 ? 0 : 180, { units: 'meters' });
          return f;
        }
      } catch (e) { log('Error applying offset: ' + e); }
      return feature;
    });
  }

  function convertCoordinates(sourceCRS, targetCRS, coordinates) {
    const stripped = stripZ(coordinates);
    if (Array.isArray(stripped[0])) return stripped.map(c => convertCoordinates(sourceCRS, targetCRS, c));
    try { return proj4(sourceCRS, targetCRS, stripped); } catch (e) { return stripped; }
  }

  function transformGeoJSON(geoJSON, sourceCRS, targetCRS) {
    const isValid = crs => typeof crs === 'string' && /^EPSG:\d{4,5}$/.test(crs);
    if (!isValid(sourceCRS) || !isValid(targetCRS) || !proj4.defs[sourceCRS] || !proj4.defs[targetCRS]) return geoJSON;
    const transform = f => { if (f.geometry) f.geometry.coordinates = convertCoordinates(sourceCRS, targetCRS, f.geometry.coordinates); return f; };
    if (geoJSON.type === 'FeatureCollection') geoJSON.features = geoJSON.features.map(transform);
    else if (geoJSON.type === 'Feature') transform(geoJSON);
    geoJSON.crs = { type: 'name', properties: { name: targetCRS } };
    return geoJSON;
  }

  // ─── File parsing ────────────────────────────────────────────────────────────
  async function parseFileFormat(fileContent, fileext, filename) {
    let geoJSON = null;
    switch (fileext.toUpperCase()) {
      case 'GEOJSON': case 'JSON':
        geoJSON = typeof fileContent === 'string' ? JSON.parse(fileContent) : fileContent; break;
      case 'KML':
        const kml = new GeoKMLer(); geoJSON = kml.toGeoJSON(kml.read(fileContent), true); break;
      case 'KMZ': {
        const kmz = new GeoKMZer(); const contents = await kmz.read(fileContent);
        const all = []; for (const { content } of contents) { const k = new GeoKMLer(); const r = k.toGeoJSON(k.read(content), true); if (r.type === 'FeatureCollection') all.push(...r.features); else if (r.type === 'Feature') all.push(r); }
        geoJSON = { type: 'FeatureCollection', features: all }; break; }
      case 'GPX': { const gpx = new GeoGPXer(); geoJSON = gpx.toGeoJSON(gpx.read(fileContent)); break; }
      case 'GML': { const gml = new GeoGMLer(); geoJSON = gml.toGeoJSON(gml.read(fileContent)); break; }
      case 'WKT': { const wkt = new GeoWKTer(); geoJSON = wkt.toGeoJSON(wkt.read(fileContent, filename)); break; }
      case 'ZIP': { const shp = new GeoSHPer(); await shp.read(fileContent); geoJSON = shp.toGeoJSON(); break; }
      default: throw new Error(`Unsupported file format: ${fileext}`);
    }
    if (!geoJSON) throw new Error('Failed to parse file');
    if (geoJSON.type === 'Feature') geoJSON = { type: 'FeatureCollection', features: [geoJSON] };
    else if (geoJSON.type !== 'FeatureCollection') geoJSON = { type: 'FeatureCollection', features: [{ type: 'Feature', geometry: geoJSON, properties: {} }] };
    return stripZFromGeoJSON(geoJSON);
  }

  async function handleFileImport(file) {
    const dotIdx = file.name.lastIndexOf('.');
    const fileext = dotIdx !== -1 ? file.name.substring(dotIdx + 1) : '';
    const filename = dotIdx !== -1 ? file.name.substring(0, dotIdx) : file.name;

    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = async (e) => {
        try {
          let geoJSON = await parseFileFormat(e.target.result, fileext, filename);
          if (!geoJSON?.features?.length) { WazeToastr.Alerts.error('Import Error', 'No features found'); reject('No features'); return; }
          let sourceCRS = 'EPSG:4326';
          const crsName = geoJSON.crs?.properties?.name;
          if (typeof crsName === 'string') sourceCRS = projectionMap[crsName] || crsName;
          if (sourceCRS !== 'EPSG:4326') geoJSON = transformGeoJSON(geoJSON, sourceCRS, 'EPSG:4326');

          const selectedAttrs = await presentFeaturesAttributesSDK(geoJSON.features, geoJSON.features.length, ['street', 'number', 'nepali']);
          if (selectedAttrs.nepali) selectedNepaliAttribute = selectedAttrs.nepali;

          const features = geoJSON.features.map((feature, idx) => {
            const numberValue = feature.properties[selectedAttrs.number];
            if (!numberValue) return null;
            const streetValue = selectedAttrs.street ? feature.properties[selectedAttrs.street] : null;
            const nepaliValue = selectedAttrs.nepali ? feature.properties[selectedAttrs.nepali] : null;
            let point = feature.geometry.type === 'Point' ? feature.geometry : turf.center(turf.feature(feature.geometry)).geometry;
            const featureObj = {
              type: 'Feature', id: `file-${filename}-${idx}`,
              geometry: point,
              properties: {
                street: streetValue ? normalizeNepalStreetName(String(streetValue)) : '',
                streetOriginal: streetValue ? String(streetValue) : '',
                number: String(numberValue), municipality: filename, type: 'active'
              }
            };
            if (nepaliValue) featureObj.properties[selectedAttrs.nepali] = nepaliValue;
            return featureObj;
          }).filter(Boolean);

          if (!features.length) { WazeToastr.Alerts.error('Import Error', 'No valid features'); reject('No valid features'); return; }
          uploadedFileFeatures = features;
          try { await storeUploadedFeatures(file.name); } catch (e) { log('Error saving to IndexedDB: ' + e); }

          const coords = features.map(f => f.geometry.coordinates);
          const center = [(Math.min(...coords.map(c=>c[0]))+Math.max(...coords.map(c=>c[0])))/2, (Math.min(...coords.map(c=>c[1]))+Math.max(...coords.map(c=>c[1])))/2];
          WazeToastr.Alerts.success('Import Success', `Loaded ${features.length} features from ${file.name}`);
          try { wmeSDK.Map.setMapCenter({ lonLat: { lon: center[0], lat: center[1] }, zoomLevel: 19 }); } catch (e) {}
          resolve(features);
        } catch (error) {
          WazeToastr.Alerts.error('Import Error', 'Failed to process file');
          reject(error);
        }
      };
      reader.onerror = () => { WazeToastr.Alerts.error('File Error', 'Failed to read file'); reject('Read error'); };
      (fileext.toUpperCase() === 'ZIP' || fileext.toUpperCase() === 'KMZ') ? reader.readAsArrayBuffer(file) : reader.readAsText(file);
    });
  }

  function presentFeaturesAttributesSDK(features, nbFeatures, attributeTypes) {
    return new Promise((resolve, reject) => {
      const allAttributes = new Set();
      features.slice(0, 10).forEach(f => f.properties && Object.keys(f.properties).forEach(k => allAttributes.add(k)));
      if (!allAttributes.size) { WazeToastr.Alerts.error('Import Error', 'No attributes found'); reject('No attributes'); return; }

      const overlay = Object.assign(document.createElement('div'), { style: 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:9999;' });
      const modal = Object.assign(document.createElement('div'), { style: 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:inherit;padding:20px;border-radius:8px;box-shadow:0 4px 20px rgba(0,0,0,0.3);z-index:10000;max-width:600px;max-height:80vh;overflow-y:auto;' });
      modal.innerHTML = `<h3 style="margin-top:0">Select Attributes for Import</h3><p>Found ${nbFeatures} features. Select which attributes to map:</p>`;

      const selectors = {};
      attributeTypes.forEach(attrType => {
        const isRequired = attrType === 'number';
        const label = document.createElement('label');
        label.textContent = `${attrType.charAt(0).toUpperCase()+attrType.slice(1)} attribute${isRequired ? '' : ' (optional)'}:`;
        label.style.cssText = 'display:block;margin-top:10px;';
        modal.appendChild(label);
        const sel = document.createElement('select');
        sel.style.cssText = 'width:100%;padding:5px;margin-top:5px;';
        sel.innerHTML = '<option value="">-- Select --</option>';
        Array.from(allAttributes).sort().forEach(a => sel.innerHTML += `<option value="${a}">${a}</option>`);
        modal.appendChild(sel);
        selectors[attrType] = sel;
      });

      const btnRow = document.createElement('div');
      btnRow.style.cssText = 'display:flex;gap:10px;margin-top:20px;';
      const importBtn = Object.assign(document.createElement('button'), { textContent: 'Import', style: 'flex:1;padding:10px;background:#4CAF50;color:white;border:none;border-radius:4px;cursor:pointer;' });
      importBtn.onclick = () => {
        const sel = {}; attributeTypes.forEach(t => sel[t] = selectors[t].value);
        if (!sel.number) { WazeToastr.Alerts.warning('Import Warning', 'Number attribute is required'); return; }
        document.body.removeChild(overlay); document.body.removeChild(modal); resolve(sel);
      };
      const cancelBtn = Object.assign(document.createElement('button'), { textContent: 'Cancel', style: 'flex:1;padding:10px;background:#f44336;color:white;border:none;border-radius:4px;cursor:pointer;' });
      cancelBtn.onclick = () => { document.body.removeChild(overlay); document.body.removeChild(modal); reject('User cancelled'); };
      btnRow.append(importBtn, cancelBtn); modal.appendChild(btnRow);
      document.body.append(overlay, modal);
    });
  }

  // ─── Messages overlay ────────────────────────────────────────────────────────
  let Messages = (() => {
    const lookup = new Map();
    const container = Object.assign(document.createElement('div'), {
      style: 'position:absolute;bottom:35px;width:100%;pointer-events:none;'
    });
    return {
      init: () => wmeSDK.Map.getMapViewportElement().appendChild(container),
      add: (id, innerHTML, width) => {
        const msg = document.createElement('div');
        msg.style.cssText = `margin:5px auto;width:${width};text-align:center;background:rgba(0,0,0,0.5);color:white;border-radius:3px;padding:5px 15px;display:none;`;
        msg.innerHTML = innerHTML; container.appendChild(msg); lookup.set(id, msg);
      },
      show: (id, params) => { const m = lookup.get(id); params?.forEach((v,k) => m.querySelector(k).textContent=v); m.style.display = null; },
      hide: (id) => lookup.get(id).style.display = 'none'
    };
  })();
  Messages.add('loading', '<i class="fa fa-pulse fa-spinner"></i> Loading address points', '300px');
  Messages.add('autocomplete', '⭐ <span class="qhni-number"></span> missing house <span class="qhni-unit"></span> visible. Autofill with Ctrl+space', '500px');

  // ─── Keyboard shortcut ───────────────────────────────────────────────────────
  let Shortcut = (() => {
    const ID = "QuickHNImporterAutocomplete";
    let added = false;
    const callback = () => {
      autocompleteFeatures.forEach(feature => {
        const seg = findNearestSegment(feature, true) || findNearestSegment(feature, false);
        if (!seg) return;
        wmeSDK.Editing.setSelection({ selection: { ids: [seg.id], objectType: "segment" } });
        wmeSDK.DataModel.HouseNumbers.addHouseNumber({ number: feature.properties.number, point: feature.geometry, segmentId: seg.id });
      });
      Messages.hide('autocomplete');
      wmeSDK.Map.redrawLayer({ layerName: LAYER_NAME });
    };
    return {
      activate: () => { if (added) return; added = true; wmeSDK.Shortcuts.createShortcut({ shortcutKeys: "C+32", shortcutId: ID, description: "Autocomplete HN", callback }); },
      deactivate: () => { if (!added) return; added = false; wmeSDK.Shortcuts.deleteShortcut({ shortcutId: ID }); }
    };
  })();

  // ─── Feature repository ──────────────────────────────────────────────────────
  let Repository = (() => {
    let groups = [], directory = new Map(), sources = [];
    const toIndex = (lon, lat) => [Math.floor(lon * 100), Math.floor(lat * 200)];
    const toCoord = (x, y) => [x / 100, y / 200];

    const getData = (x, y) => {
      const cell = groups[x]?.[y];
      if (cell instanceof Array) return Promise.resolve(cell);
      if (cell instanceof Promise) return cell;
      const promise = new Promise(resolve => {
        const [left, top] = toCoord(x, y);
        Promise.all(sources.map(s => s(left, top - 0.005, left + 0.01, top))).then(groups_ => {
          if (!groups[x]) groups[x] = [];
          groups[x][y] = [];
          groups_.forEach(g => g.forEach(f => { groups[x][y].push(f); directory.set(f.id, f); }));
          resolve([].concat(...groups_));
        });
      });
      if (!groups[x]) groups[x] = [];
      if (!groups[x][y]) groups[x][y] = promise;
      return promise;
    };

    return {
      addSource: (s) => sources.push(s),
      getExtentData: async function(extent) {
        let features = [];
        const [left, bottom] = toIndex(extent[0], extent[1]);
        const [right, top] = toIndex(extent[2], extent[3]);
        let sanity = 10;
        for (let x = left; x <= right; x++) {
          for (let y = top + 1; y >= bottom; y--) {
            if (--sanity <= 0) break;
            features = features.concat(await getData(x, y));
          }
        }
        // Merge file features
        const [el, eb, er, et] = extent;
        const fileInExtent = uploadedFileFeatures.filter(f => { try { const [lon,lat]=f.geometry.coordinates; const ok=lon>=el&&lon<=er&&lat>=eb&&lat<=et; if(ok) directory.set(f.id,f); return ok; } catch(e){return false;} });
        const urlInExtent = urlFeatures.filter(f => { try { const [lon,lat]=f.geometry.coordinates; const ok=lon>=el&&lon<=er&&lat>=eb&&lat<=et; if(ok) directory.set(f.id,f); return ok; } catch(e){return false;} });
        features = features.concat(fileInExtent, urlInExtent);

        // Deduplicate
        const seen = new Set();
        return features.filter(f => { const k=f.properties.municipality+'|'+f.properties.street+'|'+f.properties.number; if(seen.has(k)) return false; seen.add(k); return true; });
      },
      cull: () => {
        groups.forEach((col, xi) => col.forEach((row, yi) => {
          if (turf.distance(toCoord(xi, yi), Object.values(wmeSDK.Map.getMapCenter())) > 1) {
            row.forEach(f => { try { wmeSDK.Map.removeFeatureFromLayer({ layerName: LAYER_NAME, featureId: f.id }); directory.delete(f.id); } catch(e){} });
            col.splice(yi, 1);
            if (!col.length) groups.splice(xi, 1);
          }
        }));
      },
      getFeatureById: (id) => directory.get(id),
      getDirectory: () => directory,
      clearAll: () => {
        groups.forEach(col => col.forEach(row => row.forEach(f => { try { wmeSDK.Map.removeFeatureFromLayer({ layerName: LAYER_NAME, featureId: f.id }); } catch(e){} })));
        groups = []; directory.clear();
      }
    };
  })();

  // ─── Sidebar UI ──────────────────────────────────────────────────────────────
  function createFileUploadUI() {
    wmeSDK.Sidebar.registerScriptTab().then(({ tabLabel, tabPane }) => {
      tabLabel.textContent = '🏠QHN4NP';
      tabLabel.title = 'Quick HN Importer for NP';

      const container = document.createElement('div');
      container.style.cssText = 'padding:auto;font-family:Arial,sans-serif;';

      const addElem = (tag, props, parent) => { const el = Object.assign(document.createElement(tag), props); parent.appendChild(el); return el; };

      addElem('div', { textContent: 'Quick HN Importer for NP', style: 'text-align:center;font-weight:bold;font-size:16px;' }, container);
      addElem('div', { innerHTML: 'Current Version ' + scriptVersion, style: 'text-align:center;font-size:0.9em;margin-bottom:15px;border-bottom:2px solid #4CAF50;padding-bottom:5px;' }, container);
      addElem('div', { textContent: 'Supported formats: GeoJSON, KML, KMZ, GML, GPX, WKT, ZIP (Shapefile)', style: 'font-size:10px;margin-bottom:15px;' }, container);

      const fileInput = addElem('input', { type: 'file', accept: '.geojson,.json,.kml,.kmz,.gml,.gpx,.wkt,.zip', style: 'display:none;' }, container);

      const uploadBtn = addElem('button', { textContent: '📁 Choose File', style: 'width:100%;padding:10px;background:#4CAF50;color:white;border:none;border-radius:4px;cursor:pointer;margin-bottom:8px;font-weight:bold;font-size:13px;' }, container);
      uploadBtn.onclick = () => fileInput.click();

      const clearBtn = addElem('button', { textContent: '🗑️ Clear Uploaded Data', style: 'width:100%;padding:10px;background:#f44336;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold;font-size:13px;margin-bottom:15px;' }, container);
      clearBtn.onclick = async () => clearUploadedData();

      const offsetBtn = addElem('button', { textContent: '↕️ Configure Offset', style: 'width:100%;padding:10px;background:#2196F3;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold;font-size:13px;margin-bottom:15px;' }, container);
      offsetBtn.onclick = () => showHNLayerOffsetDialog();

      addElem('div', { style: 'border-top:1px solid #ddd;margin:15px 0;' }, container);
      addElem('div', { textContent: 'URL Data Source:', style: 'font-size:11px;font-weight:bold;margin-bottom:8px;' }, container);

      const cbContainer = addElem('div', { style: 'display:flex;align-items:center;padding:8px;border-radius:4px;margin-bottom:5px;' }, container);
      const urlCheckbox = addElem('input', { type: 'checkbox', id: 'qhni-url-source-checkbox', style: 'margin-right:8px;cursor:pointer;' }, cbContainer);
      urlCheckbox.checked = localStorage.getItem('qhni-enable-url-source') === 'true';
      addElem('label', { htmlFor: 'qhni-url-source-checkbox', textContent: 'Load Metric House for LMC', style: 'font-size:11px;cursor:pointer;' }, cbContainer);
      addElem('div', { textContent: 'Loads house numbers from Lalitpur Metropolitan City API', style: 'font-size:10px;margin-bottom:10px;' }, container);

      const status = addElem('div', {
        id: 'qhni-upload-status',
        style: 'font-size:11px;padding:10px;border-radius:4px;min-height:20px;border-left:3px solid #ddd;'
      }, container);

      const updateStatus = () => {
        if (uploadedFileFeatures.length > 0 && urlFeatures.length > 0) { status.textContent = `✅ File: ${uploadedFileFeatures.length} | URL: ${urlFeatures.length} features`; status.style.color = '#4CAF50'; }
        else if (uploadedFileFeatures.length > 0) { status.textContent = `✅ Restored ${uploadedFileFeatures.length} features`; status.style.color = '#4CAF50'; }
        else if (urlFeatures.length > 0) { status.textContent = `✅ ${urlFeatures.length} Metric House features`; status.style.color = '#4CAF50'; }
        else { status.textContent = 'No file loaded'; status.style.color = ''; }
      };
      updateStatus();

      urlCheckbox.addEventListener('change', async () => {
        localStorage.setItem('qhni-enable-url-source', urlCheckbox.checked);
        if (urlCheckbox.checked) {
          status.textContent = '⏳ Loading Metric House data...'; status.style.color = '#ff9800';
          try {
            const features = await fetchMetricHouseData();
            urlFeatures = features;
            if (features.length > 0) {
              await storeURLFeatures();
              updateStatus();
              updateLayer();
            } else {
              urlCheckbox.checked = false;
              localStorage.setItem('qhni-enable-url-source', 'false');
              updateStatus();
            }
          } catch (e) {
            log('Error loading URL data: ' + e);
            urlCheckbox.checked = false; localStorage.setItem('qhni-enable-url-source', 'false');
            updateStatus();
          }
        } else {
          wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: LAYER_NAME });
          await clearURLFeatures();
          updateStatus(); updateLayer();
        }
      });

      fileInput.addEventListener('change', async (e) => {
        const file = e.target.files[0]; if (!file) return;
        status.textContent = '⏳ Processing...'; status.style.color = '#ff9800';
        try {
          const features = await handleFileImport(file);
          updateStatus();
          setTimeout(() => updateLayer(), 1000);
        } catch (error) {
          status.textContent = `❌ Failed: ${error.message || 'Unknown error'}`; status.style.color = '#f44336';
        }
        fileInput.value = '';
      });

      addElem('div', { style: 'border-top:1px solid #ddd;margin:15px 0;' }, container);
      addElem('div', {
        innerHTML: 'Street name normalizations applied:<br><b>Marg → Marga</b>, <b>Street → St</b>, <b>Road → Rd</b>, <b>Saraswoti → Saraswati</b><br><br><b>Note:</b> Always verify with local community before modifying street names in WME.',
        style: 'font-size:11px;'
      }, container);

      tabPane.appendChild(container);
    }).catch(e => log('Error registering sidebar: ' + e));
  }

  function showHNLayerOffsetDialog() {
    let dialog = document.getElementById('hn-offset-dialog');
    if (!dialog) {
      dialog = document.createElement('div');
      dialog.id = 'hn-offset-dialog';
      dialog.style.cssText = 'position:fixed;top:15%;left:50%;transform:translateX(-50%);z-index:9999;background:#73a9bd;padding:0;border-radius:14px;box-shadow:5px 6px 14px rgba(0,0,0,0.58);min-width:250px;';

      const header = document.createElement('div');
      header.style.cssText = 'background:#4d6a88;color:#fff;padding:8px 12px;border-radius:14px 14px 0 0;font-weight:bold;font-size:14px;display:flex;justify-content:space-between;align-items:center;';
      header.innerHTML = '<span>House Number Layer Offset</span>';
      const closeBtn = Object.assign(document.createElement('button'), { textContent: '✕', style: 'background:none;border:none;color:#eaf6ff;font-size:20px;cursor:pointer;' });
      closeBtn.onclick = () => dialog.style.display = 'none';
      header.appendChild(closeBtn); dialog.appendChild(header);

      const body = document.createElement('div');
      body.style.cssText = 'padding:12px;background:#d6e6f3;border-radius:0 0 14px 14px;';

      // Radio buttons for step size
      const radioDiv = document.createElement('div'); radioDiv.style.cssText = 'display:flex;gap:12px;margin-bottom:10px;';
      [['1', true], ['10', false]].forEach(([v, checked]) => {
        const r = Object.assign(document.createElement('input'), { type: 'radio', id: `hn-shift-${v}`, name: 'hn-shift-amt', value: v, checked });
        const l = Object.assign(document.createElement('label'), { htmlFor: `hn-shift-${v}`, textContent: `${v}m` });
        radioDiv.append(r, l);
      });
      body.appendChild(radioDiv);

      const getAmt = () => parseFloat(document.querySelector('input[name="hn-shift-amt"]:checked').value);
      const btnStyle = 'border:1px solid #8ea0b7;color:#4d6a88;border-radius:8px;cursor:pointer;font-weight:bold;font-size:16px;width:30px;height:30px;padding:0;';

      const makeBtn = (icon, title, onClick) => { const b = Object.assign(document.createElement('button'), { innerHTML: `<i class="fa ${icon}"></i>`, title, style: btnStyle }); b.onclick = onClick; return b; };

      const grid = document.createElement('div'); grid.style.cssText = 'display:grid;grid-template-columns:30px 30px 30px;grid-template-rows:30px 30px 30px;gap:4px;margin:10px auto;width:fit-content;';
      grid.appendChild(document.createElement('div'));
      grid.appendChild(makeBtn('fa-angle-up', 'North', () => { hnLayerOffset.y += getAmt(); updateOffsetDisplay(); refreshHNLayer(); WazeToastr.Alerts.info(scriptName, `Shifted ${getAmt()}m North`, false, false, 2000); }));
      grid.appendChild(document.createElement('div'));
      grid.appendChild(makeBtn('fa-angle-left', 'West', () => { hnLayerOffset.x -= getAmt(); updateOffsetDisplay(); refreshHNLayer(); WazeToastr.Alerts.info(scriptName, `Shifted ${getAmt()}m West`, false, false, 2000); }));
      grid.appendChild(document.createElement('div'));
      grid.appendChild(makeBtn('fa-angle-right', 'East', () => { hnLayerOffset.x += getAmt(); updateOffsetDisplay(); refreshHNLayer(); WazeToastr.Alerts.info(scriptName, `Shifted ${getAmt()}m East`, false, false, 2000); }));
      grid.appendChild(document.createElement('div'));
      grid.appendChild(makeBtn('fa-angle-down', 'South', () => { hnLayerOffset.y -= getAmt(); updateOffsetDisplay(); refreshHNLayer(); WazeToastr.Alerts.info(scriptName, `Shifted ${getAmt()}m South`, false, false, 2000); }));
      grid.appendChild(document.createElement('div'));
      body.appendChild(grid);

      const display = Object.assign(document.createElement('div'), { id: 'hn-offset-display', style: 'font-size:12px;color:#4d6a88;background:#fff;border-radius:6px;margin:10px 0;padding:8px;text-align:center;font-weight:bold;' });
      body.appendChild(display);

      const resetBtn = Object.assign(document.createElement('button'), { textContent: 'Reset Offset', style: 'width:100%;padding:8px;background:#f44336;color:white;border:none;border-radius:5px;cursor:pointer;font-weight:bold;' });
      resetBtn.onclick = () => { hnLayerOffset = { x: 0, y: 0 }; updateOffsetDisplay(); refreshHNLayer(); WazeToastr.Alerts.info(scriptName, 'Offset reset to 0m', false, false, 2000); };
      body.appendChild(resetBtn);

      dialog.appendChild(body);
      document.body.appendChild(dialog);
    }
    dialog.style.display = 'block';
    updateOffsetDisplay();
  }

  function updateOffsetDisplay() {
    const el = document.getElementById('hn-offset-display');
    if (el) el.textContent = `Current offset: X = ${hnLayerOffset.x.toFixed(0)} m, Y = ${hnLayerOffset.y.toFixed(0)} m`;
  }

  function refreshHNLayer() { updateLayer(); }

  async function clearUploadedData() {
    uploadedFileFeatures = [];
    try { await clearUploadedFeatures(); } catch (e) { log('Error clearing DB: ' + e); }
    const status = document.getElementById('qhni-upload-status');
    if (status) {
      if (urlFeatures.length > 0) { status.textContent = `✅ ${urlFeatures.length} Metric House features`; status.style.color = '#4CAF50'; }
      else { status.textContent = 'No file loaded'; status.style.color = ''; }
    }
    updateLayer();
    WazeToastr.Alerts.info('Cleared', 'Uploaded file data cleared');
  }

  // ─── Initialization ──────────────────────────────────────────────────────────
  function init() {
    cleanup.all();
    setupProjectionsAndTransforms();
    Messages.init();
    createFileUploadUI();
    previousCenterLocation = Object.values(wmeSDK.Map.getMapCenter());

    // SVG title fix for house number polygons
    const svgRoot = document.querySelector("#WazeMap svg[id*='RootContainer']");
    if (svgRoot) {
      const obs = new MutationObserver(muts => muts.forEach(m => m.addedNodes.forEach(el => {
        if (el.nodeName === "svg" && el.getAttribute("title") && !el.querySelector("title")) {
          const t = document.createElementNS("http://www.w3.org/2000/svg", "title");
          t.textContent = el.getAttribute("title"); el.appendChild(t);
        }
      })));
      obs.observe(svgRoot, { childList: true, subtree: true });
      cleanup.addObserver(obs);
    }

    // Register the overlay layer with color-coded style context
    wmeSDK.Map.addLayer({
      layerName: LAYER_NAME,
      styleContext: {
        fillColor: ({ feature }) => {
          if (!feature.properties?.street) return '#fb9c4f';
          if (!streetNames.has(feature.properties.street.toLowerCase())) return '#bb3333';
          if (selectedStreetNames.includes(feature.properties.street.toLowerCase())) return '#99ee99';
          return '#fb9c4f';
        },
        radius: ({ feature }) => feature.properties?.number ? Math.max(8 + feature.properties.number.length * 2, 10) : 10,
        opacity: ({ feature }) => isHouseNumberAlreadyAdded(feature) ? 0.3 : 1,
        cursor: ({ feature }) => isHouseNumberAlreadyAdded(feature) ? '' : 'pointer',
        title: ({ feature }) => {
          if (!feature.properties?.number) return '';
          let t = feature.properties.street ? feature.properties.street + ' - ' : '';
          t += feature.properties.number;
          const nepali = selectedNepaliAttribute ? feature.properties[selectedNepaliAttribute] : feature.properties.rd_nanep;
          if (nepali) t += '\n' + (typeof preeti === 'function' ? preeti(nepali) : nepali);
          if (feature.properties.streetOriginal) t += '\n' + feature.properties.streetOriginal;
          return t;
        },
        number: ({ feature }) => feature.properties?.number || ''
      },
      styleRules: [{
        style: {
          fillColor: '${fillColor}', fillOpacity: '${opacity}', fontColor: '#111111', fontOpacity: '${opacity}',
          fontWeight: 'bold', fontSize: '12px', strokeColor: '#ffffff', strokeOpacity: '${opacity}',
          strokeWidth: 2, pointRadius: '${radius}', graphicName: 'circle', label: '${number}',
          cursor: '${cursor}', title: '${title}'
        }
      }]
    });

    wmeSDK.Map.setLayerVisibility({ layerName: LAYER_NAME, visibility: false });
    wmeSDK.Events.trackLayerEvents({ layerName: LAYER_NAME });
    wmeSDK.Events.trackLayerEvents({ layerName: "house_numbers" });

    cleanup.addEvent(wmeSDK.Events.on({ eventName: "wme-layer-visibility-changed", eventHandler: updateLayer }));
    cleanup.addEvent(wmeSDK.Events.on({ eventName: "wme-map-move-end", eventHandler: () => {
      updateLayer();
      const cur = Object.values(wmeSDK.Map.getMapCenter());
      if (turf.distance(cur, previousCenterLocation) > 1) { previousCenterLocation = cur; Repository.cull(); }
    }}));

    cleanup.addEvent(wmeSDK.Events.on({ eventName: "wme-layer-feature-clicked", eventHandler: (clickEvent) => {
      const feature = Repository.getFeatureById(clickEvent.featureId);
      if (!feature || isHouseNumberAlreadyAdded(feature)) return;

      const addHN = (seg) => {
        wmeSDK.Editing.setSelection({ selection: { ids: [seg.id], objectType: "segment" } });
        wmeSDK.DataModel.HouseNumbers.addHouseNumber({ number: feature.properties.number, point: feature.geometry, segmentId: seg.id });
        if (feature.properties.street) {
          const norm = normalizeNepalStreetName(feature.properties.street).toLowerCase();
          if (!streetNumbers.has(norm)) streetNumbers.set(norm, new Set());
          streetNumbers.get(norm).add(simplifyNumber(feature.properties.number));
        }
        wmeSDK.Map.redrawLayer({ layerName: LAYER_NAME });
      };

      let seg = findNearestSegment(feature, true);
      if (!seg) {
        seg = findNearestSegment(feature, false);
        if (!seg) { WazeToastr.Alerts.error('No Segment Found', 'No nearby segments found'); return; }
        const segStreet = wmeSDK.DataModel.Streets.getById({ streetId: seg.primaryStreetId })?.name;
        if (!segStreet?.trim()) {
          WazeToastr.Alerts.error('No Street Name', 'Nearest segment has no street name assigned');
          wmeSDK.Editing.setSelection({ selection: { ids: [seg.id], objectType: "segment" } }); return;
        }
        if (!feature.properties.street?.trim()) { addHN(seg); return; }
        if (isCachedStreetPair(feature.properties.street, segStreet)) { addHN(seg); return; }
        WazeToastr.Alerts.prompt(scriptName,
          `Street "${feature.properties.street}" not found. Add to "${segStreet}"?\nMinutes to remember (0=don't):`,
          '0',
          (input) => {
            const dur = Number(input);
            if (isNaN(dur) || dur < 0) { WazeToastr.Alerts.warning(scriptName, 'Invalid input'); return; }
            if (dur > 0) addToCacheStreetPair(feature.properties.street, segStreet, dur);
            addHN(seg);
          }, () => {}, 'text');
        return;
      }
      addHN(seg);
    }}));

    cleanup.addEvent(wmeSDK.Events.on({ eventName: "wme-selection-changed", eventHandler: () => {
      const sel = wmeSDK.Editing.getSelection();
      if (!sel || sel.objectType !== 'segment' || !sel.ids.length) { selectedStreetNames = []; }
      else {
        const streetIds = sel.ids.flatMap(id => { const s = wmeSDK.DataModel.Segments.getById({ segmentId: id }); return s ? [s.primaryStreetId, ...s.alternateStreetIds] : []; });
        selectedStreetNames = streetIds.filter(Boolean).map(id => wmeSDK.DataModel.Streets.getById({ streetId: id })?.name?.toLowerCase()).filter(Boolean);
      }
      updateLayer();
    }}));

    wmeSDK.Events.trackDataModelEvents({ dataModelName: "segmentHouseNumbers" });
    wmeSDK.Events.trackDataModelEvents({ dataModelName: "streets" });

    cleanup.addEvent(wmeSDK.Events.on({ eventName: "wme-data-model-objects-added", eventHandler: (ev) => {
      if (ev.dataModelName === "segmentHouseNumbers") {
        ev.objectIds.forEach(id => {
          if (Number.isInteger(id)) return;
          const segId = id.substring(0, id.indexOf("/"));
          const hn = id.substring(segId.length + 1);
          const seg = wmeSDK.DataModel.Segments.getById({ segmentId: Number(segId) });
          if (!seg) return;
          [seg.primaryStreetId, ...seg.alternateStreetIds].map(sid => wmeSDK.DataModel.Streets.getById({ streetId: sid })?.name).filter(Boolean).forEach(name => {
            const norm = normalizeNepalStreetName(name).toLowerCase();
            if (!streetNumbers.has(norm)) streetNumbers.set(norm, new Set());
            streetNumbers.get(norm).add(simplifyNumber(hn));
          });
        });
      } else if (ev.dataModelName === "streets") {
        ev.objectIds.map(id => wmeSDK.DataModel.Streets.getById({ streetId: id })).filter(Boolean).forEach(s => streetNames.add(s.name.toLowerCase()));
      }
      wmeSDK.Map.redrawLayer({ layerName: LAYER_NAME });
    }}));

    cleanup.addEvent(wmeSDK.Events.on({ eventName: "wme-data-model-objects-removed", eventHandler: (ev) => {
      if (ev.dataModelName === "segmentHouseNumbers") {
        ev.objectIds.forEach(id => {
          if (Number.isInteger(id)) return;
          const segId = id.substring(0, id.indexOf("/"));
          const hn = simplifyNumber(id.substring(segId.length + 1));
          const seg = wmeSDK.DataModel.Segments.getById({ segmentId: Number(segId) });
          if (!seg) return;
          [seg.primaryStreetId, ...seg.alternateStreetIds].map(sid => wmeSDK.DataModel.Streets.getById({ streetId: sid })?.name).filter(Boolean).forEach(name => {
            const norm = normalizeNepalStreetName(name).toLowerCase();
            streetNumbers.get(norm)?.delete(hn);
            if (!streetNumbers.get(norm)?.size) streetNumbers.delete(norm);
          });
        });
      } else if (ev.dataModelName === "streets") {
        ev.objectIds.map(id => wmeSDK.DataModel.Streets.getById({ streetId: id })).filter(Boolean).forEach(s => streetNames.delete(s.name.toLowerCase()));
      }
    }}));

    function rebuildStreetNumbers() {
      const W = (unsafeWindow || window).W;
      if (!W?.model?.segmentHouseNumbers) return;
      streetNumbers.clear();
      W.model.segmentHouseNumbers.getObjectArray().forEach(hn => {
        const number = hn.getAttribute('number'); if (!number) return;
        const segmentId = hn.getSegmentId?.(); if (!segmentId) return;
        const segment = W.model.segments.getObjectById(segmentId); if (!segment) return;
        [segment.getAttribute('primaryStreetID'), ...(segment.getAttribute('streetIDs') || [])].filter(Boolean).forEach(sid => {
          const name = normalizeNepalStreetName(W.model.streets.getObjectById(sid)?.getAttribute('name') || '').toLowerCase();
          if (!name) return;
          if (!streetNumbers.has(name)) streetNumbers.set(name, new Set());
          streetNumbers.get(name).add(simplifyNumber(number));
        });
      });
    }

    function refreshLayerFeatures() {
      const ext = wmeSDK.Map.getMapExtent();
      const visible = Array.from(Repository.getDirectory().values()).filter(f => { const [lon,lat]=f.geometry.coordinates; return lon>=ext[0]&&lon<=ext[2]&&lat>=ext[1]&&lat<=ext[3]; });
      wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: LAYER_NAME });
      if (visible.length) wmeSDK.Map.addFeaturesToLayer({ layerName: LAYER_NAME, features: visible });
    }

    cleanup.addEvent(wmeSDK.Events.on({ eventName: "wme-after-undo", eventHandler: () => { rebuildStreetNumbers(); refreshLayerFeatures(); } }));
    cleanup.addEvent(wmeSDK.Events.on({ eventName: "wme-after-redo-clear", eventHandler: () => { rebuildStreetNumbers(); refreshLayerFeatures(); } }));
    cleanup.addEvent(wmeSDK.Events.on({ eventName: "wme-data-model-objects-saved", eventHandler: (ev) => {
      if (ev.dataModelName === "segmentHouseNumbers") { rebuildStreetNumbers(); refreshLayerFeatures(); }
    }}));

    updateLayer();
  }

  // ─── Layer update ────────────────────────────────────────────────────────────
  function updateLayer() {
    const visible = wmeSDK.Map.isLayerVisible({ layerName: "house_numbers" });
    const zoom = wmeSDK.Map.getZoomLevel();
    const layerVisible = wmeSDK.Map.isLayerVisible({ layerName: LAYER_NAME });

    if (!visible || zoom < 19) { wmeSDK.Map.setLayerVisibility({ layerName: LAYER_NAME, visibility: false }); return; }
    if (!layerVisible) wmeSDK.Map.setLayerVisibility({ layerName: LAYER_NAME, visibility: true });

    Messages.show('loading');
    const extent = wmeSDK.Map.getMapExtent();
    let fetchExtent = extent;

    if (hnLayerOffset.x || hnLayerOffset.y) {
      const d = 111320;
      fetchExtent = [extent[0]-Math.abs(hnLayerOffset.x)/d, extent[1]-Math.abs(hnLayerOffset.y)/d, extent[2]+Math.abs(hnLayerOffset.x)/d, extent[3]+Math.abs(hnLayerOffset.y)/d];
    }

    Repository.getExtentData(fetchExtent).then(features => {
      wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: LAYER_NAME });
      const offsetFeatures = applyHNLayerOffset(features);
      const dir = Repository.getDirectory();
      offsetFeatures.forEach(f => dir.set(f.id, f));
      const [el,eb,er,et] = extent;
      const visible_ = offsetFeatures.filter(f => { const [lon,lat]=f.geometry.coordinates; return lon>=el&&lon<=er&&lat>=eb&&lat<=et; });
      if (visible_.length) wmeSDK.Map.addFeaturesToLayer({ layerName: LAYER_NAME, features: visible_ });
      Messages.hide('loading'); Messages.hide('autocomplete');
      if (selectedStreetNames.length > 0) {
        autocompleteFeatures = visible_.filter(f => f.properties.street && selectedStreetNames.includes(f.properties.street.toLowerCase()) && !isHouseNumberAlreadyAdded(f) && turf.booleanContains(turf.bboxPolygon(extent), f));
        if (autocompleteFeatures.length) {
          Messages.show('autocomplete', new Map([['.qhni-number', autocompleteFeatures.length], ['.qhni-unit', autocompleteFeatures.length > 1 ? 'numbers' : 'number']]));
          Shortcut.activate();
        } else { Shortcut.deactivate(); }
      } else { autocompleteFeatures = []; Shortcut.deactivate(); }
    }).catch(e => { log('getExtentData error: ' + e); Messages.hide('loading'); });
  }

  // ─── Segment matching ────────────────────────────────────────────────────────
  function findNearestSegment(feature, matchName) {
    let streetIds = [];
    if (feature.properties.street) {
      const norm = normalizeNepalStreetName(feature.properties.street).toLowerCase();
      streetIds = wmeSDK.DataModel.Streets.getAll().filter(s => normalizeNepalStreetName(s.name).toLowerCase() === norm).map(s => s.id);
    }
    if (!matchName || streetIds.length > 0) {
      const seg = wmeSDK.DataModel.Segments.getAll()
        .filter(s => !matchName || streetIds.includes(s.primaryStreetId) || s.alternateStreetIds?.some(id => streetIds.includes(id)))
        .reduce((best, s) => { s.distance = turf.pointToLineDistance(feature.geometry, s.geometry); return s.distance < best.distance ? s : best; }, { distance: Infinity });
      return seg.distance === Infinity ? null : seg;
    }
    return null;
  }

  function isHouseNumberAlreadyAdded(feature) {
    if (!feature?.properties?.number) return false;
    const num = simplifyNumber(feature.properties.number);
    if (feature.properties.street?.trim()) {
      const norm = normalizeNepalStreetName(feature.properties.street).toLowerCase();
      return streetNumbers.has(norm) && streetNumbers.get(norm).has(num);
    }
    for (const nums of streetNumbers.values()) { if (nums.has(num)) return true; }
    return false;
  }

  // ─── Utilities ───────────────────────────────────────────────────────────────
  function simplifyNumber(number) { return number.replace(/[\/\-]/, "_").toLowerCase(); }

  function cleanupName(name) {
    const replacements = [
      ['\u2013','\u002D'],['\u2014','\u002D'],['\u2018','\u0027'],['\u2019','\u0027'],
      ['\u201C','\u0022'],['\u201D','\u0022'],['\uFF0D','\u002D'],['\uFF07','\u0027'],['\uFF02','\u0022'],
    ];
    return replacements.reduce((s,[f,r]) => s.replaceAll(f,r), name.normalize());
  }

  function normalizeNepalStreetName(name) {
    return cleanupName(name)
      .replace(/\s+/g, ' ').trim()
      .replace(/\bMarg\b/g, 'Marga')
      .replace(/\bRoad\b/gi, 'Rd')
      .replace(/\bSaraswoti\b/gi, 'Saraswati')
      .replace(/\bStreet\b/gi, 'St');
  }

})();
```
