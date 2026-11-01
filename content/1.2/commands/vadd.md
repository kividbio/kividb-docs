---
title: "VADD"
description: "Adds an element with its vector to the vector set at key, or replaces an element's vector."
version: "1.2"
command: "VADD"
syntax: "VADD key [REDUCE dim] [DISTANCE L2|COSINE|INNERPRODUCT] (FP32 | VALUES num) vector element [SETATTR json] [NOQUANT|Q8|BIN] [EF n] [M n]"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "vector", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
VADD key [REDUCE dim] [DISTANCE L2|COSINE|INNERPRODUCT] (FP32 | VALUES num) vector element [SETATTR json] [NOQUANT|Q8|BIN] [EF n] [M n]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@vector`, `@write`
<!-- generated: end -->
Adds an element with its vector to the vector set at `key`, or replaces an element's vector. A missing key is created. Every vector of a set has the same number of dimensions as the first.

## Options

| Option | Effect |
|---|---|
| `VALUES n x1 ... xn` | The vector, as `n` numbers. |
| `FP32 blob` | The vector, as little-endian 32-bit floats. |
| `DISTANCE COSINE \| L2 \| IP` | How similarity is measured, before the vector or after the element; `INNERPRODUCT` is taken for `IP`. KiviDB's own: Redis 8.10's vector sets are cosine only, and refuse the word. Left out, a new set is `COSINE` and an existing one keeps its own. |
| `SETATTR json` | Attach JSON attributes to the element. |
| `EF n`, `M n` | Accepted: `M` from 4 to 4096, `EF` from 1 to 1,000,000. |
| `NOQUANT \| Q8 \| BIN` | Accepted. Vectors are kept as 32-bit floats whichever is given; [`VINFO`](vinfo.md) reports `f32`. |
| `REDUCE dim` | Refused: vectors are kept at the dimension they are given. |

## Reply

- `1` if the element is new, `0` if its vector was replaced.
- `ERR Vector dimension mismatch - got 2 but set has 3` for a vector of another size than the set's.
- `ERR invalid vector specification` for a vector given wrong: a count that does not match the numbers, a number that is not one, `NaN`, or `VALUES 0`.
- `ERR invalid option after element` for an option it does not know, or one missing its value.
- `ERR invalid M` and `ERR invalid EF` for a value out of range.
- `ERR invalid DISTANCE: use COSINE, L2 or IP` for a distance it does not know, and `ERR asked distance mismatch with existing vector set` for one other than the set's.
- `ERR REDUCE is not supported by KiviDB` with `REDUCE`.

The errors are Redis 8.10's, except those for `DISTANCE` and `REDUCE`. Before 1.2, `REDUCE` was accepted and ignored; a `DISTANCE` it did not know was taken as `COSINE`, one other than the set's was ignored, an option it did not know was skipped, `M` and `EF` were not checked, and `VALUES 0` or a `NaN` made a set. A vector of another dimension was `ERR vector dimension mismatch: index has dim 3, got 2`.

## Examples

```
> VADD points VALUES 3 1 0 0 a
(integer) 1
> VADD points VALUES 3 0.9 0.1 0 b
(integer) 1
> VADD points VALUES 3 0 1 0 c SETATTR '{"color":"red","size":3}'
(integer) 1
> VADD points VALUES 2 1 0 d
(error) ERR Vector dimension mismatch - got 2 but set has 3
> VADD points VALUES 3 1 0 0 d FOO
(error) ERR invalid option after element
> VADD points DISTANCE L2 VALUES 3 1 0 0 d
(error) ERR asked distance mismatch with existing vector set
> VADD points REDUCE 2 VALUES 3 1 0 0 d
(error) ERR REDUCE is not supported by KiviDB: vectors are kept at the dimension they are given
```
