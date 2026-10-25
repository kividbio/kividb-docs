---
title: "JSON.NUMINCRBY"
description: "Adds number to each number path matches."
version: "1.2"
command: "JSON.NUMINCRBY"
syntax: "JSON.NUMINCRBY key path number"
group: "json"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["json", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.NUMINCRBY key path number
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Adds `number` to each number `path` matches. A result that is not a finite number fails the command, and nothing changes.

## Reply

- A JSONPath: the new values, as one JSON array in a bulk string, with `null` where a match is not a number. In RESP3, an array of numbers.
- A legacy path: the one new value.

## Examples

```
> JSON.SET d $ '{"name":"Ada","age":36}'
OK
> JSON.NUMINCRBY d $.age 2
"[38]"
> JSON.NUMINCRBY d .age 1
"39"
> JSON.NUMINCRBY d $.name 1
"[null]"
```
