---
title: "JSON.MSET"
description: "Runs JSON.SET for several key, path and value triples in one command."
version: "1.2"
command: "JSON.MSET"
syntax: "JSON.MSET key path value [key path value ...]"
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
JSON.MSET key path value [key path value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Runs [`JSON.SET`](json.set.md) for several key, path and value triples in one command. The keys can differ, and one key can appear more than once; the triples are applied in order, so a later one sees what an earlier one wrote. Use it to write to several documents in one round trip.

Each triple behaves as `JSON.SET` without `NX` or `XX`: a JSONPath sets every value it matches, a missing member of an existing object is added, and a new key must be created at the root, `$`. See [JSON paths](../reference/json-paths.md).

Before any key is changed, every triple is checked for a path that can be read and a value that is JSON text, so a mistake there changes nothing. Other failures are only found when a triple is applied, and they stop the command with the earlier triples already written: a key holding another type, a new key with a path other than `$`, a projection as the path, or a legacy path whose parent does not exist. A triple whose JSONPath matches nothing changes nothing and does not fail.

## Reply

- `OK`, when every triple was applied.

## Errors

- `ERR invalid JSON value` or a path parse error: nothing was changed.
- `ERR new objects must be created at the root`, `WRONGTYPE`, `ERR path does not exist`: the triples before the failing one were applied.

## Examples

```
> JSON.MSET a $ '{"n":1}' b $ '{"n":2}' a $.m 3
OK
> JSON.GET a
"{\"n\":1,\"m\":3}"
> JSON.MSET a $.n 10 c $ bad
(error) ERR invalid JSON value
> JSON.GET a
"{\"n\":1,\"m\":3}"
> JSON.MSET a $.n 10 c $.x 1
(error) ERR new objects must be created at the root
> JSON.GET a
"{\"n\":10,\"m\":3}"
```
