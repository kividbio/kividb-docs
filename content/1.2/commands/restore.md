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
acl_categories: ["dangerous", "generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
RESTORE key ttl serialized-value [REPLACE] [ABSTTL] [IDLETIME seconds] [FREQ frequency]
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
Creates `key` from a [`DUMP`](dump.md) payload. `ttl` is in milliseconds, `0` for no expiry.

Accepts KiviDB's own payloads and supported Redis `DUMP` encodings, so data can be imported through `DUMP`/`RESTORE` or [`MIGRATE`](migrate.md). See [Migrating from Redis](../guides/migrating-from-redis.md#4-move-the-data) for the types that can be imported.

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
