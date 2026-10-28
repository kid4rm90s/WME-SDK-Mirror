---
title: SDK.TimeFrame interface
source: interfaces/index.SDK.TimeFrame.html
created: 2026-10-28
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Interface TimeFrame

```typescript
interface TimeFrame {
  dayAlternation: DayAlternation | null ;
  daysOfMonth: DayAlternation | null ;
  endDate: string | null ;
  fromTime: string | null ;
  repeatYearly: boolean | null ;
  startDate: string | null ;
  timeZone: string | null ;
  toTime: string | null ;
  weekdays: WeekDay [] | null ;
}
```
Represents a time frame indicating when a restriction is active.
## Properties
### `dayAlternation`

```typescript
dayAlternation: DayAlternation | null
```
### `daysOfMonth`

```typescript
daysOfMonth: DayAlternation | null
```
### `endDate`

```typescript
endDate: string | null
```
### `fromTime`

```typescript
fromTime: string | null
```
### `repeatYearly`

```typescript
repeatYearly: boolean | null
```
### `startDate`

```typescript
startDate: string | null
```
### `timeZone`

```typescript
timeZone: string | null
```
### `toTime`

```typescript
toTime: string | null
```
### `weekdays`

```typescript
weekdays: WeekDay [] | null
```
