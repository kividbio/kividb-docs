---
title: "MEMORY USAGE"
description: "Returns an estimate of the bytes key and its value take; nil if the key does not exist."
version: "1.1"
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
Returns an estimate of the bytes `key` and its value take; `nil` if the key does not exist. For a large collection, the estimate is from `SAMPLES count` of its elements, 5 by default, or all of them with `0`.

## Known issue

`SAMPLES 0` on a hash, set or sorted set closes the connection, with an error in the server's log; Redis takes it as every element. Filed as [kividb#151](https://github.com/kividbio/kividb/issues/151).

## Examples

```
> SET user:1 Grace
OK
> MEMORY USAGE user:1
(integer) 32
```
