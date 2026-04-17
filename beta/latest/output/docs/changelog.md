---
title: # Next version
source: documents/CHANGELOG.html
created: 2026-04-17
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

## Next version

### Add deleteComment method

Added deleteComment method to MapComments SDK module.

### Unnecessary web-events

Fixed sdk sending unnecessary web-events when panning the map.

## v2.346

### Fix error in SDK.Editing.Selection

fix error raised from SDK.Editing.Selection when a google
place is selected.

## v2.345

### Add connectsToBigJunction method

Added DataModel.Segments.connectsToBigJunction method. It returns true for segments which are completely within or partially within(only "to" or "from" node) a big junction.

### Add isFrom/isToNodeInBigJunction methods

Added  the following methods:

- DataModel.Segments.isFromNodeInBigJunction - returns true if the segment's "from" node is part of a big junction, indicating the segment leads away from it.

- DataModel.Segments.isToNodeInBigJunction  - returns true if the segment's "to" node is part of a big junction, indicating the segment leads into it.

## v2.343

### Add isContainedInBigJunction method

Added DataModel.Segments.isContainedInBigJunction method. It returns true for segments which are completely within a big junction.

### Add mouseout event

Added the following event:

- wme-map-mouse-out - Dispatched whenever the mouse moves the cursor so that it is no longer contained within a feature on the map or the map element itself.

## v2.342

### Update migration guide

Added new items to the deprecation guide to complement the upcoming deprecation.

## v2.338

### Change wme-ready event

Introduced wme-map-initial-data-loaded, a one-time event that fires only after the initial map feature set is successfully processed.
Updated the wme-ready event to depend on this specific trigger instead of the recurring wme-map-data-loaded event. This ensures that the SDK "ready" state is only reached once essential DataModel information is fully populated.

## v2.336

### Fix doc for setLayerOpacity

The method setLayerOpacity works for any layer.
Remove documentation stating it is only for layers created
by script.

## v2.335

### Add find segment method

Added a findSegment method which allows to search for segments outside of data model.

### Add verifyTurns method

Added verifyTurns method to Segments which allows to set areFwdTurnsVerified/areRevTurnsVerified to true.

## v2.328

### Add createPathTurn method

Added createPathTurn method which creates a shortest possible path turn from the source segment to the target segment's nodes A or B.

### Add sidebar tab opened event

Added wme-sidebar-tab-opened event, dispatched after WME sidebar tab opens.

## v2.325

### Add ability to set lane guidance

added setTurnLaneGuidance method which allows to set segment turns lane guidances.

### Add ability to set selection toggling

Added following methods to control whether the features to be deselected on repeated selection:

- enableSelectionToggling

- disableSelectionToggling

### Add getEditSuggestionChanges method

Added getEditSuggestionChanges which returns all suggested changes in a per attribute format.

### Add ability to change turn lane count

Added method that allows to change segment turns lane count for a given direction.

## v2.324

### Update Waze contact emails

## v2.323

### Add link for WME_LAYER_NAMES

Added link for WME_LAYER_NAMES in the Layer events section of the README.

### Add polygon rotation/resize

Added ability to enable rotation/resize for the currently selected polygon.

### Change editor opened event trigger

Changed wme-feature-editor-opened to also trigger when selection changes but the feature type remains the same.

### Add method to change default layer styling

add addStyleRuleToLayer method to be able to change default layer styling

## v2.322

### Add restrictions to segments and turns

Add two new properties to the SDK data model:

- Segment.restrictions: An array of restrictions applicable to a segment.

- Turn.restrictions.driveProfiles: A property on turn restrictions that specifies the vehicle types (drive profiles) for which the restriction applies.

## v2.321

### Add wme layers toggles

Add following methods to LayerSwitcher :

- setPlacesLayerCheckboxChecked - toggles venues layer

- setRoadsLayerCheckboxChecked - toggles roads layer

- setPathsLayerCheckboxChecked - toggles paths layer

- setJunctionBoxesLayerCheckboxChecked - toggles junction boxes layer

- setClosuresLayerCheckboxChecked - toggles closures layer

- setHazardsLayerCheckboxChecked - toggles hazards layer

### Expose segments/venues/nodes map layers names

Exposed the following unique map layer names:

- WME_LAYER_NAMES.NODES

- WME_LAYER_NAMES.SEGMENTS

- WME_LAYER_NAMES.VENUES

### Add number of spots update method

Added updateEstimatedNumberOfSpots method to SDK Parking Lot

### Add managed areas to user info

Add managedAreas property to UserInfo

## v2.319

### Add map click event

added wme-map-mouse-up event that happens when the mouse is clicked while the pointer is inside the map.

### Add affected object ids and types to after edit

add affected object ids and types to wme-after-edit event

## v2.318

### Add canEdit method

Added the following methods to SDK Nodes:

- canEditTurns to determine whether all segments connected to the node are allowed to edit turns.

- canEdit to determine whether node properties are editable.

### Add deleteImage method to Venues

Added deleteImage method to SDK Venues

## v2.317

### Add turnsVerified segment properties

Added the following properties to the SDK Segment model:

- areFwdTurnsVerified

- areRevTurnsVerified

### Remove allowNodeTurns error

Change Nodes allowNodeTurns method to return a boolean indicating whether the change was successful. Remove behavior where the method would throw an error if there is nothing to change.

## v2.315

