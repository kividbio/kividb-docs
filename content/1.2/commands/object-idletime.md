---
title: "OBJECT IDLETIME"
description: "Seconds since the key was last read or written, while an LRU or LRM maxmemory-policy is selected; an error under an LFU policy, as in Redis."
version: "1.2"
command: "OBJECT IDLETIME"
syntax: "OBJECT IDLETIME key"
group: "generic"
since: "1.1.0"
history: []
container: "OBJECT"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
OBJECT IDLETIME key
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Seconds since the key was last read or written, while an LRU or LRM `maxmemory-policy` is selected; an error under an LFU policy, as in Redis. `0` under the policies that do not go by use (`noeviction`, the random ones, `volatile-ttl`): keys are not watched then

Seconds since the key was last read or written, while an LRU or LRM `maxmemory-policy` is selected; an error under an LFU policy, as in Redis. `0` under the policies that do not go by use (`noeviction`, the random ones, `volatile-ttl`): keys are not watched then
