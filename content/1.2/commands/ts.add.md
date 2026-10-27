---
title: "TS.ADD"
description: "Adds a sample to the time series at key: timestamp in milliseconds, or * for the server's clock, and value, a floating-point number or NaN."
version: "1.2"
command: "TS.ADD"
syntax: "TS.ADD key timestamp value [RETENTION ms] [ENCODING ...] [CHUNK SIZE size] [ON DUPLICATE policy] [LABELS label value ...]"
group: "time-series"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "timeseries", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TS.ADD key timestamp value [RETENTION ms] [ENCODING ...] [CHUNK SIZE size] [ON DUPLICATE policy] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Adds a sample to the time series at `key`: `timestamp` in milliseconds, or `*` for the server's clock, and `value`, a floating-point number or `NaN`. A missing series is created, with the `RETENTION`, `LABELS`, `ON_DUPLICATE` (its duplicate policy) and other options [`TS.CREATE`](ts.create.md) takes.

Samples can be added out of order. One at a timestamp that already has a sample follows the series' duplicate policy, or `ON_DUPLICATE policy` for this sample.

## Reply

- The timestamp stored.
- `TSDB: Duplicate sample in BLOCK policy` under `BLOCK`.

## Differences from Redis

With the default `ts-duplicate-policy`, `last`, a sample at a timestamp that already has one replaces it; Redis refuses it. Set `ts-duplicate-policy` to `block` for Redis's behaviour. See [`TS.CREATE`](ts.create.md).

## Examples

```
> TS.ADD temp:1 1000 20.5
(integer) 1000
> TS.ADD temp:1 2000 21
(integer) 2000
> TS.CREATE b DUPLICATE_POLICY BLOCK
OK
> TS.ADD b 1000 1
(integer) 1000
> TS.ADD b 1000 2
(error) TSDB: Duplicate sample in BLOCK policy
```
