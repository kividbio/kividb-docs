---
title: "JSON.DEL"
description: "Deletes the values path matches in the JSON document at key."
version: "1.1"
command: "JSON.DEL"
syntax: "JSON.DEL key [path]"
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
JSON.DEL key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Deletes the values `path` matches in the JSON document at `key`. Deleting the root deletes the key; that is what happens with no path.

## Reply

- The number of values deleted.

## Examples

```
> JSON.SET d $ '{"addr":{"city":"London","zip":"N1"}}'
OK
> JSON.DEL d $.addr.zip
(integer) 1
> JSON.DEL d
(integer) 1
> EXISTS d
(integer) 0
```
