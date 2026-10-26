---
title: "JSON.MERGE"
description: "Merges value into each value path matches, as an RFC 7396 merge patch: members are merged into objects, null deletes a member, and anything else replaces."
version: "1.2"
command: "JSON.MERGE"
syntax: "JSON.MERGE key path value"
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
JSON.MERGE key path value
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Merges `value` into each value `path` matches, as an RFC 7396 merge patch: members are merged into objects, `null` deletes a member, and anything else replaces.

## Reply

- `OK`.

## Examples

```
> JSON.SET d $ '{"addr":{"city":"London"},"email":"ada@x"}'
OK
> JSON.MERGE d $ '{"addr":{"zip":"N1"},"email":null}'
OK
> JSON.GET d
"{\"addr\":{\"city\":\"London\",\"zip\":\"N1\"}}"
```
