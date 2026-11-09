---
title: "FT.CONFIG"
description: "FT.CONFIG is a container: its subcommands read and set the search engine's settings, by the names RediSearch gives them, so that tools and clients that manage those settings work unchanged."
version: "1.2"
command: "FT.CONFIG"
syntax: "FT.CONFIG"
group: "vector-search"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["read", "search", "slow"]
history: []
subcommands: ["FT.CONFIG GET", "FT.CONFIG HELP", "FT.CONFIG SET"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.CONFIG
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`

Subcommands: [FT.CONFIG GET](ft.config-get.md), [FT.CONFIG HELP](ft.config-help.md), [FT.CONFIG SET](ft.config-set.md)
<!-- generated: end -->
`FT.CONFIG` is a container: its subcommands read and set the search engine's settings, by the names RediSearch gives them, so that tools and clients that manage those settings work unchanged.

| Subcommand | |
|---|---|
| [`FT.CONFIG GET`](ft.config-get.md) | the value of each setting whose name matches a pattern |
| [`FT.CONFIG SET`](ft.config-set.md) | change a setting |
| [`FT.CONFIG HELP`](ft.config-help.md) | the settings, each with its value |

23 of RediSearch's settings can be read and set ([`FT.CONFIG HELP`](ft.config-help.md) lists them), but only some are acted on: `CURSOR_MAX_IDLE`, `MAXSEARCHRESULTS`, `TIMEOUT`, `ON_TIMEOUT`, `DEFAULT_SCORER`, `MINSTEMLEN` and `BM25STD_TANH_FACTOR`; [`FT.CONFIG SET`](ft.config-set.md) says what each does. The others are kept and reported. `FT.CONFIG SET` refuses any other name with `Invalid option`, and [`FT.CONFIG GET`](ft.config-get.md) returns nothing for it. `TIMEOUT`, `ON_TIMEOUT` and `MINSTEMLEN` are also the server settings [`search-timeout`](../reference/configuration.md#search-timeout), [`search-on-timeout`](../reference/configuration.md#search-on-timeout) and [`search-min-stem-len`](../reference/configuration.md#search-min-stem-len): one value under either name.

`FT.CONFIG` alone, or with a name that is not one of these, is an error.

## Examples

```
> FT.CONFIG GET TIMEOUT
1) 1) "TIMEOUT"
   2) "0"
> FT.CONFIG
(error) Unknown subcommand
> FT.CONFIG NOPE
(error) Unknown subcommand
```
