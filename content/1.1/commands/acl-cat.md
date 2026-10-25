---
title: "ACL CAT"
description: "Returns the command categories, or the commands of one category."
version: "1.1"
command: "ACL CAT"
syntax: "ACL CAT [category]"
group: "acl"
since: "1.1.0"
history: []
container: "ACL"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ACL CAT [category]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the command categories, or the commands of one category.

The categories are: the data types `string`, `list`, `set`, `sortedset`, `hash`, `bitmap`, `hyperloglog`, `geo`, `stream`, `array`, `json`, `search`, `timeseries` and `vector`; `keyspace` and `generic`; `read` and `write`; `fast` and `slow`; `blocking`; `pubsub`, `scripting`, `transaction`, `connection`, `cluster` and `server`; and `admin` and `dangerous`.

## Examples

```
> ACL CAT hyperloglog
1) "PFADD"
2) "PFCOUNT"
3) "PFDEBUG"
4) "PFMERGE"
5) "PFSELFTEST"
```
