---
title: "SLOWLOG GET"
description: "Return the last count entries (default 128), newest first."
version: "1.2"
command: "SLOWLOG GET"
syntax: "SLOWLOG GET [count]"
group: "observability"
since: "1.1.0"
history: []
container: "SLOWLOG"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SLOWLOG GET [count]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Return the last `count` entries (default 128), newest first. Returns an empty array if no entries exist
