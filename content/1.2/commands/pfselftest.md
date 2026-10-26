---
title: "PFSELFTEST"
description: "Runs KiviDB's checks of its HyperLogLog code: an empty one counts 0, 10,000 elements are estimated within 2%, and registers read back as written."
version: "1.2"
command: "PFSELFTEST"
syntax: "PFSELFTEST"
group: "hyperloglog"
since: "1.1.0"
arity: 1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "hyperloglog", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PFSELFTEST
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@hyperloglog`, `@read`, `@slow`
<!-- generated: end -->
Runs KiviDB's checks of its HyperLogLog code: an empty one counts 0, 10,000 elements are estimated within 2%, and registers read back as written.

## Reply

- `OK`, or an error describing what failed.

## Examples

```
> PFSELFTEST
OK
```
