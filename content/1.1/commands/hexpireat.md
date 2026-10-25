---
title: "HEXPIREAT"
description: "Set per-field expiry as an absolute Unix timestamp in seconds; a past timestamp deletes the field immediately and returns 2"
version: "1.1"
command: "HEXPIREAT"
syntax: "HEXPIREAT key unix-time-seconds [NX | XX | GT | LT] FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -6
flags: ["write"]
acl_categories: ["hash", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HEXPIREAT key unix-time-seconds [NX | XX | GT | LT] FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
## Description

Set per-field expiry as an absolute Unix timestamp in seconds; a past timestamp deletes the field immediately and returns `2`
