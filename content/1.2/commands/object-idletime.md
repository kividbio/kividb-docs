---
title: "OBJECT IDLETIME"
description: "Returns how many seconds ago key was last read or written."
version: "1.2"
command: "OBJECT IDLETIME"
syntax: "OBJECT IDLETIME key"
group: "generic"
since: "1.1.0"
history: []
container: "OBJECT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
OBJECT IDLETIME key
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns how many seconds ago `key` was last read or written. It is kept while an LRU or LRM `maxmemory-policy` is selected.

## Reply

- The seconds.
- `0` under the policies that do not go by use (`noeviction`, the random ones, `volatile-ttl`): keys are not watched then.
- An error under an LFU policy, as in Redis.

## Examples

```
> SET a 1
OK
> OBJECT IDLETIME a
(integer) 0
```
