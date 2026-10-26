---
title: "TS.CREATE"
description: "Creates a time series at key: samples, each a timestamp in milliseconds and a floating-point value, kept in timestamp order."
version: "1.2"
command: "TS.CREATE"
syntax: "TS.CREATE key [RETENTION ms] [ENCODING COMPRESSED|UNCOMPRESSED] [CHUNK SIZE size] [DUPLICATE_POLICY BLOCK|FIRST|LAST|MIN|MAX|SUM] [LABELS label value ...]"
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
TS.CREATE key [RETENTION ms] [ENCODING COMPRESSED|UNCOMPRESSED] [CHUNK SIZE size] [DUPLICATE_POLICY BLOCK|FIRST|LAST|MIN|MAX|SUM] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Creates a time series at `key`: samples, each a timestamp in milliseconds and a floating-point value, kept in timestamp order.

## Options

| Option | Effect |
|---|---|
| `RETENTION ms` | Drop samples older than this, measured back from the newest; `0` keeps them all (the default). |
| `LABELS label value ...` | Name-value pairs that [`TS.MGET`](ts.mget.md), [`TS.MRANGE`](ts.mrange.md) and [`TS.QUERYINDEX`](ts.queryindex.md) select series by. |
| `DUPLICATE_POLICY policy` | What a sample at a timestamp that already has one does: `BLOCK` (an error), `FIRST`, `LAST`, `MIN`, `MAX` or `SUM`. |
| `CHUNK SIZE size` | Accepted, and reported by `TS.INFO`. |
| `ENCODING COMPRESSED \| UNCOMPRESSED` | Accepted; KiviDB stores every series one way. |

## Reply

- `OK`.
- `TSDB: key already exists`.

## Differences from Redis

The default `DUPLICATE_POLICY` is `LAST`: a second sample at a timestamp replaces the first. In Redis it is `BLOCK`, an error. Give `DUPLICATE_POLICY BLOCK` to get Redis's behaviour. Filed as [kividb#127](https://github.com/kividbio/kividb/issues/127).

## Examples

```
> TS.CREATE temp:1 LABELS room kitchen kind temp
OK
> TS.CREATE temp:1
(error) TSDB: key already exists
```
