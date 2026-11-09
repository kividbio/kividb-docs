---
title: "TIME"
description: "Returns the server's clock: Unix time in seconds, and the microseconds within that second, as two bulk strings."
version: "1.2"
command: "TIME"
syntax: "TIME"
group: "server"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["fast", "server"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TIME
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@server`
<!-- generated: end -->
Returns the server's clock: Unix time in seconds, and the microseconds within that second, as two bulk strings. It reads the clock of the machine the server runs on, so it can be used to compare clients' clocks with the server's, or to stamp data with one time for every client.

Join the two parts for microseconds since 1970: `1792968400` and `89815` are `1792968400089815`.

## Reply

An array of two bulk strings.

## Examples

```
> TIME
1) "1792968400"
2) "89815"
```
