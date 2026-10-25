---
title: "BITFIELD_RO"
description: "Read-only variant of BITFIELD; only GET subcommands are accepted"
version: "1.2"
command: "BITFIELD_RO"
syntax: "BITFIELD_RO key [GET encoding offset [GET encoding offset ...]]"
group: "bitmap"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["bitmap", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BITFIELD_RO key [GET encoding offset [GET encoding offset ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@read`, `@slow`
<!-- generated: end -->
## Description

Read-only variant of `BITFIELD`; only `GET` subcommands are accepted
