---
title: "OBJECT REFCOUNT"
description: "Returns 1 — semantically correct since every value is behind a single Arc; returns nil for missing or expired keys"
version: "1.1"
command: "OBJECT REFCOUNT"
syntax: "OBJECT REFCOUNT key"
group: "generic"
since: "1.1.0"
history: []
container: "OBJECT"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
OBJECT REFCOUNT key
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Returns `1` — semantically correct since every value is behind a single `Arc`; returns nil for missing or expired keys

Returns `1` for existing keys; nil for missing
