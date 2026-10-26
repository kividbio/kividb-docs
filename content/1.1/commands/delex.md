---
title: "DELEX"
description: "Deletes key, optionally only if its string value, or the value's digest, matches."
version: "1.1"
command: "DELEX"
syntax: "DELEX key [IFEQ val | IFNE val | IFDEQ digest | IFDNE digest]"
group: "string"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DELEX key [IFEQ val | IFNE val | IFDEQ digest | IFDNE digest]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
Deletes `key`, optionally only if its string value, or the value's [digest](digest.md), matches. The comparison and the deletion happen in one step.

## Options

| Option | Delete only if |
|---|---|
| `IFEQ value` | the value equals `value` |
| `IFNE value` | the value differs from `value` |
| `IFDEQ digest` | the value's digest equals `digest` |
| `IFDNE digest` | the value's digest differs from `digest` |

Without a condition, `DELEX` deletes a key of any type, like `DEL`.

## Reply

- `1` if the key was deleted.
- `0` if the key does not exist, or the condition was not met.
- `ERR Key should be of string type if conditions are specified` if a condition is given and the key is not a string.

## Examples

```
> SET d hello
OK
> DELEX d IFEQ nope
(integer) 0
> DELEX d IFEQ hello
(integer) 1
> SET d hello
OK
> DELEX d IFDEQ 9555e8555c62dcfd
(integer) 1
```
