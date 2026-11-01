---
title: "FT.CONFIG SET"
description: "Sets a setting."
version: "1.2"
command: "FT.CONFIG SET"
syntax: "FT.CONFIG SET option value"
group: "vector-search"
since: "1.1.0"
history: []
container: "FT.CONFIG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.CONFIG SET option value
```

**Available since:** 1.1.0
<!-- generated: end -->
Sets a setting. An unknown name, or a value of the wrong kind, is an error.

These are acted on; the others are kept and reported:

| Setting | |
|---|---|
| `CURSOR_MAX_IDLE` | The longest a cursor may sit unread, in milliseconds. |
| `MAXSEARCHRESULTS` | The largest `LIMIT` an `FT.SEARCH` may ask for. |
| `TIMEOUT` | The time limit of a query that names none, in milliseconds; `0`, the default, is none. One value with [`search-timeout`](../reference/configuration.md#search-timeout). |
| `ON_TIMEOUT` | `return`, `fail` or `return_strict`: what a query that runs out of time replies. One value with [`search-on-timeout`](../reference/configuration.md#search-on-timeout). |
| `DEFAULT_SCORER` | The scorer of a query that names none: `BM25STD` by default. |
| `MINSTEMLEN` | The shortest word that is stemmed, in bytes: 4 by default, at least 2. One value with [`search-min-stem-len`](../reference/configuration.md#search-min-stem-len). |
| `BM25STD_TANH_FACTOR` | The factor of the `BM25STD.TANH` scorer. |

Settings changed here are not kept across a restart; the three that are also server settings can be given in the configuration file, by those names. Before 1.2, `TIMEOUT` and `ON_TIMEOUT` did not cut a query short, and `DEFAULT_SCORER` and `MINSTEMLEN` did nothing.

## Examples

```
> FT.CONFIG SET MAXSEARCHRESULTS 1000
OK
> FT.CONFIG SET NOPE 1
(error) Invalid option
> FT.CONFIG SET MINSTEMLEN 1
(error) Minimum stem length cannot be lower than 2
```
