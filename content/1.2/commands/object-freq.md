---
title: "OBJECT FREQ"
description: "Returns the key's use count: a number that grows with how often the key is used, logarithmically, and falls with time, as Redis's LFU counter does."
version: "1.2"
command: "OBJECT FREQ"
syntax: "OBJECT FREQ key"
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
OBJECT FREQ key
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the key's use count: a number that grows with how often the key is used, logarithmically, and falls with time, as Redis's LFU counter does. It is kept while an LFU `maxmemory-policy` (`allkeys-lfu`, `volatile-lfu`) is selected; `lfu-log-factor` and `lfu-decay-time` tune it.

## Reply

- The count.
- An error if no LFU policy is selected, as in Redis.

## Examples

```
> OBJECT FREQ a
(error) ERR An LFU maxmemory policy is not selected, access frequency not tracked. Please note that when switching between policies at runtime LRU and LFU data will take some time to adjust.
```
