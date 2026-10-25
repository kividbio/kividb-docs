---
title: "FT.ALTER"
description: "Add new fields to an existing index schema."
version: "1.2"
command: "FT.ALTER"
syntax: "FT.ALTER index [SKIPINITIALSCAN] SCHEMA ADD field type [options ...]"
group: "vector-search"
since: "1.1.0"
arity: -1
flags: ["write"]
acl_categories: ["search", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FT.ALTER index [SKIPINITIALSCAN] SCHEMA ADD field type [options ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
## Description

Add new fields to an existing index schema. TEXT/TAG/NUMERIC fields take effect immediately. VECTOR fields have a fresh live index provisioned and are backfilled from existing keys unless SKIPINITIALSCAN is given. Multiple VECTOR fields per index are supported; each is queryable by `@field_name` in KNN clauses