### Change splitSegment to return segments

Method splitSegment changed to return 2 segments the original segment was split into.

### Add isRoadTypeDrivable method

add isRoadTypeDrivable method to Segments.

### Add getVirtualNodes method

add getVirtualNodes method to Segments which returns virtually connected nodes.

### Add isVirtual method

add isVirtual method to Nodes to be able to determine whether the node is virtually connected to any segment.

## v2.314

### Add rank property to segments

add rank property to segments

## v2.312

### Improve docs of multiple methods

Fix docs for multiple methods to include documentation
for method arguments.

## v2.311

### Update map comment

- add updateComment method to MapComments.

### House numbers specific segments

Add ability to specify segments for house numbers to be snapped to. Affected methods:

- addHouseNumber

- moveHouseNumber

- updateHouseNumber

### Add map comment

Add addComment method to MapComments.

## v2.310

### Add properties to HouseNumber

add folllowing properties to HouseNumber:

- isForced

- updatedBy

### Update fractionPoint description

update HouseNumber fractionPoint description.

## v2.306

### Fix error when reading response for fetchHouseNumbers

### Add Segments.getReversedSegments method

The method identifies which segments in a given list of IDs are directionally reversed

### Add markdown export

### Expose zoomLevel for style predicate

expose current zoomLevel for style predicate functions to remove the need to call sdk.Map.getZoomLevel.

### Add a method to add a RoadClosure

Add RoadClosures.addClosure method that allows adding new RoadClosure objects.

### Fix turn closure view

fix turn closure view when adding turn closures via sdk:

- set non-saved turn closure status to unknown

- disallow to use non-saved turn closure actions

### Add mapping for residential

## v2.304

### Export "SDKFeature" types

### Add ability to edit isResidential Venue property

Added updateVenueResidential method to Venues

### Add ability to edit brand Venue property

Added brand param to Venues updateVenue method

### Add ability to edit lockRank Venue property

Added lockRank param to Venues updateVenue method

### Fix venue Residence category name

## v2.303

### Added restrictions property to Turn

This property is an array of TurnRestriction objects that apply to a turn

### Fix not being able to add turn closures

fix turn closure not being added when providing some events ids.

## v2.302

### Add isTurnAllowedBySegmentDirections method

Add isTurnAllowedBySegmentDirections method to determine if a turn can be made based on the driving directions. Helps to determine reverse connections(eg. the turn is allowed according to turn data, but not allowed by driving direction).

### Add ability to edit description Venue property

Added description param to Venues updateVenue method.

## v2.301

### Add splitSegment method to Segments

This method divides a segment into two segments at the provided point

### Fix documentation for areShortcutKeysInUse

Fix the documentation for shortcutKeys as it expects
a shortcut key combination and not a shortcut id.

### Add viewport related coordinates to map events

added viewportX/viewportY properties to SdkMouseEvent (wme-map-mouse-down|wme-map-mouse-move|wme-map-mouse-up).

## v2.300

### Create schedule when "no end date"

The issue arose because form.handleSubmit(data) includes disabled fields as undefined. When the "end date" was not selected, recurrencePattern became disabled and its value was undefined in the submitted data.
Our logic then incorrectly set repeatsYearly to true since undefined doesn't equal RECURRENCE_PATTERN.NONE. This led to a backend error, as it received repeatsYearly: true without a corresponding UNTIL (end date) value.

### Add FeatureStyle type into SDK documentation

### Add loadingIssueTrackerMapData to migration guide

update migration guide to use wme-map-data-loaded event instead of change:loadingIssueTrackerMapData to determine whether the map data is loaded.

### Add support of getting redo changes length

add getRedoChangesCount to Editing class.

### Additional tracked layer events

add tracked layer events:

- wme-layer-feature-mouse-enter when the mouse enters a tracked feature layer

- wme-layer-feature-mouse-leave when the mouse leaves a tracked feature layer

### Add marker layer example to docs

Add an example of a layer with external graphic feature styles.

### Add showVenueUpdateRequestDialog method to Venues class

It displays the Place Update Request dialog for the specified venue,
showing any pending update requests

### Added method updateStreet to Streets class

updateStreet method updates street attributes. Currently, only supports updating the direction of a street

### Added street view button events

Added wme-street-view-button-activated | wme-street-view-button-deactivated
Dispatched when WME user starts/stops dragging the street view button.

### Add getLocalizedUserProfileLink to Users class

The method returns a localized formatted link for a users editor profile page.

### Added wme-street-view-panel-visibility-changed event

The event is dispatched when the street view panel changes its visibility.

### Added optional param isChecked to addLayerCheckbox method

isChecked param gives ability to set initial checked state of the layer switcher checkbox.

## v2.298

### Update country lane width documentation

Specify units in which values are returned.

### Update isEditingHouseNumbers documentation

Updated editingHouseNumbers event and method documentation to prepare
for upcoming deletion.
The SDK HouseNumbers module is the recommended replacement.

## v2.297

### Add map update request open event

Add wme-update-request-panel-opened event that happens when
a map update request panel opens.

### Add geometry to state object

add geoJSON geometry to state object.

### Add isDeletable method to DataModel

The method take the data model name (e.g., "segments", "venues") and the object ID as input.

### Update categories with updateVenue

Added ability to update categories via SDK Venue.updateVenue.

### Additional state methods

Add following state methods:

