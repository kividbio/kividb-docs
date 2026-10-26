---
title: "HRANDFIELD"
description: "Returns fields of the hash at key, picked at random."
version: "1.1"
command: "HRANDFIELD"
syntax: "HRANDFIELD key [count [WITHVALUES]]"
group: "hash"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["hash", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HRANDFIELD key [count [WITHVALUES]]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
Returns fields of the hash at `key`, picked at random.

## Options

| Option | Effect |
|---|---|
| `count` | Return up to `count` different fields; a negative `count` returns exactly `-count` fields, which may repeat. |
| `WITHVALUES` | Return each field with its value. |

## Reply

- Without `count`: a field name, or `nil` if the key does not exist.
- With `count`: an array, empty if the key does not exist.

## Examples

```
> HSET h a 1 b 2 c 3
(integer) 3
> HRANDFIELD h
"b"
> HRANDFIELD h -5
1) "b"
2) "b"
3) "a"
4) "c"
5) "a"
> HRANDFIELD h 2 WITHVALUES
1) "b"
2) "2"
3) "c"
4) "3"
```
