---
title: "XGROUP"
description: "Creates and manages consumer groups: named readers of a stream that share its entries among their consumers, and track what each consumer has been given and not yet acknowledged."
version: "1.1"
command: "XGROUP"
syntax: "XGROUP"
group: "stream"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
subcommands: ["XGROUP CREATE", "XGROUP CREATECONSUMER", "XGROUP DELCONSUMER", "XGROUP DESTROY", "XGROUP SETID"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XGROUP
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`

Subcommands: [XGROUP CREATE](xgroup-create.md), [XGROUP CREATECONSUMER](xgroup-createconsumer.md), [XGROUP DELCONSUMER](xgroup-delconsumer.md), [XGROUP DESTROY](xgroup-destroy.md), [XGROUP SETID](xgroup-setid.md)
<!-- generated: end -->
Creates and manages consumer groups: named readers of a stream that share its entries among their consumers, and track what each consumer has been given and not yet acknowledged. See its subcommands.