- getAllWithoutDefault - get all the states apart from default in the WME data model.

- hasStates - returns true if there are any states apart from the default state in the WME data model.

### Add HouseNumber events

Added wme-house-number-added|wme-house-number-moved|wme-house-number-updated|wme-house-number-deleted events

## v2.296

### Add objects events

Added wme-data-model-object-state-deleted | wme-data-model-object-changed-id events.

### Add isDeleted method to DataModel

The method take the data model name (e.g., "segments", "venues") and the object ID as input

### Add isNew method to DataModel

The method take the data model name (e.g., "segments", "venues") and the object ID as input

### Add routingRoadType to Segments.updateSegments

### Additional isTurnAllowed method

additional method to determine if a turn is allowed between segments.

### Additional no edits event

additional no edits event which is dispatched after WME user performs the last undo or save indicating no edits left to be able to undo or save.

### Do not allow to add turn closures to disallowd turns

## v2.294

### Add EditSuggestions model

Implement EditSuggestions.getAll and EditSuggestions.getById methods.

### A method to add a TurnClosure

Add TurnClosures.addClosure method that allows adding new TurnClosure.

## v2.293

### Add TurnClosures model

Implement TurnClosures.getAll and TurnClosures.getById methods.

## v2.292

### Improve sdk documentation

Update documentation to include SDK API and remove
WME internals.

### Fix updateHouseNumber signature

For updateHouseNumber was changed signature: geometry argument renamed to point .

### Add support for adding HouseNumbers

Added addHouseNumber method in the HouseNumbers class.
This method creates a new house number and associates it
with the closest road segment to the given point.

### Additional isMapLoading method

Add isMapLoading state method.

### Return proper userName for venueUpdateRequest

### Userscript shortcuts persisting on reload

Fix userscript shortcuts persisting on reload after assigning null shortcuts and reassigning in the cheatsheet.

### Additional special keys

- Changed cheatsheet labels for numpad keys

- Added cheatsheet lables for the following keys: Insert, Home, Page Up, End, Page Down

## v2.291

### Tile layer interactions

- update Map.setLayerZIndex method to allow setting z-index for tile
layers, created by SDK

- fix Map.removeLayer method to allow removing tile layers, created by
SDK

### Add support for deleting HouseNumbers

Added deleteHouseNumber method in the HouseNumbers class.
This method allows you to remove an existing house number.

### Add support for updating HouseNumbers

Added updateHouseNumber method in the HouseNumbers class.
This method allows you to modify various properties of a house number,
such as its geometry, fraction point, or the house number string.

### Change getTurnsThroughNode to return unknown turns

change getTurnsThroughNode to return unknown turns as disallowed turns.

### Save mode changed event

Add an event that is dispatched on save mode change.

### Additional shortcuts note

Add a note about changing shortcuts

### Allow updating Segment direction

Allow setting Segment direction (A_TO_B/B_TO_A/TWO_WAY).

### Added snapping mode for WmeSDK.Map.drawPoint

Added snapTo parameter. If the snapTo parameter is set to "segment" ,
the point will be snapped to the nearest segment

### Support updateVenueUpdateRequest action

added method updateVenueUpdateRequest into Venues class

### Fix docs for getConnectedSegments

### Add guard for update turn method

Add guard to sdk method for updating turns that checks
if the user can perform an action with the current
save mode

### Get map resolution

Add Map.getMapResolution method to the SDK that returns current map resolution.

### Expose map zoom constraints

- expose Map.MIN_ZOOM_LEVEL and Map.MAX_ZOOM_LEVEL properties

- adjust ZoomLevel type to reflect the available zoom values

## v2.290

### Include map point coordinates into mouse events

Include x, y, lon, lat coordinates of the pointer to the mouse events.

### Add method to redraw map layer

Add possibility to redraw a map layer through SDK.

## v2.289

### Additional layer event

Add the changelayer event.

### Get countries that are managed by the current user

Add State.getManagedCountries method, that returns the list of the
countries that are managed by the current user.

### Return connected segments

Fixed getConnectedSegments methods of Segments class to return
connected segments even when all turns are disabled or segment has pedestrian/walking road type

### Add map projection

Add local and remote methods of map projection.

### Generate types only for sdk

### Allow to update Segment flag attributes

Added ability to update Segment flagAttributes through updateSegment of Segments class

### Additional editing methods

Add the following editing methods: isEditingAllowed, isDrawingInProgress, getCurrentSaveMode

### Editing locking methods

Add the following editing locking methods: lockEditing, releaseEditingLock.

### Additional edit events

Add the following edit events: wme-after-edit, wme-after-clear-redo, wme-after-undo.

### Add restrictionSubscriptions to Country

Add new restrictionSubscriptions property to the SDK output for a Country object.

### Add more information for turns

Added properties to Turn interface

- hasCustomTTS

- hasShieldsPopulated

- hasTowardsGuidance

- hasTurnGuidance

- hasVisualInstruction

### Add a possibility to move a Node

added the method moveNode into Nodes class

## v2.288

### Add support for getting parking lots category attributes

Added Parking Lot class with methods:

- getBrands - method to get the venue brands

- canExitWhileClosed - method to check if the venue can be exited while closed

- getCostType - method to get the venue cost type

- getEstimatedNumberOfSpots - method to get the estimated number of spots for

- isLotTypeDependentOnDayTime - method to check if the venue type vary depending on time/day

