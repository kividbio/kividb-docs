---
title: "HPEXPIRE"
description: "Same as HEXPIRE but TTL in milliseconds"
version: "1.2"
command: "HPEXPIRE"
syntax: "HPEXPIRE key milliseconds [NX | XX | GT | LT] FIELDS numfields field [field ...]"
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
HPEXPIRE key milliseconds [NX | XX | GT | LT] FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
## Description

Same as `HEXPIRE` but TTL in milliseconds
