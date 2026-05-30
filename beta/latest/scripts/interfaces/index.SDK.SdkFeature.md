---
title: SDK.SdkFeature interface
source: interfaces/index.SDK.SdkFeature.html
created: 2026-05-30
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface SdkFeature<G>

```typescript
interface SdkFeature < G extends SdkFeatureGeometry = SdkFeatureGeometry > {
  geometry: G ;
  id: string | number ;
  properties ?: SdkFeatureProperties ;
  type: "Feature" ;
}
```
## Properties
### `geometry`

```typescript
geometry: G
```
### `id`

```typescript
id: string | number
```
### **Optional** `properties`

```typescript
properties ?: SdkFeatureProperties
```
### `type`

```typescript
type: "Feature"
```
