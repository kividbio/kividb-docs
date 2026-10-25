---
title: "LMOVEM"
description: "Moves several elements from one end of source to one end of destination in one step, a command of Redis 8.10."
version: "1.2"
command: "LMOVEM"
syntax: "LMOVEM source destination LEFT|RIGHT LEFT|RIGHT [<COUNT count | EXACTLY count> <OBO | BULK>]"
group: "list"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LMOVEM source destination LEFT|RIGHT LEFT|RIGHT [<COUNT count | EXACTLY count> <OBO | BULK>]
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
Moves several elements from one end of `source` to one end of `destination` in one step, a command of Redis 8.10. Without a count it moves one element.

## Options

| Option | Effect |
|---|---|
| `COUNT count` | Move up to `count` elements. |
| `EXACTLY count` | Move exactly `count` elements, or none if `source` has fewer. |
| `OBO` | Move them one by one, as repeated `LMOVE` would: into the head of `destination`, their order is reversed. |
| `BULK` | Move them as a block, keeping their order. |

## Reply

- An array of the elements moved, in the order they now have in `destination`.
- `nil` if `EXACTLY` could not be met, or `source` does not exist; nothing is moved.

## Examples

```
> RPUSH a 1 2 3 4 5
(integer) 5
> LMOVEM a b LEFT LEFT COUNT 3 OBO
1) "3"
2) "2"
3) "1"
> LRANGE b 0 -1
1) "3"
2) "2"
3) "1"
> RPUSH c 1 2 3 4 5
(integer) 5
> LMOVEM c d LEFT LEFT COUNT 3 BULK
1) "1"
2) "2"
3) "3"
> LRANGE d 0 -1
1) "1"
2) "2"
3) "3"
> LMOVEM c d LEFT LEFT EXACTLY 5 BULK
(nil)
```
