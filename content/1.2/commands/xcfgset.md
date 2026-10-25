---
title: "XCFGSET"
description: "Sets the configuration of the stream at key."
version: "1.2"
command: "XCFGSET"
syntax: "XCFGSET key field value [field value ...]"
group: "stream"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XCFGSET key field value [field value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
Sets the configuration of the stream at `key`.

| Field | Effect |
|---|---|
| `MAX-ENTRIES n` | Trim the stream to `n` entries on every `XADD`; `0` stops it. |
| `MAX-DELETED-ENTRY-ID id` | Raise the greatest ID counted as deleted; it never goes down. |
| `IDMP-DURATION seconds` | How long idempotent IDs are remembered, per producer; the default is `stream-idmp-duration`. |
| `IDMP-MAXSIZE n` | How many idempotent IDs are remembered, per producer; the default is `stream-idmp-maxsize`. |

## Reply

- `OK`.
- `ERR syntax error` for another field.

## Examples

```
> XCFGSET i MAX-ENTRIES 2
OK
> XADD i * x 1
"1792966338096-0"
> XADD i * x 2
"1792966338097-0"
> XADD i * x 3
"1792966338097-1"
> XLEN i
(integer) 2
```
