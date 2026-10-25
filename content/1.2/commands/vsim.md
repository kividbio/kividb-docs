---
title: "VSIM"
description: "Return elements ordered by cosine similarity to the query vector; ELE queries by an existing element's vector; scores are similarities computed using the set's stored distance metric (1.0 = identical…"
version: "1.2"
command: "VSIM"
syntax: "VSIM key (ELE | FP32 | VALUES num) vector [WITHSCORES] [WITHATTRIBS] [COUNT num] [EF n] [NOTHREAD] [TRUTH]"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "vector"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
VSIM key (ELE | FP32 | VALUES num) vector [WITHSCORES] [WITHATTRIBS] [COUNT num] [EF n] [NOTHREAD] [TRUTH]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
## Description

Return elements ordered by cosine similarity to the query vector; `ELE` queries by an existing element's vector; scores are similarities computed using the set's stored distance metric (1.0 = identical for cosine/IP, bounded 0–1 for L2)
