---
title: "BITCOUNT"
description: "Count the number of set bits; without range counts the whole string; BYTE mode (default) treats start/end as byte indices; BIT mode treats them as bit indices; negative indices count from the end"
version: "1.2"
command: "BITCOUNT"
syntax: "BITCOUNT key [start end [BYTE | BIT]]"
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
BITCOUNT key [start end [BYTE | BIT]]
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@read`, `@slow`
<!-- generated: end -->
## Description

Count the number of set bits; without range counts the whole string; `BYTE` mode (default) treats start/end as byte indices; `BIT` mode treats them as bit indices; negative indices count from the end
