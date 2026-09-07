---
name: wme-sdk
description: Use this skill for ANY Waze Map Editor (WME) script work — migrating legacy W object, OpenLayers, or deprecated WazeWrap functions to the WME SDK, querying venues/nodes/junctions/segments, building map layers with advanced styling predicates and dynamic getters, managing keyboard shortcuts with conflict detection, handling data models and country context, or implementing features with Turf.js. Covers error handling, high-performance feature loading (dangerouslyAddFeaturesToLayerWithoutValidation), mutable style state optimization for 1000+ features, zoom-aware predicates, viewport queries (getMapExtent, getMapCenter), event listeners (map-move-end, layer-checkbox-toggled), sidebar tab customization, and IndexedDB persistence. Provides before/after migration examples, SDK method references, real-world patterns from production scripts, working Tampermonkey examples, and best practices. Trigger on WME scripts, SDK migration, venues/nodes/junctions APIs, map styling, layer management, performance optimization, shortcuts, country detection, viewport filtering, detecting deprecated WazeWrap calls, or "how do I" questions about WME script development.
compatibility: Requires access to local WME SDK documentation and Tampermonkey userscript context
---

# WME SDK Development & Migration

You're working with Waze Map Editor (WME) scripts in a Tampermonkey context. This skill provides structured guidance for **migrating legacy code to the WME SDK** and **building new features using modern SDK patterns**.

## ⚙️ Configuration: Local Documentation Path

**If you have cloned the WME-SDK-Mirror repository**, set your local path below for faster offline access:

```
/path/to/your/WME-SDK-Mirror/beta/latest/output/docs
/path/to/your/WME-SDK-Mirror/production/latest/output/docs
```

To customize for your local setup, replace the path above with your own clone location. Examples:

**For Beta version**
- Mac: `/Users/username/projects/WME-SDK-Mirror/beta/latest/output/docs`
- Windows: `/path/to/your/WME-SDK-Mirror/beta/latest/output/docs`

**For Production version**
- Mac: `/Users/username/projects/WME-SDK-Mirror/production/latest/output/docs`
- Windows: `/path/to/your/WME-SDK-Mirror/production/latest/output/docs`

If not set, the skill will reference GitHub Pages (beta): `https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/` & GitHub Pages (production): `https://kid4rm90s.github.io/WME-SDK-Mirror/production/latest/output/docs/`

---

## Your Context

