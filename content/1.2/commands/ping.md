---
title: "PING"
description: "Checks that the server answers."
version: "1.2"
command: "PING"
syntax: "PING [message]"
group: "pub-sub"
since: "1.1.0"
arity: -1
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PING [message]
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`
<!-- generated: end -->
Checks that the server answers. On a subscribed connection it replies the way subscribers' messages are replied, as an array.

## Reply

- `PONG`, or `message` if one is given.
- On a subscribed connection: `["pong", ""]`, or `["pong", message]`.

## Examples

```
> PING
PONG
> PING hi
"hi"
> SUBSCRIBE news
...
> PING hi
1) "pong"
2) "hi"
```
