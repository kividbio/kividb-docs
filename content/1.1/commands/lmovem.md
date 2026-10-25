---
title: "LMOVEM"
description: "Move several elements between lists in one atomic step (Redis 8.10); one element if no count is given."
version: "1.1"
command: "LMOVEM"
syntax: "LMOVEM source destination LEFT|RIGHT LEFT|RIGHT [<COUNT count | EXACTLY count> <OBO | BULK>]"
group: "list"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
LMOVEM source destination LEFT|RIGHT LEFT|RIGHT [<COUNT count | EXACTLY count> <OBO | BULK>]
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Move several elements between lists in one atomic step (Redis 8.10); one element if no count is given. `COUNT` moves up to that many; `EXACTLY` moves that many or nothing (nil). `OBO` moves them one by one, as repeated `LMOVE` would; `BULK` moves them as a block, keeping their order. Returns the moved elements
