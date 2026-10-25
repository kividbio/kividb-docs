---
title: "LPOS"
description: "Return the index of matching elements; RANK skips the first n-1 matches (negative=scan from tail), COUNT=number of matches to return (0=all), MAXLEN=limit scan length"
version: "1.1"
command: "LPOS"
syntax: "LPOS key element [RANK rank] [COUNT num-matches] [MAXLEN len]"
group: "list"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["list", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
LPOS key element [RANK rank] [COUNT num-matches] [MAXLEN len]
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@read`, `@slow`
<!-- generated: end -->
## Description

Return the index of matching elements; RANK skips the first n-1 matches (negative=scan from tail), COUNT=number of matches to return (0=all), MAXLEN=limit scan length
