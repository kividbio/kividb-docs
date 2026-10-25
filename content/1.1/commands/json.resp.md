---
title: "JSON.RESP"
description: "Each match in RESP: null as nil, booleans as true/false, integers as integers, other numbers and strings as bulk strings, an array as [ followed by its elements, an object as { followed by alternatin…"
version: "1.1"
command: "JSON.RESP"
syntax: "JSON.RESP key [path]"
group: "json"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["json", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
JSON.RESP key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
## Description

Each match in RESP: null as nil, booleans as `true`/`false`, integers as integers, other numbers and strings as bulk strings, an array as `[` followed by its elements, an object as `{` followed by alternating names and values
