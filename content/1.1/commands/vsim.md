---
title: "VSIM"
description: "Returns the elements of the vector set at key most similar to a vector, most similar first."
version: "1.1"
command: "VSIM"
syntax: "VSIM key (ELE | FP32 | VALUES num) vector [WITHSCORES] [WITHATTRIBS] [COUNT num] [EF n] [NOTHREAD] [TRUTH]"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "vector"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
VSIM key (ELE | FP32 | VALUES num) vector [WITHSCORES] [WITHATTRIBS] [COUNT num] [EF n] [NOTHREAD] [TRUTH]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns the elements of the vector set at `key` most similar to a vector, most similar first.

## Options

| Option | Effect |
|---|---|
| `ELE element` | Use an element's vector. |
| `VALUES n x1 ... xn`, `FP32 blob` | Use this vector. |
| `COUNT n` | Return at most `n` elements (10 by default). |
| `WITHSCORES` | Give each element's similarity: `1` is identical. |
| `WITHATTRIBS` | Give each element's attributes. |
| `EF n`, `NOTHREAD`, `TRUTH` | Accepted. Every search compares every vector, so results are exact. |
| `FILTER expr` | Accepted, and ignored in KiviDB 1.1: every element is returned. See [kividb#132](https://github.com/kividbio/kividb/issues/132), fixed in 1.2. |

## Reply

- An array of elements; with `WITHSCORES` or `WITHATTRIBS`, each followed by its score or attributes.
- `ERR element not found in vector set` for an `ELE` that does not exist.

## Examples

```
> VSIM points VALUES 3 1 0 0 WITHSCORES COUNT 2
1) "a"
2) "1.000000"
3) "b"
4) "0.993884"
> VSIM points ELE c WITHATTRIBS COUNT 1
1) "c"
2) "{\"color\":\"red\",\"size\":3}"
```

## Known issue

`WITHSCORES` gives the cosine similarity itself, from `-1` to `1`. Redis gives it on a scale from `0` to `1`, as `(1 + cosine) / 2`. Identical vectors score `1` in both, but vectors at right angles score `0` here and `0.5` in Redis, and opposite vectors `-1` here and `0` in Redis. The order of the results is the same. Filed as [kividb#171](https://github.com/kividbio/kividb/issues/171).
