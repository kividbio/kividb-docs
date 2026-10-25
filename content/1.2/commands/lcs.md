---
title: "LCS"
description: "Finds the longest common subsequence of the strings at key1 and key2: the longest run of characters found in both, in the same order, not necessarily next to each other."
version: "1.2"
command: "LCS"
syntax: "LCS key1 key2 [LEN] [IDX] [MINMATCHLEN n] [WITHMATCHLEN]"
group: "string"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["read", "slow", "string"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LCS key1 key2 [LEN] [IDX] [MINMATCHLEN n] [WITHMATCHLEN]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@string`
<!-- generated: end -->
Finds the longest common subsequence of the strings at `key1` and `key2`: the longest run of characters found in both, in the same order, not necessarily next to each other.

## Options

| Option | Effect |
|---|---|
| `LEN` | Reply with the length only. |
| `IDX` | Reply with where the matching ranges are in each string. |
| `MINMATCHLEN n` | With `IDX`, leave out matches shorter than `n`. |
| `WITHMATCHLEN` | With `IDX`, give each match's length. |

A missing key counts as an empty string.

## Reply

- The subsequence, as a bulk string.
- With `LEN`: its length.
- With `IDX`: `matches`, a list of `[[start1, end1], [start2, end2]]` ranges (with `WITHMATCHLEN`, each followed by its length), from last to first, and `len`.

## Examples

```
> SET s1 ohmytext
OK
> SET s2 mynewtext
OK
> LCS s1 s2
"mytext"
> LCS s1 s2 LEN
(integer) 6
> LCS s1 s2 IDX MINMATCHLEN 4 WITHMATCHLEN
1) "matches"
2) 1) 1) 1) (integer) 4
         2) (integer) 7
      2) 1) (integer) 5
         2) (integer) 8
      3) (integer) 4
3) "len"
4) (integer) 6
```
