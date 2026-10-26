---
title: "SETRANGE"
description: "Overwrites the string at key from byte offset on with value."
version: "1.2"
command: "SETRANGE"
syntax: "SETRANGE key offset value"
group: "string"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SETRANGE key offset value
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
Overwrites the string at `key` from byte `offset` on with `value`. If the string is shorter than `offset`, it is padded with zero bytes first. A missing key is created.

## Reply

- The length of the string afterwards.

## Examples

```
> SET k "hello world"
OK
> SETRANGE k 6 there
(integer) 11
> GET k
"hello there"
> SETRANGE pad 5 x
(integer) 6
> GET pad
"\x00\x00\x00\x00\x00x"
```
