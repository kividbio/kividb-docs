---
title: "DELEX"
description: "Delete a key, optionally only if its string value (or digest) matches; the comparison and the deletion are one atomic step."
version: "1.1"
command: "DELEX"
syntax: "DELEX key [IFEQ val | IFNE val | IFDEQ digest | IFDNE digest]"
group: "string"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
DELEX key [IFEQ val | IFNE val | IFDEQ digest | IFDNE digest]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
## Description

Delete a key, optionally only if its string value (or digest) matches; the comparison and the deletion are one atomic step. Returns 1 if deleted, 0 if the key is missing or the condition is not met. Without a condition it deletes a key of any type
