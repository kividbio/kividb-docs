---
title: "JSON paths"
description: "How the JSON commands select values in a document: JSONPath and legacy paths, filters, functions and projections."
version: "1.2"
weight: 30
---

Every JSON command that takes a path reads it with the same engine. The kind of path decides the shape of the reply.

## Two kinds of path

| Kind | Looks like | Matches | Reply |
|---|---|---|---|
| JSONPath | starts with `$`: `$.books[*].title` | any number of values | one entry per match, in document order; `nil` where a match is not of the type the command works on. `JSON.GET` returns a JSON array of the matches, `[]` when there are none. |
| Legacy | anything else: `.store.name`, `a[0]`, `["a"]` | the first match only | a plain value; a match of the wrong type is an error |

A command given no path uses the legacy root, `.`.

```
> JSON.SET d $ '{"name":"Ada","addr":{"city":"London"}}'
OK
> JSON.GET d $.name
"[\"Ada\"]"
> JSON.GET d .name
"\"Ada\""
> JSON.GET d $.nope
"[]"
```

## Selecting

| Syntax | Selects |
|---|---|
| `$` | the root |
| `.name`, `['name']`, `["name"]` | a member. Brackets take any name; the dot form takes any characters but `. [ ] ( ) , = ! < > & \| * ~ ' " ? { }` and spaces |
| `[0]`, `[-1]` | an element; negative indexes count from the end |
| `.*`, `[*]` | every child of an object or array |
| `..name`, `..*` | the same at any depth, in document order |
| `[a,b]` | several selectors at once |
| `[start:end:step]` | a slice of an array; each part is optional, and `step` may be negative |
| `[?expr]`, `[?(expr)]` | the children for which `expr` holds: `@` is the child, `$` the root |
| `path~` | the member names of the objects matched, as strings; it ends a path |

```
> JSON.SET s $ '{"books":[{"t":"A","price":8},{"t":"B","price":12},{"t":"C","price":20}],"allow":["A","C"],"a":3,"b":5}'
OK
> JSON.GET s '$.books[*].t'
"[\"A\",\"B\",\"C\"]"
> JSON.GET s '$.books[0:2].t'
"[\"A\",\"B\"]"
> JSON.GET s '$.books[-1].t'
"[\"C\"]"
> JSON.GET s '$~'
"[\"books\",\"allow\",\"a\",\"b\"]"
```

## Filters

A filter keeps the children for which its expression holds.

| | |
|---|---|
| Comparison | `==` `!=` `<` `<=` `>` `>=`, and `=~` for a regular expression search. `==` and `!=` compare any JSON value, arrays and objects included; `1` equals `1.0`. |
| Logic | `&&`, `\|\|`, `!` and parentheses |
| Arithmetic | `+` `-` `*` `/` `%`, and unary `-` and `+`. **They need spaces around them**: `@.a + 1` adds, while `@.a+1` is a member named `a+1`. `/` always gives a floating-point number. |
| Membership | `x in array`, `x nin array` |
| Sets | `a subsetof b`, `a anyof b`, `a noneof b` |
| Size | `x sizeof n` (or `size`), `x empty true`, `x empty false`, for strings, arrays and objects |

```
> JSON.GET s '$.books[?(@.price >= 10)].t'
"[\"B\",\"C\"]"
> JSON.GET s '$.books[?@.price < 10 || @.t == "C"].t'
"[\"A\",\"C\"]"
> JSON.GET s '$.books[?@.t in $.allow].t'
"[\"A\",\"C\"]"
> JSON.GET s '$.books[?@.t =~ "^[AB]"].t'
"[\"A\",\"B\"]"
```

## Functions and projections

These functions can be written `f(x, ...)` or `x.f(...)`:

`length()` `count()` `value()` `keys()` `match()` `search()` `concat()` `abs()` `ceiling()` `floor()` `first()` `last()` `index()` `min()` `max()` `avg()` `sum()` `stddev()` `append()` `subsetof()` `anyof()` `noneof()`

A path that only selects, like `$.books[*].t`, names values in the document. Anything else computes values, and is a projection: `$.a + 1`, `$.books.length()`, `sum($.books[*].price)`, `$.obj~`. The reading commands return what it computes. The writing commands refuse it, since there is nothing to write to.

```
> JSON.GET s '$.books.length()'
"[3]"
> JSON.GET s 'sum($.books[*].price)'
"[40]"
> JSON.GET s '($.a + $.b) / 2'
"[4.0]"
> JSON.SET s '$.a + 1' 2
(error) ERR the path must select values, not compute one
```

## When something does not fit

Evaluating a path never fails. An operand that cannot be evaluated, such as a type that does not fit, a division by zero, an index out of range, or the wrong number of arguments to a function, gives *nothing*: a filter treats it as false, and a projection gives `[]`.

A path that cannot be parsed is an error:

```
> JSON.GET s '$.books[?@.nope > 1].t'
"[]"
> JSON.GET s '$.books[[bad'
(error) ERR invalid path: expected a selector at position 8
```

## Writing through a path

The writing commands change every value a JSONPath matches:

```
> JSON.SET s '$.books[?(@.price<10)].price' 9
OK
> JSON.NUMINCRBY s '$.books[*].price' 1
"[10,13,21]"
```

[`JSON.SET`](../commands/json.set.md) can also add a member that a path names but that does not exist, if its parent is one existing object.
