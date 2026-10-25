---
title: "FT.SPELLCHECK"
description: "Return spelling suggestions for unrecognised query terms."
version: "1.2"
command: "FT.SPELLCHECK"
syntax: "FT.SPELLCHECK index query [DISTANCE n] [TERMS INCLUDE|EXCLUDE dict ...]"
group: "vector-search"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["read", "search", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FT.SPELLCHECK index query [DISTANCE n] [TERMS INCLUDE|EXCLUDE dict ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
## Description

Return spelling suggestions for unrecognised query terms. Vocabulary is maintained incrementally on every indexed HSET, so query latency is independent of dataset size. Tokens are not removed from the vocabulary on document delete — full rebuild is via index drop and recreate
