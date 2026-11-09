---
title: "ECHO"
description: "Returns message."
version: "1.2"
command: "ECHO"
syntax: "ECHO message"
group: "server"
since: "1.1.0"
arity: 2
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ECHO message
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`
<!-- generated: end -->
Returns `message`, unchanged. It touches no key and needs no data, so it is a simple way to check that a connection works and round trips are as fast as expected, like [`PING`](ping.md), but with a payload of your choosing to match the reply against.

`message` is one argument: quote it if it contains spaces.

## Reply

`message`, as a bulk string.

## Examples

```
> ECHO hello
"hello"
> ECHO "hello world"
"hello world"
> ECHO a b
(error) ERR wrong number of arguments for 'echo' command
```
