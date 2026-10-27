---
title: "MEMORY USAGE"
description: "Returns an estimate of the bytes key and its value take; nil if the key does not exist."
version: "1.2"
command: "MEMORY USAGE"
syntax: "MEMORY USAGE key [SAMPLES count]"
group: "server"
since: "1.1.0"
history: []
container: "MEMORY"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MEMORY USAGE key [SAMPLES count]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns an estimate of the bytes `key` and its value take; `nil` if the key does not exist. For a large collection, the estimate is from `SAMPLES count` of its elements, 5 by default, or all of them with `0`. A `count` that is not a number is an error, and a negative one, or an option other than `SAMPLES`, a syntax error. Before 1.2, `SAMPLES 0` on a hash, set or sorted set closed the connection, and a `count` that was not a number was taken as 5.

## Examples

```
> SET user:1 Grace
OK
> MEMORY USAGE user:1
(integer) 32
> HSET user:2 name Ada lang en
(integer) 2
> MEMORY USAGE user:2 SAMPLES 0
(integer) 196
> MEMORY USAGE user:2 SAMPLES five
(error) ERR value is not an integer or out of range
```