- getParkingLotType - method to get parking type of the venue

- getLotTypes - method to get parking lot types of the venue

- getPaymentMethods - method to get venue payment methods

### Cover additional MapUpdateRequest functionality

- allow to add comments to MapUpdateRequest

- allow to retrieve and update MapUpdateRequest resolution state (mark as open/solved/not identified)

- allow to listen to the events on "updateRequestSessions" model

### Add support for getting charging station category attributes

Added Charging Station class with methods:

- getChargersAccessType - method to get the venue chargers access type

- getCostType - method to get the venue cost type

- getNetwork - method to get the venue network

- getPaymentMethods - method to get venue payment methods

- getBrands - method to get venue brands

### Add method to dangerously add features to layer

Add method to dangerously add features to layer without validation for
viewing in exceptional cases.

### Add Junctions support

add Junctions object support to DataModel

### Add methods to SegmentHouseNumbers class

- fetchHouseNumbers - to fetch house numbers

- clearHouseNumbers - removing house numbers from the internal store if they are not in use
added ability to listen to the house numbers events

### Add venueUpdateRequests to venue

Added venueUpdateRequests property to the Venue interface

## v2.287

### Add user preferences to MapUpdateRequest

Include user preferences into MapUpdateRequest through a separate
userPreferences attribute.

### Add BigJunctions.getAllPossibleTurns method

Allow to get all possible turns for a BigJunction using getAllPossibleTurns method.

### Add methods to convert geo coordinates to map pixel

Add the following methods in the Map:

- getLonLatFromMapPixel - converts pixel coordinates, relative to the top-left corner of the map component, to geographic coordinates

- getMapPixelFromLonLat - converts geographic coordinates to pixel coordinates, relative to the top-left corner of the map component

### Added localizationTypeName to Selection interface

### Add hasClosures to Segment

Add new hasClosures property to the SDK output for a Segment object.

## v2.285

### Add regionCode to Country

Add new regionCode property to the SDK output for a Country object.

## v2.283

### Add support for moving the fractional point of a house number

Added moveHouseNumberFractionPoint method in the HouseNumbers class.
This method allows you to relocate the fractional part of an existing house number
to a different position.

### Add support for moving HouseNumbers

Added HouseNumbers class.
Added moveHouseNumber method in the HouseNumbers class.
This method allows you to relocate an existing house number to a different position.

### Fixed link for TS typings in documentation

The issue occurred because the placeholder %%WME_SDK_TYPINGS_URL%% is used
within a href attribute of the README.md file. URLs have specific character
restrictions, and the % character is not allowed without encoding.
So %%WME_SDK_TYPINGS_URL%% was encoded to %25%25WME_SDK_TYPINGS_URL%25%25.
When sed was trying to replace was %%WME_SDK_TYPINGS_URL%% with real string, there
was no %%WME_SDK_TYPINGS_URL%% but %25%25WME_SDK_TYPINGS_URL%25%25.
To resolve this, the placeholder was changed from %%WME_SDK_TYPINGS_URL%%
to --WME_SDK_TYPINGS_URL--. The - character is allowed within URLs,
so it is not encoded and could be properly replaced with the actual URL during
the subsequent substitution step in the upload_sdk_docs.sh script.

## v2.282

### Add return values for addIntersection method

addIntersection returns ids of the four newly created segments

## v2.281

### Add support for adding segment intersections

Added addIntersection method in the Segments class.
This method divides two intersecting segments into four new segments,
with a new node created at the intersection point to connect them.

## v2.280

### Add support for venue images

Added images property to the Venue interface

### Add support for venue opening hours

Added openingHours property to the Venue interface.
Added support of updating opening hours through
updateVenue method in the Venues class.

### Added new venue attributes

Attributes added to Venue interface:

- isAdLocked

- aliases

- brand

- phone

- services

- url
Added ability to update via SDK Venue.updateVenue
method:

- aliases

- phone

- services

- url

### Add support for replacing venues navigation points

Adds the ability to replace entry and exit points for venues
using the replaceNavigationPoints method in the Venues class.
The replaceNavigationPoints method accepts an navigationPoints argument, an array of NavigationPoints objects.

## v2.279

### Add more specific return types for getSelection

Selection interface was replaced with Selection type:
type Selection =
| { ids: Array ; objectType: typeof ObjectType.SEGMENT }
| { ids: Array ; objectType: typeof ObjectType.VENUE }
...

### Add ability to manually set layerSwitcher checkbox value

Added methods:

- isLayerCheckboxChecked

- setLayerCheckboxChecked

### Add method to determine if Turns are editable

Added canEditTurnsThroughNode to Turns class

### Add event for adding house number on map

Previously, we had a house number mode activated by clicking a special
button. This fired an event used by scripts to detect on-screen HN
input. Due to the house number revamp, this event is no longer fired,
and there's no special mode to edit HN.
added an event wme-map-house-number-marker-added indicating when a
user places a house number on the map. This event replaces the previous
event wme-editing-house-numbers related to house number mode.

## v2.278

### Add "Working with complex geometries" section to README

Added a "Working with geometries" section with an example showing how
to process complex geometries (MultiLineStrings, MultiPolygons, etc.)
using turf.flatten.

### Add examples to Map.addLayer method

Add usage examples to Map.addLayer method, covering approaches to
feature styling.

### Add segment attributes; add level to updateSegment method

