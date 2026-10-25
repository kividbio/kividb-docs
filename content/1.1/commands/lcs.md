---
title: "LCS"
description: "Find the longest common subsequence; LEN=return length only, IDX=return match positions, MINMATCHLEN=filter short matches, WITHMATCHLEN=include match lengths in IDX output"
version: "1.1"
command: "LCS"
syntax: "LCS key1 key2 [LEN] [IDX] [MINMATCHLEN n] [WITHMATCHLEN]"
group: "string"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["read", "slow", "string"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
LCS key1 key2 [LEN] [IDX] [MINMATCHLEN n] [WITHMATCHLEN]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@string`
<!-- generated: end -->
## Description

Find the longest common subsequence; LEN=return length only, IDX=return match positions, MINMATCHLEN=filter short matches, WITHMATCHLEN=include match lengths in IDX output
