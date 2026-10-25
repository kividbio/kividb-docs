---
title: "HSETEX"
description: "Atomically set fields, with one TTL for all of them if one is given; FNX=only if none of the fields exist, FXX=only if all of them do, KEEPTTL=leave each field's TTL as it is; with no TTL option the…"
version: "1.2"
command: "HSETEX"
syntax: "HSETEX key [FNX | FXX] [EX seconds | PX milliseconds | EXAT unix-seconds | PXAT unix-milliseconds | KEEPTTL] FIELDS numfields field value [field value ...]"
group: "hash"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["hash", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HSETEX key [FNX | FXX] [EX seconds | PX milliseconds | EXAT unix-seconds | PXAT unix-milliseconds | KEEPTTL] FIELDS numfields field value [field value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
## Description

Atomically set fields, with one TTL for all of them if one is given; `FNX`=only if none of the fields exist, `FXX`=only if all of them do, `KEEPTTL`=leave each field's TTL as it is; with no TTL option the fields end up without one. Returns 1 if applied, 0 if `FNX`/`FXX` blocked it. The older KiviDB form `HSETEX key seconds [FNX | FXX] [KEEPTTL] FIELDS …` is still accepted
