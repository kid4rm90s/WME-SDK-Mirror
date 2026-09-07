---
title: SDK.TimeFrame interface
source: interfaces/index.SDK.TimeFrame.html
created: 2026-09-07
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TimeFrame

```typescript
interface TimeFrame {
  dayAlternation: null | DayAlternation ;
  daysOfMonth: null | DayAlternation ;
  endDate: null | string ;
  fromTime: null | string ;
  repeatYearly: null | boolean ;
  startDate: null | string ;
  timeZone: null | string ;
  toTime: null | string ;
  weekdays: null | WeekDay [] ;
}
```
Represents a time frame indicating when a restriction is active.
## Properties
### `dayAlternation`

```typescript
dayAlternation: null | DayAlternation
```
### `daysOfMonth`

```typescript
daysOfMonth: null | DayAlternation
```
### `endDate`

```typescript
endDate: null | string
```
### `fromTime`

```typescript
fromTime: null | string
```
### `repeatYearly`

```typescript
repeatYearly: null | boolean
```
### `startDate`

```typescript
startDate: null | string
```
### `timeZone`

```typescript
timeZone: null | string
```
### `toTime`

```typescript
toTime: null | string
```
### `weekdays`

```typescript
weekdays: null | WeekDay []
```
