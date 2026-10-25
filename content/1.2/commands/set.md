---
title: "SET"
description: "Set a key to a string value; NX=only if absent, XX=only if present, IFEQ/IFNE=conditional on value match, IFDEQ/IFDNE=conditional on digest match, GET=return old value, EX/PX/EXAT/PXAT=set expiry, KE…"
version: "1.2"
command: "SET"
syntax: "SET key value [NX | XX | IFEQ ifeq-value | IFNE ifne-value | IFDEQ ifdeq-digest | IFDNE ifdne-digest] [GET] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | KEEPTTL]"
group: "string"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SET key value [NX | XX | IFEQ ifeq-value | IFNE ifne-value | IFDEQ ifdeq-digest | IFDNE ifdne-digest] [GET] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | KEEPTTL]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
## Description

Set a key to a string value; NX=only if absent, XX=only if present, IFEQ/IFNE=conditional on value match, IFDEQ/IFDNE=conditional on digest match, GET=return old value, EX/PX/EXAT/PXAT=set expiry, KEEPTTL=preserve existing expiry
