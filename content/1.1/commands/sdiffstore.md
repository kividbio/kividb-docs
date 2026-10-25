---
title: "SDIFFSTORE"
description: "Store the diff result in destination, replacing whatever was there (and its TTL); returns count of members stored."
version: "1.1"
command: "SDIFFSTORE"
syntax: "SDIFFSTORE destination key [key ...]"
group: "set"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["set", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SDIFFSTORE destination key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@set`, `@slow`, `@write`
<!-- generated: end -->
## Description

Store the diff result in destination, replacing whatever was there (and its TTL); returns count of members stored. An empty result leaves no destination key — likewise for `SINTERSTORE` and `SUNIONSTORE`