- **Role**: Front-end developer building/maintaining WME userscripts
- **SDK Documentation**: 
  - Local (if configured above): Check your configured path
  - GitHub Pages(beta): `https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/`
  - GitHub Pages(production): `https://kid4rm90s.github.io/WME-SDK-Mirror/production/latest/output/docs/`
  - Repo: [WME-SDK-Mirror](https://github.com/kid4rm90s/WME-SDK-Mirror)
- **Legacy Patterns to Replace**: `W` namespace (global Waze object), OpenLayers APIs
- **Modern Stack**: WME SDK + Turf.js for geometry, proper initialization/auth

## Workflow: Identify Your Task

### Task Type 1: Migration
**User provides**: Existing code using `W` object, OpenLayers, or legacy patterns  
**You produce**:
1. **Migration Summary** — High-level overview of areas being changed
2. **Before/After Examples** — Each legacy pattern with explanation and SDK replacement
3. **SDK Initialization** — How to set up and authenticate the SDK for this script
4. **Migration Checklist** — Key areas to test after migration

### Task Type 2: New Feature Design
**User provides**: Feature requirement or desired functionality  
**You produce**:
1. **Feature Design** — How to implement using WME SDK + Turf.js
2. **Code Example** — Correct initialization, classes, methods, and patterns
3. **SDK Integration Steps** — Ready-state handling, event subscription, etc.
4. **Best Practices** — Patterns to follow for Tampermonkey context

## How to Work

### Step 1: Consult the Documentation

Always start by reading the **index.md** file from the SDK docs folder, then load relevant sections based on the task:

| File | When to load |
|------|--------------|
| `classes.md` | Working with SDK classes, properties, methods |
| `interfaces.md` | Looking up interface shapes and data types |
| `types.md` | Type definitions and enums |
| `functions.md` | Available SDK functions and utilities |
| `variables.md` | SDK variables and constants |
| `modules.md` | SDK modules and their exports |
| `how-to-get-started-with-the-wmeSDK.md` | SDK initialization patterns |
| `migration-guide.md` | Legacy W-object → SDK migration patterns |
| `script-example-1.md` through `script-example-6.md` | Real-world working examples |
| `Turf-Docs.md` | Geometry operations (replacing OpenLayers) |
| `wmeSDK_typedefs.d.md` | Full TypeScript definitions if needed |
| `geojson_typeddefs.d.md` | GeoJSON TypeScript typings |
| `changelog.md` | Changelog |

### Step 2: Analyze the Code or Requirement

**If migrating:**
- Scan for `W.map`, `W.model`, `OpenLayers.Geometry`, `L.` patterns
- Group changes by area (map model, geometry, events, etc.)
- Note dependencies and side effects

**If building new:**
- Understand what data/events the feature needs
- Check SDK classes/functions that provide that capability
- Plan initialization and error handling

### Step 3: Produce Guidance

For **migrations**, show each pattern as:
```
## Pattern: [Name of legacy pattern]
**Before (Legacy):**
[Code using W or OpenLayers]

**After (WME SDK + Turf.js):**
[Modern equivalent]

**Why:** [Explanation of the change and why it's better]
**Reference:** [Specific SDK doc file/section]
```

For **new features**, structure as:
```
## Feature: [Feature name]
**Design Overview:**
[What the feature does and how it uses the SDK]

**Code Example:**
[Working Tampermonkey userscript example with proper initialization]

**SDK Methods/Classes Used:**
- `ClassName.method()` — [what it does]

**Integration Steps:**
1. Initialize the SDK
2. Set up event listeners
3. [Any other key steps]
```

### Step 4: Include Essential Context

Always provide:

- **SDK Initialization Code** — Show how to properly set up the SDK in a Tampermonkey script, including auth and ready-state handling
- **Error Handling** — How to handle SDK not being available or initialization failures
- **Testing Guidance** — What to verify after migration/implementation (e.g., "Check console for initialization messages", "Verify data is fetching correctly")
- **Reference Links** — Point to specific documentation files so the user can dive deeper

## Key Principles

1. **Tampermonkey Context Matters** — Account for sandboxing, `unsafeWindow`, and userscript lifecycle
2. **Turf.js Replaces OpenLayers** — Use Turf for geometry; link to `Turf-Docs.md` for examples
3. **SDK is the Authority** — When in doubt about what's possible, check the docs; don't guess from memory
4. **Real Examples Matter** — Reference `script-example-*.md` files to show users working patterns
5. **Migration is Staged** — Don't try to rewrite everything at once; migrate by feature area and test incrementally

## Common Migration Patterns

As you work, you'll encounter recurring legacy patterns. Refer to `migration-guide.md` for the canonical transformations, but here are the categories:

- **Map Model Access** — `W.map` / `W.model` → SDK model objects
- **Geometry Operations** — OpenLayers Geometry → Turf.js
- **Event Handling** — `W.map.on()` / `W.selectionManager.on()` → SDK event subscriptions
- **Drawing/Rendering** — OpenLayers layers → SDK rendering APIs
- **User/Session Data** — `W.currentUser` → SDK user context

## Output Structure (Use This Template)

```
# [Feature/Migration Name] with WME SDK

## Summary
[1-2 sentence overview]

## Migration/Feature Breakdown
### [Area 1: Pattern/Feature Name]
[Before/After or Design section]

### [Area 2: Pattern/Feature Name]
[Before/After or Design section]

## SDK Initialization
[Code block showing proper setup]

## Testing Checklist
- [ ] Item 1
- [ ] Item 2

## Reference Documentation
- [File name](path) — [Brief note on what's in this file]
```

---

## Advanced Patterns (From Real-World Scripts)

### Settings Persistence
Scripts often store user preferences in localStorage:

```javascript
const SETTINGS_KEY = '_wme_myscript_settings';
function loadSettings() {
  const saved = localStorage.getItem(SETTINGS_KEY);
  return saved ? JSON.parse(saved) : { layerColor: '#FF0000', enabled: true };
}
function saveSettings(settings) {
  localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings));
}
```

**When to use:** Storing user layer colors, zoom thresholds, enabled/disabled state.

### Sidebar Tab Registration
Register a custom UI panel in WME's sidebar:

```javascript
wmeSDK.Sidebar.registerScriptTab({
  tabName: "My Script",
  tabLabel: "My Script",
  htmlString: `<div id="my-script-tab"><button>Do something</button></div>`,
  onOpen: () => console.log("Tab opened"),
  onClose: () => console.log("Tab closed"),
}).then((tab) => {
  // tab.tabPane and tab.tabLabel are now in the DOM
  document.getElementById("my-script-tab").addEventListener("click", () => {
    console.log("Button clicked");
  });
});
```

**When to use:** Creating settings UIs, showing script status, or interactive controls.

### Advanced Layer Styling
Use predicates and style context for dynamic styling:

```javascript
wmeSDK.Map.addLayer({
  layerName: "smart_layer",
  styleRules: [
    {
      predicate: (props, zoomLevel) => props.isHighlighted && zoomLevel > 12,
      style: { strokeColor: "#FF0000", strokeWidth: 5 }
    },
    {
      style: { strokeColor: "#0000FF", strokeWidth: 2 } // Default
    }
  ],
  styleContext: {
    getStrokeColor: ({ feature, zoomLevel }) => 
      zoomLevel > 15 ? "#00FF00" : feature?.properties.color ?? "#000000",
  }
});
```

**When to use:** Highlighting features based on zoom level, user selection, or complex conditions.

### External Data API Integration
Scripts often fetch GIS data from ArcGIS, Census, or other APIs:

```javascript
// In userscript header, declare permissions:
// @grant        GM_xmlhttpRequest
// @connect      arcgis.com
// @connect      census.gov

// In code:
GM_xmlhttpRequest({
  method: 'GET',
  url: 'https://services.arcgis.com/...',
  onload: (response) => {
    const data = JSON.parse(response.responseText);
    // Convert ArcGIS geometry to GeoJSON
    const features = data.features.map(f => ({
      type: "Feature",
      geometry: arcgisToGeoJSON(f.geometry),
      properties: f.attributes
    }));
  }
});
```

**When to use:** Displaying boundaries, external datasets, or real-time data overlays.

### Performance Optimization
For scripts handling hundreds of features, optimize:

```javascript
// 1. Debounce map movement (prevents API spam)
let mapMoveTimer;
wmeSDK.Events.on({
  eventName: "wme-map-move-end",
  eventHandler: () => {
    clearTimeout(mapMoveTimer);
    mapMoveTimer = setTimeout(fetchData, 250);
  }
});

// 2. Cache expensive calculations
const polygonCache = new Map();
function getCachedArea(feature) {
  if (!polygonCache.has(feature.id)) {
    polygonCache.set(feature.id, turf.area(feature.geometry));
  }
  return polygonCache.get(feature.id);
}

// 3. Batch feature additions (single map operation, not per-feature)
const features = [];
// ... collect features ...
features.forEach(f => wmeSDK.Map.addFeatureToLayer({ layerName, feature: f }));
```

**When to use:** Scripts with 50+ features, frequent updates, or complex geometry.

### Complex Geometry Handling
GeoJSON rings follow the right-hand rule (exterior CCW, holes CW):

```javascript
// Ring orientation (exterior boundary = counter-clockwise)
const polygon = {
  type: "Polygon",
  coordinates: [
    // Outer boundary (counter-clockwise)
    [[-118.5, 34.5], [-118.5, 34.8], [-118.1, 34.8], [-118.1, 34.5], [-118.5, 34.5]],
    // Hole (clockwise - represents "cut out" area)
    [[-118.3, 34.6], [-118.2, 34.6], [-118.2, 34.7], [-118.3, 34.7], [-118.3, 34.6]]
  ]
};

// Polygon clipping to screen boundary (useful for large boundaries)
const screenPoly = turf.polygon([screenBounds.coordinates]);
const clipped = turf.intersect(largePolygon, screenPoly);
```

**When to use:** Rendering multi-part boundaries (Michigan, Hawaii), handling holes, or clipping large geometries.

### Venues Data API
Query place/venue data with filtering and categorization:

```javascript
// Get all venues currently visible on map
const allVenues = wmeSDK.DataModel.Venues.getAll();

// Get venue by ID
const venue = wmeSDK.DataModel.Venues.getById({ venueId: "12345" });
console.log(venue.name, venue.geometry, venue.categories);

// Get venue address (house number, street name, etc.)
const address = wmeSDK.DataModel.Venues.getAddress({ venueId: venue.id });
console.log(`${address?.houseNumber ?? ''} ${address?.street?.name ?? ''}`);

// Get all venue category types
const mainCats = wmeSDK.DataModel.Venues.getVenueMainCategories();
const subCats = wmeSDK.DataModel.Venues.getVenueSubCategories();
// Use for building category filters or displaying localized names
const catName = subCats.find(s => s.subCategoryId === 'CAT_ID')?.localizedName;
```

**Use for:** Scripts that query place data, build place catalogs, filter by category, or work with venue geometry.

**Reference:** `classes.md` → `DataModel.Venues` methods

---

### Nodes & Junctions API
Access map junction and node geometry for angle calculations:

```javascript
// Get node by ID (nodes are map vertices)
const node = wmeSDK.DataModel.Nodes.getById({ nodeId: 5678 });
console.log(node.geometry); // GeoJSON Point

// Get junction (roundabout or big junction)
const junction = wmeSDK.DataModel.Junctions.getById({ junctionId: "junction_123" });
console.log(junction.geometry, junction.segmentIds);

// Common use: calculate angle between three points
const fromNode = wmeSDK.DataModel.Nodes.getById({ nodeId: segment.fromNodeId });
const toNode = wmeSDK.DataModel.Nodes.getById({ nodeId: segment.toNodeId });

const angle = turf.bearing(
  turf.point(fromNode.geometry.coordinates),
  turf.point(toNode.geometry.coordinates)
);
```

**Use for:** Junction angle calculations, roundabout analysis, routing logic verification.

**Reference:** `classes.md` → `DataModel.Nodes`, `DataModel.Junctions` methods

---

### Shortcuts Full Lifecycle
Create, manage, and delete custom keyboard shortcuts:

```javascript
// Register a new keyboard shortcut
wmeSDK.Shortcuts.createShortcut({
  shortcutId: 'myScript_actionX',           // Unique ID
  description: 'My Script: Do Action X',    // User-visible name
  shortcutKeys: 'shift+a',                  // Combo format: "A+R", "shift+a", null for none
  callback: () => {
    console.log('Shortcut activated!');
    doSomething();
  }
});

// Check if shortcut is already registered
if (wmeSDK.Shortcuts.isShortcutRegistered({ shortcutId: 'myScript_actionX' })) {
  console.log('Already registered');
}

// Get all shortcuts (including any the user has already registered)
const allShortcuts = wmeSDK.Shortcuts.getAllShortcuts();
const myShortcut = allShortcuts.find(s => s.shortcutId === 'myScript_actionX');
console.log(myShortcut.shortcutKeys); // Current key combo

// Delete a shortcut
wmeSDK.Shortcuts.deleteShortcut({ shortcutId: 'myScript_actionX' });
```

**Important Gotcha:** The SDK returns shortcuts in **inconsistent formats**:
- On initial load: combo format (`"A+R"`)
- After user edits: raw format (`"4,82"`)
- After reload: combo format again

**Normalize before saving:**
```javascript
function normalizeShortcut(sdkKey) {
  if (!sdkKey) return { raw: null, combo: null };
  if (typeof sdkKey === 'string') {
    if (sdkKey.includes('+')) return { combo: sdkKey, raw: null };  // combo format
    if (sdkKey.includes(',')) return { raw: sdkKey, combo: null };  // raw format
  }
  return { raw: null, combo: null };
}

// Always save the normalized combo version
wmeSDK.Shortcuts.createShortcut({
  shortcutId: 'myScript_action',
  description: 'My Action',
  shortcutKeys: normalizeShortcut(storedKey).combo,
  callback: myCallback
});
```

**Use for:** Power-user features, quick toggles, customizable actions in your script.

**Reference:** `classes.md` → `Shortcuts` class (createShortcut, deleteShortcut, getAllShortcuts, isShortcutRegistered)

---

### Clearing & Managing Layers
Clear features from layers for re-rendering or cleanup:

```javascript
// Remove all features from a specific layer
wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: 'my_layer' });

// Common pattern: re-render by clearing and adding new features
function updateLayerData(newFeatures) {
  wmeSDK.Map.removeAllFeaturesFromLayer({ layerName: 'my_layer' });
  
  newFeatures.forEach(feature => {
    wmeSDK.Map.addFeatureToLayer({
      layerName: 'my_layer',
      feature: feature
    });
  });
}

// Or batch add multiple features
newFeatures.forEach(f => {
  wmeSDK.Map.addFeatureToLayer({ layerName: 'my_layer', feature: f });
});
```

**Use for:** Refreshing data displays, cleaning up temporary overlays, avoiding duplicate features.

**Reference:** `classes.md` → `Map.removeAllFeaturesFromLayer()`

---

### Error Handling with SDK Exception Types
Handle SDK errors gracefully using typed exception checks:

```javascript
try {
  wmeSDK.Map.removeLayer({ layerName: 'my_layer' });
} catch (e) {
  if (!(e instanceof wmeSDK.Errors.InvalidStateError)) {
    throw e;  // Re-throw if it's a different error
  }
  // Layer doesn't exist — this is expected and safe to ignore
}
```

**Why:** Layers may or may not exist when you try to remove them. This pattern safely handles the case without crashing or polluting logs.

**Use for:** Scripts that toggle layers, reload/refresh layers, or clean up after edits.

**Reference:** `classes.md` → `Errors` class

---

### High-Performance Feature Addition (Dangerous Path)
For scripts loading 100s or 1000s of features, bypass SDK validation:

```javascript
const features = [...many features from GeoJSON...]; // e.g., 50,000+

const startTime = performance.now();
wmeSDK.Map.dangerouslyAddFeaturesToLayerWithoutValidation({
  features,
  layerName: 'gis_import_layer'
});
console.log(`Loaded ${features.length} features in ${(performance.now() - startTime).toFixed(0)}ms`);
```

**Why:** SDK validation is the bottleneck when adding thousands of features. The `dangerously*` variant skips validation checks, trading safety for speed. Features are assumed to be valid GeoJSON.

**Use for:** GIS imports, large geometry imports (SHP, KML, GeoJSON), bulk feature operations.

**Assumption:** Your features are already validated before passing them (or validation happens elsewhere).

**Reference:** `functions.md` → `Map.dangerouslyAddFeaturesToLayerWithoutValidation()`

---

### Mutable Style State for Live Re-rendering
Optimize styling updates by mutating a shared state object and calling `redrawLayer()`:

```javascript
// 1. Create mutable state object that styleContext getters close over
const mutableStyle = {
  color: '#FF0000',
  lineopacity: 1,
  fontsize: 14,
  labelpos: 'cm',
};

// 2. Create styleContext with getter functions that read from mutableStyle
const layerConfig = {
  styleContext: {
    getColor: () => mutableStyle.color,
    getLineopacity: () => mutableStyle.lineopacity,
    getFontsize: () => mutableStyle.fontsize,
    getLabelPos: () => mutableStyle.labelpos,
  },
  styleRules: [
    {
      predicate: () => true,
      style: {
        stroke: true,
        strokeColor: '${getColor}',
        strokeOpacity: '${getLineopacity}',
        pointRadius: '${getFontsize}',
      }
    }
  ],
};

// 3. Add layer once
wmeSDK.Map.addLayer({
  layerName: 'styled_layer',
  ...layerConfig,
  zIndexing: true,
});

// 4. Later: Update styles instantly without re-adding features
async function updateStyles(newColor, newOpacity) {
  mutableStyle.color = newColor;
  mutableStyle.lineopacity = newOpacity;
  
  // Tell SDK to re-invoke all styleContext getters for every feature
  await wmeSDK.Map.redrawLayer({ layerName: 'styled_layer' });
  // No features are removed/re-added; rendering is fast (~100-200ms for 1000+ features)
}
```

**Why:** When you have 1000+ features with dynamic styles, re-adding features is slow. This pattern keeps features on the map and only updates style values, making live style changes feel instantaneous.

**Performance Gain:** 10–100× faster than clearing and re-adding features.

**Use for:** Interactive style editors, live color pickers, opacity sliders, zoom-dependent styling, filters that toggle on/off.

**Reference:** `classes.md` → `Map.redrawLayer()`

---

### Dynamic styleContext Getters with Feature Properties
Access feature properties and geometry in style calculations:

```javascript
const layerConfig = {
  styleContext: {
    // Simple getter — runs for every render
    getLabel: (context) => context.feature?.properties?.label,
    
    // Zoom-aware getter — access zoomLevel from destructured argument
    getOffset: ({ zoomLevel }) => -zoomLevel,  // Negative offset at high zoom
    
    // Complex calculation
    getStrokeColor: ({ feature, zoomLevel }) => {
      if (zoomLevel > 15) return feature?.properties?.detailedColor ?? '#FF0000';
      if (zoomLevel > 12) return feature?.properties?.mediumColor ?? '#00FF00';
      return '#0000FF';
    }
  },
};

wmeSDK.Map.addLayer({
  layerName: 'smart_layer',
  styleRules: [{ style: { /* base style */ } }],
  ...layerConfig,
});
```

**Use for:** Label templates, dynamic colors based on properties, zoom-aware styling without predicates.

**Reference:** `classes.md` → `Map.addLayer()` styleContext parameter

---

### Feature-Level Predicates with Zoom Level
Show/hide features or apply conditional styles based on zoom:

```javascript
styleRules: [
  {
    // Show only at high zoom
    predicate: (featureProperties, zoomLevel) => {
      return featureProperties.importance === 'high' && zoomLevel > 12;
    },
    style: { strokeColor: '#FF0000', strokeWidth: 3 }
  },
  {
    // Show at medium zoom
    predicate: (featureProperties, zoomLevel) => {
      return zoomLevel >= 10 && zoomLevel <= 12;
    },
    style: { strokeColor: '#00FF00', strokeWidth: 2 }
  },
  {
    // Default style (always shown)
    predicate: () => true,
    style: { strokeColor: '#0000FF', strokeWidth: 1 }
  }
]
```

**Use for:** Level-of-detail rendering, hiding low-importance features at low zoom, simplifying dense maps.

**Reference:** `classes.md` → `Map.addLayer()` styleRules predicate parameter

---

### Detecting Shortcut Key Conflicts
Check if a shortcut key combo is already in use before registering:

```javascript
function registerMyShortcut(shortcutId, description, callback) {
  // Get the user's preferred keys (or null if not set)
  let shortcutKeys = getUserSavedShortcutKeys(shortcutId); // e.g., "shift+a" or null

  if (shortcutKeys) {
    // Check if another script is already using these keys
    if (wmeSDK.Shortcuts.areShortcutKeysInUse({ shortcutKeys })) {
      console.warn(`Shortcut keys "${shortcutKeys}" already in use.`);
      shortcutKeys = null; // Register without keys; user assigns later
    }
  }

  try {
    wmeSDK.Shortcuts.createShortcut({
      shortcutId,
      description,
      shortcutKeys, // Can be null; user will assign in settings
      callback,
    });
  } catch (e) {
    console.error(`Failed to register shortcut: ${e.message}`);
  }
}
```

**Use for:** Multi-script environments, graceful fallback, preventing registration errors.

**Reference:** `classes.md` → `Shortcuts.areShortcutKeysInUse()`, `Shortcuts.createShortcut()`

---

### Querying Map Viewport
Get current map center and bounding box for filtering or analytics:

```javascript
// Get current map center (WGS84 coordinates)
const center = wmeSDK.Map.getMapCenter();
console.log(`Center: lat ${center.latitude}, lon ${center.longitude}`);

// Get current visible extent (bounding box)
const extent = wmeSDK.Map.getMapExtent();
// extent = { north, south, east, west } in WGS84

// Filter features to only those in current view
const visibleLayers = allLayers.filter(layer => {
  const layerBounds = turf.bbox(layer.geometry); // [minLon, minLat, maxLon, maxLat]
  const viewBounds = turf.bboxPolygon([extent.west, extent.south, extent.east, extent.north]);
  return turf.booleanIntersects(layer.geometry, viewBounds);
});
```

**Use for:** Viewport-based filtering, "What's in view?" queries, level-of-detail decisions, map-aware data fetching.

**Reference:** `functions.md` → `Map.getMapCenter()`, `Map.getMapExtent()` | `Turf-Docs.md` → `bbox()`, `booleanIntersects()`

---

### Detecting Current Country Context
Query which country is at the center of the map:

```javascript
const wmeTopCountry = wmeSDK.DataModel.Countries.getTopCountry();
if (wmeTopCountry) {
  console.log(`Currently viewing: ${wmeTopCountry.name} (ID: ${wmeTopCountry.countryID})`);
  
  // Enable/disable features based on country
  if (wmeTopCountry.countryID === 'US') {
    loadUSSpecificLayers();
  } else if (wmeTopCountry.countryID === 'GB') {
    loadUKSpecificLayers();
  }
}
```

**Why:** Multi-region scripts need to adapt UI/data based on current map location. The country at screen center is the most reliable indicator.

**Use for:** Regional feature toggles, country-specific data sources, localized label templates.

**Returns:** Object with `{ countryID, name, ...}` or `null` if no country under center.

**Reference:** `classes.md` → `DataModel.Countries.getTopCountry()`

---

### Direct DOM Manipulation After Sidebar Registration
Access and customize tab DOM elements directly after registration:

```javascript
// Register sidebar tab — returns DOM element references
const { tabLabel, tabPane } = await wmeSDK.Sidebar.registerScriptTab({
  tabName: 'MyScript',
  tabLabel: 'My',
});

// tabLabel and tabPane are live DOM nodes in the sidebar
// Customize them directly without re-registration
tabLabel.innerHTML = '<strong>My Script</strong> <span class="badge">5</span>';

// Build tab content
const contentHTML = `
  <div id="my-settings">
    <button id="save-btn">Save Settings</button>
    <div id="status">Ready</div>
  </div>
`;
tabPane.innerHTML = contentHTML;

// Set up event listeners on your new elements
document.getElementById('save-btn').addEventListener('click', () => {
  document.getElementById('status').textContent = 'Saving...';
  saveSettings().then(() => {
    document.getElementById('status').textContent = 'Saved!';
  });
});
```

**Why:** After registration, the tab is live in the DOM. Direct manipulation is faster and more flexible than re-registering or using jQuery selectors across the page.

**Use for:** Dynamic tab labels, badge updates, status indicators, interactive settings panels.

**Reference:** `classes.md` → `Sidebar.registerScriptTab()`

---

### Reacting to Map Events
Listen for map interactions and layer state changes:

```javascript
// React to map panning/zooming finishing
wmeSDK.Events.on({
  eventName: 'wme-map-move-end',
  eventHandler: () => {
    const extent = wmeSDK.Map.getMapExtent();
    console.log(`Map moved. New bounds: ${extent.north}, ${extent.south}, ...`);
    updateVisibleLayers(extent);
  },
});

// React to user toggling layer visibility
wmeSDK.Events.on({
  eventName: 'wme-layer-checkbox-toggled',
  eventHandler: (layerInfo) => {
    console.log(`Layer "${layerInfo.layerName}" is now ${layerInfo.visible ? 'visible' : 'hidden'}`);
  },
});

// React to user selection changes (if needed)
wmeSDK.Events.on({
  eventName: 'wme-selection-changed',
  eventHandler: (selection) => {
    console.log(`Selection updated: ${selection.segments.length} segments, ${selection.nodes.length} nodes`);
  },
});
```

**Use for:** Triggering data fetches on map move, syncing external UI with layer state, responsive feature updates.

**Common Events:**
- `wme-map-move-end` — Map finished panning/zooming
- `wme-layer-checkbox-toggled` — User toggled layer visibility
- `wme-selection-changed` — User selection updated
- `wme-map-zoom-changed` — Zoom level changed (if SDK version supports)

**Reference:** `classes.md` → `Events.on()`; check SDK changelog for complete event list

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

## When to Use This Skill

✓ You have WME userscript code using `W` object or OpenLayers  
✓ You're building a new WME feature and want SDK guidance  
✓ You need help with SDK initialization or authentication  
✓ You're adding settings UI, keyboard shortcuts, or advanced styling  
✓ You're integrating external GIS data or APIs  
✓ You need performance optimization for many features  
✓ You're unsure how to do something in WME SDK (check docs via this skill)  

✗ General JavaScript questions (use your standard tools)  
✗ Waze Editor UI/UX feedback (not relevant to scripting)  
✗ Non-Tampermonkey contexts

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
- **Mirror Docs (Production):** https://kid4rm90s.github.io/WME-SDK-Mirror/production/latest/output/docs/
- **Mirror Docs (Beta):** https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/
- **WME-SDK-Mirror (GitHub original):** https://github.com/JS55CT/WME-SDK-Mirror
- **WME-SDK-Mirror (GitHub fork):** https://github.com/kid4rm90s/WME-SDK-Mirror
- **Waze Map Editor:** https://www.waze.com/editor/
- **WME icons Collection:** https://73vw.github.io/The-unofficial-Waze-map-editor-icons-studio/