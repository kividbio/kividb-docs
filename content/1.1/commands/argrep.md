---
title: "ARGREP"
description: "Returns the indexes of the slots from start to end whose values match."
version: "1.1"
command: "ARGREP"
syntax: "ARGREP key start end <EXACT string | MATCH string | GLOB pattern | RE pattern [...]> [AND | OR | LIMIT limit | WITHVALUES | NOCASE ...]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["array", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ARGREP key start end <EXACT string | MATCH string | GLOB pattern | RE pattern [...]> [AND | OR | LIMIT limit | WITHVALUES | NOCASE ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the indexes of the slots from `start` to `end` whose values match. `-` and `+` stand for the first and last indexes.

| Predicate | Matches values |
|---|---|
| `EXACT string` | equal to `string` |
| `MATCH string` | containing `string` |
| `GLOB pattern` | matching a glob-style pattern |
| `RE pattern` | matching a regular expression |

Several predicates match a value that any of them matches; `AND` makes it all of them. `NOCASE` ignores case, `LIMIT limit` returns at most that many, and `WITHVALUES` returns `[index, value]` pairs.

## Examples

```
> ARSET t 0 apple banana cherry Apricot
(integer) 4
> ARGREP t - + MATCH an
1) (integer) 1
> ARGREP t - + GLOB a* NOCASE WITHVALUES
1) 1) (integer) 0
   2) "apple"
2) 1) (integer) 3
   2) "Apricot"
> ARGREP t - + RE ^b OR MATCH rr
1) (integer) 1
2) (integer) 2
```
