---
title: "HMSET"
description: "Another name for HSET, kept for old clients."
version: "1.2"
command: "HMSET"
syntax: "HMSET key field value [field value ...]"
group: "hash"
since: "1.1.0"
arity: -4
flags: ["fast", "write"]
acl_categories: ["fast", "hash", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HMSET key field value [field value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
Sets fields of the hash at `key`, each to its value, as [`HSET`](hset.md) does, and replies `OK` instead of a count. `HSET` has taken several field-value pairs since Redis 4.0; `HMSET` remains for clients written before that. In new code use `HSET`, which also tells you how many fields were added.

The behaviour is otherwise that of `HSET`:

- a missing key is created as a hash;
- existing fields are overwritten, and keep their place in the hash's field order;
- setting a field that has an [expiry](hexpire.md) removes the expiry;
- a field given twice takes the last value.

## Reply

- `OK`.

## Errors

- `ERR wrong number of arguments for 'hmset' command` if a field has no value.
- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key holds something other than a hash.

## Examples

```
> HMSET u name Ada lang Rust
OK
> HMSET u name Grace lang COBOL
OK
> HGETALL u
1) "name"
2) "Grace"
3) "lang"
4) "COBOL"
> HMSET u name
(error) ERR wrong number of arguments for 'hmset' command
```
