---
title: "HIMPORT PREPARE"
description: "Defines a fieldset on this connection: a name for an ordered list of hash field names."
version: "1.2"
command: "HIMPORT PREPARE"
syntax: "HIMPORT PREPARE fieldset field [field ...]"
group: "hash"
since: "1.1.0"
history: []
container: "HIMPORT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HIMPORT PREPARE fieldset field [field ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Defines a fieldset on this connection: a name for an ordered list of hash field names. [`HIMPORT SET`](himport-set.md) then creates a hash from the fieldset by giving only the values, in the same order, so a bulk load of many hashes with the same fields does not send the field names again for each one. See [`HIMPORT`](himport.md).

- `fieldset`: the name to define. Preparing a name that is already defined replaces it.
- `field ...`: one or more field names, of any bytes, kept as [`HSET`](hset.md) keeps them. No name may appear twice. Before 1.2.1, they had to be valid UTF-8.

A fieldset belongs to the connection that prepared it: other connections cannot use it, and it is forgotten when the connection closes, or on [`RESET`](reset.md); 1.2.0 kept it through `RESET`. [`HIMPORT DISCARD`](himport-discard.md) and `HIMPORT DISCARDALL` forget fieldsets explicitly. `HIMPORT PREPARE` changes no data, so it is allowed wherever a read is, including on a replica.

## Reply

- `OK`.

## Errors

- `ERR duplicate field name '<field>' in fieldset` if a field is named twice.
- `ERR wrong number of arguments for 'himport|prepare' command` if no field is given.

## Examples

```
> HIMPORT PREPARE person name lang
OK
> HIMPORT SET p:1 person Ada Rust
OK
> HIMPORT PREPARE person name lang born
OK
> HIMPORT SET p:2 person Grace COBOL 1906
OK
> HGETALL p:2
1) "name"
2) "Grace"
3) "lang"
4) "COBOL"
5) "born"
6) "1906"
> HIMPORT PREPARE person name name
(error) ERR duplicate field name 'name' in fieldset
```

On another connection the fieldset does not exist:

```
client 2> HIMPORT SET p:3 person Alan Lisp 1912
(error) ERR no such fieldset 'person'; define it with HIMPORT PREPARE on this connection
```
