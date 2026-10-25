---
title: "DIGEST"
description: "Returns a digest of the string at key: the XXH3 64-bit hash of the value, as 16 hexadecimal digits."
version: "1.1"
command: "DIGEST"
syntax: "DIGEST key"
group: "string"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "string"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DIGEST key
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@string`
<!-- generated: end -->
Returns a digest of the string at `key`: the XXH3 64-bit hash of the value, as 16 hexadecimal digits. It is what the `IFDEQ` and `IFDNE` conditions of [`SET`](set.md) and [`DELEX`](delex.md) compare against, so a client can make a write conditional on a large value without sending the value back. KiviDB computes the same digest as Redis.

## Reply

- The digest, as a bulk string.
- `nil` if the key does not exist.

## Examples

```
> SET d hello
OK
> DIGEST d
"9555e8555c62dcfd"
```
