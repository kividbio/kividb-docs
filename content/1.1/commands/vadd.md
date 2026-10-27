---
title: "VADD"
description: "Adds an element with its vector to the vector set at key, or replaces an element's vector."
version: "1.1"
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
| `DISTANCE L2 \| COSINE \| INNERPRODUCT` | How similarity is measured. |
| `SETATTR json` | Attach JSON attributes to the element. |
| `EF n`, `M n` | Accepted. |
| `REDUCE dim`, `NOQUANT \| Q8 \| BIN` | Accepted, and ignored in KiviDB 1.1: vectors keep their dimensions and are stored unquantized. See [kividb#132](https://github.com/kividbio/kividb/issues/132), fixed in 1.2. |

## Reply

- `1` if the element is new, `0` if its vector was replaced.
- `ERR vector dimension mismatch` for a vector of another size.

## Examples

```
> VADD points VALUES 3 1 0 0 a
(integer) 1
> VADD points VALUES 3 0.9 0.1 0 b
(integer) 1
> VADD points VALUES 3 0 1 0 c SETATTR '{"color":"red","size":3}'
(integer) 1
> VADD points VALUES 2 1 0 d
(error) ERR vector dimension mismatch: index has dim 3, got 2
```
