---
title: SDK.Venue interface
source: interfaces/index.SDK.Venue.html
created: 2026-07-08
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface Venue

```typescript
interface Venue {
  aliases: string [] ;
  approved: boolean ;
  brand: null | string ;
  categories: VenueCategoryId [] ;
  description: string ;
  externalProviderIds: string [] ;
  geometry: Point | Polygon ;
  id: string ;
  images: VenueImage [] ;
  isAdLocked: boolean ;
  isResidential: boolean ;
  lockRank: number ;
  modificationData: ModificationMetadata ;
  name: string ;
  navigationPoints: NavigationPoint [] ;
  openingHours: OpeningHour [] ;
  phone: string ;
  services: ServiceType [] ;
  url: string ;
  venueUpdateRequests: VenueUpdateRequest [] ;
}
```
## Properties
### `aliases`

```typescript
aliases: string []
```
### `approved`

```typescript
approved: boolean
```
### `brand`

```typescript
brand: null | string
```
### `categories`

```typescript
categories: VenueCategoryId []
```
### `description`

```typescript
description: string
```
### `externalProviderIds`

```typescript
externalProviderIds: string []
```
### `geometry`

```typescript
geometry: Point | Polygon
```
### `id`

```typescript
id: string
```
### `images`

```typescript
images: VenueImage []
```
### `isAdLocked`

```typescript
isAdLocked: boolean
```
### `isResidential`

```typescript
isResidential: boolean
```
### `lockRank`

```typescript
lockRank: number
```
### `modificationData`

```typescript
modificationData: ModificationMetadata
```
### `name`

```typescript
name: string
```
### `navigationPoints`

```typescript
navigationPoints: NavigationPoint []
```
### `openingHours`

```typescript
openingHours: OpeningHour []
```
### `phone`

```typescript
phone: string
```
### `services`

```typescript
services: ServiceType []
```
### `url`

```typescript
url: string
```
### `venueUpdateRequests`

```typescript
venueUpdateRequests: VenueUpdateRequest []
```