Attributes added to Segment interface:

- length

- separator

- level

- allowNoDirection
Added ability to update level via SDK Segment.updateSegment method

### Allow to delete Segment lanes info

Allow to update fromLanesInfo/toLanesInfo with null, that will remove
lanes info for a segment.

## v2.266

### Allow to update address for a Venue with empty address

Before this CL, the updateAddress method for a Venue with empty address triggered an exception.
This fix allows to update Venue's streetId, even if the Venue does not have it now.

### Add Map.getPixelFromLonLat method

Implement Map.getPixelFromLonLat method, that returns the pixel coordinates on the screen of the given LonLat coordinates.

## v2.265

### Add attribute to determine a two-way segment

Add isTwoWay method to Segment model, that allows to distinguish between two-way and undetermined segment direction.
Include the corresponding attribute to SDK Segment model output.

### Allow creating an empty shortcut

This CL allows SDK users to create a shortcut without defining shortcut keys.
This empty shortcut will be displayed in the shortcuts dialog, and users will be able to define a custom key combination.

### Add lockRank attribute to updateSegment

Allow to update lockRank via SDK Segment.updateSegment method.

## v2.264

### Fire event on feature editor render in the sidepanel

Add "wme-feature-editor-opened" event that triggers when the feature editor was rendered.

### Add docs for SDK initialization troubleshooting

Document the issues that may happen when using wrong @run-at setting [1], or @grant headers [2], [3].
[1] https://www.tampermonkey.net/documentation.php#meta:run_at [2] https://www.tampermonkey.net/documentation.php#meta:grant [3] http://shortn/_lK8EfA3KOK

### Return known turns from Turns.getTurnsThroughNode method

Fix typo in turns filtering that prevented Turns.getTurnsThroughNode that led to getting only unknown turns instead of known ones.

## v2.262

### Add getUpdateRequestDetails method

Add support for getting an update request session
for the MapUpdateRequests model.

### Additional map events

Add the following map events: mousemove, mousedown,
mouseup, addlayer, removelayer.

### DeleteShortcut now removes empty groups

Shortcuts.deleteShortcut method now removes the
group if it is deleting the last shortcut in it.

### Add hasPermissions method for Venue

Allow to check a specific Venue permission by
using the hasPermissions method.

### Add hasToll attribute to updateSegment

Allow to update fwdToll/revToll attributes via
updateSegment method.

### Add RestrictedDrivingAreas methods

Add support for getAll, getById and getAddress
methods for the RestrictedDrivingAreas model.

### Return the original shortcut string

Shortcuts.getAllShortcuts() now returns the
original shortcut string.

### Enhance Segment.hasPermissions method

Allow to check a specific Segment permission by
using the hasPermissions method.

## v2.260

### Fix

### Remove early adoption message

Remove message noting this SDK is in early adoption mode.

## v2.259

### Add stateId to City

Add new stateId property to the SDK output for a
City object.

## v2.257

### Support for dynamic layer styles

Support including dynamic feature styles when adding a layer.

### Add PH model and Cameras methods

Create PermanentHazards model, add support for
getAllCameras and getByCameraId methods in it.

### Support Segment lanes info

Add Segment lanes info into the SDK output and
allow to update the info through the updateSegment method.

### Add wme-map-move-end event

Add wme-map-move-end event which fires when map move is
complete.
The wme-map-move event added in http://wger/944464 is fired
continuously while the map is being dragged.

## v2.256

### Add ManagedAreas methods

Add support for getAll and getById methods for the
ManagedAreas model.

### Typo in Venue docs

### Add lockRank attribute to models

### Get marker DOM element

Support marker DOM element retrieval from the
getFeatureDomElement method.

### Get feature SVG element

Support retrieval of the SVG DOM element, that is
rendered for a feature in the map, by the feature
id and its layer name.

### Get/set layer z-index

## v2.255

### Enable zIndexing on feature layers

### Additional segment attributes

### Add dailyEditCount to UserProfile interface

Add the daily edit counts to the UserProfile interface.
Rename editCount to totalEditCount to clarify difference.

## v2.254

### Make SDK_INITIALIZED inline script work with CSP

Hash for the script: sha256-c3CetKrjl6LG3ufzMQDbBziMP7naDmn6ehtnHi/2zWo=

### Add data model events

Trigger events on the SDK.Events module when a
data model repository triggers:

- objectschanged

- objectssynced

- objectsadded

- objectsremoved
To turn on tracking, first call SDK.Events.trackDataModelEvents.

### Add layers to the menu via SDK

### Add wme-layer-feature-clicked event

Add an event triggered on the SDK.Events module when a
feature is clicked on a tracked layer.
To turn on tracking, first call SDK.Events.trackLayerEvents.

### Update migration table for some events

## v2.253

### Additional Venue attributes

### Provide layer visibility change event

### Add BigJunctions support

### Support adding a raster tile layer

Support adding a raster tile layer via the SDK.

## v2.252

### Convert State getters into methods

Convert getters in the State module into methods and add tracking of
method calls
BREAKING CHANGE

### Dispatch WME events on the SDK event bus

Migrate SDK events from the DOM CustomEvents to the SDK event bus (see
the Sdk.Events module). Errors from event handlers are caught and will
not break the execution.
BREAKING CHANGE

### Introduce a generic statically typed event bus

### Update getWmeSdk() description

Add info about subsequent getWmeSdk() calls

