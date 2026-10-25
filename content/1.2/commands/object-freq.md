---
title: "OBJECT FREQ"
description: "The key's logarithmic use count (Redis's LFU counter, with lfu-log-factor and lfu-decay-time) while an LFU maxmemory-policy is selected; an error otherwise, as in Redis"
version: "1.2"
command: "OBJECT FREQ"
syntax: "OBJECT FREQ key"
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
OBJECT FREQ key
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

The key's logarithmic use count (Redis's LFU counter, with `lfu-log-factor` and `lfu-decay-time`) while an LFU `maxmemory-policy` is selected; an error otherwise, as in Redis

The key's logarithmic use count (Redis's LFU counter, with `lfu-log-factor` and `lfu-decay-time`) while an LFU `maxmemory-policy` is selected; an error otherwise, as in Redis
