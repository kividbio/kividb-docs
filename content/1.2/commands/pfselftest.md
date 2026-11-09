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
Runs KiviDB's checks of its HyperLogLog code and says whether they passed. Use it to check a build on a new platform; it is not needed in normal operation. It works in memory, on HyperLogLogs of its own: no key is read or written.

It checks three things, in order, and stops at the first that fails:

- an empty HyperLogLog counts `0`;
- 10,000 different elements are estimated within 2%;
- each of the 16,384 registers, set to a value, reads back the same value.

It takes no arguments. Its ACL categories include `@admin` and `@dangerous`, so a user needs them to run it.

## Reply

- `OK` if every check passed.
- `ERR HLL self-test failed: ...`, naming the check that failed and what it got.

## Examples

```
> PFSELFTEST
OK
> PFSELFTEST x
(error) ERR wrong number of arguments for 'pfselftest' command
```