### Add a window.SDK_INITIALIZED promise

Add a window.SDK_INITIALIZED promise that is available for userscripts
on DOMContentLoaded event before the WME is initialized. The promise
gets resolved once the getWmeSdk() function is available on the window.
Since the promise is available so early, userscripts can rely on it for
their initialization: window.SDK_INITIALIZED.then(initScript)

### Generate SDK changelog and include it into the SDK docs

- Generate the SDK changelog from semantic commit messages that have an
sdk scope

- Update the typedoc to be able to reference external markdown documents

- Reference the changelog from the docs generated by the typedoc

## v2.251

### Set visibility for all layers

### Generate & publish SDK typings

- generate a single tree-shaken typings file for the SDK

- build an npm package in .tgz format

- put the package next to the sdk docs

- add a usage example to the README with placeholders

- build script to replace placeholders with the public url of the
typings package

### Add api to get user profile

## v2.250

### Add readme for save events

### Add MapUpdateRequests methods

## v2.249

### Add events on save

Add save success/failure events to the SDK.

## v2.248

### Add more documentation for the sdk

- Add description of SDK modules and functionality of each one

- Add list of triggered events and usage example

- Add migration guide listing SDK methods for commonly used internal
WME instances

### Add MapComments methods

### Add MapProblems methods

### Create internal ClosureStatus type

## v2.247

### Add MajorTrafficEvents methods

### Add methods to get & set layer visibility and opacity

SDK methods can only modify layers that were created using the SDK.

- add Map.isLayerVisible()

- add Map.setLayerVisibility()

- add Map.getLayerOpacity()

- add Map.setLayerOpacity()

### Add methods to add/remove multiple features at once

- add Map.addFeaturesToLayer()

- add Map.removeFeaturesFromLayer()

- add Map.removeAllFeaturesFromLayer()

### Add more info for closure.isPermanent

### Add defaultLaneWidthPerRoadType to country

Add the attribute defaultLaneWidthPerRoadType to the country
interface exposed in the SDK.

### Update geometry with updateVenue

Use the action UpdateFeatureGeometry when updating a venue
geometry. The method updateVenue was previously using the
UpdateObject action which does not apply the new geometry.

### Fix setSelection

Fix bugs in setSelection method:

- setSelection with empty array clears selection

- setSelection replaces selected objects
Extract unselect logic to new method, clearSelection,
instead of allowing null in setSelection

### Add methods to get category brands

Add methods to get brands for relevant categories.

### Add isLeftHandTraffic to country interface

### Validate lon/lat arg is defined

Validate the lon/lat arg is defined for:

- Map.setMapCenter

- Segments.createRoundabout

### Add RoadClosures methods

### Add Cities methods

## v2.246

### Add Countries methods

### Add Nodes.getAll method

### Add States.getAll method

## v2.245

### Update docs for Map.getMapExtent

### Add methods for zoom in/out and to extent

### Add method Map.isStreetViewActive

### Add method Shortcuts.areShortcutKeysInUse

Support check if shortcut keys are in use.

### Add method Settings.setRegionCode

Changes the region code and reloads the app.

## v2.243

### Add Segments.updateAddress() method

add a helper method to update segment address and alt addresses

### Add Venues.updateAddress()

add a helper method to update address of the venue

### Add street ids to sdk segment interface

### Change getPermalink arg to optional

### Track all SDK method calls

### Introduce an SdkMethodTracker decorator

Introduce an SdkMethodTracker decorator that wraps SDK methods and
reports their execution using web event. All SDK modules now need to
extend an abstract SdkModule class to ensure that they have a scriptId
available. For the same reason, static methods no longer allowed.
Track Shortcuts module methods execution. Remaining SDK modules would be
migrated in a follow-up CL.

### Arg validator to preserve the original method name

Make the ArgsValidatorDecorator to preserve the original decorated
method name to improve error stacktraces.

### Update speed limit through Segments.updateSegment()

- allow to update fwd/rev segment speed limit

- verify if user allowed to update each prop

### Allow no arg to SDK method if all fields are optional

make SdkArgumentValidator to allow no arg when all object fields are
optional to improve userscripts SDK dev UX

### Document the shortcut declaration notation

add info and examples of valid shortcuts

## v2.242

### Add DataModel.Turns.updateTurn() helper method

add a helper method to update a turn

### Expose info about turn lanes in the turn DTO

### Add a Turn.getById() method

add a helper method to find existing turn by id

### Add helper methods to find turns through the segment

- add Turns.getTurnsFromSegment()

- add Turns.getTurnsToSegment()

### Add Turns.getTurnsThroughNode() helper method

add a helper method to find all the turns that go through the node

### Add DataModel.Turns.getAll()

introduce a helper method to list all the turns on the map

### Add script_name param to sdk init event

Add script_name param to the sdk init event.

### Add method Map.getLiveMapLink

Get livemap link via sdk.
Add new sdk tracking param for the livemap link.

### Add method Map.getPermalink

### Add setUserSettings method

Allow setting user settings via SDK:

- isCompactMode

- isCreateRoadsAsTwoWay

- isCreateRoadsWithAllTurnsAllowed

- isDisplayTransparentTurnArrows

- isImperial

- isSelectOnlyOnEmptySelection

- isSpreadOverlappingTurnArrows

### Convert Settings to class

Convert Settings to class.
Will be required in next CL in order to allow arg
validation.

