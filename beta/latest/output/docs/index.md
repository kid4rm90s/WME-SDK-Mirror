---
sdk: WME
version: v2.348-7-g65f6c19c77
generated: 2026-04-17
sections:
  classes: classes.md
  modules: modules.md
  types: types.md
  interfaces: interfaces.md
  variables: variables.md
  functions: functions.md
  changelog: changelog.md
docs:
  typedefs:
    - wmeSDK_typedefs.d.md
  external:
    - GeoJSON-Format-RFC-7946.md
    - Turf-Docs.md
  guides:
    - geometry-file-converters.md
    - how-to-get-started-with-the-wmeSDK.md
    - migration-guide.md
    - script-example-1.md
    - script-example-2.md
    - script-example-3.md
    - script-example-4.md
    - script-example-5.md
    - script-example-6.md
    - script-example-7.md
    - script-example-8.md
---

## Table of Contents

- [Source Guide](#source-guide)
- [Classes](#classes)
- [Modules](#modules)
- [Types](#types)
- [Interfaces](#interfaces)
- [Variables](#variables)
- [Functions](#functions)
- [Changelog](#changelog)
- [Type Definition Files](#type-definition-files)
- [External Documentation Files](#external-documentation-files)
- [Getting Started / How-To Guides](#getting-started--how-to-guides)

> **Use this index to discover available documentation and their content.**
> For searching SDK entities, refer to the Source Guide below, then navigate to the relevant section.

> **SDK Version:** v2.348-7-g65f6c19c77
> **Docs generated:** 2026-04-17

> Each section below lists the source file and the entities it contains.

## Source Guide

This section describes each documentation source included for NotebookLM comprehension and search.

- **classes.md**: All documented SDK classes, grouped by class. Use for questions about class properties and methods.
- **modules.md**: All documented modules in the SDK. Use for module structure and contents.
- **types.md**: SDK type definitions, enums, and type aliases. Useful for type-related queries.
- **interfaces.md**: All SDK interfaces, with descriptions and members.
- **variables.md**: Variables and constants exported by the SDK.
- **functions.md**: All SDK functions, including parameters and return details.
- **changelog.md**: Historical list of SDK changes and version releases.
- **Multiple type definition files**: (e.g. geojson_typedefs.md, tufs_typedefs.md, wmeSDK_typedefs.md): The TypeScript type definitions for external types referenced by the SDK.
- **externalDocs**: Additional external documentation files for referenced libraries and standards, such as Turf and GeoJSON RFCs:
    - GeoJSON-Format-RFC-7946.md ([link](https://www.rfc-editor.org/rfc/rfc7946))
    - Turf-Docs.md ([link](https://turfjs.org/))

- **Getting Started & example scripts.**
  - **how-to-get-started-with-the-wmeSDK.md**: A user walk thru guide to setting up a new script and working with the wme SDK
  - **migration-guide.md**: Waze Map Editor JavaScript SDK: Migration & Prompt Guide
  - **geometry-file-converters.md**: javascript Utils to convert from KML, KMZ, WKT, GPX, GML, and shapefiles(SHP,SHX,DBF).ZIP to geoJSON
  - **script-example-1.md**: WME Cities Overlay - Script Example
  - **script-example-2.md**: WME GIS Layers - Script Example
  - **script-example-3.md**: WME FC Layer - Script Example
  - **script-example-4.md**: WME Utils - Bootstrap - Script Example
  - **script-example-5.md**: WME GeoFile - Script Example
  - **script-example-6.md**: WME US Government Boundaries - Script Example
  - **script-example-7.md**: WME Quick HN Importer for NP - Script Example
  - **script-example-8.md**: WME EZRoad Mod - Script Example
## Classes

- [classes.md](classes.md) — *38 entries*
    - index.SDK.BigJunctions
    - index.SDK.ChargingStation
    - index.SDK.Cities
    - index.SDK.Countries
    - index.SDK.DataModel
    - index.SDK.DataModelNotFoundError
    - index.SDK.EditSuggestions
    - index.SDK.Editing
    - index.SDK.HouseNumbers
    - index.SDK.InvalidStateError
    - index.SDK.Junctions
    - index.SDK.LayerSwitcher
    - index.SDK.MajorTrafficEvents
    - index.SDK.ManagedAreas
    - index.SDK.Map
    - index.SDK.MapComments
    - index.SDK.MapProblems
    - index.SDK.MapUpdateRequests
    - index.SDK.Nodes
    - index.SDK.ParkingLot
    - index.SDK.PermanentHazards
    - index.SDK.RestrictedDrivingAreas
    - index.SDK.RoadClosures
    - index.SDK.SdkEventBus
    - index.SDK.Segments
    - index.SDK.Settings
    - index.SDK.Shortcuts
    - index.SDK.Sidebar
    - index.SDK.States
    - index.SDK.Streets
    - index.SDK.TurnClosures
    - index.SDK.Turns
    - index.SDK.Users
    - index.SDK.ValidationError
    - index.SDK.Venues
    - index.SDK.WMEError
    - index.SDK.WmeSDK
    - index.SDK.WmeState

> See Also: [Type Definition Files](#type-definition-files), [External Documentation Files](#external-documentation-files)

## Modules

- [modules.md](modules.md) — *2 entries*
    - index.SDK
    - index

> See Also: [Type Definition Files](#type-definition-files), [External Documentation Files](#external-documentation-files)

## Types

- [types.md](types.md) — *67 entries*
    - index.SDK.BBox
    - index.SDK.CameraType
    - index.SDK.ChargersAccessType
    - index.SDK.ChargingStationCostType
    - index.SDK.ClosureStatus
    - index.SDK.DataModelName
    - index.SDK.DriveProfiles
    - index.SDK.EditSuggestionSource
    - index.SDK.EditSuggestionStatus
    - index.SDK.Extract
    - index.SDK.GENERAL_SERVICE_TYPE
    - index.SDK.InstructionOpCode
    - index.SDK.IssueSeverity
    - index.SDK.LaneGuidanceMode
    - index.SDK.LaneInstructionStrategy
    - index.SDK.LotType
    - index.SDK.MajorTrafficEventCategory
    - index.SDK.MapProblemType
    - index.SDK.OLMouseEventName
    - index.SDK.ObjectType
    - index.SDK.PARKING_LOT_SERVICE_TYPE
    - index.SDK.PLACE_UPDATE_ACTION
    - index.SDK.PLACE_UPDATE_SUBJECT
    - index.SDK.ParkingLotCostType
    - index.SDK.ParkingType
    - index.SDK.Partial
    - index.SDK.PaymentMethod
    - index.SDK.PaymentType
    - index.SDK.Pick
    - index.SDK.PlaceUpdateType
    - index.SDK.Position
    - index.SDK.RESTRICTION_TYPE
    - index.SDK.Record
    - index.SDK.RegionCode
    - index.SDK.RestrictionSegmentDirection
    - index.SDK.RoadTypeId
    - index.SDK.SaveMode
    - index.SDK.SdkFeatureGeometry
    - index.SDK.SdkFeatureProperties
    - index.SDK.SdkFeatureStyleContext
    - index.SDK.SdkFeatureStylePredicate
    - index.SDK.SdkMouseEventName
    - index.SDK.SegmentDirection
    - index.SDK.SegmentLaneGuidanceDirection
    - index.SDK.SegmentPermission
    - index.SDK.Selection
    - index.SDK.SelectionWithLocalizedTypeName
    - index.SDK.ServiceType
    - index.SDK.SidebarTabName
    - index.SDK.SnapTo
    - index.SDK.SpotsEstimate
    - index.SDK.SuggestibleActionType
    - index.SDK.SuggestionResolutionRejectionReason
    - index.SDK.SuggestionResolutionStatus
    - index.SDK.UnpavedRoadsSetting
    - index.SDK.UpdateRequestSource
    - index.SDK.UpdateRequestType
    - index.SDK.UpdateableMapProblemState
    - index.SDK.UserRank
    - index.SDK.VehicleType
    - index.SDK.VenueCategoryId
    - index.SDK.VenueMainCategoryId
    - index.SDK.VenuePermission
    - index.SDK.VenueResidentialId
    - index.SDK.VenueSubCategoryId
    - index.SDK.WME_LAYER_NAMES
    - index.SDK.ZoomLevel

> See Also: [Type Definition Files](#type-definition-files), [External Documentation Files](#external-documentation-files)

## Interfaces

- [interfaces.md](interfaces.md) — *75 entries*
    - index.SDK.AffectedObject
    - index.SDK.BaseAddress
    - index.SDK.BaseRestriction
    - index.SDK.BigJunction
    - index.SDK.CallSite
    - index.SDK.Camera
    - index.SDK.ChangedField
    - index.SDK.ChangedIDsInfo
    - index.SDK.City
    - index.SDK.ConversationElement
    - index.SDK.Country
    - index.SDK.DriveProfile
    - index.SDK.EditSuggestion
    - index.SDK.EditSuggestionChange
    - index.SDK.ErrorOptions
    - index.SDK.FeatureStyle
    - index.SDK.GeoJsonObject
    - index.SDK.HouseNumber
    - index.SDK.Junction
    - index.SDK.KeyboardShortcut
    - index.SDK.LineString
    - index.SDK.LocalizedString
    - index.SDK.LonLat
    - index.SDK.MajorTrafficEvent
    - index.SDK.ManagedArea
    - index.SDK.ManagedAreaShort
    - index.SDK.MapComment
    - index.SDK.MapProblem
    - index.SDK.MapUpdateRequest
    - index.SDK.ModificationMetadata
    - index.SDK.MultiLineString
    - index.SDK.MultiPolygon
    - index.SDK.NavigationPoint
    - index.SDK.Node
    - index.SDK.OpeningHour
    - index.SDK.Pixel
    - index.SDK.Point
    - index.SDK.Polygon
    - index.SDK.RegisterSidebarTabResult
    - index.SDK.RestrictedDrivingArea
    - index.SDK.RoadClosure
    - index.SDK.RoadType
    - index.SDK.SdkEvents
    - index.SDK.SdkFeature
    - index.SDK.SdkFeatureStyleRule
    - index.SDK.SdkMouseEvent
    - index.SDK.SdkWazeFeature
    - index.SDK.Segment
    - index.SDK.SegmentAddress
    - index.SDK.SegmentFlagAttributes
    - index.SDK.SegmentLanesInfo
    - index.SDK.State
    - index.SDK.Street
    - index.SDK.Subscription
    - index.SDK.Suggestion
    - index.SDK.SuggestionAttributeChange
    - index.SDK.SuggestionEntityEdit
    - index.SDK.SuggestionResolution
    - index.SDK.TileLayerOptions
    - index.SDK.TrackedDataModel
    - index.SDK.TrackedLayer
    - index.SDK.Turn
    - index.SDK.TurnClosure
    - index.SDK.TurnLanes
    - index.SDK.UpdateRequestDetails
    - index.SDK.UpdateRequestUserPreferences
    - index.SDK.UserProfile
    - index.SDK.UserSession
    - index.SDK.UserSettings
    - index.SDK.Venue
    - index.SDK.VenueAddress
    - index.SDK.VenueCategory
    - index.SDK.VenueImage
    - index.SDK.VenueSubCategory
    - index.SDK.VenueUpdateRequest

> See Also: [Type Definition Files](#type-definition-files), [External Documentation Files](#external-documentation-files)

## Variables

- [variables.md](variables.md) — *18 entries*
    - index.SDK.DATA_MODEL_NAMES
    - index.SDK.EditSuggestionStatus
    - index.SDK.GENERAL_SERVICE_TYPE
    - index.SDK.ObjectType
    - index.SDK.PARKING_LOT_SERVICE_TYPE
    - index.SDK.PLACE_UPDATE_ACTION
    - index.SDK.PLACE_UPDATE_SUBJECT
    - index.SDK.RESTRICTION_TYPE
    - index.SDK.ROAD_TYPE
    - index.SDK.SegmentDirection
    - index.SDK.SegmentPermission
    - index.SDK.SidebarTabName
    - index.SDK.UpdateableMapProblemState
    - index.SDK.VENUE_MAIN_CATEGORY
    - index.SDK.VENUE_RESIDENTIAL
    - index.SDK.VENUE_SUBCATEGORIES
    - index.SDK.VenuePermission
    - index.SDK.WME_LAYER_NAMES

> See Also: [Type Definition Files](#type-definition-files), [External Documentation Files](#external-documentation-files)

## Functions

- [functions.md](functions.md) — *1 entries*
    - index.getWmeSdk

> See Also: [Type Definition Files](#type-definition-files), [External Documentation Files](#external-documentation-files)

## [Changelog](changelog.md)

## Type Definition Files

*1 files*
- [wmeSDK_typedefs.d.md](wmeSDK_typedefs.d.md)

> See Also: [External Documentation Files](#external-documentation-files)

## External Documentation Files

*2 files*
- [GeoJSON-Format-RFC-7946.md](GeoJSON-Format-RFC-7946.md) ([Official Docs](https://www.rfc-editor.org/rfc/rfc7946))
- [Turf-Docs.md](Turf-Docs.md) ([Official Docs](https://turfjs.org/))

## Getting Started / How-To Guides

- [GeoSHPer: shapefile to GeoJSON Converter](geometry-file-converters.md)
- [How-to-get-started-with-the-wmesdk](how-to-get-started-with-the-wmeSDK.md)
- [Waze Map Editor JavaScript SDK: Migration & Prompt Guide](migration-guide.md)
- [WME Cities Overlay - Script Example](script-example-1.md)
- [WME GIS Layers - Script Example](script-example-2.md)
- [WME FC Layer - Script Example](script-example-3.md)
- [WME Utils - Bootstrap - Script Example](script-example-4.md)
- [WME GeoFile - Script Example](script-example-5.md)
- [WME US Government Boundaries - Script Example](script-example-6.md)

