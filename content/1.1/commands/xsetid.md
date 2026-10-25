---
title: "XSETID"
description: "Set the stream's last-generated ID and metadata"
version: "1.1"
command: "XSETID"
syntax: "XSETID key last-id [ENTRIESADDED n] [MAXDELETEDID id]"
group: "stream"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XSETID key last-id [ENTRIESADDED n] [MAXDELETEDID id]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
## Description

Set the stream's last-generated ID and metadata