### Add method isBetaEnvironment

### Add method getRegionCode

Add a method to get the current region code of the app.

### Add method getLocale

Add a method to get the current local code and name.

### Init sdk with script name

Initialize the sdk with a script name as well as script id.
The script name will be used for display purposes such as
in the shortcut modal

### Expose more user settings via the sdk

Expose additional user settings via the sdk:

- isCreateRoadsAsTwoWay

- isCreateRoadsWithAllTurnsAllowed

- isDisplayTransparentTurnArrows

- isSelectOnlyOnEmptySelection

- isSpreadOverlappingTurnArrows
Modify the settings documentation for clarity.
Extract Settings e2e tests to a file.

### Modify sdk init web event

Modify the web event sent when a userscript initializes
the wme sdk:

- change the event name to "WME_USERSCRIPTS_SDK_INITIALIZED"
for clarity

- send the event after the sdk is initialized

- add param for the initialized sdk as well as the requested version
See sample of event: http://gpaste/6293112051990528

## v2.241

### Remove W.map.getExtent() patch & fix e2e test

Remove the patch that makes the SDK method Map.getMapExtent() to return
a wrong value. Update the e2e test.

### Add Map.drawLine() helper method

### Add Map.drawPolygon() helper method

### Add Map.drawPoint() helper method

Add a way to draw a point on the map. The point is drawn on the sketch
layer and so is temporary. The method returns the Point geometry which
can later be wrapped into a feature and added to the map using DataLayer
methods (i.e. addNode())

### Don't allow to override existing shortcuts

## v2.240

### Add initialization message

Log message to console when initializing sdk.

### Add Venue.getAddress() helper method

### Add Segments.getConnectedSegments() helper method

### Add Node.getById() helper method

### Allow only one instance of sdk per scriptId

an error is thrown if requested versions don't match

### Add Map.getLonLatFromPixel() helper

## v2.239

### Add sdk function getUserProfileLink

Add function returning the user profile link for a
given username. To replace access to
W.Config.user_profile.url patched in
userscripts-support.js

### Support centerMapOnGeometry

### Add function to set zoom level

Add function to set the map zoom level.

### Support optional zoom for setMapCenter

Support an optional zoom level to set in setMapCenter.

### Support get venue main/sub categories

Add methods to get the venue main/sub categories:
sdk.DataModel.Venues.getVenueMainCategories()
sdk.DataModel.Venues.getVenueSubCategories()
This will replace patching W.Config in userscripts-support.js

### Track preferences change with wme-user-settings-changed event

the event is dispatched only if exposed WME preferences get changed

### Add docs to public methods & classes

Validate doc comments with eslint plugins

### Add methods to add/remove layers and features

- add Map.addLayer() that supports feature styles per geometry type

- add Map.removeLayer()

- add Map.addFeatureToLayer()

- add Map.removeFeatureFromLayer()

- cover with e2e tests

### Revise README doc for sdk

Revise the sdk README and add usage disclaimer based on
pwg consultation. Also reword/restyle some text.

## v2.238

### Update readme file

Update the SDK README file.

## v2.237

### Report get sdk event

Report an event when a userscript requests an sdk
reference.

### Pass script id to sdk modules

Pass the script id which was used to initialize an
sdk instance into the Sidebar module which requires
it to register the sidebar tab.
Previously, registering the sidebar required passing
the script id again.

### Remove users data model from sdk

Remove exposure of users data model from the sdk in order
to not expose user ids (PII).
Instead, add modification meta data to other data models
so scripts can get the relevant information from there
(createdBy/On, updatedBy/On). Instead of exposing user ids,
get the createdBy/updatedBy username which is publicly displayed
in the UI.

### Add isPracticeMode & isSnapshotMode

Add the methods isPracticeMode & isSnapshotMode
to sdk editing Module. Also move isEditingHouseNumbers
getter from WmeState to Editing module.

### Add username to logged in user

Add username (publicly visible) to logged in
user data. This was already added and removed
due to privacy concerns. Since the username
is publicly visible (e.g. in edit history),
we can add it back.

### Add SdkArgumentValidator to all SDK methods with args

### Add decorator that validates options with yup

Add an SdkArgumentValidator decorator that validates sdk method options
object using yup. If there's an error, a ValidationError is thrown.
The Actions object became a class with a static method because
decorators in object literal aren't working [0].
[0]: https://github.com/microsoft/TypeScript/issues/5770

### Reduce data exposed for logged in user

Following design review and scripter feedback,
reduce the data exposed when getting the logged in
user state to only return:
isAreaManager
isCountryManager
rank
This can be augmented as required in the future.
The user data was added in http://wger/942992 .

### Add getUserSettings method

Add method to getUserSettings which returns
a subset of the preferences model.
Currently returns isImperial and isCompactMode, based
on the scripts usage.
Return a single object instead of individual methods
for simplicity.

## v2.236

### Add DataModel.Venues.updateVenue() helper method

add a method to cover the UpdateObject & UpdateFeatureGeometry actions
use case for venues for userscripts

### Add Segments.updateSegment() method

add a method to cover the UpdateObject & UpdateFeatureGeometry actions
use case for segments for userscripts

### Define a VenueCategory type for SDK

- define a separate VenueCategory type with an id and localized name

- use it in the Venues.addVenue()

- add Venues.getVenueCategories() method that returns all available
venue categories and their translations

