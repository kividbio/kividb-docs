---
title: "HRANDFIELD"
description: "Return random field(s); negative count allows repeats"
version: "1.1"
command: "HRANDFIELD"
syntax: "HRANDFIELD key [count [WITHVALUES]]"
group: "hash"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["hash", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HRANDFIELD key [count [WITHVALUES]]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
## Description

Return random field(s); negative count allows repeats
