---
title: "VRANGE"
description: "Return elements in lexicographical range of element names; bounds follow ZRANGEBYLEX syntax: [inclusive, (exclusive, - for start, + for end"
version: "1.1"
command: "VRANGE"
syntax: "VRANGE key start end [count]"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "vector"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
VRANGE key start end [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
## Description

Return elements in lexicographical range of element names; bounds follow ZRANGEBYLEX syntax: `[inclusive`, `(exclusive`, `-` for start, `+` for end
