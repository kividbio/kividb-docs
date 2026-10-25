---
title: "JSON.NUMINCRBY"
description: "Add to each matched number."
version: "1.1"
command: "JSON.NUMINCRBY"
syntax: "JSON.NUMINCRBY key path number"
group: "json"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["json", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
JSON.NUMINCRBY key path number
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
## Description

Add to each matched number. Returns the new values as one JSON array in a bulk string, `null` where the match is not a number — `"[1820,1972,null]"` (RESP3: an array of numbers). A legacy path returns the one new value. A result that is not a finite number fails the command and changes nothing