- add a snapshot test for the getVenueCategories() to ensure that we
won't implicitly change the set of known venue categories

### Add Actions.addAlternateStreet() helper function

add a method to cover the AddAlternateStreet action use case for
userscripts

### Add Actions.addStreet() and Streets.getStreet() helpers

Add two method to cover the AddOrGetStreet action use case for
userscripts. Separate adding & getting the street for better dev UX.

### Add Actions.addCity() and Cities.getCity() helper functions

Add two method to cover the AddOrGetCity action use case for
userscripts. Separate adding & getting the city for better dev UX.

### Add Actions.createRoundabout() helper function

add a method to cover the CreateRoundabout action use case for
userscripts

### Add Actions.addVenue()

add a method to cover the AddVenue action use case for userscripts

### Add Actions.allowNodeTurns()

add a method to cover the ModifyAllConnections action use case for
userscripts

### Add Actions.mergeSegments()

add a method to cover the MergeSegments action use case for userscripts

### Add Actions.deleteFeature()

add a method to cover the DeleteObject and DeleteSegment actions

### Add Actions.addSegment()

add a method to cover the AddSegment action use case for userscripts

## v2.234

### Add State.isEditingHouseNumbers and event

Introduce a state property and a DOM event for tracking if house numbers
editor is enabled or not

### Add map zoom and map move events

### Add information about logged in user to State.userInfo

## v2.233

### Add Shortcuts.isShortcutRegistered() method

add a helper method to check if a shortcut (action) has already been
registered

### Add Sidebar.registerScriptTab() & removeScriptTab()

Add methods to create and remove script tabs. The registerScriptTab()
waits for tab label and tab pane elements to be connected to the DOM.
The waitForElementConnected() is integrated into the registerScriptTab()
so there's no need to export it separately.

### Add Sidebar.getSelection() and .setSelection() methods

Add SDK methods to query and replace current selection.

### Add wme-selection-changed event

trigger wme-selection-changed event when selecting or unselected data
model objects

### Add Shortcuts.getAllShortcuts()

add a helper method to list all userscript shortcuts

### Add Shortcuts.createShortcut() and Shortcuts.deleteShortcut()

Add a method to create and delete shortcuts. Shortcuts created with SDK
have a forUserscript: true on them. Its impossible to delete a shortcut
that wasn't created through the SDK.
Shortcuts become visible in the shortcuts editor. Shortcut description
becomes injected into I18n like WazeWrap does.

### Add Shortcuts.addShortcutGroup()

Add helper function to register a new shortcut group. The new group
becomes visible in the keyboard shortcuts dialog. The group name is
injected into I18n translations using technique similar to what WazeWrap
does.
Shortcuts e2e tests were extracted into a separate module.
Introduced a generic InternalWMEError that indicates that some
assumptions about how WME works were broken.

### Add DataModel.Segments.getAddress()

### Add multiple fields to the DataModel.Segment

add unit test to check if all the fields are present

### Add DataModel.RoadTypes.getAll()

## v2.232

### Add props to city interface

Add properties to the city interface returned
by sdk method:

- countryId

- isEmpty
These properties are referenced in top scripts.

### Add getAll/getById for users

### Add States.getById

Add method to get a state by id.

### Add get by id for models

- Streets (b/340742761)

- Segments (b/340742659)

- Venues

### Add get all segments

### Add get all streets

### Add 'abbr' property to country

Add property 'abbr' to the country interface used
by the SDK. Prop is used by top downloaded
script.

### Add get all venues

### Return facades over data models

Instead of returning instances of data models
from SDK methods, create facades over those models.
Returning JSON objects instead of internal data models
will decouple the WME internals from the userscripts
relying on the SDK, allowing internal changes to
be done freely without breaking usages.
Furthermore, changes to the SDK interfaces will be
recognized and announced to the community when
changed.

### Align get top city

Change method to get top city instead of
city id. This is to align with the getters
for top country and state.

## v2.231

### Add isTollSegment to sdk

Add new method to SegmentsRestrictionsUseCase to
detect if a segment has a toll-free restriction.
Update unit tests for SegmentsRestrictionsUseCase.

### Add Shortcuts.getAllShortcutGroups() method

### Add Editing.refresh()

### Add Editing.undoAll()

add sdk helper function to undo all stacked actions

### Add Editing.redo()

### Add Editing.undo()

### Add Editing.save() method

Introduce an Editing.save() method that would save changes or fail with
an InvalidStateError if there's nothing to save or save is not allowed.
The save also doesn't support edit suggestions yet.

## v2.230

### Add functions to get sdk and wme versions

Add:

- getSDKVersion

- getWMEVersion

- getWMEBackEndVersion

### Add segment functions to sdk

### Add getTop* functions

Support SDK functions:

- getTopCityId

- getTopState

- getTopCountry

### Add isImperial function

Add Settings.isImperial function to SDK.

## v2.229

### Add Editing.getUnsavedChangesCount()

add sdk helper function to return a number of unsaved actions

### Add Map.getMapExtent() method

### Add Map.getMapViewportElement() method

also introduce a generic error for missing elements

### Define a withSDK helper function for e2e tests

the withSDK helper function simplifies writing tests for sdk functions

## v2.227

### Define a WmeSDK interface

this results into more readable type suggestions in LSP / IDEs

## v2.224

### Add Map.getZoomLevel() function
