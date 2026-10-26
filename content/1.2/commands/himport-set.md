---
title: "HIMPORT SET"
description: "Creates the hash at key from a fieldset this connection prepared, with one value per field in the fieldset's order."
version: "1.2"
command: "HIMPORT SET"
syntax: "HIMPORT SET key fieldset value [value ...]"
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
HIMPORT SET key fieldset value [value ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Creates the hash at `key` from a fieldset this connection [prepared](himport-prepare.md), with one value per field in the fieldset's order. An existing key is replaced.

## Reply

- `OK`.
- An error if the fieldset does not exist on this connection, or the number of values does not match its fields.

## Examples

```
> HIMPORT PREPARE person name lang
OK
> HIMPORT SET p:1 person Ada Rust
OK
> HIMPORT SET p:2 person Grace COBOL
OK
> HGETALL p:2
1) "name"
2) "Grace"
3) "lang"
4) "COBOL"
> HIMPORT SET p:3 person OnlyOne
(error) ERR number of values (1) does not match the fieldset's field count (2)
```
