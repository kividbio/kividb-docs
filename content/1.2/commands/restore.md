---
title: "RESTORE"
description: "Creates key from a DUMP payload."
version: "1.2"
command: "RESTORE"
syntax: "RESTORE key ttl serialized-value [REPLACE] [ABSTTL] [IDLETIME seconds] [FREQ frequency]"
group: "generic"
since: "1.1.0"
arity: -4
flags: ["write"]
acl_categories: ["dangerous", "keyspace", "slow", "write"]
history: [{"release": "1.2.1", "change": "acl categories: removed generic"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
RESTORE key ttl serialized-value [REPLACE] [ABSTTL] [IDLETIME seconds] [FREQ frequency]
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@keyspace`, `@slow`, `@write`

**History:**

- 1.2.1: acl categories: removed generic
<!-- generated: end -->
Creates `key` from a [`DUMP`](dump.md) payload. `ttl` is in milliseconds, `0` for no expiry.

Accepts KiviDB's own payloads and supported Redis `DUMP` encodings, so data can be imported through `DUMP`/`RESTORE` or [`MIGRATE`](migrate.md). See [Migrating from Redis](../guides/migrating-from-redis.md#4-move-the-data) for the types that can be imported.

Since 1.2.1 it also takes the payloads of Valkey 9.0 and 9.1, KeyDB's, and Dragonfly's hashes with field times to live and JSON documents. It refuses a sorted set with a `NaN` score with `ERR Bad data format`, as Redis does, and a JSON document nested 128 levels or deeper. A key of any bytes can be restored, the empty key and keys that are not UTF-8 included; a 1.2.0 server refuses such a key, so a `MIGRATE` of one to it fails. A time series' payload carries no compaction rules: see [`TS.CREATERULE`](ts.createrule.md).

## Options

| Option | Effect |
|---|---|
| `REPLACE` | Replace `key` if it exists. |
| `ABSTTL` | `ttl` is a Unix time in milliseconds, not a duration. |
| `IDLETIME seconds`, `FREQ frequency` | Accepted for compatibility with Redis; only one of the two can be given. |

## Reply

- `OK`.
- `BUSYKEY Target key name already exists.` if `key` exists and `REPLACE` was not given.
- `ERR DUMP payload version or checksum are wrong` if the payload is too short, has an unsupported version, or fails checksum validation.
- `ERR Bad data format` if the version and checksum are accepted but the value cannot be decoded, including unsupported encodings.

## Examples

```
> SET src hello
OK
> DUMP src
"\x01\x05\x00\x00\x00hello..."
> RESTORE copy 0 "\x01\x05\x00\x00\x00hello..."
OK
> GET copy
"hello"
> RESTORE copy 5000 "\x01\x05..." REPLACE
OK
> PTTL copy
(integer) 5000
```
