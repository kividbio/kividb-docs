---
title: "TS.ADD"
description: "Adds a sample to the time series at key: timestamp in milliseconds, or * for the server's clock, and value, a floating-point number or NaN."
version: "1.2"
command: "TS.ADD"
syntax: "TS.ADD key timestamp value [RETENTION ms] [ENCODING ...] [CHUNK_SIZE size] [DUPLICATE_POLICY policy] [ON_DUPLICATE policy] [LABELS label value ...]"
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
TS.ADD key timestamp value [RETENTION ms] [ENCODING ...] [CHUNK_SIZE size] [DUPLICATE_POLICY policy] [ON_DUPLICATE policy] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Adds a sample to the time series at `key`: `timestamp` in milliseconds, or `*` for the server's clock, and `value`, a floating-point number or `NaN`. A missing series is created, with the `RETENTION`, `LABELS`, `DUPLICATE_POLICY` and other options [`TS.CREATE`](ts.create.md) takes. `timestamp` is from `0` to 2^63 - 1; a larger one is refused, where before 1.2.1 it was replied as a negative number and lost on replicas.

Samples can be added out of order. One at a timestamp that already has a sample follows the series' duplicate policy, or `ON_DUPLICATE policy` for this sample alone, as in RedisTimeSeries. KiviDB's older `ON DUPLICATE policy`, with a space, still makes `policy` the series' own, as it did in 1.2.0, where `ON_DUPLICATE` did too. A sample the policy refuses changes nothing: before 1.2.1, the `RETENTION` and `DUPLICATE_POLICY` given with it were applied anyway, on the master alone.

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
