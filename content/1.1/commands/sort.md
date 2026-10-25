---
title: "SORT"
description: "Sort the elements of a list, set, or sorted set; numeric sort by default; ALPHA for lexicographic; LIMIT for pagination; STORE writes result as a List and returns count; BY pattern sorts by external…"
version: "1.1"
command: "SORT"
syntax: "SORT key [BY pattern] [LIMIT offset count] [GET pattern [...]] [ASC|DESC] [ALPHA] [STORE destination]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["movablekeys", "write"]
acl_categories: ["dangerous", "generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SORT key [BY pattern] [LIMIT offset count] [GET pattern [...]] [ASC|DESC] [ALPHA] [STORE destination]
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
## Description

Sort the elements of a list, set, or sorted set; numeric sort by default; `ALPHA` for lexicographic; `LIMIT` for pagination; `STORE` writes result as a List and returns count; `BY pattern` sorts by external string key or hash field (`hash_*->field`); `GET pattern` returns external values instead of elements; `GET #` returns the element itself
