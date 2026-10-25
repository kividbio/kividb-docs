---
title: "XTRIM"
description: "Trim stream by length or minimum ID."
version: "1.1"
command: "XTRIM"
syntax: "XTRIM key MAXLEN|MINID [=|~] threshold [LIMIT count] [KEEPREF | DELREF | ACKED]"
group: "stream"
since: "1.1.0"
arity: -4
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XTRIM key MAXLEN|MINID [=|~] threshold [LIMIT count] [KEEPREF | DELREF | ACKED]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
## Description

Trim stream by length or minimum ID. With `~` trimming is approximate, removing whole nodes of `stream-node-max-entries` entries, and `LIMIT` caps how many are removed (an error without `~`, as in Redis). `KEEPREF` (default) leaves consumer groups' pending references to trimmed entries, `DELREF` removes them, `ACKED` stops at the first entry not yet acknowledged by every group
