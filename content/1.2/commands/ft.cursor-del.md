---
title: "FT.CURSOR DEL"
description: "Closes a cursor before it is read to the end."
version: "1.2"
command: "FT.CURSOR DEL"
syntax: "FT.CURSOR DEL index cursor_id"
group: "vector-search"
since: "1.1.0"
history: []
container: "FT.CURSOR"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.CURSOR DEL index cursor_id
```

**Available since:** 1.1.0
<!-- generated: end -->
Closes a cursor opened by [`FT.AGGREGATE ... WITHCURSOR`](ft.aggregate.md) before it has been read to the end, and frees the rows it holds. Use it when a client stops paging through an aggregation early; otherwise the cursor stays until it has been unread for its `MAXIDLE`.

- `index`: the index the aggregation ran on, by its own name. An alias, or another index, gets `Cursor does not exist`.
- `cursor_id`: the number `FT.AGGREGATE` or [`FT.CURSOR READ`](ft.cursor-read.md) returned.

A cursor read to the end is already closed: [`FT.CURSOR READ`](ft.cursor-read.md) returned `0` for it, and deleting it is an error.

## Reply

`OK`.

## Errors

- `Cursor does not exist`: no open cursor with that number on that index.
- `SEARCH_INDEX_NOT_FOUND Index not found: <index>`: no such index.
- `ERR wrong number of arguments for 'FT.CURSOR' command`: the number is missing or is not a number.

## Examples

```
> FT.AGGREGATE products * LOAD 1 @name WITHCURSOR COUNT 2
1) 1) (integer) 2
   2) 1) "name"
      2) "Wireless keyboard"
   3) 1) "name"
      2) "USB-C cable, 2 m"
2) (integer) 6143584328685655263
> FT.CURSOR DEL products 6143584328685655263
OK
> FT.CURSOR DEL products 6143584328685655263
(error) Cursor does not exist
> FT.CURSOR READ products 6143584328685655263
(error) Cursor not found
```
