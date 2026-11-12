---
title: "TYPE"
description: "Returns the type of the value at key."
version: "1.2"
command: "TYPE"
syntax: "TYPE key"
group: "generic"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "keyspace", "read"]
history: [{"release": "1.2.1", "change": "acl categories: removed generic"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TYPE key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@keyspace`, `@read`

**History:**

- 1.2.1: acl categories: removed generic
<!-- generated: end -->
Returns the type of the value at `key`.

## Reply

A simple string, one of:

| Type | Value |
|---|---|
| `string` | a string |
| `list` | a list |
| `set` | a set |
| `zset` | a sorted set |
| `hash` | a hash |
| `stream` | a stream |
| `ReJSON-RL` | a JSON document, the name Redis's JSON module uses |
| `none` | no such key |

## Examples

```
> SET a 1
OK
> TYPE a
string
> JSON.SET j $ 1
OK
> TYPE j
ReJSON-RL
> TYPE missing
none
```
